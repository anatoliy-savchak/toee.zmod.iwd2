import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py06615_daemon_orc_fort, py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, py14764_npc_portal, utils_pc

MODULE_SCRIPT_ID = 6616

def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)

def cs(): return py06615_daemon_orc_fort.cs()

class CtrlOrcWarrior(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.make_class(const_toee.stat_level_npc_warriror, 1) 
		utils_npc_build.NPCAbilitiesSetup(12, 15, utils_races.RACE_ABILITY_BONUSES_ORC).generate().focus_melee().npc_setup_random(npc)

		npc.feat_add(toee.feat_rapid_reload)
		npc.feat_add(toee.feat_cleave, 1)
		return

	def setup_gear(self, npc):
		self.create_armor(npc)
		self.create_weapon(npc)
		if self.should_add_ranged():
			self.create_ranged(npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(2, 12))
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 0)
		return

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc)
		return

	def create_ranged(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, npc).obj_set_int(toee.obj_f_ammo_quantity, 2)
		return

	def should_add_ranged(self): return 0

class CtrlOrcWarriorCrossbow(CtrlOrcWarrior):

	def should_add_ranged(self): return 2

class CtrlOrcWarriorGreataxe(CtrlOrcWarrior):

	def create_weapon(self, npc):
		super(CtrlOrcWarriorGreataxe, self).create_weapon(npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATAXE, npc)
		return

class CtrlOrcWarriorGreataxeCB(CtrlOrcWarrior):
	def should_add_ranged(self): return 2

class CtrlOrcWarriorShield(CtrlOrcWarrior):

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_ORCISH, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

class CtrlOrcWarriorScaleMail(CtrlOrcWarrior):

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SCALE_MAIL, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

class CtrlOrcWarriorGuard(CtrlOrcWarrior):

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SCALE_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_ORCISH, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

class CtrlOrcWarriorGuardCB(CtrlOrcWarriorGuard):
	def should_add_ranged(self): return 2

class CtrlOrcWarriorGuardHeavy(CtrlOrcWarrior):

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_HALF_PLATE, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_ORCISH, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

class CtrlOrcWarriorGuardHeavyGreataxe(CtrlOrcWarriorGuardHeavy):

	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATAXE, npc)
		return

	def should_add_ranged(self): return 2


class CtrlOrcSergeant(CtrlOrcWarrior):

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.make_class(toee.stat_level_fighter, 4)
		utils_npc.npc_abilities_set(npc, [18, 12, 13, 9, 8, 4])

		npc.feat_add(toee.feat_great_fortitude)
		npc.feat_add(toee.feat_lightning_reflexes)
		npc.feat_add(toee.feat_weapon_focus_greataxe)
		npc.feat_add(toee.feat_weapon_specialization_greataxe)
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_alertness, 1)

		# create inventory
		self.create_armor(npc)
		self.create_weapon(npc)
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(40, 50))
		npc.item_wield_best_all()

		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 0)
		return

	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATAXE_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_LONGBOW_COMPOSITE_16_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc).obj_set_int(toee.obj_f_ammo_quantity, 1)
		return

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

class CtrlOrcSergeantJunior(CtrlOrcWarrior):

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.make_class(toee.stat_level_fighter, 3)
		utils_npc.npc_abilities_set(npc, [14, 10, 11, 10, 10, 6])

		npc.feat_add(toee.feat_great_fortitude)
		npc.feat_add(toee.feat_lightning_reflexes)
		npc.feat_add(toee.feat_weapon_focus_scimitar)
		npc.feat_add(toee.feat_weapon_specialization_scimitar)
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_alertness, 1)

		# create inventory
		self.create_armor(npc)
		self.create_weapon(npc)
		self.create_ranged(npc)
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(40, 50))
		npc.item_wield_best_all()

		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 0)
		return

	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_SCIMITAR_MASTERWORK, npc)
		return

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_ORCISH, npc)
		return

class CtrlOrcLeader(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.make_class(toee.stat_level_fighter, 4) 
		utils_npc.npc_abilities_set(npc, [16, 10, 13, 10, 7, 5])

		npc.feat_add(toee.feat_weapon_focus_heavy_flail)
		npc.feat_add(toee.feat_improved_trip)
		npc.feat_add(toee.feat_blind_fight)
		npc.feat_add(toee.feat_alertness, 1)

		# create inventory
		self.create_armor(npc)
		self.create_weapon(npc)
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(40, 50))
		npc.item_wield_best_all()

		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		return

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOAK_RED, npc, 1)
		return

	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_FLAIL_HEAVY_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_LONGBOW_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc).obj_set_int(toee.obj_f_ammo_quantity, 2)
		return

	def create_tactics(self, npc):
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
			tac.add_trip()
			tac.add_attack()
			tac.add_approach_single()
			tac.add_attack()
			tac.add_ready_vs_approach()
			tac.add_stop()
		else:
			npc.obj_set_obj(toee.obj_f_npc_combat_focus, toee.OBJ_HANDLE_NULL)
			print("No target, Total Defense")
			npc.float_text_line('Total Defense', toee.tf_yellow)
			tac.add_total_defence()
			tac.add_stop()
		return tac

class CtrlOrcCleric1(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		cleric_levels = 2
		utils_npc_build.NPCAbilitiesSetup(12, 15, utils_races.RACE_ABILITY_BONUSES_ORC).generate().focus_cleric().npc_setup_random(npc)
		npc.make_class(toee.stat_level_cleric, cleric_levels)

		npc.skill_ranks_set(toee.skill_concentration, 3 + (cleric_levels-1)*1)

		npc.feat_add(toee.feat_combat_casting, 1)

		# create inventory
		self.create_armor(npc)
		self.create_weapon(npc)
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(2, 12))
		npc.item_wield_best_all()

		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		return

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_HALF_PLATE, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY_MASTERWORK, npc) # no ammo, by design
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.stat_level_cleric
		caster_level = attachee.highest_divine_caster_level
		# 1
		self.spells.add_spell(toee.spell_bane, stat_class, caster_level)
		self.spells.add_spell(toee.spell_bless, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_cure_minor_wounds, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())
		while (1):
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

