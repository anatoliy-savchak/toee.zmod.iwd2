import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py06610_daemon_corinth, py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, module_globals, item_knowstone

MODULE_SCRIPT_ID = 6611

def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)

def cs(): return py06610_daemon_corinth.cs()


class CtrlThugBase(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID

		#npc.feat_add(toee.feat_armor_proficiency_light)
		#npc.feat_add(toee.feat_armor_proficiency_medium)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_EVIL) 

		return

class CtrlThug(CtrlThugBase):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlThug, self).after_created(npc)

		nameid = utils_toee.make_custom_name("Thug")
		if (nameid):
			npc.obj_set_int(toee.obj_f_critter_description_unknown, nameid)
			npc.obj_set_int(const_toee.obj_f_description_correct, nameid)
		npc.obj_set_int(toee.obj_f_critter_portrait, 7760) # Retainer

		#npc.feat_add(toee.feat_toughness) #removed, hp too big, although it was in vanilla
		npc.feat_add(toee.feat_weapon_focus_longsword)

		utils_npc_build.NPCAbilitiesSetup(10, 16).generate().focus_melee().npc_setup_random(npc)
		#npc.make_class(toee.stat_level_fighter, 1) # should be warrior, but meh
		npc.make_class(const_toee.stat_level_npc_warriror, 1) # should be warrior, but meh

		npc.feat_add(toee.feat_iron_will, 1)

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, npc)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc).item_flag_set(toee.OIF_NO_LOOT)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CAP_LEATHER, npc).item_flag_set(toee.OIF_NO_LOOT)
		
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, npc).obj_set_int(toee.obj_f_ammo_quantity, 1)
		utils_item.item_money_create_in_inventory(npc, 0, 4)

		npc.item_wield_best_all()
		#utils_npc.npc_generate_hp(npc)
		utils_npc.npc_generate_hp_avg_first(npc)
		return

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		foes_adjacent = self._vars_tactics.get("foes_adjacent")
		assert isinstance(foes_adjacent, list)
		foes_threatening = self._vars_tactics.get("foes_threatening")
		assert isinstance(foes_threatening, list)

		current_primary_ranged = utils_npc.npc_get_weapon(npc, 1)

		tac = utils_tactics.TacticsHelper(self.get_name())
		
		target = toee.OBJ_HANDLE_NULL
		if (not target and foes_threatening): target = foes_threatening[0]
		if (not target and foes_adjacent): target = foes_adjacent[0]
		if (target):
			tac.add_target_obj(target.id)
			tac.add_go_melee()
			tac.add_attack()
		else:
			tac.add_target_low_ac()
			if (current_primary_ranged):
				if (toee.game.random_range(0, 1)):
					tac.add_ready_vs_spell()
				else:
					tac.add_attack()
					tac.add_go_melee()
					tac.add_halt()
			else:
				tac.add_attack()

		tac.add_total_defence()
		print("create_tactics {}".format(npc))
		return tac


