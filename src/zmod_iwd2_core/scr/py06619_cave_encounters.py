import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, py14764_npc_portal, py06621_kots_monsters
import py06618_daemon_cave_entrance, py06620_daemon_cave_level2

MODULE_SCRIPT_ID = 6619

def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)

def cs(): return None

class CtrlCavesPortalGroundToLevel1(py14764_npc_portal.CtrlPortalDownImmediate):
	def get_dest_location(self): return module_consts.ZMOD_CAVE_LEVEL2_ENTRY_ENTRY_NW
	def get_dest_map(self): return module_consts.MAP_ID_ZMOD_CAVE_LEVEL2

class CtrlCavesPortalLevel1ToGround(py14764_npc_portal.CtrlPortalUpImmediate):
	def get_dest_location(self): return module_consts.ZMOD_CAVE_ENTRY_ENTRY_SW
	def get_dest_map(self): return module_consts.MAP_ID_ZMOD_CAVE_ENTRANCE

class CtrlBrownBear(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14996

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID

		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30
		npc.condition_add("Multiattack")
		
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_improved_grapple)
		npc.feat_add(toee.feat_alertness, 1)

		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlBrownBearLeader(CtrlBrownBear):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlBrownBearLeader, self).after_created(npc)

		npc.critter_flag_unset(toee.OCF_MONSTER)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.scripts[const_toee.sn_heartbeat] = 0
		attachee.turn_towards(triggerer)
		if not attachee.has_met(triggerer):
			triggerer.begin_dialog(attachee, 10)
			return toee.SKIP_DEFAULT
		else:
			triggerer.begin_dialog(attachee, 100)
		return toee.SKIP_DEFAULT

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		# is disabled in dialog_initial_started for optimization!

		# only first time
		if not attachee.has_met(toee.game.leader):
			pc = utils_npc.npc_find_nearest_pc_prefer_leader(attachee)
			if (pc):
				attachee.turn_towards(pc)
				pc.begin_dialog(attachee, 10)
		return toee.RUN_DEFAULT

	def dialog_charge(self, npc, pc):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		npc.critter_flag_set(toee.OCF_MONSTER)
		npc.attack(pc)
		return

	@staticmethod
	def get_quest():
		return toee.game.quests[module_quests.QUEST_CAVE_ENTRANCE_BEAR_DEAD_BODY]

	def dialog_bear_dead_quest_mentioned(self, npc, pc):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		quest = self.get_quest()
		if quest.state < toee.qs_mentioned:
			quest.state = toee.qs_mentioned
		return

	def dialog_can_show_camp_question(self, npc, pc):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		quest = self.get_quest()
		if quest.state >= toee.qs_mentioned and quest.state < toee.qs_completed:
			meat_item = pc.item_find_by_proto(8005)
			if not meat_item:
				return True
		return False

	def dialog_can_show_meat_question(self, npc, pc):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		quest = self.get_quest()
		if quest.state >= toee.qs_mentioned and quest.state < toee.qs_completed:
			meat_item = pc.item_find_by_proto(8005)
			if meat_item:
				return True
		return False

	def dialog_bear_dead_quest_completed(self, npc, pc):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		quest = self.get_quest()
		if quest.state < toee.qs_completed:
			meat_item = pc.item_find_by_proto(8005)
			if meat_item:
				meat_item.destroy()
			quest.state = toee.qs_completed
			py06618_daemon_cave_entrance.cs().dialog_enable_camping()
		return False

class CtrlGiantSpiderGuardC02(py06621_kots_monsters.CtrlGiantSpider):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlGiantSpiderGuardC02, self).after_created(npc)

		npc.critter_flag_unset(toee.OCF_NO_FLEE)
		return