class CtrlOrcWizard1(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		wizard_levels = 6
		utils_npc_build.NPCAbilitiesSetup(12, 15, utils_races.RACE_ABILITY_BONUSES_ORC).generate().focus_wizard().npc_setup_random(npc)
		npc.make_class(toee.stat_level_wizard, wizard_levels)

		npc.skill_ranks_set(toee.skill_concentration, 3 + (wizard_levels-1)*1)

		npc.feat_add(toee.feat_spell_focus_enchantment)
		npc.feat_add(toee.feat_spell_focus_evocation)
		npc.feat_add(toee.feat_greater_spell_focus_enchantment)
		npc.feat_add(toee.feat_greater_spell_focus_evocation)
		npc.feat_add(toee.feat_toughness)
		npc.feat_add(toee.feat_improved_initiative)
		npc.feat_add(toee.feat_combat_casting, 1)

		# create inventory
		self.create_armor(npc)
		self.create_weapon(npc)
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(2, 12))
		npc.item_wield_best_all()

		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		return

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_BRACERS_OF_ARMOR_PLUS_1, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_ROBES_WIZARD_BLUE, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.stat_level_wizard
		caster_level = attachee.highest_arcane_caster_level
		# 3, 3
		self.spells.add_spell(toee.spell_deep_slumber, stat_class, caster_level)
		self.spells.add_spell(toee.spell_fireball, stat_class, caster_level)
		self.spells.add_spell(toee.spell_fireball, stat_class, caster_level)
		# 2, 4
		self.spells.add_spell(toee.spell_web, stat_class, caster_level)
		self.spells.add_spell(toee.spell_scorching_ray, stat_class, caster_level)
		self.spells.add_spell(toee.spell_scorching_ray, stat_class, caster_level)
		self.spells.add_spell(toee.spell_glitterdust, stat_class, caster_level)
		# 1, 4
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())

		spell_fireball_tactic = utils_npc_spells_tactics.STFireball(npc, self.spells, tac)
		while (1):
			if (0 and spell_fireball_tactic.spells_left()):
				if (not utils_npc_spells_tactics.STFireball(npc, self.spells, tac).execute()):
					pass

			if (not utils_npc_spells_tactics.STWeb(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STDeepSlumber(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STGlitterdust(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STScorchingRay(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STMagicMissle(npc, self.spells, tac).execute()):
				break

			# default
			return None
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

class CtrlOrcFortPortalGroundToTowersSE(py14764_npc_portal.CtrlPortalUp):
	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		toee.game.fade_and_teleport(
			0, 0, 0, 
			self.get_dest_map(), 
			self.get_dest_location()[0], 
			self.get_dest_location()[1]
			)
		return toee.SKIP_DEFAULT

	def get_dest_location(self): return module_consts.ZMOD_ORC_FORT_TOWERS_ENTRY_SE
	def get_dest_map(self): return module_consts.MAP_ID_ZMOD_ORC_FORT_TOWERS

class CtrlOrcFortPortalGroundToTowersSW(CtrlOrcFortPortalGroundToTowersSE):
	def get_dest_location(self): return module_consts.ZMOD_ORC_FORT_TOWERS_ENTRY_SW
	def get_dest_map(self): return module_consts.MAP_ID_ZMOD_ORC_FORT_TOWERS

class CtrlOrcFortPortalTowersToGroundSE(CtrlOrcFortPortalGroundToTowersSE):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_PORTAL_DOWN
	def get_dest_location(self): return module_consts.ZMOD_ORC_FORT_ENTRY_SE
	def get_dest_map(self): return module_consts.MAP_ID_ZMOD_ORC_FORT

class CtrlOrcFortPortalTowersToGroundSW(CtrlOrcFortPortalTowersToGroundSE):
	def get_dest_location(self): return module_consts.ZMOD_ORC_FORT_ENTRY_SW
	def get_dest_map(self): return module_consts.MAP_ID_ZMOD_ORC_FORT

class CtrlTiger(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14640
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 6, 8, 0)
		utils_npc.npc_abilities_set(npc, [23, 15, 17, 2, 12, 6])
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 4)

		npc.obj_set_int(toee.obj_f_critter_portrait, 5050) # MOO_5051_m_Shadow_Mastiff todo
		#npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL)
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 3) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 5)

		cat = const_toee.mc_type_animal
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)

		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 4) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 2) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d6").packed)

		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 1, const_toee.nwt_bite)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 1, 4-2) # natural bab, multiattack lowers from -5 to -2 
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 1, 1) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 1, toee.dice_new("1d8").packed)

		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30
		
		#npc.condition_add("Rend") # too powerful

		npc.feat_add(toee.feat_greater_weapon_focus_unarmed_strike_medium_sized_being)
		npc.feat_add(toee.feat_alertness, 1)
		utils_npc.npc_description_set_new(npc, "Tiger")

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlRope(py14764_npc_portal.CtrlPortalLaddersUp):
	@classmethod
	def get_dialog_line_cls(cls, npc): return 20

	@classmethod
	def get_dialog_script_id_cls(cls, npc):	return MODULE_SCRIPT_ID

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlRope, self).after_created(npc)
		utils_npc.npc_description_set_new(npc, "Rope")
		return

	def dialog_climb(self, npc, pc):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)

		cs().activate_encounter_assault(1)

		npc.destroy()

		toee.game.fade_and_teleport(
			0, 0, 0, 
			module_consts.MAP_ID_ZMOD_ORC_FORT_TOWERS, 
			module_consts.ZMOD_ORC_FORT_TOWERS_ENTRY_SNEAK[0], 
			module_consts.ZMOD_ORC_FORT_TOWERS_ENTRY_SNEAK[1]
			)
		return

	def dialog_skip_climb(self, npc, pc):
		return

class CtrlTroll(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14262

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		#npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID

		#utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum([23, 14, 23, 6, 9, 6], utils_npc.stats_random(-2, 2)))

		npc.condition_add_with_args("Monster Regeneration 5", toee.D20DT_FIRE, toee.D20DT_ACID)

		npc.feat_add(toee.feat_lightning_reflexes)
		npc.feat_add(toee.feat_alertness, 1)

		# create inventory
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(40, 60))
		utils_item.item_create_in_inventory(const_proto_items.PROTO_GENERIC_JASPER_BLUE, npc, 14)
		npc.item_wield_best_all()

		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 0)
		return