class CtrlThugLeader(CtrlThugBase):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlThugLeader, self).after_created(npc)

		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID

		utils_npc.npc_abilities_set(npc, [16, 15, 14, 10, 9, 9])
		#utils_npc.npc_abilities_set(npc, [1, 15, 14, 10, 9, 9])
		#npc.make_class(toee.stat_level_fighter, 3) # should be warrior, but meh
		npc.make_class(const_toee.stat_level_npc_warriror, 3) 

		nameid = utils_toee.make_custom_name("Thug Leader")
		if (nameid):
			npc.obj_set_int(toee.obj_f_critter_description_unknown, nameid)
			npc.obj_set_int(const_toee.obj_f_description_correct, nameid)
		npc.obj_set_int(toee.obj_f_critter_portrait, 7450) # Rentsch

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		if (hairStyle):
			hairStyle.style = const_toee.hair_style_shorthair
			hairStyle.color = const_toee.hair_color_red
			hairStyle.update_npc(npc)

		#npc.feat_add(toee.feat_armor_proficiency_heavy) # fighter has it
		npc.feat_add(toee.feat_improved_initiative)
		#npc.feat_add(toee.feat_improved_grapple) # alter: trip
		npc.feat_add(toee.feat_improved_trip) # alter: trip
		npc.feat_add(toee.feat_rapid_reload)
		#npc.feat_add(toee.feat_weapon_focus_longsword) # alter: trip
		npc.feat_add(toee.feat_weapon_focus_light_flail)
		npc.feat_add(toee.feat_cleave, 1)

		npc.condition_add_with_args("AI_Improved_Trip_Aoo", 0, 0)

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SPLINT_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_3, npc)

		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc).item_flag_set(toee.OIF_NO_LOOT)
		#utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CAP_LEATHER, npc).item_flag_set(toee.OIF_NO_LOOT)
		
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_FLAIL, npc)
		utils_item.item_money_create_in_inventory(npc, 0, 8)

		npc.item_wield_best_all()
		#utils_npc.npc_generate_hp(npc)
		utils_npc.npc_generate_hp_avg_first(npc)
		return

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#debug.breakp("create_tactics")

		foes_adjacent = self._vars_tactics.get("foes_adjacent")
		assert isinstance(foes_adjacent, list)
		foes_threatening = self._vars_tactics.get("foes_threatening")
		assert isinstance(foes_threatening, list)

		tac = utils_tactics.TacticsHelper(self.get_name())
		
		target = self.tactics_determine_target(npc, 0)
		if (target):
			if (target.d20_query(toee.Q_Prone)):
				tac.add_target_obj(target.id)
				tac.add_attack()
			else:
				#tac.add_d20_action(toee.D20A_TRIP, 0)
				tac.add_trip()
		else:
			tac.add_target_closest()
			tac.add_approach_single()
			tac.add_attack()

		#tac.add_attack_threatened()
		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

	def do_execute_strategy(self, npc, tgt):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(tgt, toee.PyObjHandle)

		tac = tpai.AiTactic()
		tac.performer = npc
		tac.target = tgt

		res = (0, None)

		# get new target
		target_new = toee.OBJ_HANDLE_NULL
		if (1):
			foes_adjacent = self._vars_tactics.get("foes_adjacent")
			assert isinstance(foes_adjacent, list)
			foes_threatening = self._vars_tactics.get("foes_threatening")
			assert isinstance(foes_threatening, list)

			print("foes_threatening: {}".format(foes_threatening))
			if (not target_new and foes_threatening): target_new = foes_threatening[0]
			print("foes_adjacent: {}".format(foes_adjacent))
			if (not target_new and foes_adjacent): target_new = foes_adjacent[0]
			print("target_new: {}".format(target_new))
			if (target_new):
				tac.target = target_new

		if (not tac.target):
			tdef = tpai.get_tactic_def("target closest")
			print("exec: target closest, tdef: {}".format(tdef))
			result = tdef.execute(tac)
			print("\texec res: target closest, result: {}, tac.target: {}".format(result, tac.target))

		if (tac.target and not tac.target.d20_query(toee.Q_Prone)):
			print("exec: trip")
			res = utils_strategy.tactic_exec(npc, "trip", tac)
			print("\texec res: trip, result: {}, tac.target: {}".format(res[0], tac.target))

		if (not res[0]):
			tdef = tpai.get_tactic_def("attack")
			print("exec: attack, tdef: {}, tac.target: {}".format(tdef, tac.target))
			result = tdef.execute(tac)
			print("\texec res: attack, result: {}, tac.target: {}".format(result, tac.target))

		return 1

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		# only first time
		if not attachee.has_met(toee.game.leader):
			pc = utils_npc.npc_find_nearest_pc_prefer_leader(attachee)
			if (pc):
				attachee.turn_towards(pc)
				pc.begin_dialog(attachee, 110)
		return toee.RUN_DEFAULT

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.turn_towards(triggerer)
		triggerer.begin_dialog(attachee, 110)
		return toee.SKIP_DEFAULT

