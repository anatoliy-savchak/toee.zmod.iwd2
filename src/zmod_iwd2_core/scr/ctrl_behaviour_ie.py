import toee, debug
import ctrl_behaviour, inf_scripting, ctrl_daemon, utils_storage, utils_npc
import utils_npc_spells_inf, utils_query, const_inf, utils_npc_spells_tactics, utils_tactics
import random

__metaclass__ = type

class CtrlBehaviourIE(ctrl_behaviour.CtrlBehaviourAI, inf_scripting.InfScriptSupportNPC):
	def __init__(self):
		super(CtrlBehaviourIE, self).__init__()

		self.script_vars = dict()
		return

	def __repr__(self):
		repr = self.vars.get("alias")
		if not repr:
			repr = self.id
		if not repr:
			repr = id(self)
		return '{}({})'.format(self.__class__.__name__, repr)

	def __str__(self):
		repr = self.vars.get("alias")
		if not repr:
			repr = self.id
		if not repr:
			repr = id(self)
		return '{}({})'.format(self.__class__.__name__, repr)

	def _gnpc(self):
		attachee = self.vars.get("attachee")
		if attachee is None:
			attachee = self.npc_get()
		assert isinstance(attachee, toee.PyObjHandle)
		return attachee

	def _gtriggerer(self):
		triggerer = self.vars.get("triggerer")
		assert isinstance(triggerer, toee.PyObjHandle)
		return triggerer

	def get_globals(self, area):
		area = inf_scripting.strip_quotes(area)
		print('get_globals {}'.format(area))
		if area.lower() == "myarea" or area.lower() == "area":
			return ctrl_daemon.CtrlDaemon.get_current_daemon().get_globals(area)
		elif area.lower() == "locals":
			result = self.vars.get("locals")
			if result is None:
				result = dict()
				self.vars["locals"] = result
			return result
		return super(CtrlBehaviourIE, self).get_globals(area)

	def _prepare_scripting(self, attachee = None, triggerer = None):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		if attachee is None:
			attachee = self.npc_get()

		self.vars["attachee"] = attachee
		self.vars["triggerer"] = triggerer
		return

	def _unprepare_scripting(self):
		self.vars["attachee"] = None
		self.vars["triggerer"] = None
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		try:
			self._prepare_scripting(attachee, triggerer)
			
			line_id = self.script_dialog(attachee, triggerer)
			if not line_id is None and line_id >= 0:
				self.has_met_inc()
		finally:
			self._unprepare_scripting()
			self.script_vars['last_talked_to_id'] = attachee.id
		
		return toee.SKIP_DEFAULT

	@inf_scripting.dump_args
	def dialog_test(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		try:
			self.vars["attachee"] = npc
			self.vars["triggerer"] = pc
			
			result = self.dialog_test_do(npc, pc, index)
		finally:
			self.vars["attachee"] = None
			self.vars["triggerer"] = None
		
		return result

	@inf_scripting.dump_args
	def iEnemy(self):
		self.set_allegiance(self.npc_get(), 255)
		return

	@inf_scripting.dump_args
	def iForceMarkedSpell(self, spell):
		"""
		ForceMarkedSpell(I:Spell*Spell)
		Essentially will set LastMarkedSpell to spell. Typically ForceMarkedSpell(MARKED_SPELL), e.g. clear spell. Due to MARKED_SPELL = 0.
		"""
		if str(spell).upper() == 'MARKED_SPELL':
			self.script_vars['iMarkedSpell'] = None
		else:
			raise Exception("iForceMarkedSpell - Unknown spell: {}".format(spell))
		return 1

	@inf_scripting.dump_args
	def iSetSpellTarget(self, obj):
		"""
		SetSpellTarget(O:Object*)
		Actually as per scripts_index.json there are none other than Nothing
		"""
		if str(obj).upper() == 'NOTHING':
			self.script_vars['iMarkedSpellTarget'] = None
		else:
			raise Exception("iForceMarkedSpell - Unknown obj: {}".format(obj))
		return 1

	@inf_scripting.dump_args
	def iIsMarkedSpell(self, spell):
		"""
		IsMarkedSpell(I:Spell*Spell)
		"""
		if spell == "MARKED_SPELL":
			return not self.script_vars.get('iMarkedSpell')
		elif spell == "WIZARD_EXECUTIONERS_EYES":
			return False
		elif spell == "WIZARD_IMPROVED_HASTE":
			return False
		raise Exception("Not implemented function: IsMarkedSpell!")
		return

	@inf_scripting.dump_args
	def iHaveSpell(self, spell):
		"""
		HaveSpell(I:Spell*Spell)
		"""
		spell_rec = utils_npc_spells_inf.get_spell_rec(spell)
		if not spell_rec:
			print('no spell')
			return

		spell_id = spell_rec["spell_id"]
		if spell_id:
			return self.spells.get_spell_count(spell_id)
		return

	@inf_scripting.dump_args
	def iIsSpellTargetValid(self, obj, spell, flags):
		"""
		IsSpellTargetValid(O:Object*, I:Spell*Spell, I:Flags*SplCast)
		"""
		return self.is_spell_target_valid(obj, spell, flags)

	def is_spell_target_valid(self, obj, spell, flags, set_marked = False):
		query = obj if isinstance(obj, utils_query.NPCQuery) else utils_query.NPCQuery(self, obj)

		spell_rec = utils_npc_spells_inf.get_spell_rec(spell)
		if not spell_rec:
			print('no spell')
			return
		
		spell_name = spell_rec["name"]
		spell_cls = spell_rec["spell_cls"]
		if not spell_rec:
			print('spell_cls not found')
			return
		
		#assert isinstance(spell_cls, utils_npc_spells_tactics.SpellTactic)
		npc = self.npc_get()

		spell_obj = spell_cls(npc=npc, spells=self.spells, tacs=None, target = None, options = None)
		assert isinstance(spell_obj, utils_npc_spells_tactics.SpellTactic)
		spell_obj.should_approach = 1
		query.should_see = spell_obj.should_see()
		processed_count = 0
		for targtup in query.gen():
			processed_count += 1
			spell_obj.target = targtup[0]
			err = spell_obj.execute(mode_blank = True)
			print('iMarkSpellAndObject spell_obj.execute(blank) = {} ({}) of {} / {}'.format(err, spell_obj, npc, self))
			if err in (utils_npc_spells_tactics.EDOT_NO_SPELLS_LEFT, utils_npc_spells_tactics.EDOT_CANNOT_CAST_VERBAL, utils_npc_spells_tactics.EDOT_CANNOT_CAST_SOMATIC):
				break
			if err:
				continue
			if set_marked:
				self.script_vars['iMarkedSpellTarget'] = targtup
				self.script_vars['iMarkedSpell'] = spell_name
				print('is_spell_target_valid marked_spell: {}, marked_spell_target: {}'.format(self.script_vars['iMarkedSpell'], self.script_vars['iMarkedSpellTarget']))
			return True
		if not processed_count:
			print('is_spell_target_valid: No targets in query: {} for {}!'.format(query.query, npc))
		return

	def iSpell(self, target, spell):
		"""
		Spell(O:Target*, I:Spell*Spell)
		"""
		self.script_vars['iMarkedSpellTargetExecute'] = self.script_vars.get('iMarkedSpellTarget')
		self.script_vars['iMarkedSpellExecute'] = self.script_vars.get('iMarkedSpell')
		return


	@inf_scripting.dump_args
	def iMarkSpellAndObject(self, spells, obj, flags):
		"""
		MarkSpellAndObject(S:Spells*, O:Object*, I:Flags*SplCast)
		"""

		iMarkedSpell = self.script_vars.get('iMarkedSpell')
		if iMarkedSpell:
			print('Already has spell (iMarkedSpell): {}'.format(iMarkedSpell))
			return
		flags = int(flags)
		query = utils_query.NPCQuery(self, obj)
		spell_list = []
		if isinstance(spells, list):
			spell_list = spells
			if flags & const_inf.SPELLCAST_RANDOM:
				random.shuffle(spell_list)
		else:
			spell_list.append(spells)

		print('spell_list: {}'.format(spell_list))
		for spell in spell_list:
			if self.is_spell_target_valid(query, spell, flags, set_marked = True):
				return True
		return

	@inf_scripting.dump_args
	def iSee(self, obj, seedead):
		"""
		See(O:Object*, I:SeeDead*)
		"""
		npc = self.npc_get()
		query = utils_query.NPCQuery(self, obj)
		for targtup in query.gen():
			target = targtup[0]
			can_see = (target == npc or (npc.can_see(target) or npc.has_loa(target)))
			if can_see:
				self.script_vars['iLastMarkedObject'] = targtup
				print('ISee FOUND: {} for {} of {}'.format(target, query.query, npc))
				return True
			else:
				print('ISee cannot see: {} for {} of {}'.format(target, query.query, npc))

		print('ISee {} of {} returned nothing!'.format(query.query, npc))
		#self.script_vars['iLastMarkedObject'] = None
		return 

	def dialog_action(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		try:
			self.vars["attachee"] = npc
			self.vars["triggerer"] = pc
			
			result = self.dialog_action_do(npc, pc, index)
		finally:
			self.vars["has_met"] = self.has_met() + 1
			self.vars["attachee"] = None
			self.vars["triggerer"] = None
		
		return result

	def critter_dying(self, attachee, triggerer):
		super(CtrlBehaviourIE, self).critter_dying(attachee, triggerer)
		if self.vars.get("critical_path"):
			# that critter should not die!
			# see iSetCriticalPathObject
			toee.game.moviequeue_play_end_game()
		return

	def has_met(self):
		result = self.vars.get("has_met")
		if result is None:
			result = 0
			self.vars["has_met"] = result
		return result

	def has_met_inc(self):
		result = self.vars.get("has_met")
		if result is None:
			result = 0
		result += 1
		self.vars["has_met"] = result
		return result

	def has_met_set(self, value):
		self.vars["has_met"] = value
		return self.vars["has_met"]

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		return toee.RUN_DEFAULT

	def setup(self, npc):
		super(CtrlBehaviourIE, self).setup(npc)
		return

	def get_dialog_trigger_max_index(self): return None

	def test_dialog_triggers(self, pc = None, specific_trigger_id_else_all = None):
		max_index = self.get_dialog_trigger_max_index()
		if not max_index:
			return 0

		npc = self.npc_get()
		if not specific_trigger_id_else_all is None:
			result = self.dialog_test(npc, toee.game.leader, specific_trigger_id_else_all)
			return 1

		for i in range(1, max_index+1):
			result = self.dialog_test(npc, toee.game.leader, i)

		return max_index

	def get_state_to_line(self, state): return

	def start_dialog_at_state(self, npc, pc, state):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)

		line_id = self.get_state_to_line(state)
		if line_id:
			pc.begin_dialog(npc, line_id)
		else:
			raise Exception('State {} not found as line!'.format(state))
		return

	def hide_creature(self, npc, hidden):
		assert isinstance(npc, toee.PyObjHandle)
		self.vars["hidden"] = hidden
		if npc:
			if hidden:
				npc.object_flag_set(toee.OF_DONTDRAW)
			else:
				npc.object_flag_unset(toee.OF_DONTDRAW)
		return

	def locus_make(self):
		return {'dameon_id': self.vars.get('dameon_id'), 'npc_id': self.id}

	def get_allegiance(self): 
		return self.vars.get('allegiance', self.get_allegiance_default())

	def set_allegiance(self, npc, allegiance): 
		self.vars['allegiance'] = allegiance
		kos = allegiance == 255
		if kos:
			npc.npc_flag_set(toee.ONF_KOS)
		else:
			npc.npc_flag_unset(toee.ONF_KOS)
		return

	def allegiance_update(self, npc):
		allegiance = self.get_allegiance()
		npc_leader = npc.leader_get()
		if npc_leader:
			lead_ctrl = ctrl_behaviour.get_ctrl(npc_leader.id)
			if lead_ctrl:
				lead_allegiance = lead_ctrl.get_allegiance()
				allegiance = lead_allegiance
		self.set_allegiance(npc, allegiance)
		return

	def enable_dialog(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.critter_flag_unset(toee.OCF_MUTE)
		return

	def generic_heartbeat_dialog_start_when_in_range(self, npc, range):
		pc = utils_npc.npc_find_nearest_pc_prefer_leader(npc, range, should_see = True)
		if pc:
			#pc.begin_dialog(npc)
			self.script_dialog(npc, pc)
			return True
		return

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		tac = None
		print('create_tactics IE')
		bcs_combat = self.get_bcs_combat()
		print('bcs_combat: {}'.format(bcs_combat))
		if bcs_combat:
			#debug.breakp('create_tactics IE')
			self.script_vars['iMarkedSpellTarget'] = None
			self.script_vars['iMarkedSpell'] = None
			self.script_vars['iMarkedSpellTargetExecute'] = None
			self.script_vars['iMarkedSpellExecute'] = None

			bcs_combat.do_execute_simple(self)

			#marked_spell_target = self.script_vars.get('iMarkedSpellTarget')
			#marked_spell = self.script_vars.get('iMarkedSpell')
			iMarkedSpellTargetExecute = self.script_vars.get('iMarkedSpellTargetExecute')
			iMarkedSpellExecute = self.script_vars.get('iMarkedSpellExecute')
			#print('create_tactics IE executed marked_spell: {}, marked_spell_target: {}'.format(marked_spell, marked_spell_target))
			print('create_tactics IE executed iMarkedSpellTargetExecute: {}, iMarkedSpellExecute: {}'.format(iMarkedSpellTargetExecute, iMarkedSpellExecute))
			if iMarkedSpellExecute and iMarkedSpellExecute:
				tac = self.execute_market_spell_to_tac(npc)

			#debug.breakp('create_tactics IE END')

			self.script_vars['iMarkedSpellTarget'] = None
			self.script_vars['iMarkedSpell'] = None
		return tac

	def setup_char(self, npc):
		_dir = dir(self)
		if 'setup_char_abilities' in _dir:
			self.setup_char_abilities(npc)
		if 'setup_char_classes' in _dir:
			self.setup_char_classes(npc)
		if 'setup_char_natural' in _dir:
			self.setup_char_natural(npc)
		if 'setup_char_cr' in _dir:
			self.setup_char_cr(npc)
		if 'setup_char_feats' in _dir:
			self.setup_char_feats(npc)
		if 'setup_char_saves' in _dir:
			self.setup_char_saves(npc)
		if 'setup_char_hp' in _dir:
			self.setup_char_hp(npc)
		if 'setup_char_skills' in _dir:
			self.setup_char_skills(npc)
		if 'setup_char_alignment' in _dir:
			self.setup_char_alignment(npc)
		if 'setup_spells' in _dir:
			self.setup_spells(npc)
		return

	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 1
		return npc.get_base_attack_bonus() // 5 + 1

	def get_bcs_general(self): return None

	def get_bcs_class(self): return None

	def get_bcs_combat(self): return None

	def get_bcs_movement(self): return None

	def get_bcs_team(self): return None

	def get_bcs_special_one(self): return None
	
	def execute_market_spell_to_tac(self, npc):
		marked_spell_target = self.script_vars.get('iMarkedSpellTargetExecute')
		marked_spell = self.script_vars.get('iMarkedSpellExecute')
		print('execute_market_spell_to_tac iMarkedSpellTargetExecute: {}, iMarkedSpellExecute: {} of {}'.format(marked_spell_target, marked_spell, npc))

		spell_rec = utils_npc_spells_inf.get_spell_rec(marked_spell)
		if not spell_rec:
			print('marked_spell: {} not found!'.format(marked_spell))
			return
		
		spell_cls = spell_rec["spell_cls"]
		if not spell_rec:
			print('spell_cls not found')
			return
		
		target = marked_spell_target[0]
		tac = utils_tactics.TacticsHelper(self.get_name())
		spell_obj = spell_cls(npc=npc, spells=self.spells, tacs=tac, target = target, options = None)
		assert isinstance(spell_obj, utils_npc_spells_tactics.SpellTactic)
		spell_obj.should_approach = 1

		err = spell_obj.execute(mode_blank = False)
		print('execute_market_spell_to_tac spell_obj.execute() = {} ({}) of {} / {}'.format(err, spell_obj, npc, self))
		if err or tac.count == 0:
			return None
		tac.add_stop() # to prevent "attempting default..."
		print('tacs: {}'.format(tac))
		return tac