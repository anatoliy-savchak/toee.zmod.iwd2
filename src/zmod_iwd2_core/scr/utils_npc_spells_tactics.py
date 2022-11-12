import toee, utils_npc, utils_npc_spells, utils_tactics, tpdp

# returns error code !!!!!!

EDOT_OK = 0
EDOT_NO_SPELLS_LEFT = 1
EDOT_TARGET_TOO_FAR = 2
EDOT_CANNOT_BE_AFFECTED = 3
EDOT_CANNOT_CAST_VERBAL = 4
EDOT_CANNOT_CAST_SOMATIC = 5
EDOT_TARGET_TOO_FAR_FOR_APPROACH = 6

class SpellTactic(object):
	def __init__(self, npc, spells, tacs, target = toee.OBJ_HANDLE_NULL, options = None):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(spells, utils_npc_spells.NPCSpells)
		assert isinstance(tacs, utils_tactics.TacticsHelper)
		assert isinstance(target, toee.PyObjHandle)
		self.npc = npc
		self.spells = spells
		self.tacs = tacs
		self.target = target
		self.options = options
		self._spell_range = None
		self._spell_components = None
		return

	@staticmethod
	def _get_spell_num():
		raise Exception("Not implemented!")
		return 0

	def _is_personal(self):
		se = tpdp.SpellEntry(self._get_spell_num())
		if ("get_spell_range_exact" in dir(se)):
			print("{} ({}) se.spellRange: {}".format(type(self).__name__, toee.game.get_spell_mesline(se.spell_enum), se.spellRange))
			if (se.spellRange == tpdp.SpellRangeType.SRT_Personal):
				return 1
		return 0

	def _is_no_target(self):
		return 0

	def _check_distance(self):
		return self._check_distance_target(self.target)

	def _check_distance_target(self, target):
		if (self._is_personal()): return EDOT_OK
		self._calc_spell_range()
		dist = self.npc.distance_to(target)
		if (dist > self._spell_range):
			if self._should_approach():
				speed = self.npc.stat_level_get(toee.stat_movement_speed)
				if dist <= speed:
					EDOT_OK
				else:
					print("{} ({}) EDOT_TARGET_TOO_FAR_FOR_APPROACH (range: {}, dist: {}, speed: {}) by {} on {}".format(type(self).__name__, toee.game.get_spell_mesline(self._get_spell_num()), self._spell_range, dist, speed, self.npc, target))
					return EDOT_TARGET_TOO_FAR_FOR_APPROACH

			print("{} ({}) EDOT_TARGET_TOO_FAR (range: {}, dist: {}) by {} on {}".format(type(self).__name__, toee.game.get_spell_mesline(self._get_spell_num()), self._spell_range, dist, self.npc, target))
			return EDOT_TARGET_TOO_FAR
		return EDOT_OK

	def _calc_spell_range(self):
		self._calc_spell_range_default()
		se = tpdp.SpellEntry(self._get_spell_num())
		if ("get_spell_range_exact" in dir(se)):
			spell_rec = self.spells.get_spell(self._get_spell_num())
			caster_level = spell_rec.spell_level
			range = se.get_spell_range_exact(caster_level, self.npc)
			self._spell_range = range
		self._spell_components = se.spell_component_flags
		return

	def _calc_spell_range_default(self):
		self._spell_range = 0
		return

	def _subject(self):
		return self.npc if (self._is_personal()) else self.target

	def _except_q(self):
		return 0

	def _except_spell_condition(self):
		return 0

	def _check_already(self):
		q = self._except_q()
		if q: 
			obj = self._subject()
			if (not obj): return EDOT_OK

			if (obj.d20_query(q)):
				return EDOT_CANNOT_BE_AFFECTED

		q = self._except_spell_condition()
		print('_except_spell_condition {} for {} of {}'.format(q, toee.game.get_spell_mesline(self._get_spell_num()), self.npc))
		if q: 
			obj = self._subject()
			print('_except_spell_condition {} {} for {} subject:  of {}'.format(q, toee.game.get_spell_mesline(self._get_spell_num()), obj, self.npc))
			if (not obj): return EDOT_OK

			has = obj.d20_query_has_spell_condition(q)
			print('has:{} _except_spell_condition {} {} for {} subject:  of {}'.format(has, q, toee.game.get_spell_mesline(self._get_spell_num()), obj, self.npc))
			if has:
				return EDOT_CANNOT_BE_AFFECTED
		return EDOT_OK

	def _check_uninhibited(self):
		if not self._spell_components is None:

			if self._spell_components & toee.SCF_VERBAL:
				if self.npc.d20_query(toee.Q_Critter_Is_Deafened) or self.npc.d20_query_has_spell_condition(toee.spell_silence):
					return EDOT_CANNOT_CAST_VERBAL

			if self._spell_components & toee.SCF_SOMATIC:
				if self.npc.d20_query(toee.Q_Critter_Is_Grappling) or self.npc.d20_query(toee.Q_Critter_Is_Stunned) or self.npc.d20_query(toee.Q_Helpless):
					return EDOT_CANNOT_CAST_SOMATIC
		return EDOT_OK

	def _add_spell_exec(self):
		self.tacs.add_cast_single_code(self.spells.prep_spell(self.npc, self._get_spell_num()))
		return EDOT_OK

	def _should_approach(self): return 0

	def spells_left(self):
		return self.spells.get_spell_count(self._get_spell_num())

	def set_target(self, target):
		self.target = target
		return

	def execute(self, mode_blank = False):
		print("{} ({}) execute by {} on {}".format(type(self).__name__, toee.game.get_spell_mesline(self._get_spell_num()), self.npc, self.target))
		if (self.spells_left() == 0): 
			print("{} EDOT_NO_SPELLS_LEFT for {} by {}".format(type(self).__name__, toee.game.get_spell_mesline(self._get_spell_num()), self.npc))
			return EDOT_NO_SPELLS_LEFT

		result = self._check_already()
		if (result): 
			return result

		self._calc_spell_range()
		result = self._check_uninhibited()
		if (result): 
			return result

		is_no_target = self._is_no_target()
		is_personal = None
		if (not is_no_target):
			is_personal = self._is_personal()
			if (not is_personal):
				result = self._check_distance()
				if (result):
					return result

		if not mode_blank:
			if (self.options and self._skip_five_foot_step()):
				pass
			else:
				if not is_personal and self._should_approach():
					self.tacs.add_approach()
				else:
					self.tacs.add_five_foot_step()

			if (self.options and self.options.get("add_halt_before")):
				self.tacs.add_halt()

			if (is_personal is None): is_personal = self._is_personal()
			if (is_personal):
				self.tacs.add_target_self()
			else:
				self._check_target()
				if (self.target):
					self.tacs.add_target_obj(self.target.id)
				else:
					self.tacs.add_target_closest()
		
			result = self._add_spell_exec()
		else:
			result = EDOT_OK

		if (result): 
			return result

		return EDOT_OK

	def _check_target(self):
		# in most cases no action, but for area spells could be useful
		return

	def _skip_five_foot_step(self):
		return None if not self.options else self.options.get("skip_five_foot_step")

	def set_target_first(self, targets):
		if not self.spells_left(): 
			return
		for t in targets:
			self.set_target(t)
			if not self.execute(True):
				return t
		self.set_target(None)
		return

	def set_target_first_self(self, targets):
		self.find_target_first(targets)
		return self

class STDivineFavor(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_divine_favor

class STHoldPerson(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_hold_person

	def _except_q(self): return toee.Q_Critter_Is_Held

class STCauseFear(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_cause_fear

	def _except_q(self): return toee.Q_Critter_Is_Afraid

	def _is_personal(self): return 0 # bug currently 2021-10-04

class STDoom(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_doom

	def _except_spell_condition(self): return toee.sp_Doom

	def _is_personal(self): return 0 # bug currently 2021-10-04

class STBlindnessDeafness(SpellTactic): #todo verify
	@staticmethod
	def _get_spell_num(): return toee.spell_blindness_deafness
	def _except_q(self): return toee.Q_Critter_Is_Blinded
	def _is_personal(self): return 0

class STBless(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_bless

	def _is_personal(self): return 1

	def _except_spell_condition(self): return toee.sp_Bless

class STBaneSelf(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_bane

	def _is_personal(self): return 1

class STShieldOfFaith(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_shield_of_faith

class STSoundBurst(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_sound_burst

	def _check_target(self):
		spell_range_a = self.options.get("spell_range")
		spell_range = self._spell_range if spell_range_a is None else spell_range_a
		return

class STMagicMissle(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_magic_missile

	def _is_personal(self): return 0 # bug currently 2021-11-27

class STTashasHideousLaughter(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_tashas_hideous_laughter

	def _is_personal(self): return 0 # check

	def _except_q(self): return self.npc.d20_query_has_spell_condition(toee.sp_Tashas_Hideous_Laughter)

class STMirrorImage(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_mirror_image

class STMageArmor(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_mage_armor

class STScorchingRay(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_scorching_ray

	def _is_personal(self): return 0 # check

class STAcidSplash(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_acid_splash

	def _is_personal(self): return 0 # check

class STRayOfEnfeeblement(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_ray_of_enfeeblement

	def _is_personal(self): return 0 # check

class STSummonMonster(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_summon_monster_i

	def _is_no_target(self): return 1

	def _is_personal(self): return 1

class STSummonMonster2(STSummonMonster):
	@staticmethod
	def _get_spell_num(): return toee.spell_summon_monster_ii

class STSummonMonster3(STSummonMonster):
	@staticmethod
	def _get_spell_num(): return toee.spell_summon_monster_iii

class STInflictWoundsLight(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_inflict_light_wounds

	def _skip_five_foot_step(self): return True

class STInflictWoundsModerate(STInflictWoundsLight):
	@staticmethod
	def _get_spell_num(): return toee.spell_inflict_moderate_wounds

class STInflictWoundsSerious(STInflictWoundsLight):
	@staticmethod
	def _get_spell_num(): return toee.spell_inflict_serious_wounds

class STFireball(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_fireball

	def _add_spell_exec(self):
		self.tacs.add_cast_fireball_code(self.spells.prep_spell(self.npc, self._get_spell_num()))
		return EDOT_OK

class STDeepSlumber(STFireball):
	@staticmethod
	def _get_spell_num(): return toee.spell_deep_slumber

class STSlow(STFireball):
	@staticmethod
	def _get_spell_num(): return toee.spell_slow

class STWeb(STFireball):
	@staticmethod
	def _get_spell_num(): return toee.spell_web

class STWebSingle(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_web

	def pick_target_best(self, available_targets, skip_if_any_has_effect = True):
		target = None
		if available_targets:
			print("checking pick_target_best")
			for obj in available_targets:
				assert isinstance(obj, toee.PyObjHandle)
				print("checking pick_target_best obj: {}".format(obj))
				if (obj.d20_query_with_data(toee.Q_Critter_Has_Spell_Active, self._get_spell_num(), 0) 
					or obj.d20_query_has_spell_condition(self._get_spell_num())
					or obj.d20_query(toee.Q_Is_BreakFree_Possible)):
					print("FOUND HAS EFFECT!")
					if skip_if_any_has_effect:
						return None
					else:
						continue
				target = obj
				if not skip_if_any_has_effect:
					break
		self.target = target
		print("pick_target_best pick_target_best: {}".format(target))
		return target

class STGlitterdust(STFireball):
	@staticmethod
	def _get_spell_num(): return toee.spell_glitterdust

class STDominatePerson(STInflictWoundsLight):
	@staticmethod
	def _get_spell_num(): return toee.spell_dominate_person

	def pick_target_best(self, available_targets):
		target = None
		target_will = 100
		if available_targets:
			for obj in available_targets:
				assert isinstance(obj, toee.PyObjHandle)
				if obj.d20_query_with_data(toee.Q_Critter_Has_Spell_Active, self._get_spell_num(), 0):
					continue
				obj_will = obj.stat_level_get(toee.stat_save_willpower)
				if obj_will < target_will:
					target = obj
					target_will = obj_will
		self.target = target
		print("pick_target_best pick_target_best: {}".format(target))
		return target

class STBlurSelf(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_blur
	def _is_personal(self): return 1

class STDisplacementSelf(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_displacement
	def _is_personal(self): return 1

class STDisplacementApproach(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_displacement
	def _is_personal(self): return 0
	def _should_approach(self): return 1

class STBullsStrengthSelf(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_bulls_strength
	def _is_personal(self): return 1

class STHasteSelf(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_haste
	def _is_personal(self): return 1

	def _add_spell_exec(self):
		self.tacs.add_cast_area_code(self.spells.prep_spell(self.npc, self._get_spell_num()))
		return EDOT_OK

class STSilenceParty(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_silence

	def _add_spell_exec(self):
		self.tacs.add_cast_party_code(self.spells.prep_spell(self.npc, self._get_spell_num()))
		return EDOT_OK

class STSilence(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_silence

class STCommand(SpellTactic):
	@staticmethod
	def _get_spell_num(): return toee.spell_command
	def _except_spell_condition(self): return toee.sp_Command
	def _is_personal(self): return 0