class CtrlLizardman(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return py04000_monster_manual1_p1.CtrlLizardfolkBase.get_proto_id()

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlLizardman, self).after_created(npc)

		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID

		# utils_npc.npc_abilities_set(npc, [13, 10, 13, 9, 10, 10]) # average
		stats = utils_npc.stats_sum(utils_npc.stats_roll(8, 12), [3, 0, 3, -1, 0, 0])
		utils_npc.npc_abilities_set(npc, stats)

		wealth_gp = toee.game.random_range(72, 99)
		utils_item.item_money_create_in_inventory(npc, 0, wealth_gp)
		return

class CtrlLizardmanLeaderC02(CtrlLizardman):
	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		if (attachee.is_active_combatant()):
			attachee.scripts[const_toee.sn_dialog] = 0
			attachee.scripts[const_toee.sn_heartbeat] = 0
			return toee.RUN_DEFAULT

		# only first time
		if not attachee.has_met(toee.game.leader):
			pc = utils_npc.npc_find_nearest_pc_prefer_leader(attachee)
			if (pc):
				attachee.turn_towards(pc)
				pc.begin_dialog(attachee, 120)
		return toee.RUN_DEFAULT

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.turn_towards(triggerer)
		triggerer.begin_dialog(attachee, 120)
		return toee.SKIP_DEFAULT

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlLizardmanLeaderC02, self).after_created(npc)

		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		attachee.scripts[const_toee.sn_dialog] = 0
		attachee.scripts[const_toee.sn_heartbeat] = 0
		return toee.RUN_DEFAULT

class CtrlLizardmanClericC03(CtrlLizardman):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlLizardmanClericC03, self).after_created(npc)

		npc.obj_set_int(toee.obj_f_critter_portrait, 3530)

		#utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # as in KoTC
		
		utils_npc_build.NPCAbilitiesSetup(10, 16).generate().focus_cleric().npc_setup_random(npc)
		cleric_levels = 4
		npc.make_class(toee.stat_level_cleric, cleric_levels) 

		npc.skill_ranks_set(toee.skill_concentration, 3 + (cleric_levels-1)*1)

		npc.feat_add(toee.feat_combat_casting)
		npc.feat_add(toee.feat_greater_weapon_focus_unarmed_strike_medium_sized_being, 1)

		npc.item_wield_best_all()
		#utils_npc.npc_generate_hp(npc)
		utils_npc.npc_generate_hp_avg_first(npc)
		return
	
	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.stat_level_cleric
		caster_level = attachee.highest_divine_caster_level
		# 2
		self.spells.add_spell(toee.spell_hold_person, stat_class, caster_level)
		self.spells.add_spell(toee.spell_cure_moderate_wounds, stat_class, caster_level)
		# 1
		self.spells.add_spell(toee.spell_divine_favor, stat_class, caster_level)
		self.spells.add_spell(toee.spell_cause_fear, stat_class, caster_level)
		self.spells.add_spell(toee.spell_shield_of_faith, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_cure_minor_wounds, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#debug.breakp("create_tactics")

		foes_adjacent = self._vars_tactics.get("foes_adjacent")
		assert isinstance(foes_adjacent, list)
		foes_threatening = self._vars_tactics.get("foes_threatening")
		assert isinstance(foes_threatening, list)

		tac = utils_tactics.TacticsHelper(self.get_name())
		
		target = self.tactics_determine_target(npc, 1)
		npc.obj_set_obj(toee.obj_f_npc_combat_focus, target)

		while (target):
			if (not utils_npc_spells_tactics.STShieldOfFaith(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STDivineFavor(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STHoldPerson(npc, self.spells, tac, target).execute()):
				break

			if (not utils_npc_spells_tactics.STCauseFear(npc, self.spells, tac, target).execute()):
				break

			tac.add_target_obj(target.id)
			tac.add_attack()
			tac.add_approach_single()
			tac.add_attack()
			tac.add_ready_vs_approach()
			tac.add_stop()
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

class CtrlLizardmanShamanC04(CtrlLizardman):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlLizardmanShamanC04, self).after_created(npc)

		npc.obj_set_int(toee.obj_f_critter_portrait, 3530)

		#utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # as in KoTC
		
		utils_npc_build.NPCAbilitiesSetup(10, 16).generate().focus_cleric().npc_setup_random(npc)
		cleric_levels = 5
		npc.make_class(toee.stat_level_cleric, cleric_levels) 

		npc.skill_ranks_set(toee.skill_concentration, 3 + (cleric_levels-1)*1)

		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 4-4) # natural bab: +4
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 2) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d4").packed)

		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 1, const_toee.nwt_bite)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 1, 4-2-4) # natural bab: +4, multiattack
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 1, 1) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 1, toee.dice_new("1d4").packed)

		npc.feat_add(toee.feat_combat_casting)
		#npc.feat_add(toee.feat_greater_weapon_focus_unarmed_strike_medium_sized_being, 1)

		npc.item_wield_best_all()
		#utils_npc.npc_generate_hp(npc)
		utils_npc.npc_generate_hp_avg_first(npc)
		return
	
	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.stat_level_cleric
		caster_level = attachee.highest_divine_caster_level
		# 3:2
		self.spells.add_spell(toee.spell_inflict_serious_wounds, stat_class, caster_level)
		self.spells.add_spell(toee.spell_summon_monster_iii, stat_class, caster_level)
		# 2:3
		self.spells.add_spell(toee.spell_silence, stat_class, caster_level)
		self.spells.add_spell(toee.spell_hold_person, stat_class, caster_level)
		self.spells.add_spell(toee.spell_cure_moderate_wounds, stat_class, caster_level)
		self.spells.add_spell(toee.spell_inflict_moderate_wounds, stat_class, caster_level)
		# 1:4
		self.spells.add_spell(toee.spell_divine_favor, stat_class, caster_level)
		self.spells.add_spell(toee.spell_cause_fear, stat_class, caster_level)
		self.spells.add_spell(toee.spell_shield_of_faith, stat_class, caster_level)
		self.spells.add_spell(toee.spell_cure_light_wounds, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_cure_minor_wounds, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#debug.breakp("create_tactics")

		foes_adjacent = self._vars_tactics.get("foes_adjacent")
		assert isinstance(foes_adjacent, list)
		foes_threatening = self._vars_tactics.get("foes_threatening")
		assert isinstance(foes_threatening, list)

		tac = utils_tactics.TacticsHelper(self.get_name())
		
		target = self.tactics_determine_target(npc, 1)
		npc.obj_set_obj(toee.obj_f_npc_combat_focus, target)

		while (target):
			if (self.tactics_process_critical(npc, tac)):
				break

			if (not utils_npc_spells_tactics.STSummonMonster3(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STInflictWoundsSerious(npc, self.spells, tac).execute()):
				break

			if (len(foes_adjacent) == 0 and not utils_npc_spells_tactics.STShieldOfFaith(npc, self.spells, tac).execute()):
				break

			if (len(foes_adjacent) == 0 and not utils_npc_spells_tactics.STDivineFavor(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STHoldPerson(npc, self.spells, tac, target).execute()):
				break

			if (not utils_npc_spells_tactics.STCauseFear(npc, self.spells, tac, target).execute()):
				break

			tac.add_target_obj(target.id)
			tac.add_attack()
			tac.add_approach_single()
			tac.add_attack()
			tac.add_ready_vs_approach()
			tac.add_stop()
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

class CtrlLizardmanKing(CtrlLizardman):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlLizardmanKing, self).after_created(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID

		utils_npc.npc_hitdice_set(npc, 1, 8, 0) # as in KoTC
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # as in KoTC
		
		utils_npc.npc_abilities_set(npc, [16, 14, 17, 10, 12, 8])
		npc.make_class(toee.stat_level_fighter, 4) 

		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 4-4) # natural bab: +4
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 2) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d4").packed)

		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 1, const_toee.nwt_bite)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 1, 4-2-4) # natural bab: +4, multiattack
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 1, 1) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 1, toee.dice_new("1d4").packed)

		npc.feat_add(toee.feat_cleave)
		#npc.feat_add(toee.feat_weapon_focus_halberd)
		npc.feat_add(toee.feat_improved_trip) # alter: trip
		npc.feat_add(toee.feat_weapon_focus_heavy_flail)
		npc.feat_add(toee.feat_toughness)
		npc.feat_add(toee.feat_great_fortitude, 1)

		npc.condition_add_with_args("AI_Improved_Trip_Aoo", 0, 0)

		#utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_HALBERD_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_FLAIL_HEAVY_MASTERWORK, npc)
		npc.item_wield_best_all()
		#utils_npc.npc_generate_hp(npc)
		utils_npc.npc_generate_hp_avg_first(npc, 0)
		return

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#debug.breakp("create_tactics")

		foes_adjacent = self._vars_tactics.get("foes_adjacent")
		assert isinstance(foes_adjacent, list)
		foes_threatening = self._vars_tactics.get("foes_threatening")
		assert isinstance(foes_threatening, list)

		tac = utils_tactics.TacticsHelper(self.get_name())
		
		target = self.tactics_determine_target(npc, 0)
		if (target):
			if (target.d20_query(toee.Q_Prone)):
				tac.add_target_obj(target.id)
				tac.add_attack()
			else:
				if (not target in foes_adjacent and npc.distance_to(target) <= 10):
					tac.add_five_foot_step()
				tac.add_trip()
		else:
			tac.add_target_closest()
			tac.add_approach_single()
			tac.add_attack()

		#tac.add_attack_threatened()
		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		for npc in toee.game.obj_list_vicinity(attachee.location, toee.OLC_CRITTERS):
			if (npc == attachee or attachee.allegiance_shared(npc)): 
				npc.condition_add("SurpriseRound2")
			else:
				npc.condition_add("Surprised2")
		return toee.RUN_DEFAULT

class CtrlLizardmanClericC07(CtrlLizardman):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlLizardmanClericC07, self).after_created(npc)

		npc.obj_set_int(toee.obj_f_critter_portrait, 3530)

		#utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # as in KoTC
		
		utils_npc_build.NPCAbilitiesSetup(10, 16).generate().focus_cleric().npc_setup_random(npc)
		cleric_levels = 1
		npc.make_class(toee.stat_level_cleric, cleric_levels) 

		npc.skill_ranks_set(toee.skill_concentration, 3 + (cleric_levels-1)*1)

		npc.feat_add(toee.feat_combat_casting)

		utils_item.item_create_in_inventory(const_proto_wands.PROTO_WAND_OF_DOOM, npc)
		npc.item_wield_best_all()
		utils_npc.npc_generate_hp_avg_first(npc, 0)
		return
	
	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.stat_level_cleric
		caster_level = attachee.highest_divine_caster_level
		# 1:2
		self.spells.add_spell(toee.spell_cause_fear, stat_class, caster_level)
		self.spells.add_spell(toee.spell_shield_of_faith, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_cure_minor_wounds, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#debug.breakp("create_tactics")

		foes_adjacent = self._vars_tactics.get("foes_adjacent")
		assert isinstance(foes_adjacent, list)
		foes_threatening = self._vars_tactics.get("foes_threatening")
		assert isinstance(foes_threatening, list)

		tac = utils_tactics.TacticsHelper(self.get_name())
		
		target = self.tactics_determine_target(npc, 1)
		npc.obj_set_obj(toee.obj_f_npc_combat_focus, target)

		while (target):
			if (self.tactics_process_critical(npc, tac)):
				break

			if (not utils_npc_spells_tactics.STShieldOfFaith(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STCauseFear(npc, self.spells, tac, target).execute()):
				break

			tac.add_target_obj(target.id)
			tac.add_attack()
			tac.add_approach_single()
			tac.add_attack()
			tac.add_ready_vs_approach()
			tac.add_stop()
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

class CtrlLizardmanWizardC07(CtrlLizardman):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlLizardmanWizardC07, self).after_created(npc)

		npc.obj_set_int(toee.obj_f_critter_portrait, 3530)

		#utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # as in KoTC
		
		utils_npc_build.NPCAbilitiesSetup(10, 16).generate().focus_cleric().npc_setup_random(npc)
		levels = 2
		npc.make_class(toee.stat_level_wizard, levels) 

		npc.skill_ranks_set(toee.skill_concentration, 3 + (levels-1)*1)

		npc.feat_add(toee.feat_combat_casting)

		npc.item_wield_best_all()
		utils_npc.npc_generate_hp_avg_first(npc, 0)
		return
	
	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.stat_level_wizard
		caster_level = attachee.highest_arcane_caster_level
		# 1:2
		self.spells.add_spell(toee.spell_mage_armor, stat_class, caster_level)
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)

		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#debug.breakp("create_tactics")

		foes_adjacent = self._vars_tactics.get("foes_adjacent")
		assert isinstance(foes_adjacent, list)
		foes_threatening = self._vars_tactics.get("foes_threatening")
		assert isinstance(foes_threatening, list)

		tac = utils_tactics.TacticsHelper(self.get_name())
		
		target = self.tactics_determine_target(npc, 1)
		npc.obj_set_obj(toee.obj_f_npc_combat_focus, target)

		while (target):
			if (self.tactics_process_critical(npc, tac)):
				break

			if (not utils_npc_spells_tactics.STMageArmor(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STMagicMissle(npc, self.spells, tac, target).execute()):
				break

			tac.add_target_obj(target.id)
			tac.add_attack()
			tac.add_approach_single()
			tac.add_attack()
			tac.add_ready_vs_approach()
			tac.add_stop()
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

class CtrlGiantSnake(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14388 

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID

		npc.feat_add(toee.feat_improved_trip, 1)

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		return

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#debug.breakp("create_tactics")

		foes_adjacent = self._vars_tactics.get("foes_adjacent")
		assert isinstance(foes_adjacent, list)
		foes_threatening = self._vars_tactics.get("foes_threatening")
		assert isinstance(foes_threatening, list)

		tac = utils_tactics.TacticsHelper(self.get_name())
		
		target = self.tactics_determine_target(npc, 0)
		if (target):
			if (target.d20_query(toee.Q_Prone)):
				tac.add_target_obj(target.id)
				tac.add_attack()
			else:
				if (not target in foes_adjacent and npc.distance_to(target) <= 10):
					tac.add_five_foot_step()
				tac.add_trip()
		else:
			tac.add_target_closest()
			tac.add_approach_single()
			tac.add_attack()

		#tac.add_attack_threatened()
		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

class CtrlCommonerGarnWife(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WOMAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		#npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		utils_npc.npc_description_set_new(npc, "Commoner")

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		# create inventory
		utils_item.item_create_in_inventory(self.get_cloth_garb(), npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		
		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		return

	def get_cloth_garb(self): return const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_BLUE

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.turn_towards(triggerer)
		attachee.float_text_line("Hello, please talk to Garn.")
		return toee.SKIP_DEFAULT

class CtrlCommonerGarnDaughter(CtrlCommonerGarnWife):
	def get_cloth_garb(self): return const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_OCHRE

class CtrlCommonerGarn(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		#npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		utils_npc.npc_description_set_new(npc, "Garn")

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		# create inventory
		utils_item.item_create_in_inventory(self.get_cloth_garb(), npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		
		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		return

	def get_cloth_garb(self): return const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_RED

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		quest_liberate_state = toee.game.quests[module_quests.QUEST_CORINTH_LIBERATE].state
		attachee.turn_towards(triggerer)
		if (not attachee.has_met(triggerer) or quest_liberate_state < toee.qs_mentioned):
			triggerer.begin_dialog(attachee, 200) # meet and overview
		elif (quest_liberate_state < toee.qs_completed):
			if (cs().quest_evaluate_corinth_liberated()):
			   triggerer.begin_dialog(attachee, 250) # congrats and notify about free slaves quest
			else:
				triggerer.begin_dialog(attachee, 290) # urge liberate
		else: # quest_liberate_state >= toee.qs_completed
			triggerer.begin_dialog(attachee, 280) # hail heroes
		return toee.SKIP_DEFAULT

	@staticmethod
	def dialog_ensure_corinth_liberate_quest(new_state = toee.qs_mentioned):
		q = toee.game.quests[module_quests.QUEST_CORINTH_LIBERATE]
		if (q.state < new_state):
			q.state = new_state
		return

	@staticmethod
	def dialog_award_corinth_liberate_quest():
		q = toee.game.quests[module_quests.QUEST_CORINTH_LIBERATE]
		if (q.state < toee.qs_completed):
			q.state = qs_completed

			key = toee.game.obj_create(const_proto_items.PROTO_KEY_IRON_RUSTY, toee.game.leader.location)
			key.obj_set_int(toee.obj_f_key_key_id, module_consts.KEY_CORINTH_BARN)

			utils_obj.obj_timed_receive(toee.game.leader, key, 100)
		return

	@staticmethod
	def dialog_ensure_corinth_free_slaves_quest():
		q = toee.game.quests[module_quests.QUEST_CORINTH_FREE_SLAVES]
		if (q.state < toee.qs_mentioned): 
			q.state = toee.qs_accepted
		return

class CtrlCommonerMarkus(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		#npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		utils_npc.npc_description_set_new(npc, "Markus")

		npc.obj_set_int(toee.obj_f_critter_portrait, 6340) # NPC_6341_m_JakkBorton
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		# create inventory
		utils_item.item_create_in_inventory(self.get_cloth_garb(), npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		
		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		return

	def get_cloth_garb(self): return const_proto_cloth.PROTO_CLOTH_GARB_NOBLE_PURPLE

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		# is disabled in dialog_initial_started for optimization!

		# only first time
		if not attachee.has_met(toee.game.leader):
			pc = utils_npc.npc_find_nearest_pc_prefer_leader(attachee)
			if (pc):
				self.dialog(attachee, pc)
				#attachee.turn_towards(pc)
				#pc.begin_dialog(attachee, 350)
		return toee.RUN_DEFAULT

	def dialog_initial_started(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_heartbeat] = 0
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.turn_towards(triggerer)
		if (not attachee.has_met(triggerer)):
			self.dialog_initial_started(attachee)
			triggerer.begin_dialog(attachee, 350) # meet and overview
		else: # quest_liberate_state >= toee.qs_completed
			triggerer.begin_dialog(attachee, 390) # come back
		return toee.SKIP_DEFAULT

	@staticmethod
	def dialog_not_lizardmen():
		toee.game.quests[module_quests.QUEST_CORINTH_NOT_LIZARDMEN].state = toee.qs_completed
		toee.game.quests[module_quests.QUEST_INVADE_ORC_FORT].state = toee.qs_mentioned
		return

	@staticmethod
	def dialog_witch_mentioned():
		if (not rumor_control.is_rumor_given(module_quests.RUMOR_CORINTH_MARKUS_WITCH_MENTIONED)):
			rumor_control.rumor_give(module_quests.RUMOR_CORINTH_MARKUS_WITCH_MENTIONED)
		return

	@staticmethod
	def get_shoplist():
		# todo add adamantine chain shirt, reduce monster arcane 3
		return [const_proto_weapon.PROTO_WEAPON_LONGBOW_COMPOSITE_16_PLUS1
		  , const_proto_armor.PROTO_ARMOR_MITHRAL_SHIRT
		  , const_proto_rings.PROTO_RING_OF_PROTECTION_PLUS_2
		  , const_proto_scrolls.PROTO_SCROLL_OF_CHARM_MONSTER
		  , const_proto_scrolls.PROTO_SCROLL_OF_REDUCE_PERSON]

	@staticmethod
	def get_shoplist_knowstones():
		return [toee.spell_charm_monster, toee.spell_reduce]

	def dialog_barter(self, npc):
		utils_item.barter_list(npc, self.get_shoplist(), 1, item_knowstone.knowstone_create_list(self.get_shoplist_knowstones(), npc.location))
		return

class CtrlCommonerMarkusBodyguard(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		#npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		npc.make_class(const_toee.stat_level_npc_warriror, 4)

		utils_npc.npc_description_set_new(npc, "Bodyguard")

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		# create inventory
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_HALF_PLATE, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_MASTERWORK_STEEL, npc, 1, 1)
		
		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		return

class CtrlWitch(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WOMAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID

		utils_npc.npc_description_set_new(npc, "Old Witch")

		npc.make_class(toee.stat_level_wizard, 4)

		npc.obj_set_int(toee.obj_f_critter_portrait, 7430) # NPC_7431_m_Skole
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_longhair
		hairStyle.color = const_toee.hair_color_red
		hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		# create inventory
		utils_item.item_create_in_inventory(self.get_cloth_garb(), npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		
		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		return

	def get_cloth_garb(self): return const_proto_cloth.PROTO_CLOTH_ROBES_GREEN

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.turn_towards(triggerer)
		if (not attachee.has_met(triggerer)):
			triggerer.begin_dialog(attachee, 500) # meet and overview
		elif (not self.dialog_can_fort()):
			triggerer.begin_dialog(attachee, 500) # from the beginning
		elif (not self.dialog_quest_helped()):
			triggerer.begin_dialog(attachee, 600) # continue Fort help quest
		else: 
			triggerer.begin_dialog(attachee, 610) # after Fort help quest
		return toee.SKIP_DEFAULT

	@staticmethod
	def dialog_can_fort():
		return rumor_control.is_rumor_given(module_quests.RUMOR_CORINTH_MARKUS_WITCH_MENTIONED)

	@staticmethod
	def dialog_quest_helped():
		return toee.game.quests[module_quests.QUEST_CORINTH_WITCH_HELP] >= toee.qs_completed

	@staticmethod
	def dialog_ensure_witch_help_quest(new_state = toee.qs_mentioned):
		q = toee.game.quests[module_quests.QUEST_CORINTH_WITCH_HELP]
		if (q.state < new_state):
			q.state = new_state
		return

	@classmethod
	def dialog_quest_help_start(cls, npc):
		assert isinstance(npc, toee.PyObjHandle)
		toee.game.quests[module_quests.QUEST_CORINTH_WITCH_HELP].state = toee.qs_accepted
		npc.object_flag_set(toee.OF_OFF)
		npc.object_flag_set(toee.OF_DONTDRAW)
		return

	@classmethod
	def dialog_quest_help_complete_do_effect(cls, npc):
		assert isinstance(npc, toee.PyObjHandle)
		# sleep
		for foe in toee.game.obj_list_range(npc.location, 20, toee.OLC_NPC):
			if (not foe.faction_has(factions_zmod.FACTION_ENEMY)): continue
			foe.condition_add_with_args("Napping", 0, 20)
		return

	@classmethod
	def dialog_quest_help_complete_meet(cls, npc):
		assert isinstance(npc, toee.PyObjHandle)
		toee.game.quests[module_quests.QUEST_CORINTH_WITCH_HELP].state = toee.qs_completed
		toee.game.global_flags[module_globals.GFLAG_ORC_FORT_SKIP_ASSAULT] = 1
		toee.game.quests[module_quests.QUEST_INVADE_ORC_FORT].state = toee.qs_completed
		return

	@classmethod
	def dialog_quest_help_complete_begone(cls, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.destroy()
		return

	@classmethod
	def dialog_quest_help_complete_omitted(cls):
		toee.game.quests[module_quests.QUEST_CORINTH_WITCH_HELP].state = toee.qs_botched
		toee.game.quests[module_quests.QUEST_INVADE_ORC_FORT].state = toee.qs_completed
		return