class CtrlOrcWizard2(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		wizard_levels = 3
		utils_npc_build.NPCAbilitiesSetup(8, 15, utils_races.RACE_ABILITY_BONUSES_ORC).generate().focus_wizard().npc_setup_random(npc)
		npc.make_class(toee.stat_level_wizard, wizard_levels)

		npc.skill_ranks_set(toee.skill_concentration, 3 + (wizard_levels-1)*1)

		npc.feat_add(toee.feat_spell_focus_conjuration)
		npc.feat_add(toee.feat_combat_casting, 1)

		# create inventory
		self.create_armor(npc)
		self.create_weapon(npc)
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(2, 12))
		npc.item_wield_best_all()

		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		return

	def create_armor(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_ROBES_WIZARD_BLUE, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_DAGGER, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, npc).obj_set_int(toee.obj_f_ammo_quantity, 3)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.stat_level_wizard
		caster_level = attachee.highest_arcane_caster_level
		# 2: 1
		#self.spells.add_spell(toee.spell_web, stat_class, caster_level)
		self.spells.add_spell(toee.spell_glitterdust, stat_class, caster_level)
		# 1, 3
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		#self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		self.spells.add_spell(toee.spell_ray_of_enfeeblement, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())


		while (1):
			# web is OP probably
			if 0:
				spell_web_tactic = utils_npc_spells_tactics.STWebSingle(npc, self.spells, tac)
				if (spell_web_tactic.spells_left()):
					epicenter = utils_obj.sec2loc(478, 473)
					target_web = utils_npc.npc_find_nearest_enemy_loc(npc, epicenter, 30, 0, 0, 0)
					if target_web:
						tac.add_target_obj(target_web.id)
						if (spell_web_tactic.execute()):
							pass
						tac.add_clear_target()

			if (not utils_npc_spells_tactics.STGlitterdust(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STRayOfEnfeeblement(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STMagicMissle(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STAcidSplash(npc, self.spells, tac).execute()):
				break

			# default
			return None
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

class CtrlOrcSergeantR06(CtrlOrcWarrior):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.make_class(toee.stat_level_fighter, 3)
		utils_npc.npc_abilities_set(npc, [19, 11, 11, 8, 5, 8])

		npc.feat_add(toee.feat_great_fortitude)
		npc.feat_add(toee.feat_point_blank_shot)
		npc.feat_add(toee.feat_weapon_focus_scimitar)
		npc.feat_add(toee.feat_toughness, 1)

		# create inventory
		self.create_armor(npc)
		self.create_weapon(npc)
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(1, 2))
		npc.item_wield_best_all()

		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 0)
		return

	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_SCIMITAR_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_LONGBOW_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc).obj_set_int(toee.obj_f_ammo_quantity, 3)
		return

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_ORCISH, npc)
		return

	def recon_is_focus_ranged(self, npc):
		# in this case he has cover everywhere, so has_los will fail. Let's force ranged
		result = super(CtrlOrcSergeantR06, self).recon_is_focus_ranged(npc)
		if result:
			foes_threatening = self._vars_tactics["foes_threatening"]
			if not foes_threatening:
				result = 2
		return result

class CtrlOrcWarriorArcherR06(CtrlOrcWarrior):
	def create_ranged(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_LONGBOW, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc).obj_set_int(toee.obj_f_ammo_quantity, 3)
		return

	def should_add_ranged(self): return 2

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

class CtrlOrcWarriorArcherR06Leather(CtrlOrcWarriorArcherR06):
	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_SCIMITAR, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_ORCISH, npc)
		return

class CtrlOrcWarriorArcherR06Studded(CtrlOrcWarriorArcherR06Leather):

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

class CtrlOrcWarriorArcherR06HalberdStudded(CtrlOrcWarriorArcherR06Studded):
	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_HALBERD, npc)
		return

class CtrlOrcWarriorArcherR06HalberdScale(CtrlOrcWarriorArcherR06HalberdStudded):
	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SCALE_MAIL, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

class CtrlOrcWarriorR08(CtrlOrcWarrior):
	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_SCIMITAR, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_ORCISH, npc)
		return
	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SCALE_MAIL, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return
	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

class CtrlLiutenentR10(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		return

	def setup_appearance(self, npc):
		#npc.obj_set_int(toee.obj_f_critter_portrait, 9230) # NPC_9231_m_battlehammer_warrior.tga
		npc.obj_set_int(toee.obj_f_critter_portrait, 9200) # NPC_9201_m_hextor_priest.tga
		utils_npc.npc_description_set_new(npc, "Liutenent")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) 
		utils_npc.npc_abilities_set(npc, [20, 12+2, 15-2, 9, 8, 10])
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 7
		npc.make_class(toee.stat_level_fighter, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)

		npc.feat_add(toee.feat_weapon_focus_scimitar)
		npc.feat_add(toee.feat_weapon_specialization_scimitar)
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_great_cleave)
		npc.feat_add(toee.feat_blind_fight)
		npc.feat_add(toee.feat_toughness)
		npc.feat_add(toee.feat_toughness)
		npc.feat_add(toee.feat_iron_will, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE_PLUS_1_BLACK, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_SCIMITAR_PLUS_1, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_ORCISH, npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(50, 70))
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.scripts[const_toee.sn_heartbeat] = 0
		attachee.turn_towards(triggerer)
		triggerer.begin_dialog(attachee, 30)
		return toee.SKIP_DEFAULT

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		# is disabled in dialog for optimization!

		# only first time
		if not attachee.has_met(toee.game.leader):
			pc = utils_npc.npc_find_nearest_pc_prefer_leader(attachee)
			if (pc):
				attachee.turn_towards(pc)
				attachee.scripts[const_toee.sn_heartbeat] = 0
				pc.begin_dialog(attachee, 30)
		return toee.RUN_DEFAULT

class CtrlGuardHumanR10(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		return

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 8570) # NPC_8571_m_Ronald, NPC_8321_m_Gadham: leather, NPC_7731_m_GranksBandit: generic, NPC_7482_s_Knight: full, NPC_7111_m_Barkinar: full, NPC_6812_s_MoathouseBandit: chapayevka, NPC_6781_m_LarethGuard: guard myska
		utils_npc.npc_description_set_new(npc, "Guard")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_NEUTRAL_EVIL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_HUMAN_ARRAY, utils_npc.stats_random(-2, 2)))
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 3
		npc.make_class(const_toee.stat_level_npc_warriror, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # NPC class like Warrior has lower CR than class level, see CritterKillAwardXp

		npc.feat_add(toee.feat_weapon_focus_greataxe)
		npc.feat_add(toee.feat_lightning_reflexes)
		npc.feat_add(toee.feat_iron_will, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELMET_CHAIN, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SPLINT_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATAXE, npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(5, 15))
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

class CtrlGuardHumanR10Chainmail(CtrlGuardHumanR10):
	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 7730) # NPC_8571_m_Ronald, NPC_8321_m_Gadham: leather, NPC_7731_m_GranksBandit: generic, NPC_7482_s_Knight: full, NPC_7111_m_Barkinar: full, NPC_6812_s_MoathouseBandit: chapayevka, NPC_6781_m_LarethGuard: guard myska
		utils_npc.npc_description_set_new(npc, "Guard")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_EVIL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_HUMAN_ARRAY, utils_npc.stats_random(-2, 2)))
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 2
		npc.make_class(const_toee.stat_level_npc_warriror, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # NPC class like Warrior has lower CR than class level, see CritterKillAwardXp

		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_toughness, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELM_GENERIC, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAINMAIL, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_3, npc)
		return