class CtrlGiantSpiderGuardLeaderC02(CtrlGiantSpiderGuardC02):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlGiantSpiderGuardLeaderC02, self).after_created(npc)

		npc.critter_flag_unset(toee.OCF_MONSTER)
		npc.critter_flag_unset(toee.OCF_MUTE)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.scripts[const_toee.sn_heartbeat] = 0
		attachee.turn_towards(triggerer)
		if not attachee.has_met(triggerer):
			triggerer.begin_dialog(attachee, 200)
			return toee.SKIP_DEFAULT
		else:
			triggerer.begin_dialog(attachee, 200)
		return toee.SKIP_DEFAULT

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		# is disabled in dialog_initial_started for optimization!

		# only first time
		if not attachee.has_met(toee.game.leader):
			pc = utils_npc.npc_find_nearest_pc_prefer_leader(attachee)
			if (pc):
				attachee.turn_towards(pc)
				pc.begin_dialog(attachee, 200)
		return toee.RUN_DEFAULT

	def dialog_quest_given(self, npc, pc):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		if toee.game.quests[module_quests.QUEST_CAVE_LEVEL2_SPIDERS_UNDEAD_CLEAR].state < toee.qs_mentioned:
			toee.game.quests[module_quests.QUEST_CAVE_LEVEL2_SPIDERS_UNDEAD_CLEAR].state = toee.qs_mentioned
		npc.critter_flag_set(toee.OCF_MONSTER)
		return

	def dialog_flee(self, npc, pc):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		kill_timout = 8000 #ms
		for obj in toee.game.obj_list_vicinity(npc.location, toee.OLC_NPC):
			if obj != npc and obj.leader_get() == npc:
				obj.critter_flag_set(toee.OCF_MUTE)
				obj.ai_flee_add(pc)
				utils_obj.obj_timed_destroy(obj, kill_timout)

		npc.critter_flag_set(toee.OCF_MUTE)
		npc.ai_flee_add(pc)
		utils_obj.obj_timed_destroy(npc, kill_timout)
		return

class CtrlAmenoptes(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 6540) # NPC_6541_m_Ashrem
		utils_npc.npc_description_set_new(npc, "Amenoptes")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_EVIL) 
		utils_npc.npc_abilities_set(npc, [16, 12, 14, 8, 16, 8])
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		cleric_levels = 5
		npc.make_class(toee.stat_level_cleric, cleric_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_concentration, 3 + (cleric_levels-1)*1 + 10)

		npc.feat_add(toee.feat_weapon_focus_morningstar)
		npc.feat_add(toee.feat_combat_casting, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_ROBES_BROWN, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE_PLUS_1_BLACK, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_MORNINGSTAR_MASTERWORK, npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(50, 70))
		return

	def setup_end(self, npc):
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.stat_level_cleric
		caster_level = attachee.highest_divine_class
		# 3: 2
		self.spells.add_spell(toee.spell_inflict_serious_wounds, stat_class, caster_level)
		self.spells.add_spell(toee.spell_inflict_serious_wounds, stat_class, caster_level)
		# 2: 3
		#self.spells.add_spell(toee.spell_silence, stat_class, caster_level)
		self.spells.add_spell(toee.spell_inflict_moderate_wounds, stat_class, caster_level)
		self.spells.add_spell(toee.spell_inflict_moderate_wounds, stat_class, caster_level)
		self.spells.add_spell(toee.spell_inflict_moderate_wounds, stat_class, caster_level)
		# 2: 4
		self.spells.add_spell(toee.spell_inflict_light_wounds, stat_class, caster_level)
		self.spells.add_spell(toee.spell_inflict_light_wounds, stat_class, caster_level)
		self.spells.add_spell(toee.spell_inflict_light_wounds, stat_class, caster_level)
		self.spells.add_spell(toee.spell_shield_of_faith, stat_class, caster_level)
		self.spells.add_spell(toee.spell_bless, stat_class, caster_level)
		self.spells.add_spell(toee.spell_bane, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())
		while (1):
			if (not utils_npc_spells_tactics.STShieldOfFaith(npc, self.spells, tac).execute()):
				break

			target, kind = self.tactics_determine_targeting_melee(npc)
			if target and kind in ("foes_adjacent", "foes_threatening"):
				if (not utils_npc_spells_tactics.STInflictWoundsSerious(npc, self.spells, tac).execute()):
					break
				if (not utils_npc_spells_tactics.STInflictWoundsModerate(npc, self.spells, tac).execute()):
					break
				if (not utils_npc_spells_tactics.STInflictWoundsLight(npc, self.spells, tac).execute()):
					break

			if (not utils_npc_spells_tactics.STBless(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STBaneSelf(npc, self.spells, tac).execute()):
				break

			# default
			return None
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

class CtrlQuinox(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		return

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 8380) # NPC_8381_m_Verbobonc_Guard
		utils_npc.npc_description_set_new(npc, "Quinox")
		return

	def setup_char(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) 
		utils_npc.npc_abilities_set(npc, [16, 8, 14-2, 11, 11, 9+2])
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_fighter, 2) # 20 is max

		npc.feat_add(toee.feat_weapon_focus_falchion)
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_toughness, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BROWN, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_HALF_PLATE, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_FALCHION_MASTERWORK, npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(20, 40))
		return

	def setup_end(self, npc):
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlVampire(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WOMAN

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 7340) # NPC_7342_s_Paida
		utils_npc.npc_description_set_new(npc, "Vampire")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_NEUTRAL_EVIL) 
		#utils_npc.npc_abilities_set(npc, [19, 17, 10, 12, 11, 12]) typical vampire
		#  Saves have a DC of 10 + 1/2 vampire's HD + vampire's Cha modifier unless noted otherwise.
		utils_npc.npc_abilities_set(npc, [18, 15, 12, 11, 11, 16])
		utils_npc.npc_hitdice_set(npc, 0, 0, 0 )# from vampire
		#utils_npc.npc_hitdice_set(npc, 1, 12, 0 )# from vampire

		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 2) # from vampire
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 6) # from vampire

		# healing should damage
		cat = const_toee.mc_type_undead + ((toee.mc_subtype_human) << 32)
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)

		character_levels = 1
		npc.make_class(toee.stat_level_fighter, character_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_concentration, 3 + (character_levels-1)*1)

		atk_index = 0
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, atk_index, const_toee.nwt_slam)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, atk_index, 1) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, atk_index, 1) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, atk_index, toee.dice_new("1d6").packed)

		on_attacks = (1<<(1-1)) # on first attack
		heal_hp = 5
		npc.condition_add_with_args("Energy_Drain_Su", on_attacks, heal_hp) # Negative Level

		#npc.condition_add_with_args("Monster Regeneration 5", toee.D20DT_POSITIVE_ENERGY, toee.D20DT_POSITIVE_ENERGY)
		npc.condition_add_with_args("Fast_Healing", 5)
		npc.condition_add_with_args("Monster Energy Resistance", toee.D20DT_COLD, 10)
		npc.condition_add_with_args("Monster Energy Resistance", toee.D20DT_ELECTRICITY, 10)

		# "Monster Plant" (No args)
		#* Immunity to all mind-affecting effects (charms, compulsions, phantasms, patterns, and morale effects).
		#* Immunity to poison, sleep effects, paralysis, polymorph, and stunning.
		#* Not subject to critical hits.
		npc.condition_add("Monster Plant")

		npc.condition_add_with_args("Monster_DR", 10, toee.D20DAP_SILVER)

		npc.feat_add(toee.feat_combat_casting)
		npc.feat_add(toee.feat_toughness)
		npc.feat_add(toee.feat_dodge, 1)

		dc_cha = max(npc.stat_base_get(toee.stat_cha_mod), 1)
		dc_wisdom = npc.stat_base_get(toee.stat_wis_mod)
		# dc default = 10 + spell_level + dc_wisdom
		# dc target = 10 + spell_level + dc_cha
		dc_increase = dc_cha - dc_wisdom
		print("dc_increase: {}".format(dc_increase))
		dc_increase += 5 # for this Vampire
		npc.condition_add_with_args("Spell_DC_Mod", 0, dc_increase)

		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_GLOVES_PADDED_TAN, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOAK_RED, npc, 0)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SPLINT_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20))
		return

	def setup_end(self, npc):
		print("npc_generate_hp_avg_first")
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.domain_special
		caster_level = 10
		# 5: 1
		self.spells.add_spell(toee.spell_dominate_person, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())
		while (1):
			target, kind = None, None
			if toee.game.combat_turn == 1:
				target, kind = self.tactics_determine_targeting_melee(npc)
				if not (target and kind in ("foes_adjacent", "foes_threatening")):
					tac.add_charge()
					break

			dominate = utils_npc_spells_tactics.STDominatePerson(npc, self.spells, tac)
			if (dominate.spells_left() > 0):
				foes_can_los = self._vars_tactics["foes_can_los"]
				if dominate.pick_target_best(foes_can_los):
					if not dominate.execute():
						break
			# default
			return None
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

class CtrlGiantSpiderC10Base(py06621_kots_monsters.CtrlGiantSpider):
	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return

class CtrlGiantSpiderC10Cleric(CtrlGiantSpiderC10Base):
	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		utils_npc.npc_hitdice_set(npc, 3, 8, 0) # was 4d8
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum([15, 17, 12, 15, 14, 14], utils_npc.stats_random(-2, 2)))

		npc.condition_add("Monster_Sole_Natural")
		npc.condition_add_with_args("Monster DR Magic", 5)
		npc.condition_add_with_args("Monster_Ability_Drain_Su", 0, 0, toee.stat_strength, toee.dice_new("1d3").packed)

		char_levels = 1
		npc.make_class(toee.stat_level_cleric, char_levels) # 20 is max
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 1) # was 2 CR, but now should be 2 in total

		ecl_levels = npc.stat_level_get(toee.stat_level)

		int_mod = npc.stat_level_get(toee.stat_int_mod)
		npc.skill_ranks_set(toee.skill_tumble, 3 + (ecl_levels-1)*1)
		npc.skill_ranks_set(toee.skill_concentration, 3 + (ecl_levels-1)*int_mod)

		# monster caster level = HD
		# monster DC is based on Wisdom by default

		dc_cha = max(npc.stat_base_get(toee.stat_cha_mod), 1)
		dc_wisdom = npc.stat_base_get(toee.stat_wis_mod)
		# dc default = 10 + spell_level + dc_wisdom
		# dc target = 10 + spell_level + dc_cha
		dc_increase = dc_cha - dc_wisdom
		print("dc_increase: {}".format(dc_increase))
		dc_increase += 2 # for Web
		npc.condition_add_with_args("Spell_DC_Mod", 0, dc_increase)
		
		npc.feat_add(toee.feat_spell_penetration)
		npc.feat_add(toee.feat_combat_casting)
		npc.feat_add(toee.feat_alertness, 1)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(320, 350))
		return

	def setup_end(self, npc):
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.domain_special
		caster_level = 2
		# 2
		self.spells.add_spell(toee.spell_web, stat_class, caster_level)

		stat_class = toee.stat_level_cleric
		caster_level = 1
		# 1: 1
		self.spells.add_spell(toee.spell_bless, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		print("create_tactics CtrlGiantSpiderC10Cleric")
		tac = utils_tactics.TacticsHelper(self.get_name())
		while (1):
			#if (not utils_npc_spells_tactics.STWeb(npc, self.spells, tac).execute()):
			#	break

			web_spell_tactic = utils_npc_spells_tactics.STWebSingle(npc, self.spells, tac)
			if web_spell_tactic.spells_left() > 0:
				foes_can_los = self._vars_tactics["foes_can_los"]
				if not foes_can_los:
					foes_can_los = self._vars_tactics["foes_can_sense"]
				if web_spell_tactic.pick_target_best(foes_can_los):
					if not web_spell_tactic.execute():
						print("web_spell_tactic.execute break")
						break
				else:
					print("web_spell_tactic.pick_target_best: FALSE")

			print("checking other spells")
			if not utils_npc_spells_tactics.STBless(npc, self.spells, tac).execute():
				break

			if not utils_npc_spells_tactics.STBaneSelf(npc, self.spells, tac).execute():
				break

			# default
			print("default")
			return None
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

class CtrlGiantSpiderC10ClericBane(CtrlGiantSpiderC10Cleric):
	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(320, 350))
		utils_item.item_create_in_inventory(const_proto_scrolls.PROTO_SCROLL_OF_PRAYER, npc)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.domain_special
		caster_level = 2
		# 2
		self.spells.add_spell(toee.spell_web, stat_class, caster_level)

		stat_class = toee.stat_level_cleric
		caster_level = 1
		# 1: 1
		self.spells.add_spell(toee.spell_bane, stat_class, caster_level)
		return toee.RUN_DEFAULT


class CtrlGiantSpiderC10(CtrlGiantSpiderC10Base):
	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(250, 280))
		return

class CtrlGiantSpiderC10Blindfight(CtrlGiantSpiderC10Base):
	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(250, 280))
		return

	def setup_feats(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_blind_fight)
		npc.feat_add(toee.feat_alertness, 1)
		return


class CtrlGiantSpiderC10Kutula(CtrlGiantSpiderC10Base):
	@classmethod
	def get_proto_id(cls): return 14048

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		utils_npc.npc_hitdice_set(npc, 4, 8, 0) # was 4d8
		utils_npc.npc_abilities_set(npc, [16, 17, 18, 18, 12, 4])

		npc.condition_add("Monster_Sole_Natural")
		npc.condition_add_with_args("Monster DR Magic", 5)
		npc.condition_add_with_args("Monster_Ability_Drain_Su", 0, 0, toee.stat_strength, toee.dice_new("1d3").packed)

		char_levels = 5
		npc.make_class(toee.stat_level_wizard, char_levels) # 20 is max

		ecl_levels = npc.stat_level_get(toee.stat_level)

		int_mod = npc.stat_level_get(toee.stat_int_mod)
		npc.skill_ranks_set(toee.skill_tumble, 3 + (ecl_levels-1)*1)
		npc.skill_ranks_set(toee.skill_concentration, 3 + (ecl_levels-1)*int_mod)

		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0)

		# monster caster level = HD
		# monster DC is based on Wisdom by default

		dc_cha = max(npc.stat_base_get(toee.stat_cha_mod), 1)
		dc_wisdom = npc.stat_base_get(toee.stat_wis_mod)
		# dc default = 10 + spell_level + dc_wisdom
		# dc target = 10 + spell_level + dc_cha
		dc_increase = dc_cha - dc_wisdom
		print("dc_increase: {}".format(dc_increase))
		dc_increase += 2 # for Web
		npc.condition_add_with_args("Spell_DC_Mod", toee.spell_web, dc_increase) # need to check
		
		npc.feat_add(toee.feat_spell_focus_conjuration)
		npc.feat_add(toee.feat_spell_focus_evocation)
		npc.feat_add(toee.feat_combat_casting)
		npc.feat_add(toee.feat_toughness)
		npc.feat_add(toee.feat_alertness, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory(const_proto_rings.PROTO_RING_OF_PROTECTION_PLUS_1, npc)
		utils_item.item_create_in_inventory(const_proto_scrolls.PROTO_SCROLL_OF_DISPLACEMENT, npc)
		utils_item.item_create_in_inventory(const_proto_scrolls.PROTO_SCROLL_OF_HEROISM, npc)
		utils_item.item_create_in_inventory(const_proto_scrolls.PROTO_SCROLL_OF_SCORCHING_RAY, npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(650, 700) + 200)
		utils_item.item_create_in_inventory(const_proto_items.PROTO_GENERIC_PEARL_BLACK, npc)
		return

	def setup_end(self, npc):
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		print("enter_combat kutula")

		stat_class = toee.domain_special
		caster_level = 2
		# 2
		self.spells.add_spell(toee.spell_web, stat_class, caster_level)

		stat_class = toee.stat_level_wizard
		caster_level = 5
		# 3: 2
		self.spells.add_spell(toee.spell_displacement, stat_class, caster_level)
		self.spells.add_spell(toee.spell_fireball, stat_class, caster_level)
		self.spells.add_spell(toee.spell_haste, stat_class, caster_level)
		# 2: 3
		self.spells.add_spell(toee.spell_blur, stat_class, caster_level)
		#self.spells.add_spell(toee.spell_silence, stat_class, caster_level)
		#self.spells.add_spell(toee.spell_melfs_acid_arrow, stat_class, caster_level)
		self.spells.add_spell(toee.spell_bulls_strength, stat_class, caster_level)
		self.spells.add_spell(toee.spell_scorching_ray, stat_class, caster_level)
		self.spells.add_spell(toee.spell_scorching_ray, stat_class, caster_level)
		
		# 1: 4
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		print("kutula create_tactics")
		tac = utils_tactics.TacticsHelper(self.get_name())

		while (1):
			target, kind = self.tactics_determine_targeting_ranged(npc)
			#if (not utils_npc_spells_tactics.STWeb(npc, self.spells, tac).execute()):
			#	break

			if (not utils_npc_spells_tactics.STFireball(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STSilence(npc, self.spells, tac, target).execute()):
				break

			if (not utils_npc_spells_tactics.STDisplacementSelf(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STBlurSelf(npc, self.spells, tac).execute()):
				break

			#if not utils_npc_spells_tactics.STBlurSelf(npc, self.spells, tac).execute():
			#	break

			foes_threatening = self._vars_tactics["foes_threatening"]
			if not utils_npc_spells_tactics.STHasteSelf(npc, self.spells, tac).execute() and not len(foes_threatening) > 1:
				break

			if not utils_npc_spells_tactics.STBullsStrengthSelf(npc, self.spells, tac).execute() and not len(foes_threatening) > 0:
				break

			# default
			return None
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac
