import toee, debug, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls
import utils_target_list, utils_npc, tpdp, tpactions, copy
import logging

def get_ctrl(id):
	assert isinstance(id, str)
	ctrl = None
	storage = utils_storage.obj_storage_by_id(id)
	if storage:
		ctrl = get_ctrl_from_storage(storage)
	return ctrl

def get_ctrl_from_storage(storage):
	ctrl = None
	if storage:
		for t in storage.data.iteritems():
			if (issubclass(type(t[1]), CtrlBehaviour)):
				ctrl = t[1]
				break
	return ctrl

def san_start_combat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	ctrl = CtrlBehaviour.get_from_obj(attachee)
	print("san_start_combat {}, {}".format(attachee, ctrl))
	if (ctrl):
		return ctrl.start_combat(attachee, triggerer)
	return toee.RUN_DEFAULT

def san_enter_combat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	ctrl = CtrlBehaviour.get_from_obj(attachee)
	if (ctrl):
		return ctrl.on_enter_combat(attachee, triggerer)
	return toee.RUN_DEFAULT

def san_end_combat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	ctrl = CtrlBehaviour.get_from_obj(attachee)
	if (ctrl):
		return ctrl.on_end_combat(attachee, triggerer)
	return toee.RUN_DEFAULT

def san_exit_combat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	ctrl = CtrlBehaviour.get_from_obj(attachee)
	if (ctrl):
		return ctrl.exit_combat(attachee, triggerer)
	return toee.RUN_DEFAULT

def san_will_kos(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	#print("will_kos({}, {})".format(attachee, triggerer))
	ctrl = CtrlBehaviour.get_from_obj(attachee)
	if (ctrl):
		return ctrl.will_kos(attachee, triggerer)
	else: print("san_will_kos ctrl not found")
	return toee.RUN_DEFAULT

def san_dialog(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	ctrl = CtrlBehaviour.get_from_obj(attachee)
	if (ctrl):
		return ctrl.dialog(attachee, triggerer)
	return toee.RUN_DEFAULT

def san_heartbeat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	ctrl = CtrlBehaviour.get_from_obj(attachee)
	if (ctrl):
		return ctrl.heartbeat(attachee, triggerer)

	# RUN_DEFAULT means
	# If not toee.game.combat_is_active() than AiProcess will be called else nothing
	# If toee.game.combat_is_active() and SKIP_DEFAULT then skip turn completely

	return toee.RUN_DEFAULT

def san_wield_off(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	ctrl = CtrlBehaviour.get_from_obj(attachee)
	if (ctrl and "wield_off" in dir(ctrl)):
		return ctrl.wield_off(attachee, triggerer)
	return toee.RUN_DEFAULT


class CtrlBehaviour(object):
	def __init__(self):
		self.id = None
		self.spells = utils_npc_spells.NPCSpells()
		self.vars = dict()
		#self.items = dict()
		return

	def created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		# assign scripts
		#npc.scripts[const_toee.sn_start_combat] = 6213
		# create inventory
		self.id = npc.id
		self.after_created(npc)
		return

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		return

	@classmethod
	def get_proto_id(cls):
		return 0

	@classmethod
	def get_alias(self):
		return

	@classmethod
	def create_obj_and_class(cls, loc, call_created=1, register=1):
		protoid = cls.get_proto_id()
		if (protoid <= 0):
			print("protoId cannot be zero! {}".format(cls.__name__))
			debug.breakp("protoId cannot be zero!")
			raise Exception("protoId cannot be zero!")
		npc = cls._create_npc_obj(protoid, loc)
		if (not npc):
			debug.breakp("obj created cannot be null!")
			raise Exception("Failed to create obj by proto: {}!".format(protoid))
		print("obj_create({}, {}) = {}".format(protoid, loc, npc))
		ctrl = cls()
		if (register):
			o = utils_storage.obj_storage(npc)
			o.data["ctrl"] = ctrl
			o.alias = cls.get_alias()
			o.origin = npc.origin
		if (call_created):
			ctrl.created(npc)
		return npc, ctrl

	@classmethod
	def _create_npc_obj(cls, protoid, loc, offset_x = None, offset_y = None):
		npc = toee.game.obj_create(protoid, loc, offset_x, offset_y) if not offset_x is None else toee.game.obj_create(protoid, loc)
		if npc:
			npc.condition_add("InitiativeInfoHelper")
		return npc

	@classmethod
	def create_obj(cls, loc):
		npc, ctrl = cls.create_obj_and_class(loc)
		return npc

	@classmethod
	def create_obj_at_loc(cls, loc):
		npc = cls.create_obj(loc)
		npc.move(loc)
		return npc

	@classmethod
	def get_name(cls):
		return type(cls).__name__

	def set_alias(self, alias, npc):
		self.vars["alias"] = alias
		o = utils_storage.obj_storage(npc)
		o.alias = alias
		return

	@classmethod
	def ensure(cls, npc):
		data = utils_storage.obj_storage(npc).data
		ctrl = None
		if (cls.get_name() in data):
			ctrl = data["ctrl"]
		else:
			ctrl = cls()
			ctrl.created(npc)
			utils_storage.obj_storage(npc).data["ctrl"] = ctrl
		return ctrl

	@classmethod
	def get_from_obj(cls, npc):
		data = utils_storage.obj_storage(npc).data
		if (data and "ctrl" in data):
			ctrl = data["ctrl"]
			assert isinstance(ctrl, CtrlBehaviour)
			return ctrl
		return

	def npc_get(self):
		npc = None
		if (self.id):
			npc = toee.game.get_obj_by_id(self.id)
		if (not npc):
			print("Failed to get NPC ctrl: {}, id: {}".format(type(self).__name__, self.id))
		return npc

	def start_combat(self, attachee, triggerer):
		print("")
		print("{}::{} (round: {})".format(type(self).__name__, "start_combat", toee.game.combat_turn))
		print("------------------------")
		#debugg.breakp("start_combat")
		if (utils_npc.npc_hp_current(attachee) >= 0):
			tac = self.create_tactics(attachee)
			if (not tac):
				tac = self.create_tactics_default(attachee)

			if (tac and tac.count > 0):
				tac.set_strategy(attachee)
		return toee.RUN_DEFAULT

	def exit_combat(self, attachee, triggerer):
		return toee.RUN_DEFAULT

	def on_enter_combat(self, attachee, triggerer):
		result = self.enter_combat(attachee, triggerer)
		return result

	def enter_combat(self, attachee, triggerer):
		return toee.RUN_DEFAULT

	def on_end_combat(self, attachee, triggerer):
		self.end_combat(attachee, triggerer)
		return toee.RUN_DEFAULT

	def end_combat(self, attachee, triggerer):
		return toee.RUN_DEFAULT

	def will_kos(self, attachee, triggerer):
		return toee.RUN_DEFAULT

	def dying(self, attachee, triggerer):
		return toee.RUN_DEFAULT

	def dialog(self, attachee, triggerer):
		return toee.RUN_DEFAULT

	def join(self, npc, follower):
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		return None

	def create_tactics_default(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())
		tac.add_clear_target()
		tac.add_target_closest()
		tac.add_sniper()
		tac.add_use_potion()
		tac.add_attack()
		tac.add_approach()
		tac.add_attack()
		return tac

	def revealed(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		return

	def revealing(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		return

	def activated(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		return

	def activating(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		return

	def trigger_step(self, npc, step):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(step, int)
		return

	def get_var(self, name, default_value = None):
		if (self.vars and name in self.vars):
			return self.vars[name]
		self.vars[name] = default_value
		return default_value

	def tactic_coup_de_grace(self, npc, foes = None):
		assert isinstance(npc, toee.PyObjHandle)
		if (foes is None):
			foes = utils_target_list.AITargetList(npc, 1, 0, utils_target_list.AITargetMeasure.by_all()).rescan()
		coup_de_grace_targets = foes.get_coup_de_grace_targets()
		if (coup_de_grace_targets): 
			#debug.breakp("coup_de_grace_targets")
			tac = utils_tactics.TacticsHelper(self.get_name())
			tac.add_target_closest()
			tac.add_target_obj(coup_de_grace_targets[0].target.id)
			tac.add_approach_single()
			tac.add_d20_action(toee.D20A_COUP_DE_GRACE, 0)
			tac.add_attack_threatened()
			tac.add_total_defence()
			return tac
		return

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		return toee.RUN_DEFAULT

	def cooldown(self, var_name):
		if (var_name is None): return
		var_value = self.get_var(var_name, 0)
		if (var_value > 0):
			var_value -=1
			self.vars[var_name] = var_value
		return var_value

	def cooldown_all(self):
		for key in self.vars.iterkeys():
			assert isinstance(key, str)
			if ("cooldown" in key):
				self.cooldown(key)
		return

	def on_execute_strategy(self, npc, target):
		return

class CtrlBehaviourAI(CtrlBehaviour):
	def __init__(self):
		super(CtrlBehaviourAI, self).__init__()
		self._vars = dict()
		self._vars_tactics = dict()
		return

	def start_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		print("")
		print("")
		print("")
		print("")
		print("")
		print("{}::{} (round: {})".format(type(self).__name__, "start_combat", toee.game.combat_turn))
		print("------------------------")

		self._vars_tactics = dict()

		hp_current = attachee.stat_level_get(toee.stat_hp_current)
		self._vars_tactics["hp_current"] = hp_current
		
		if (hp_current <= -10):
			print("Tactics: Skip - Is Dead for {}".format(attachee))
			return toee.SKIP_DEFAULT

		if (hp_current < 0):
			print("Tactics: Skip - Is Dying for {}".format(attachee))
			return toee.SKIP_DEFAULT

		if (attachee.d20_query(toee.Q_Unconscious)):
			print("Tactics: Skip - Is Unconscious for {}".format(attachee))
			return toee.SKIP_DEFAULT

		if (attachee.d20_query(toee.Q_Helpless)):
			print("Tactics: Skip - Is Helpless for {}".format(attachee))
			return toee.SKIP_DEFAULT

		if (attachee.d20_query(toee.Q_Critter_Is_Stunned)):
			print("Tactics: Skip - Is Stunned for {}".format(attachee))
			return toee.SKIP_DEFAULT

		if (attachee.d20_query(toee.Q_Critter_Is_Held)):
			print("Tactics: Skip - Is Held for {}".format(attachee))
			return toee.SKIP_DEFAULT

		seq = tpactions.get_cur_seq()
		if (seq and seq.tb_status):
			if (not seq.tb_status.hourglass_state):
				print("Tactics: Skip - hourglass_state == no actions for {}".format(attachee))
				#attachee.condition_add("Fighting_Defensively_Monster")
				return toee.SKIP_DEFAULT

		tac = utils_tactics.TacticsHelper(self.get_name())
		self.tactics_recon(attachee)
		while (True):
			if (self.tactics_process_critical(attachee, tac)):
				break
			tac = self.create_tactics(attachee)
			if (tac): break

			tac = self.create_tactics_default2(attachee)
			break

		self._vars_tactics = None
		if (tac):
			tac.set_strategy(attachee)

		return toee.RUN_DEFAULT

	def on_end_combat(self, attachee, triggerer):
		self.vars["exec_strategy_counter"] = 0
		self.end_combat(attachee, triggerer)
		return toee.RUN_DEFAULT

	def tactics_process_critical(self, npc, tac):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(tac, utils_tactics.TacticsHelper)

		#foes_adjacent = self._vars_tactics["foes_adjacent"] if "foes_adjacent" in self._vars_tactics else list()

		prefer_offense = self.tactics_prefer_offense(npc)

		hp = npc.stat_level_get(toee.stat_hp_current)
		if (hp == 0):
			if (not prefer_offense):
				item = self.tactics_get_heal_item(npc, True)
				if (item):
					tac.add_five_foot_step()
					tac.add_use_item(item.id)
					tac.add_stop()
					return True

		foes_could_be_approached = self._vars_tactics.get("foes_could_be_approached")
		assert isinstance(foes_could_be_approached, list)

		foes_adjacent = self._vars_tactics["foes_adjacent"]
		assert isinstance(foes_adjacent, list)

		# coup de grace
		if (foes_adjacent or foes_could_be_approached):

			foes_can_be_graced = list(o for o in foes_adjacent if o.d20_query(toee.Q_Helpless))
			if (not foes_can_be_graced):
				foes_can_be_graced = list(o[0] for o in foes_could_be_approached if o[0].d20_query(toee.Q_Helpless))
			if (foes_can_be_graced):
				tac.add_target_obj(foes_can_be_graced[0].id)
				tac.add_approach()
				tac.add_d20_action(toee.D20A_COUP_DE_GRACE, 0)
				return True

		return False

	def tactics_recon(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		reckon_debug_print = self.is_reckon_debug_print(npc)
		if reckon_debug_print: print("tactics_recon {}".format(npc))

		hourglass_state = None
		tb_status = tpactions.get_cur_seq().tb_status
		if tb_status:
			hourglass_state = tb_status.hourglass_state
		self._vars_tactics["hourglass_state"] = hourglass_state

		movement_speed = npc.stat_level_get(toee.stat_movement_speed)
		self._vars_tactics["movement_speed"] = movement_speed

		if reckon_debug_print >= 2:
			hourglass_state_str = "None" 
			if hourglass_state == toee.D20ACT_NULL: hourglass_state_str = "D20ACT_NULL ({})".format(hourglass_state)
			elif hourglass_state == toee.D20ACT_Move_Action: hourglass_state_str = "D20ACT_Move_Action ({})".format(hourglass_state)
			elif hourglass_state == toee.D20ACT_Standard_Action: hourglass_state_str = "D20ACT_Standard_Action ({})".format(hourglass_state)
			elif hourglass_state == toee.D20ACT_Partial_Charge: hourglass_state_str = "D20ACT_Partial_Charge ({})".format(hourglass_state)
			elif hourglass_state == toee.D20ACT_Full_Round_Action: hourglass_state_str = "D20ACT_Full_Round_Action ({})".format(hourglass_state)

			
			print("hourglass_state: {}, movement_speed: {} ft".format(hourglass_state_str, movement_speed))

		foes_adjacent = list()
		foes_threatening = list()
		foes = list()

		npc_can_melee = utils_npc.npc_can_melee(npc, None)
		npc_radius = utils_npc.npc_get_radius_ft(npc)
		npc_reach = utils_npc.npc_get_reach(npc)

		critters_all = toee.game.obj_list_vicinity(npc.location, toee.OLC_CRITTERS)

		critters_friendly = list()
		critters_unfriendly = list()
		for obj in critters_all:
			if obj == npc: continue
			#print("tactics_recon obj check {}".format(obj))
			if (not utils_npc.npc_could_be_attacked(obj, 0)): 
				#print("\t tactics_recon not npc_could_be_attacked {}".format(obj))
				continue
			if npc.is_friendly(obj):
				#print("\t tactics_recon is friendly {}".format(obj))
				critters_friendly.append(obj)
				continue
			critters_unfriendly.append(obj)

		critters_unfriendly = sorted(critters_unfriendly, key = lambda o: npc.distance_to(o))
		foes_can_sense = list()
		foes_can_los = list()
		for obj in critters_unfriendly:
			if (not utils_npc.npc_can_sense_in_combat(npc, obj)):
				any_baddy_can_sense = False
				for baddy in critters_friendly:
					if utils_npc.npc_can_sense_in_combat(baddy, obj):
						any_baddy_can_sense = True
						break
				#print("\t tactics_recon cannot sense in combat {}".format(obj))
				if not any_baddy_can_sense:
					continue
			else:
				foes_can_sense.append(obj)
				if npc.has_los(obj):
					foes_can_los.append(obj)

			foes.append(obj)

			if (utils_npc.npc_is_within_reach_ext(npc, obj, npc_radius, npc_reach)):
				#print("\t tactics_recon is npc_is_within_reach_ext, foes_adjacent.append {}".format(obj))
				foes_adjacent.append(obj)
			else:
				pass
				#print("\t tactics_recon not npc_is_within_reach_ext {}".format(obj))

			if (utils_npc.npc_can_melee(obj, npc) and utils_npc.npc_is_within_reach(obj, npc)):
				#print("\t tactics_recon is npc_can_melee, foes_threatening.append {}".format(obj))
				foes_threatening.append(obj)
			else:
				pass
				#print("\t tactics_recon not npc_can_melee {}".format(obj))

		foes_could_be_approached = [] # tuple (npc, len, len_straight)
		if 1:
			can_move_out = True
			if 1:
				if hourglass_state == toee.D20ACT_NULL:
					can_move_out = False

				if can_move_out and npc.d20_query(toee.Q_Is_BreakFree_Possible):
					can_move_out = False

				if reckon_debug_print >= 2: print("can_move_out = {}".format(can_move_out))
				self._vars_tactics["can_move_out"] = can_move_out
				if can_move_out:
					for o in foes_can_sense:
						can_path_straight = npc.can_find_path_to_obj(o, toee.PQF_STRAIGHT_LINE)
						can_path = can_path_straight if can_path_straight else npc.can_find_path_to_obj(o)
						if reckon_debug_print >= 2: 
							print("can_path from {} to {} = {}".format(npc, o, can_path))
							print("can_path_straight from {} to {} = {}".format(npc, o, can_path_straight))
						if can_path or can_path_straight:
							#can_path_straight = npc.can_find_path_to_obj(o, toee.PQF_STRAIGHT_LINE)

							lao = None
							lao_checked = False
							if "find_path_to_obj" in dir(npc):
								lao = npc.find_path_to_obj(o)
								lao_checked = True
								print("lao: {}".format(lao)) #assert isinstance(lao, tpdp.LocAndOffsets)
							if not lao_checked or lao:
								foes_could_be_approached.append((o, can_path, can_path_straight, lao))

		if reckon_debug_print >= 1: 
			print("foes: {}".format(foes))
			print("foes_threatening: {}".format(foes_threatening))
			print("foes_adjacent: {}".format(foes_adjacent))
			print("foes_can_sense: {}".format(foes_can_sense))
			print("foes_can_los: {}".format(foes_can_los))
			print("foes_could_be_approached: {}".format(foes_could_be_approached))

		self._vars_tactics["npc_radius"] = npc_radius
		self._vars_tactics["npc_reach"] = npc_reach
		self._vars_tactics["npc_can_melee"] = npc_can_melee

		self._vars_tactics["foes_adjacent"] = foes_adjacent
		self._vars_tactics["foes_threatening"] = foes_threatening
		self._vars_tactics["foes_can_sense"] = foes_can_sense
		self._vars_tactics["foes_can_los"] = foes_can_los
		self._vars_tactics["foes_could_be_approached"] = foes_could_be_approached
		self._vars_tactics["foes"] = foes
		self._vars_tactics["friends"] = critters_friendly
		return

	def is_reckon_debug_print(self, npc):
		# 0 - none
		# 1 - headers
		# 2 - details
		return 2

	def get_recon_vars(self):
		foes_adjacent = self._vars_tactics["foes_adjacent"]
		assert isinstance(foes_adjacent, list)

		foes_threatening = self._vars_tactics["foes_threatening"]
		assert isinstance(foes_threatening, list)

		foes_can_sense = self._vars_tactics["foes_can_sense"]
		assert isinstance(foes_can_sense, list)

		foes_could_be_approached = self._vars_tactics["foes_could_be_approached"]
		assert isinstance(foes_could_be_approached, list)

		foes = self._vars_tactics["foes"]
		assert isinstance(foes, list)

		# usage
		# foes_adjacent, foes_threatening, foes_can_sense, foes_could_be_approached, foes = self.get_recon_vars()
		return foes_adjacent, foes_threatening, foes_can_sense, foes_could_be_approached, foes

	def tactics_prefer_offense(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		return 0

	def tactics_get_heal_item(self, npc, best = False):
		assert isinstance(npc, toee.PyObjHandle)
		return self.tactics_get_heal_item_default(npc, best)

	def tactics_get_heal_item_default(self, npc, best = False):
		def _get_item(npc, best, item_protos):
			assert isinstance(npc, toee.PyObjHandle)
			if (best): 
				assert isinstance(item_protos, list)
				item_protos = copy.copy(item_protos)
				item_protos.reverse()
			for proto in item_protos:
				item = npc.item_find_by_proto(proto)
				if (item): return item

		item = None
		#item = _get_item(npc, best, const_proto_list_potions.PROTOS_POTIONS_HEALING)
		#if (item): return item

		#if (self.tactics_can_cast_divine_scrolls(npc)):
		#	item = _get_item(npc, best, const_proto_list_scrolls.PROTOS_SCROLLS_HEALING)
		return item

	def tactics_can_cast_divine_scrolls(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		divine_level = npc.highest_divine_caster_level()
		return divine_level

	def tactics_is_hp_critical_for_heal(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		hp = npc.stat_level_get(toee.stat_hp_current)
		return

	def create_tactics_default(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())

		current_primary_ranged = utils_npc.npc_get_weapon(npc, 1)
		target = self.tactics_determine_target(npc, True if (current_primary_ranged) else False)

		if (target):
			# set focus, otherwise targeting might decide to ignore it
			npc.obj_set_obj(toee.obj_f_npc_combat_focus, target)

			tac.add_target_obj(target.id)
			tac.add_sniper()
			tac.add_use_potion()
			tac.add_charge()
			#tac.add_approach_single()
			tac.add_attack()

			# if pathfinding fails
			tac.add_target_closest()
			tac.add_attack()

			# is entangled
			spell_id_breakfree = npc.d20_query(toee.Q_Is_BreakFree_Possible)
			if (spell_id_breakfree):
				if (not self.tactics_prefer_offense(npc)):
					tac.add_d20_action(toee.D20A_BREAK_FREE, spell_id_breakfree)
					tac.add_stop()

			tac.add_total_defence()
			#tac.add_ready_vs_approach() does nothing :(
			tac.add_stop()
		else:
			npc.obj_set_obj(toee.obj_f_npc_combat_focus, toee.OBJ_HANDLE_NULL)
			print("No target, Total Defense")
			npc.float_text_line('Total Defense', toee.tf_yellow)
			tac.add_total_defence()
			tac.add_stop()
		return tac

	def create_tactics_default2(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		tac = None
		is_focus_melee = self.recon_is_focus_melee(npc)
		is_focus_ranged = self.recon_is_focus_ranged(npc)
		print("create_tactics_default2 is_focus_ranged: {} for {}".format(is_focus_ranged, npc))
		if is_focus_ranged and is_focus_melee == 1:
			is_focus_melee = 0

		melee_checked = False
		if is_focus_melee:
			tac, target, kind = self.create_tactics_default_melee(npc)
			melee_checked = True

		if tac:
			return tac

		if is_focus_melee != 2 or is_focus_ranged:
			allowed_switch_to_melee = is_focus_ranged < 2 and not melee_checked
			tac, target, kind = self.create_tactics_default_ranged(npc, allowed_switch_to_melee)

			if not tac and not melee_checked:
				tac, target, kind = self.create_tactics_default_melee(npc)
				melee_checked = True

		if not tac:
			tac = self.tactics_seek_enemy(npc)
			if not tac:
				tac = utils_tactics.TacticsHelper(self.get_name())
				npc.obj_set_obj(toee.obj_f_npc_combat_focus, toee.OBJ_HANDLE_NULL)
				print("No default tactics, Total Defense")
				npc.float_text_line('Total Defense', toee.tf_yellow)
				tac.add_total_defence()
				tac.add_stop()
		return tac

	def create_tactics_default_melee(self, npc):
		# returns (tac, target, kind). tac could be None

		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())

		target, kind = self.tactics_determine_targeting_melee(npc)

		if target and not kind in ("foes_adjacent", "foes_threatening", "foes_could_be_approached"):
			# it means that npc cannot reach or approach any foe, but know about them
			# better to switch to other forms of attack like ranged, throwing, healing etc
			return None, target, kind

		if (target):
			# set focus, otherwise targeting might decide to ignore it
			npc.obj_set_obj(toee.obj_f_npc_combat_focus, target)
			tac.add_target_obj(target.id)
			ranged_weapon = utils_npc.npc_get_weapon(npc, 1, 1)
			if ranged_weapon:
				# todo - what if dropped or not yet equipped??
				#tac.add_go_melee()
				self.tactic_switch_melee(npc)

			if self.recon_is_cautious(npc):
				npc.condition_add("Fighting_Defensively_Monster")

			# flank routine
			if 1:
				add_flank = False
				if target.d20_query(toee.Q_CanBeFlanked):
					if kind in ("foes_adjacent", "foes_threatening"):
						if not target.is_flanked_by(npc):
							if not target.d20_query(toee.Q_AOOPossible):
								add_flank = True

					if not add_flank:
						if self.recon_is_reckless(npc):
							tac.add_flank()
						elif self.recon_is_devoted(npc):
							tac.add_total_defence()
							tac.add_flank()
				if add_flank:
					tac.add_flank()

			add_charge = False
			# charge routine
			if 1:
				if not kind in ("foes_adjacent", "foes_threatening"):
					add_charge = True

				if add_charge:
					tac.add_charge()

			tac.add_attack() # it includes approaching

			if kind == "foes_could_be_approached":
				# now sometimes T+ will go insane and will not approach although it should have
				# in this case let's move the dude outselves
				if "find_path_to_obj" in dir(npc):
					lao = npc.find_path_to_obj(target)
					if lao:
						assert isinstance(lao, tpdp.LocAndOffsets)
						#tac.add_goto_loc(lao.get_location())
						tac.add_approach_single()
						# the thing is movement will restart tactics loop
						#tac.add_halt()
						tac.add_attack()

				# and last thing - attack closest if possible
				tac.add_attack_threatened()

			# if pathfinding fails
			if add_charge:
				tac.add_target_closest()
				tac.add_attack()
			tac.add_total_defence() # in case calculations are wrong
			#tac.add_ready_vs_approach() does nothing :(
			tac.add_stop() # otherwise default T+ AI will be working
		else:
			tac = self.tactics_seek_enemy(npc)
		return tac, target, kind

	def create_tactics_default_ranged(self, npc, allowed_switch_to_melee):
		# returns (tac, target, kind). tac could be None

		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())

		target, kind = self.tactics_determine_targeting_ranged(npc)

		if target and kind == "foes_threatening" and allowed_switch_to_melee:
			# it means that npc is in reach of melee foe
			# better to switch to other forms of attack like melee
			return None, target, kind

		if target and kind == "foes_can_sense" and allowed_switch_to_melee:
			# it means that npc has no "foes_can_sense_has_los", so cannot shoot
			# better to switch to other forms of attack like melee
			# todo: perhaps better to approach
			return None, target, kind

		if (target):
			# set focus, otherwise targeting might decide to ignore it
			npc.obj_set_obj(toee.obj_f_npc_combat_focus, target)
			tac.add_target_obj(target.id)
			
			ranged_weapon = utils_npc.npc_get_weapon(npc, 1, 1)
			if not ranged_weapon:
				self.tactic_switch_ranged(npc)
				#tac.add_go_ranged()

			if self.recon_is_cautious(npc) and ("foes_adjacent", "foes_threatening"):
				npc.condition_add("Fighting_Defensively_Monster")

			#tac.add_reload() # it will reload even if already loaded, skip
			tac.add_five_foot_step() # it includes approaching
			tac.add_attack() # it includes approaching
			tac.add_reload() # 
			tac.add_total_defence() # in case calculations are wrong
			#tac.add_ready_vs_approach() does nothing :(
			tac.add_stop() # otherwise default T+ AI will be working
		else:
			tac = None
		return tac, target, kind

	def tactics_determine_target(self, npc, for_ranged):
		assert isinstance(npc, toee.PyObjHandle)
		#print("tactics_determine_target {} {}".format(type(self).__name__, npc))

		foes_adjacent = self._vars_tactics.get("foes_adjacent")
		assert isinstance(foes_adjacent, list)
		foes_threatening = self._vars_tactics.get("foes_threatening")
		assert isinstance(foes_threatening, list)
		foes = self.tactics_get_foes()

		foes_can_sense = self._vars_tactics["foes_can_sense"]
		assert isinstance(foes_can_sense, list)
		foes_could_be_approached = self._vars_tactics["foes_could_be_approached"]
		assert isinstance(foes_could_be_approached, list)

		target = toee.OBJ_HANDLE_NULL
		while (not target):
			if (foes_adjacent): 
				target = foes_adjacent[0]
				if (target): break

			if (foes_threatening): 
				target = foes_threatening[0]
				if (target): break

			if (foes_could_be_approached):
				target = foes_could_be_approached[0][0]
				if (target): break

			if (foes_can_sense):
				target = foes_can_sense[0]
				if (target): break

			break
		print("tactics_determine_target self: {} npc: {} target: {}".format(type(self).__name__, npc, target))
		return target

	def tactics_determine_targeting_melee(self, npc):
		# -> (target, kind)

		assert isinstance(npc, toee.PyObjHandle)
		foes_adjacent, foes_threatening, foes_can_sense, foes_could_be_approached, foes = self.get_recon_vars()

		target = toee.OBJ_HANDLE_NULL
		kind = "not determined"
		while (not target):
			if (foes_adjacent): 
				target = self.recon_sort_npcs(foes_adjacent, self.recon_apprise_vulnereble)[0]
				if (target): 
					kind = "foes_adjacent"
					break

			if (foes_threatening): 
				target = self.recon_sort_npcs(foes_threatening, self.recon_apprise_vulnereble)[0]
				if (target): 
					kind = "foes_threatening"
					break

			if (foes_could_be_approached):
				foes_could_be_approached_ordered = self.recon_sort_npcs(foes_could_be_approached, self.recon_apprise_vulnereble)
				hourglass_state, movement_speed = self._vars_tactics["hourglass_state"], self._vars_tactics["movement_speed"]
				print("foes_could_be_approached_ordered: {}".format(foes_could_be_approached_ordered))
				for tup in foes_could_be_approached_ordered:
					obj = tup[0]
					dist = tup[1]
					dist_straight = tup[2]
					print("checking {}, dist: {}, dist_straight: {}".format(obj, dist, dist_straight))
					if dist <= movement_speed or (dist_straight and dist_straight <= movement_speed*2 and hourglass_state >= toee.D20ACT_Partial_Charge):
						target = obj
						print("found")
						break
					else:
						print("skip")
						pass

				if (target): 
					kind = "foes_could_be_approached"
					break

			if (foes_can_sense):
				print("checking foes_can_sense...")
				target = self.recon_sort_npcs(foes_can_sense, self.recon_apprise_vulnereble)[0]
				if (target): 
					kind = "foes_can_sense"
					break

			break
		print("tactics_determine_targeting_melee self: {}, npc: {}, target: {} over {}".format(type(self).__name__, npc, target, kind))
		return target, kind

	def tactics_determine_targeting_ranged(self, npc):
		# -> (target, kind)

		assert isinstance(npc, toee.PyObjHandle)
		foes_adjacent, foes_threatening, foes_can_sense, foes_could_be_approached, foes = self.get_recon_vars()

		target = toee.OBJ_HANDLE_NULL
		kind = "not determined"
		while (not target):
			if (foes_threatening): 
				target = self.recon_sort_npcs(foes_threatening, self.recon_apprise_vulnereble)[0]
				if (target): 
					kind = "foes_threatening"
					break

			if (foes_can_sense):
				foes_can_sense_sorted = self.recon_sort_npcs(foes_can_sense, self.recon_apprise_vulnereble)
				for obj in foes_can_sense_sorted:
					if npc.has_los(obj):
						target = obj
						kind = "foes_can_sense_has_los"
						break

				if target:
					break

				target = foes_can_sense_sorted[0]
				if (target): 
					kind = "foes_can_sense"
					break

			break
		print("tactics_determine_targeting_ranged self: {}, npc: {}, target: {} over {}".format(type(self).__name__, npc, target, kind))
		return target, kind

	def tactics_seek_enemy(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		print('tactics_seek_enemy for {}'.format(npc))
		#debug.breakp('tactics_seek_enemy')
		critters_friendly = self._vars_tactics.get("friends")
		if not critters_friendly: 
			print('tactics_seek_enemy NO FRIENDS! for {}'.format(npc))
			return

		movement_speed = npc.stat_level_get(toee.stat_movement_speed)
		aware_friends = list()
		for friend in critters_friendly:
			assert isinstance(friend, toee.PyObjHandle)
			can_see_friend = npc.has_loa(friend)
			print('tactics_seek_enemy can_see_friend: {} of {} for {}'.format(can_see_friend, friend, npc))
			if not can_see_friend:
				continue
			path_len_to_friend = npc.can_find_path_to_obj(friend)
			print('tactics_seek_enemy path_len_to_friend: {} of {} for {}'.format(path_len_to_friend, friend, npc))
			if not path_len_to_friend:
				continue

			if path_len_to_friend > movement_speed * 2:
				continue

			closest_party_distance = 1000
			closest_party_member = None
			for foe in toee.game.party:
				if not friend.can_see(foe): continue
				if not utils_npc.npc_could_be_attacked(foe): continue
				foe_dist = friend.distance_to(foe)
				if foe_dist < closest_party_distance:
					closest_party_member = foe
					closest_party_distance = foe_dist

			print('tactics_seek_enemy closest_party_distance: {}, closest_party_member: {} of {} for {}'.format(closest_party_distance, closest_party_member, friend, npc))
			if closest_party_member:
				aware_friends.append((friend, closest_party_distance, closest_party_member, path_len_to_friend))

		if aware_friends:
			# sort by closest to the party
			aware_friends.sort(key = lambda t: t[1], reverse = True)

			tup = aware_friends[0]
			tac = utils_tactics.TacticsHelper(self.get_name())
			tac.add_clear_target()
			tac.add_target_obj(tup[0].id)
			tac.add_approach()
			tac.add_d20_action(toee.D20A_SEARCH, 0)
			tac.add_halt()
			tac.add_total_defence()
			return tac
		else:
			tac = utils_tactics.TacticsHelper(self.get_name())
			tac.add_d20_action(toee.D20A_SEARCH, 0)
			print('tactics_seek_enemy NO aware_friends FRIENDS! for {}'.format(npc))
			return tac
			
		return

	@staticmethod
	def recon_apprise_vulnereble(arg):
		target = arg[0] if type(arg) is tuple else arg
		assert isinstance(target, toee.PyObjHandle)
		result = target.stat_level_get(toee.stat_ac)

		hp = target.stat_level_get(toee.stat_hp_current)
		if (hp <= 0):
			# most desirable if 0
			result += -4
		elif hp <= 10:
			# this one is near death so also desirable
			result += -4
		else:
			# let's increase repulsion by 2 per each 10 HP
			result += hp // 5

		if target.d20_query(toee.Q_Critter_Is_Invisible):
			# let's increase repulsion by 2
			result += 2

		if target.d20_query(toee.Q_Critter_Has_Mirror_Image):
			# let's increase repulsion by 2
			result += 2

		if target.d20_query(toee.Q_Disarmed):
			# let's increase attractiveness by 4, as it will likely have AOO
			result += 2
		return result

	@staticmethod
	def recon_apprise_vulnereble_for_debuff(arg):
		target = arg[0] if type(arg) is tuple else arg
		assert isinstance(target, toee.PyObjHandle)
		result = 20-target.stat_level_get(toee.stat_ac)

		hp = target.stat_level_get(toee.stat_hp_current)
		if (hp <= 0):
			# most desirable if 0
			result += -4
		elif hp <= 10:
			# this one is near death so also desirable
			result += -4
		else:
			# let's increase repulsion by 2 per each 10 HP
			result += hp // 5

		if target.d20_query(toee.Q_Critter_Is_Invisible):
			# let's increase repulsion by 2
			result += 2

		if target.d20_query(toee.Q_Critter_Has_Mirror_Image):
			# let's increase repulsion by 2
			result += 2

		if target.d20_query(toee.Q_Disarmed):
			# let's increase attractiveness by 4, as it will likely have AOO
			result += 2
		return result

	def recon_sort_npcs(self, npc_list, apprise_func):
		# get weakest first
		return npc_list if len(npc_list) <=0 else sorted(npc_list, key=apprise_func)

	def recon_is_reckless(self, npc):
		# ignore AOO and go for flank as does not care
		return 0

	def recon_is_devoted(self, npc):
		# ignore AOO and go for flank as care and take damage on self
		return 0

	def recon_is_cautious(self, npc):
		# will use defensive fighting
		return 0

	def recon_is_focus_melee(self, npc):
		# 0 - no
		# 1 - yes
		# 2 - yes and only yes
		assert isinstance(npc, toee.PyObjHandle)
		if npc.critter_flags_get() & toee.OCF_MONSTER:
			return 2
		return 1

	def recon_is_focus_ranged(self, npc):
		# 0 - no
		# 1 - yes
		# 2 - yes and only yes
		assert isinstance(npc, toee.PyObjHandle)
		if npc.critter_flags_get() & toee.OCF_MONSTER:
			return 0
		ammo_q = utils_item.weapon_has_ammo(npc, npc.item_worn_at(toee.item_wear_weapon_primary))
		if ammo_q:
			return 1
		return 0

	def on_enter_combat(self, attachee, triggerer):
		# could be combat is not even started yet
		#self.alert_comrades(attachee, triggerer)
		result = self.enter_combat(attachee, triggerer)
		return result

	def alert_comrades(self, npc, target):
		# todo: it should be handled in T+
		# ABANDON it will not work
		# add others by leader
		print('alert_comrades for {}'.format(npc))
		result = 0
		leader = npc.leader_get()
		if (leader):
			#print("add others for leader: {}".format(leader))
			critters = utils_npc.critters_vicinity(npc)
			#print(critters)
			if (critters):
				for o in critters:
					assert isinstance(o, toee.PyObjHandle)
					#print('is check alerting {} by {}; is_active_combatant: {}, same_leader: {}, is_comrade: {}'.format(o, npc, o.is_active_combatant(), (o == leader or o.leader_get() == leader), self.is_comrade(npc, o, leader)))
					if (not o.is_active_combatant()) and self.is_comrade(npc, o, leader):
						print('alerting {} by {}'.format(o, npc))
						if str(o).startswith('GTH01_07'):
							debug.breakp('')
						o.attack(target)
						o.add_to_initiative()
						result += 1
		return result

	def is_comrade(self, npc, target, npc_leader):
		return target == npc_leader or target.leader_get() == npc_leader or npc.allegiance_shared(target)

	def setup(self, npc):
		self.setup_scripts(npc)
		self.setup_appearance(npc)
		self.setup_char(npc)
		self.setup_gear(npc)
		self.setup_loot(npc)
		self.setup_end(npc)
		return

	def setup_scripts(self, npc):
		return

	def setup_appearance(self, npc):
		return

	def setup_char(self, npc):
		return

	def setup_gear(self, npc):
		return

	def setup_loot(self, npc):
		return

	def setup_end(self, npc):
		return

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlBehaviourAI, self).after_created(npc)
		self.setup(npc)
		return

	def generate_hp(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		pts, hp_lines = utils_npc.npc_generate_hp_random_first(npc)
		self.vars["hp_lines"] = hp_lines
		return

	def tactics_get_foes(self):
		foes = self._vars_tactics["foes"]
		assert isinstance(foes, list)
		if (foes is None): foes = []
		return foes

	def tactic_switch_melee(self, npc, also_shield = True):
		assert isinstance(npc, toee.PyObjHandle)
		print("tactic_switch_melee {}".format(npc))
		weapon_ranged = utils_npc.npc_get_weapon(npc, 1, 1)
		if not weapon_ranged:
			return

		new_weapon = None
		new_shield = None
		items = utils_item.items_get(npc, 0)
		for item in items:
			assert isinstance(item, toee.PyObjHandle)
			if new_weapon and (new_shield or not also_shield): break
			if not new_weapon and item.type == toee.obj_t_weapon: 
				if not toee.game.is_ranged_weapon(item.get_weapon_type()): 
					new_weapon = item
			if not new_shield and also_shield and item.type == toee.obj_t_armor: 
				if utils_item.get_armor_type(item) == toee.ARMOR_TYPE_SHIELD:
					new_shield = item

		if new_weapon:
			print("tactic_switch_melee {} to {} (shield: {})".format(npc, new_weapon, new_shield))
			npc.item_worn_unwield(toee.item_wear_weapon_primary, 0)
			npc.item_worn_unwield(toee.item_wear_ammo, 0)
			npc.item_wield(new_weapon, toee.item_wear_weapon_primary)
			if new_shield:
				npc.item_wield(new_shield, toee.item_wear_shield)
			return True
		return False

	def tactic_switch_ranged(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		print("tactic_switch_melee {}".format(npc))
		weapon_ranged = utils_npc.npc_get_weapon(npc, 1, 1)
		if weapon_ranged:
			return

		new_weapon = None
		new_quiver = None
		items = utils_item.items_get(npc, 0)
		for item in items:
			assert isinstance(item, toee.PyObjHandle)
			if not new_weapon and item.type == toee.obj_t_weapon: 
				if toee.game.is_ranged_weapon(item.get_weapon_type()): 
					new_weapon = item
					break

		if new_weapon:
			for item in items:
				assert isinstance(item, toee.PyObjHandle)
				if not new_quiver and item.type == toee.obj_t_ammo: 
					if item.obj_get_int(toee.obj_f_ammo_type) == new_weapon.obj_get_int(toee.obj_f_weapon_ammo_type):
						new_quiver = item
						break

		if new_weapon and new_quiver:
			print("tactic_switch_ranged {} to {} (quiver: {})".format(npc, new_weapon, new_quiver))
			npc.item_worn_unwield(toee.item_wear_weapon_primary, 0)
			npc.item_worn_unwield(toee.item_wear_shield, 0)
			npc.item_worn_unwield(toee.item_wear_ammo, 0)

			if new_quiver:
				npc.item_wield(new_quiver, toee.item_wear_ammo)
			if new_weapon.get_weapon_type() in (toee.wt_heavy_crossbow, toee.wt_light_crossbow):
				loaded = new_weapon.obj_get_int(toee.obj_f_weapon_flags) & toee.OWF_WEAPON_LOADED
			npc.item_wield(new_weapon, toee.item_wear_weapon_primary)
			return True
		return False