class CtrlGuardHumanR10Longbow(CtrlGuardHumanR10):
	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 6780) # NPC_8571_m_Ronald, NPC_8321_m_Gadham: leather, NPC_7731_m_GranksBandit: generic, NPC_7482_s_Knight: full, NPC_7111_m_Barkinar: full, NPC_6812_s_MoathouseBandit: chapayevka, NPC_6781_m_LarethGuard: guard myska
		utils_npc.npc_description_set_new(npc, "Guard")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_EVIL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_HUMAN_ARRAY, utils_npc.stats_random(-2, 2)))
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 2
		npc.make_class(const_toee.stat_level_npc_warriror, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # NPC class like Warrior has lower CR than class level, see CritterKillAwardXp

		npc.feat_add(toee.feat_weapon_focus_longbow)
		npc.feat_add(toee.feat_improved_initiative, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELMET_SAMURAI, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_BREASTPLATE, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_SCIMITAR, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_3, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_LONGBOW_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc).obj_set_int(toee.obj_f_ammo_quantity, 3)
		return

class CtrlGuardDwarfR10Greataxe(CtrlGuardHumanR10):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 9230) # NPC_8571_m_Ronald, NPC_8321_m_Gadham: leather, NPC_7731_m_GranksBandit: generic, NPC_7482_s_Knight: full, NPC_7111_m_Barkinar: full, NPC_6812_s_MoathouseBandit: chapayevka, NPC_6781_m_LarethGuard: guard myska, NPC_9232_s_battlehammer_warrior: dwarf
		utils_npc.npc_description_set_new(npc, "Guard")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_MUL2DWARF_ARRAY, utils_npc.stats_random(-2, 2)))
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 2
		npc.make_class(const_toee.stat_level_npc_warriror, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # NPC class like Warrior has lower CR than class level, see CritterKillAwardXp

		npc.feat_add(toee.feat_weapon_focus_greatsword)
		npc.feat_add(toee.feat_toughness, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELM_GENERIC, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_BREASTPLATE, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATSWORD, npc)
		return

class CtrlGuardDwarfR10Falchion(CtrlGuardHumanR10):
	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 9230) # NPC_8571_m_Ronald, NPC_8321_m_Gadham: leather, NPC_7731_m_GranksBandit: generic, NPC_7482_s_Knight: full, NPC_7111_m_Barkinar: full, NPC_6812_s_MoathouseBandit: chapayevka, NPC_6781_m_LarethGuard: guard myska, NPC_9232_s_battlehammer_warrior: dwarf
		utils_npc.npc_description_set_new(npc, "Guard")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_NEUTRAL_EVIL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_MUL2DWARF_ARRAY, utils_npc.stats_random(-2, 2)))
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 3
		npc.make_class(const_toee.stat_level_npc_warriror, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # NPC class like Warrior has lower CR than class level, see CritterKillAwardXp

		npc.feat_add(toee.feat_iron_will)
		npc.feat_add(toee.feat_weapon_focus_falchion)
		npc.feat_add(toee.feat_toughness, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELM_GREAT, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_BANDED_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_FALCHION, npc)
		return

class CtrlGuardHumanR10Flail(CtrlGuardHumanR10):
	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 7730) # NPC_8571_m_Ronald, NPC_8321_m_Gadham: leather, NPC_7731_m_GranksBandit: generic, NPC_7482_s_Knight: full, NPC_7111_m_Barkinar: full, NPC_6812_s_MoathouseBandit: chapayevka, NPC_6781_m_LarethGuard: guard myska
		utils_npc.npc_description_set_new(npc, "Guard")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_EVIL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_HUMAN_ARRAY, utils_npc.stats_random(-2, 2)))
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 2
		npc.make_class(const_toee.stat_level_npc_warriror, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # NPC class like Warrior has lower CR than class level, see CritterKillAwardXp

		npc.feat_add(toee.feat_lightning_reflexes)
		npc.feat_add(toee.feat_cleave, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELM_GENERIC, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_BREASTPLATE, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_FLAIL_HEAVY, npc)
		return

class CtrlGuardHumanR10Warhammer(CtrlGuardHumanR10):
	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 7110) # NPC_8571_m_Ronald, NPC_8321_m_Gadham: leather, NPC_7731_m_GranksBandit: generic, NPC_7482_s_Knight: full, NPC_7111_m_Barkinar: full, NPC_6812_s_MoathouseBandit: chapayevka, NPC_6781_m_LarethGuard: guard myska
		utils_npc.npc_description_set_new(npc, "Guard")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_EVIL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_HUMAN_ARRAY, utils_npc.stats_random(-2, 2)))
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 2
		npc.make_class(const_toee.stat_level_npc_warriror, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # NPC class like Warrior has lower CR than class level, see CritterKillAwardXp

		npc.feat_add(toee.feat_weapon_focus_warhammer)
		npc.feat_add(toee.feat_great_fortitude, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELM_GREAT, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_BREASTPLATE, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_WARHAMMER, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_3, npc)
		return

class CtrlGuardElfR10Longbow(CtrlGuardHumanR10):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ELF_MAN

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 7850) # NPC_8571_m_Ronald, NPC_8321_m_Gadham: leather, NPC_7731_m_GranksBandit: generic, NPC_7482_s_Knight: full, NPC_7111_m_Barkinar: full, NPC_6812_s_MoathouseBandit: chapayevka, NPC_6781_m_LarethGuard: guard myska, NPC_7851_m_ElfPrisoner1: elf leather cap
		utils_npc.npc_description_set_new(npc, "Guard")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_EVIL) 
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_GOOD) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_ELF_ARRAY, utils_npc.stats_random(-2, 2)))
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 3
		npc.make_class(const_toee.stat_level_npc_warriror, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # NPC class like Warrior has lower CR than class level, see CritterKillAwardXp

		npc.feat_add(toee.feat_weapon_focus_longbow)
		npc.feat_add(toee.feat_point_blank_shot, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELM_LEATHER, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_BANDED_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_2, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_LONGBOW, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc).obj_set_int(toee.obj_f_ammo_quantity, 3)
		return

class CtrlWizardHumanR11Ench3(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 9660) # NPC_7272_s_Feldrin, NPC_7082_s_BelsornigPriest1, NPC_9662_s_hextor_assassin_m, NPC_9052_s_verbobonc_mage, NPC_8861_m_hextor_mage
		utils_npc.npc_description_set_new(npc, "Wizard")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_NEUTRAL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_HUMAN_ARRAY, utils_npc.stats_random(-2, 2)))
		npc.stat_base_set(toee.stat_intelligence, toee.game.random_range(11, 14))
		int_mod = npc.stat_level_get(toee.stat_int_mod)
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 3
		npc.make_class(toee.stat_level_wizard, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		npc.skill_ranks_set(toee.skill_concentration, 3 + (char_levels-1)*int_mod)

		npc.feat_add(toee.feat_improved_initiative)
		npc.feat_add(toee.feat_lightning_reflexes)
		self.setup_feat_spell_focus(npc)
		npc.feat_add(toee.feat_combat_casting, 1)
		return

	def setup_feat_spell_focus(self, npc):
		npc.feat_add(toee.feat_spell_focus_enchantment)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_DAGGER, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, npc).obj_set_int(toee.obj_f_ammo_quantity, 1)
		self.setup_gear_robes(npc)
		return

	def setup_gear_robes(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_ROBES_WIZARD_BLUE, npc, 1)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(5, 25))
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.setup_spells(npc)
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

	def setup_spells(self, npc, for_combat = False):
		assert isinstance(npc, toee.PyObjHandle)
		stat_class = toee.stat_level_wizard
		caster_level = npc.highest_arcane_caster_level
		# 2, 1
		self.spells.add_spell(toee.spell_web, stat_class, caster_level)
		# 1, 2
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		if not for_combat: self.spells.add_spell(toee.spell_mage_armor, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		self.setup_spells(attachee, True)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())

		while (1):
			if (not utils_npc_spells_tactics.STFireball(npc, self.spells, tac).execute()):
				# sometimes it won't work
				if (not utils_npc_spells_tactics.STMagicMissle(npc, self.spells, tac).execute()):
					break
				break

			web_spell_tactic = utils_npc_spells_tactics.STWebSingle(npc, self.spells, tac)
			if web_spell_tactic.spells_left() > 0:
				foes_can_los = self._vars_tactics["foes_can_los"]
				if not foes_can_los:
					foes_can_los = self._vars_tactics["foes_can_sense"]
				if web_spell_tactic.pick_target_best(foes_can_los):
					if not web_spell_tactic.execute():
						break

			if (not utils_npc_spells_tactics.STBlurSelf(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STGlitterdust(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STScorchingRay(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STMagicMissle(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STAcidSplash(npc, self.spells, tac).execute()):
				break
			# default
			return None
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

	def dialog_prepare(self, npc, surprised):
		assert isinstance(npc, toee.PyObjHandle)
		if not surprised:
			self.spells.prep_spell(npc, toee.spell_mage_armor)
			npc.cast_spell(toee.spell_mage_armor, npc)
		else:
			npc.condition_add_with_args("Surprised2", 1)
		return

class CtrlWizardHumanR11Conj3(CtrlWizardHumanR11Ench3):
	def setup_feat_spell_focus(self, npc):
		npc.feat_add(toee.feat_spell_focus_conjuration)
		return

	def setup_spells(self, npc, for_combat = False):
		assert isinstance(npc, toee.PyObjHandle)
		stat_class = toee.stat_level_wizard
		caster_level = npc.highest_arcane_caster_level
		# 2, 1
		self.spells.add_spell(toee.spell_glitterdust, stat_class, caster_level)
		# 1, 2
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		#self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		if not for_combat: self.spells.add_spell(toee.spell_mage_armor, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		self.setup_spells(attachee, True)
		return toee.RUN_DEFAULT

class CtrlWizardHumanR11Necro3(CtrlWizardHumanR11Ench3):
	def setup_feat_spell_focus(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.feat_add(toee.feat_spell_focus_necromancy)
		return

	def setup_spells(self, npc, for_combat = False):
		assert isinstance(npc, toee.PyObjHandle)
		stat_class = toee.stat_level_wizard
		caster_level = npc.highest_arcane_caster_level
		# 2, 1
		self.spells.add_spell(toee.spell_glitterdust, stat_class, caster_level)
		# 1, 2
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		#self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		if not for_combat: self.spells.add_spell(toee.spell_mage_armor, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		#self.setup_spells(attachee)
		return toee.RUN_DEFAULT

class CtrlWizardHumanR11Lv5(CtrlWizardHumanR11Ench3):

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 8860) # NPC_7272_s_Feldrin, NPC_7082_s_BelsornigPriest1, NPC_9662_s_hextor_assassin_m, NPC_9052_s_verbobonc_mage, NPC_8861_m_hextor_mage
		utils_npc.npc_description_set_new(npc, "Wizard")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_NEUTRAL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_HUMAN_ARRAY, utils_npc.stats_random(-2, 2)))
		npc.stat_base_set(toee.stat_intelligence, toee.game.random_range(16, 19))
		npc.stat_base_set(toee.stat_constitution, toee.game.random_range(15, 19))
		int_mod = npc.stat_level_get(toee.stat_int_mod)
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 5
		npc.make_class(toee.stat_level_wizard, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		npc.skill_ranks_set(toee.skill_concentration, 3 + (char_levels-1)*int_mod)

		npc.feat_add(toee.feat_improved_initiative)
		npc.feat_add(toee.feat_lightning_reflexes)
		self.setup_feat_spell_focus(npc)
		npc.feat_add(toee.feat_combat_casting, 1)
		return

	def setup_feat_spell_focus(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.feat_add(toee.feat_spell_focus_conjuration)
		npc.feat_add(toee.feat_spell_focus_evocation)
		return

	def setup_spells(self, npc, for_combat = False):
		assert isinstance(npc, toee.PyObjHandle)
		stat_class = toee.stat_level_wizard
		caster_level = npc.highest_arcane_caster_level
		# 3, 2
		self.spells.add_spell(toee.spell_fireball, stat_class, caster_level)
		self.spells.add_spell(toee.spell_fireball, stat_class, caster_level)
		# 2, 3
		self.spells.add_spell(toee.spell_blur, stat_class, caster_level)
		self.spells.add_spell(toee.spell_scorching_ray, stat_class, caster_level)
		self.spells.add_spell(toee.spell_scorching_ray, stat_class, caster_level)
		# 1, 4
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		if not for_combat: self.spells.add_spell(toee.spell_mage_armor, stat_class, caster_level)

		# 0: 5
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		self.setup_spells(attachee, 1)
		return toee.RUN_DEFAULT

	def setup_gear_robes(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_ROBES_WIZARD_RED, npc, 1)
		return

class CtrlWizardHumanR11Lv5Leader(CtrlWizardHumanR11Lv5):
	def setup_gear_robes(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_ROBES_WIZARD_RED, npc, 1)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_BRACERS_OF_ARMOR_PLUS_1, npc)
		return

class CtrlDragonGreenLarge(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14060

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return

	def setup_char(self, npc):
		# Young adult
		hd = 17
		utils_npc.npc_hitdice_set(npc, hd, 8, 0) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum([23, 10, 19, 14, 15, 14], utils_npc.stats_random(-2, 2)))

		npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 11)
		#npc.obj_set_int(toee.obj_f_npc_ac_bonus, 16)
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, -6) # debug
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) 

		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30
		npc.condition_add_with_args("Monster_DR", 5, toee.D20DAP_CHAOS)
		npc.condition_add("Immunity_Paralysis")
		npc.condition_add("Immunity_Sleep")
		npc.condition_add_with_args("Monster Energy Immunity", toee.D20DT_ACID)
		npc.condition_add_with_args("Monster Spell Resistance", 19)

		cat = const_toee.mc_type_dragon + ((toee.mc_subtype_air) << 32)
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)

		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 10)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 10)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 10)

		bab = hd
		sab = bab - 5 + 3 # multiattack
		utils_npc.npc_natural_attack(npc, 0, const_toee.nwt_bite, bab, 1, "2d6")
		utils_npc.npc_natural_attack(npc, 1, const_toee.nwt_claw, sab+1, 2, "1d8") # Weapon Focus Wings
		utils_npc.npc_natural_attack(npc, 2, const_toee.nwt_slam, sab, 2, "1d6")
		utils_npc.npc_natural_attack(npc, 3, const_toee.nwt_slap, sab+1, 1, "1d8") # Weapon Focus Tail Slap

		return

	def setup_feats(self, npc):
		npc.feat_add(toee.feat_iron_will)
		npc.feat_add(toee.feat_toughness)
		npc.feat_add(toee.feat_cleave, 1)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, toee.game.random_range(350, 380))
		return

	def setup_end(self, npc):
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

	def enter_combat1(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.domain_special
		caster_level = 2
		# 2
		self.spells.add_spell(toee.spell_web, stat_class, caster_level)
		#self.spells.add_spell(toee.spell_web, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics1(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
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
						break

			# default
			return None
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

class CtrlSlaveInStupor(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_HUMAN_ARRAY, utils_npc.stats_random(-2, 2)))
		utils_npc.npc_description_set_new(npc, "Slave")

		self.setup_cloth(npc)
		return

	def setup_cloth(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_BLUE, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, 1)
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

class CtrlSlaveInStuporElf(CtrlSlaveInStupor):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ELF_MAN

	def setup_cloth(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_GREEN, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, 1)
		return

	def setup_appearance(self, npc):
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_blue
		hairStyle.update_npc(npc)
		return

class CtrlSlaveInStuporWoman(CtrlSlaveInStupor):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WOMAN

	def setup_cloth(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_OCHRE, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, 1)
		return

	def setup_appearance(self, npc):
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_blonde
		hairStyle.update_npc(npc)
		return

class CtrlSlaveInStuporWomanBlue(CtrlSlaveInStuporWoman):
	def setup_cloth(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_BLUE, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, 1)
		return

class CtrlSlaveInStuporDwarf(CtrlSlaveInStupor):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	def setup_cloth(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_GARB_FARMER_GREY, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, 1)
		return

class CtrlTronen(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 9230) # NPC_9231_m_battlehammer_warrior.tga
		#npc.obj_set_int(toee.obj_f_critter_portrait, 9230) # NPC_9201_m_hextor_priest.tga
		utils_npc.npc_description_set_new(npc, "Tronen")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_NEUTRAL) 
		utils_npc.npc_abilities_set(npc, [13, 8+2, 14-2, 8, 16, 4])
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 8
		npc.make_class(toee.stat_level_cleric, char_levels) # 20 is max
		#npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		npc.skill_ranks_set(toee.skill_concentration, 3 + (char_levels-1)*1)

		npc.feat_add(toee.feat_spell_focus_necromancy)
		npc.feat_add(toee.feat_cleave, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, npc, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_MORNINGSTAR_PLUS_1_DISRUPTION, npc)

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE_PLUS_1, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, npc).obj_set_int(toee.obj_f_ammo_quantity, 15)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(100, 110))
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.scripts[const_toee.sn_heartbeat] = 0
		attachee.turn_towards(triggerer)
		triggerer.begin_dialog(attachee, 150)
		return toee.SKIP_DEFAULT

	def dialog_fight(self, npc, pc):
		npc.attack(pc)
		return

	def dialog_gave_quest(self, npc, pc):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)

		rumor_control.rumor_give(module_quests.RUMOR_ORC_FORT_TRONEN_HELP)

		utils_pc.pc_award_experience_each(250, 1)
		item = npc.item_find_by_proto(const_proto_weapon.PROTO_WEAPON_MORNINGSTAR_PLUS_1_DISRUPTION)
		if item:
			pc.item_get(item)
		return

class CtrlExSlave(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def setup_char(self, npc):
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID

		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_HUMAN_ARRAY, utils_npc.stats_random(-2, 2)))
		utils_npc.npc_description_set_new(npc, "Commoner")

		self.setup_cloth(npc)
		return

	def setup_cloth(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_BLUE, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, 1)
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.scripts[const_toee.sn_heartbeat] = 0
		attachee.turn_towards(triggerer)
		triggerer.begin_dialog(attachee, 240)
		return toee.SKIP_DEFAULT

class CtrlExSlaveW(CtrlExSlave):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WOMAN

	def setup_cloth(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_OCHRE, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, 1)
		return

	def setup_appearance(self, npc):
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_blonde
		hairStyle.update_npc(npc)
		return

class CtrlSlaveR19(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_exit_combat] = MODULE_SCRIPT_ID
		return

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 9230) # NPC_9231_m_battlehammer_warrior.tga
		#npc.obj_set_int(toee.obj_f_critter_portrait, 9230) # NPC_9201_m_hextor_priest.tga
		utils_npc.npc_description_set_new(npc, "Slave")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_GOOD) 
		utils_npc.npc_abilities_set(npc, [12, 9+2, 14-2, 8, 8, 8])
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 1
		npc.make_class(const_toee.stat_level_npc_warriror, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		#npc.skill_ranks_set(toee.skill_concentration, 3 + (char_levels-1)*1)

		npc.feat_add(toee.feat_weapon_focus_dagger, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, npc, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_DAGGER, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_GARB_BROWN, npc, 1)
		return

	def setup_loot(self, npc):
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.scripts[const_toee.sn_heartbeat] = 0
		attachee.turn_towards(triggerer)
		triggerer.begin_dialog(attachee, 250)
		return toee.SKIP_DEFAULT

	def exit_combat(self, attachee, triggerer):
		print("Follower removed: {}".format(attachee))
		toee.game.party[0].follower_remove(attachee)
		return toee.RUN_DEFAULT

	def dialog_award(self, npc, pc):
		utils_pc.pc_award_experience_each(1500, 1)
		return

	def dialog_runaway(self, npc, pc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog]=0
		npc.runoff(utils_obj.sec2loc(435, 486), 0, 0)
		utils_obj.obj_timed_destroy(npc, 2000, 1)
		return

class NPCDialog(object):
	def get_dialog_first(self, npc, self_initiator):
		return 0

	def get_dialog_next(self, npc, self_initiator):
		return 0

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.scripts[const_toee.sn_heartbeat] = 0
		attachee.turn_towards(triggerer)

		dialog_line = self.get_dialog_first(attachee, 0) if not attachee.has_met(triggerer) else self.get_dialog_next(attachee, 0)
		if dialog_line:
			triggerer.begin_dialog(attachee, dialog_line)
		return toee.SKIP_DEFAULT

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		dialog_line = self.get_dialog_first(attachee, 1) if not attachee.has_met(toee.game.leader) else self.get_dialog_next(attachee, 1)
		if dialog_line:
			pc = utils_npc.npc_find_nearest_pc_prefer_leader(attachee)
			if (pc):
				attachee.turn_towards(pc)
				attachee.scripts[const_toee.sn_heartbeat] = 0
				pc.begin_dialog(attachee, dialog_line)
		return toee.RUN_DEFAULT

class CtrlTandek(NPCDialog, ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		return

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 6040) # NPC_6042_s_RannosDavi NPC_7172_s_Grank
		utils_npc.npc_description_set_new(npc, "Tandek")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_EVIL) 
		utils_npc.npc_abilities_set(npc, [12, 10, 10, 10, 7, 9])
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 6
		npc.make_class(toee.stat_level_fighter, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		#npc.skill_ranks_set(toee.skill_concentration, 3 + (char_levels-1)*1)

		npc.feat_add(toee.feat_blind_fight)
		npc.feat_add(toee.feat_great_fortitude)
		npc.feat_add(toee.feat_iron_will)
		npc.feat_add(toee.feat_lightning_reflexes)
		npc.feat_add(toee.feat_weapon_focus_longsword)
		npc.feat_add(toee.feat_weapon_specialization_longsword)
		npc.feat_add(toee.feat_toughness)
		npc.feat_add(toee.feat_toughness, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, npc, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE_PLUS_1, npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(40, 60))
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 1)
		return

	def get_dialog_first(self, npc, self_initiator):
		return 270

	def get_dialog_next(self, npc, self_initiator):
		return 360

	def dialog_give_money(self, npc, pc):
		utils_pc.pc_award_experience_each(500, 1)
		utils_item.item_create_in_inventory(const_proto_items.PROTO_GENERIC_PEARL_BLACK, pc)
		return

	def dialog_attack(self, npc, pc):
		npc.attack(pc)
		return

class CtrlTandekBodyguard(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 9230) # NPC_9231_m_battlehammer_warrior.tga
		#npc.obj_set_int(toee.obj_f_critter_portrait, 9230) # NPC_9201_m_hextor_priest.tga
		utils_npc.npc_description_set_new(npc, "Bodyguard")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) 
		utils_npc.npc_abilities_set(npc, [15, 11+2, 11-2, 12, 7, 7])
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 3
		npc.make_class(const_toee.stat_level_npc_warriror, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		#npc.skill_ranks_set(toee.skill_concentration, 3 + (char_levels-1)*1)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # NPC class like Warrior has lower CR than class level, see CritterKillAwardXp

		self.setup_feats(npc)
		return

	def setup_feats(self, npc):
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_iron_will)
		npc.feat_add(toee.feat_toughness, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, npc, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATSWORD_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SCALE_MAIL, npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(5, 10))
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 1)
		return

class CtrlTandekBodyguard2(CtrlTandekBodyguard):
	def setup_feats(self, npc):
		npc.feat_add(toee.feat_improved_initiative)
		npc.feat_add(toee.feat_weapon_focus_greatsword)
		npc.feat_add(toee.feat_toughness, 1)
		return

class CtrlExecutioner(NPCDialog, ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_HILL_GIANT

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		return

	def setup_appearance(self, npc):
		#npc.obj_set_int(toee.obj_f_critter_portrait, 6040) # NPC_6042_s_RannosDavi NPC_7172_s_Grank
		utils_npc.npc_description_set_new(npc, "Executioner")
		return

	def setup_char(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_NEUTRAL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_HILL_GIANT_ARRAY, utils_npc.stats_random(-2, 2)))
		hd = 12
		utils_npc.npc_hitdice_set(npc, hd, 8, 0)
		#char_levels = 12
		#npc.make_class(toee.stat_level_fighter, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (hd-1)*1)
		#npc.skill_ranks_set(toee.skill_concentration, 3 + (char_levels-1)*1)

		bab = 9
		if 1:
			utils_npc.npc_natural_attack(npc, 0, const_toee.nwt_slam, bab, 1, "1d4")
			utils_npc.npc_natural_attack(npc, 1, const_toee.nwt_slam, bab-5, 1, "1d4")

		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 9 + 1) # natural ac + Improved_Natural_Armor
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 8)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 4)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 4)
		npc.obj_set_int(toee.obj_f_critter_reach, 10)

		cat = const_toee.mc_type_giant
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)
		

		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30
		#npc.condition_add_with_args("Improved_Natural_Armor", 1) # does not stack
		npc.condition_add_with_args("Enlarged_Weapons", 1)

		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_improved_bull_rush)
		npc.feat_add(toee.feat_improved_critical_falchion)
		npc.feat_add(toee.feat_point_blank_shot, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_FALCHION, npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(1, 5))
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 1)
		return

	def get_dialog_first(self, npc, self_initiator):
		return 370

	def dialog_sit(self, npc, pc):
		assert isinstance(pc, toee.PyObjHandle)
		toee.game.fade_and_teleport(
			0, 0, 0, 
			pc.map, 
			429, 
			445
			)
		return

	def dialog_attack(self, npc, pc):
		npc.attack(pc)
		return

class CtrlIcarus(NPCDialog, ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		return

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 6730) # NPC_6732_s_Raimol
		utils_npc.npc_description_set_new(npc, "Icarus")
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_bald
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_EVIL) 
		utils_npc.npc_abilities_set(npc, [18, 13, 16, 11, 12, 15])
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		char_levels = 8
		npc.make_class(toee.stat_level_fighter, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		#npc.skill_ranks_set(toee.skill_concentration, 3 + (char_levels-1)*1)

		npc.condition_add_with_args("Blindsignt", 60) # 60 ft
		#npc.condition_add_with_args("Blind") todo fix
		npc.condition_add("Immunity_Visual")
		
		npc.feat_add(toee.feat_blind_fight)
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_dodge)
		npc.feat_add(toee.feat_exotic_weapon_proficiency_bastard_sword)
		npc.feat_add(toee.feat_great_fortitude)
		npc.feat_add(toee.feat_weapon_focus_bastard_sword)
		npc.feat_add(toee.feat_greater_weapon_focus_bastard_sword)
		npc.feat_add(toee.feat_improved_bull_rush)
		npc.feat_add(toee.feat_improved_grapple)
		npc.feat_add(toee.feat_improved_unarmed_strike)
		npc.feat_add(toee.feat_iron_will)

		npc.feat_add(toee.feat_mobility)
		npc.feat_add(toee.feat_point_blank_shot)
		npc.feat_add(toee.feat_precise_shot)
		npc.feat_add(toee.feat_spring_attack)
		npc.feat_add(toee.feat_toughness)
		npc.feat_add(toee.feat_weapon_focus_longbow)
		npc.feat_add(toee.feat_whirlwind_attack, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, npc, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD_PLUS_1, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE_PLUS_1, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_PLUS_1_STEEL, npc)
		utils_item.item_create_in_inventory(const_proto_rings.PROTO_RING_OF_FIRE_RESISTANCE_MINOR, npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(70, 90))
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.obj_set_int(toee.obj_f_hp_pts, 66)
		return

	def get_dialog_first(self, npc, self_initiator):
		return 400

	def get_dialog_next(self, npc, self_initiator):
		return 480

class CtrlOrcWarrior3(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return

	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		char_alignments = [toee.ALIGNMENT_NEUTRAL_EVIL, toee.ALIGNMENT_CHAOTIC_EVIL]
		npc.obj_set_int(toee.obj_f_critter_alignment, char_alignments[toee.game.random_range(0, len(char_alignments)-1)])

		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_ORC_ARRAY, utils_npc.stats_random(-2, 2)))
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)

		char_levels = 3
		npc.make_class(const_toee.stat_level_npc_warriror, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # NPC class like Warrior has lower CR than class level, see CritterKillAwardXp

		self.setup_feats(npc)
		npc.feat_add(toee.feat_alertness, 1)
		return

	def setup_feats(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.feat_add(toee.feat_iron_will)
		npc.feat_add(toee.feat_cleave)
		return

	def setup_gear(self, npc):
		self.create_armor(npc)
		self.create_weapon(npc)
		if self.should_add_ranged():
			self.create_ranged(npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(2, 12))
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_BANDED_MAIL, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_ORCISH, npc)
		return

	def create_ranged(self, npc):
		quantity = self.should_add_ranged()
		if quantity:
			utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY, npc)
			utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, npc).obj_set_int(toee.obj_f_ammo_quantity, quantity)
		return

	def should_add_ranged(self): return False

class CtrlOrcWarrior3Crossbow(CtrlOrcWarrior3):
	def setup_feats(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.feat_add(toee.feat_point_blank_shot)
		npc.feat_add(toee.feat_precise_shot)
		npc.feat_add(toee.feat_toughness)
		return

	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_SCIMITAR, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_ORCISH, npc)
		return

	def create_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

	def should_add_ranged(self): return 1

class CtrlOrcWizard3(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		wizard_levels = 6
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_ORC_ARRAY, utils_npc.stats_random(-2, 2)))
		npc.make_class(toee.stat_level_wizard, wizard_levels)

		npc.stat_base_set(toee.stat_constitution, 16)
		npc.stat_base_set(toee.stat_intelligence, 16)

		npc.skill_ranks_set(toee.skill_concentration, 3 + (wizard_levels-1)*1)

		npc.feat_add(toee.feat_dodge)
		npc.feat_add(toee.feat_spell_focus_conjuration)
		npc.feat_add(toee.feat_spell_focus_transmutation)
		npc.feat_add(toee.feat_combat_casting, 1)

		# create inventory
		self.create_armor(npc)
		self.create_weapon(npc)
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(2, 12))
		npc.item_wield_best_all()

		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		return

	def create_armor(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_ROBES_WIZARD_BLUE, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc, 1)
		return

	def create_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_DAGGER, npc)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.stat_level_wizard
		caster_level = attachee.highest_arcane_caster_level
		# 3, 3
		self.spells.add_spell(toee.spell_displacement, stat_class, caster_level)
		self.spells.add_spell(toee.spell_haste, stat_class, caster_level)
		self.spells.add_spell(toee.spell_blindness_deafness, stat_class, caster_level)
		# 2, 4
		self.spells.add_spell(toee.spell_scorching_ray, stat_class, caster_level)
		self.spells.add_spell(toee.spell_scorching_ray, stat_class, caster_level)
		self.spells.add_spell(toee.spell_ray_of_enfeeblement, stat_class, caster_level)
		self.spells.add_spell(toee.spell_glitterdust, stat_class, caster_level)
		# 1, 4
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)
		self.spells.add_spell(toee.spell_magic_missile, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())

		while (1):
			target = npc.leader_get()
			if (not utils_npc_spells_tactics.STDisplacementApproach(npc, self.spells, tac, target).execute()):
				break

			if (not utils_npc_spells_tactics.STHasteSelf(npc, self.spells, tac, target).execute()):
				break

			foes_can_sense = self._vars_tactics["foes_can_sense"]
			foes_can_sense_sorted = self.recon_sort_npcs(foes_can_sense, self.recon_apprise_vulnereble_for_debuff)
			target = None if not foes_can_sense_sorted else foes_can_sense_sorted[0]
			if target:
				if (not utils_npc_spells_tactics.STBlindnessDeafness(npc, self.spells, tac, target).execute()):
					break

				if (not utils_npc_spells_tactics.STRayOfEnfeeblement(npc, self.spells, tac, target).execute()):
					break

			target, kind = self.tactics_determine_targeting_ranged(npc)
			if target:
				if (not utils_npc_spells_tactics.STScorchingRay(npc, self.spells, tac, target).execute()):
					break

			if not target:
				target, kind = self.tactics_determine_targeting_melee(npc)

			if (not utils_npc_spells_tactics.STMagicMissle(npc, self.spells, tac, target).execute()):
				break

			# default
			return None
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac
