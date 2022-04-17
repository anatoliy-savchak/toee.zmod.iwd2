import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, py06600_daemon_keep, utils_races, utils_npc_build, const_proto_npc, py14764_npc_portal
import module_consts

KOTS_KEEP_ENCOUNTERS = 6603

def cs(): return py06600_daemon_keep.cs()

ALLY_ABILITY_MIN = 8
ALLY_ABILITY_MAX = 16

FOE_ABILITY_MIN = 8
FOE_ABILITY_MAX = 14

# cheat
#FOE_ABILITY_MIN = 2
#FOE_ABILITY_MAX = 5

def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

class Ally:
	def will_kos(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		if (attachee.type == toee.obj_t_pc or triggerer.type == toee.obj_t_pc): return toee.SKIP_DEFAULT
		return toee.RUN_DEFAULT

	def exit_combat(self, attachee, triggerer):
		print("Follower removed: {}".format(attachee))
		toee.game.party[0].follower_remove(attachee)
		return toee.RUN_DEFAULT

	def enter_combat(self, attachee, triggerer):
		if (not self.get_var("was_surprised")):
			self.vars["was_surprised"] = 1
			attachee.condition_add("Surprised2")
		cs().npc_enter_combat(attachee, self)

		if ("npc_waypoints_set" in dir(attachee)):
			attachee.npc_waypoints_set(None, 1)
			attachee.npc_flag_unset(toee.ONF_WAYPOINTS_DAY)
			attachee.npc_flag_unset(toee.ONF_WAYPOINTS_NIGHT)

	def exit_combat(self, attachee, triggerer):
		cs().npc_exit_combat(attachee, self)
		return toee.RUN_DEFAULT

		return toee.RUN_DEFAULT

class CtrlWarrior(Ally, ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#utils_obj.obj_scripts_clear(npc)
		npc.scripts[const_toee.sn_start_combat] = KOTS_KEEP_ENCOUNTERS
		npc.scripts[const_toee.sn_enter_combat] = KOTS_KEEP_ENCOUNTERS
		npc.scripts[const_toee.sn_exit_combat] = KOTS_KEEP_ENCOUNTERS
		npc.scripts[const_toee.sn_will_kos] = KOTS_KEEP_ENCOUNTERS

		npc.feat_add(toee.feat_armor_proficiency_light)
		npc.feat_add(toee.feat_armor_proficiency_medium)
		npc.feat_add(toee.feat_armor_proficiency_heavy)

		utils_npc_build.NPCAbilitiesSetup(ALLY_ABILITY_MIN, ALLY_ABILITY_MAX).generate().focus_melee().npc_setup_random(npc)

		guard_portraits = [8980, 9450, 9470, 9460]
		npc.obj_set_int(toee.obj_f_critter_portrait, guard_portraits[toee.game.random_range(0, len(guard_portraits)-1)])
		#npc.obj_set_int(toee.obj_f_critter_portrait, 8980)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # as in KoTC
		npc.make_class(const_toee.stat_level_npc_warriror, 1) # should be warrior, but meh

		npc.feat_add(toee.feat_power_attack)

		# create inventory
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_CHAINMAIL_GLOVES, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)
			#npc.item_wield(item, toee.item_wear_boots)
		#utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc)
		npc.item_wield_best_all()
		return

class CtrlWarriorGuard1(CtrlWarrior):
	def after_created(self, npc):
		super(CtrlWarriorGuard1, self).after_created(npc)
		assert isinstance(npc, toee.PyObjHandle)

		#npc.scripts[const_toee.sn_heartbeat] = KOTS_ENCOUNTERS
		#npc.scripts[const_toee.sn_wield_off] = KOTS_ENCOUNTERS


		npc.feat_add(toee.feat_great_fortitude)
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_two_weapon_fighting, 1)
		self.generate_hp(npc)

		npc.condition_add("Base_Attack_Bonus1")

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SPLINT_MAIL, npc)
		sword1 = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTSWORD_MASTERWORK, npc)
		sword2 = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTSWORD, npc)
		npc.item_wield_best_all()
		npc.item_wield(sword1, toee.item_wear_weapon_primary)
		self.vars["sword1"] = sword1.id
		npc.item_wield(sword2, toee.item_wear_weapon_secondary)
		self.vars["sword2"] = sword2.id
		return

	def start_combat(self, attachee, triggerer):
		sword1 = None
		sword2 = None
		if ("sword1" in self.vars): sword1 = toee.game.get_obj_by_id(self.vars["sword1"])
		if ("sword2" in self.vars): sword2 = toee.game.get_obj_by_id(self.vars["sword2"])
		if (sword1): attachee.item_wield(sword1, toee.item_wear_weapon_primary)
		if (sword2): attachee.item_wield(sword2, toee.item_wear_weapon_secondary)
		return super(CtrlWarriorGuard1, self).start_combat(attachee, triggerer)

	def enter_combat(self, attachee, triggerer):
		sword1 = None
		sword2 = None
		if ("sword1" in self.vars): sword1 = toee.game.get_obj_by_id(self.vars["sword1"])
		if ("sword2" in self.vars): sword2 = toee.game.get_obj_by_id(self.vars["sword2"])
		if (sword1): attachee.item_wield(sword1, toee.item_wear_weapon_primary)
		if (sword2): attachee.item_wield(sword2, toee.item_wear_weapon_secondary)
		return super(CtrlWarriorGuard1, self).enter_combat(attachee, triggerer)

class CtrlWarriorGuard2(CtrlWarrior):
	def after_created(self, npc):
		super(CtrlWarriorGuard2, self).after_created(npc)
		assert isinstance(npc, toee.PyObjHandle)

		npc.feat_add(toee.feat_great_fortitude)
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_weapon_focus_longsword, 1)
		self.generate_hp(npc)

		npc.condition_add("Base_Attack_Bonus1")

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SPLINT_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_SMALL_WOODEN, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, npc)
		npc.item_wield_best_all()
		return

class CtrlWarriorGuard3(CtrlWarrior):
	def after_created(self, npc):
		super(CtrlWarriorGuard3, self).after_created(npc)
		assert isinstance(npc, toee.PyObjHandle)

		npc.feat_add(toee.feat_great_fortitude)
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_weapon_focus_falchion, 1)
		self.generate_hp(npc)

		npc.condition_add("Base_Attack_Bonus1")

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SPLINT_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_FALCHION_MASTERWORK, npc)
		npc.item_wield_best_all()
		return

class CtrlWarriorGuardDwarf(CtrlWarrior):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	def after_created(self, npc):
		super(CtrlWarriorGuardDwarf, self).after_created(npc)
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc_build.NPCAbilitiesSetup(ALLY_ABILITY_MIN, ALLY_ABILITY_MAX, utils_races.RACE_ABILITY_BONUSES_DWARF).generate().focus_melee().npc_setup_random(npc)

		npc.feat_add(toee.feat_great_fortitude)
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_weapon_focus_battleaxe, 1)
		npc.obj_set_int(toee.obj_f_critter_portrait, 9230) # Dwarf Warrior
		self.generate_hp(npc)

		npc.condition_add("Base_Attack_Bonus1")

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_BANDED_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_BATTLEAXE_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_BATTLEAXE_MASTERWORK, npc)
		npc.item_wield_best_all()
		return

class CtrlOrc(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14899

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = KOTS_KEEP_ENCOUNTERS
		npc.scripts[const_toee.sn_enter_combat] = KOTS_KEEP_ENCOUNTERS

		utils_npc_build.NPCAbilitiesSetup(FOE_ABILITY_MIN, 12, utils_races.RACE_ABILITY_BONUSES_ORC).generate().focus_melee().npc_setup_random(npc)
		self.generate_hp(npc)

		# create inventory
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, npc)
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_FALCHION, npc)
		npc.item_wield_best_all()
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		if (not self.get_var("was_surprised")):
			self.vars["was_surprised"] = 1
			attachee.condition_add("SurpriseRound2")
		cs().npc_enter_combat(attachee, self)
		return toee.RUN_DEFAULT

class CtrlOrcLeader(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14899

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = KOTS_KEEP_ENCOUNTERS
		npc.scripts[const_toee.sn_enter_combat] = KOTS_KEEP_ENCOUNTERS

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # as in KoTC
		npc.make_class(const_toee.stat_level_npc_warriror, 2) # should be warrior, but meh

		#npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		#npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		#npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_fighter)

		stats_rolls = utils_npc.stats_elite_array()
		npc.stat_base_set(toee.stat_strength, stats_rolls[0]+4)
		npc.stat_base_set(toee.stat_dexterity, stats_rolls[2])
		npc.stat_base_set(toee.stat_constitution, stats_rolls[1])
		npc.stat_base_set(toee.stat_intelligence, stats_rolls[3])
		npc.stat_base_set(toee.stat_wisdom, stats_rolls[4]-2)
		npc.stat_base_set(toee.stat_charisma, stats_rolls[5]-2)

		npc.feat_add(toee.feat_iron_will)
		npc.feat_add(toee.feat_weapon_focus_greataxe, 1)
		npc.obj_set_int(toee.obj_f_critter_portrait, 4940) # orc medium
		self.generate_hp(npc)

		# create inventory
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_BANDED_MAIL_BLACK, npc)
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_RED, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATAXE_MASTERWORK, npc)
		npc.item_wield_best_all()
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		if (not self.get_var("was_surprised")):
			self.vars["was_surprised"] = 1
			attachee.condition_add("SurpriseRound2")
		cs().npc_enter_combat(attachee, self)
		return toee.RUN_DEFAULT

class CtrlGnoll(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14631

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = KOTS_KEEP_ENCOUNTERS
		npc.scripts[const_toee.sn_enter_combat] = KOTS_KEEP_ENCOUNTERS

		utils_npc_build.NPCAbilitiesSetup(FOE_ABILITY_MIN, 12, utils_races.RACE_ABILITY_BONUSES_GNOLL).generate().focus_melee().npc_setup_random(npc)
		npc.feat_add(toee.feat_weapon_focus_scimitar, 1)
		self.generate_hp(npc)

		# create inventory
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_SCIMITAR, npc)
		npc.item_wield_best_all()
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		if (not self.get_var("was_surprised")):
			self.vars["was_surprised"] = 1
			attachee.condition_add("SurpriseRound2")
		cs().npc_enter_combat(attachee, self)
		return toee.RUN_DEFAULT

class CtrlOrcCleric(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14899

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#utils_obj.obj_scripts_clear(npc)
		npc.scripts[const_toee.sn_start_combat] = KOTS_KEEP_ENCOUNTERS
		npc.scripts[const_toee.sn_enter_combat] = KOTS_KEEP_ENCOUNTERS

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # as in KoTC
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_cleric)

		npc.feat_add(toee.feat_combat_casting, 1)
		npc.obj_set_int(toee.obj_f_critter_portrait, 5440) # orc dominator
		utils_npc_build.NPCAbilitiesSetup(FOE_ABILITY_MIN, FOE_ABILITY_MAX, utils_races.RACE_ABILITY_BONUSES_ORC).generate().focus_cleric().npc_setup_random(npc)
		self.generate_hp(npc)

		# create inventory
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, npc)
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_BLUE, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_MACE_HEAVY, npc)
		npc.item_wield_best_all()
		return

	def start_combat(self, attachee, triggerer):
		print("{}::{} (round: {})".format(type(self).__name__, "start_combat", toee.game.combat_turn))

		#debugg.breakp("start_combat")
		tac = utils_tactics.TacticsHelper(self.get_name())
		while (1):
			if (self.spells.get_spell_count(toee.spell_bless)):
				tac.add_five_foot_step()
				tac.add_target_self()
				tac.add_cast_single_code(self.spells.prep_spell(triggerer, toee.spell_bless))
				break
			if (toee.game.combat_turn >= 3 and self.spells.get_spell_count(toee.spell_bane)):
				tac.add_five_foot_step()
				tac.add_target_self()
				tac.add_cast_single_code(self.spells.prep_spell(triggerer, toee.spell_bane))
				break
			tac.add_target_closest()
			tac.add_attack()
			break

		if (not attachee.item_worn_at(toee.item_wear_weapon_primary)):
			attachee.item_wield_best_all()
		if (tac.count > 0):
			tac.set_strategy(attachee)
		return toee.RUN_DEFAULT

	def enter_combat(self, attachee, triggerer):
		if (not self.get_var("was_surprised")):
			self.vars["was_surprised"] = 1
			attachee.condition_add("SurpriseRound2")
		cs().npc_enter_combat(attachee, self)
		stat_class = toee.stat_level_cleric
		caster_level = 1
		# 1
		self.spells.add_spell(toee.spell_bless, stat_class, caster_level)
		self.spells.add_spell(toee.spell_bane, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_cure_minor_wounds, stat_class, caster_level)
		return toee.RUN_DEFAULT

class CtrlOrcWizard(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14899

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = KOTS_KEEP_ENCOUNTERS
		npc.scripts[const_toee.sn_enter_combat] = KOTS_KEEP_ENCOUNTERS

		utils_npc_build.NPCAbilitiesSetup(FOE_ABILITY_MIN, 16, utils_races.RACE_ABILITY_BONUSES_ORC).generate().focus_wizard().npc_setup_random(npc)
		npc.stat_base_set(toee.stat_intelligence, 16)
		npc.feat_add(toee.feat_martial_weapon_proficiency_handaxe)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0) # as in KoTC
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # as in KoTC
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_wizard)

		npc.feat_add(toee.feat_combat_casting, 1)
		npc.obj_set_int(toee.obj_f_critter_portrait, 5450) # orc rundor
		self.generate_hp(npc)

		# create inventory
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_ROBES_BLACK, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_HANDAXE, npc)
		npc.item_wield_best_all()
		return

	def start_combat(self, attachee, triggerer):
		print("{}::{} (round: {})".format(type(self).__name__, "start_combat", toee.game.combat_turn))

		#debugg.breakp("start_combat")
		tac = utils_tactics.TacticsHelper(self.get_name())
		while (1):
			scroll = attachee.item_find_by_proto(const_proto_scrolls.PROTO_SCROLL_OF_FIREBALL)
			print("Scroll: {}".format(scroll))
			if (scroll):
				fire_epicenter = utils_obj.sec2loc(107, 101)
				tac.add_target_closest()
				print("self.fire_epicenter: {}".format(fire_epicenter))
				if (fire_epicenter):
					trg, dist = utils_target_list.find_pc_closest_to_origin(fire_epicenter)
					print("find_pc_closest_to_origin: {}, {}".format(trg, dist))
					if (trg and dist <= 15):
						tac.add_target_obj(trg.id)
				tac.add_halt()
				tac.add_use_item(scroll.id)
				tac.add_halt()
				tac.add_attack_threatened()
				break
			if (self.spells.get_spell_count(toee.spell_mage_armor)):
				tac.add_five_foot_step()
				tac.add_target_self()
				tac.add_cast_single_code(self.spells.prep_spell(triggerer, toee.spell_mage_armor))
				break
			if (toee.game.combat_turn > 2 and self.spells.get_spell_count(toee.spell_web)):
				#debug.breakp("spell_web")
				tac.add_target_low_ac()
				tac.add_five_foot_step()
				tac.add_cast_fireball_code(self.spells.prep_spell(triggerer, toee.spell_web))
				break
			if (toee.game.combat_turn > 2 and self.spells.get_spell_count(toee.spell_sleep)):
				#debug.breakp("spell_web")
				tac.add_target_bad_will()
				tac.add_five_foot_step()
				tac.add_cast_fireball_code(self.spells.prep_spell(triggerer, toee.spell_sleep))
				break
			if (toee.game.combat_turn > 2 and self.spells.get_spell_count(toee.spell_grease)):
				#debug.breakp("spell_web")
				tac.add_target_low_ac()
				tac.add_five_foot_step()
				tac.add_cast_fireball_code(self.spells.prep_spell(triggerer, toee.spell_grease))
				break
			if (self.spells.get_spell_count(toee.spell_acid_splash)):
				# TODO!!!: check for distance
				tac.add_target_closest()
				tac.add_approach_single()
				tac.add_cast_single_code(self.spells.prep_spell(triggerer, toee.spell_acid_splash))
				tac.add_total_defence()
				break
			tac.add_target_closest()
			tac.add_attack()
			break

		if (not attachee.item_worn_at(toee.item_wear_weapon_primary)):
			attachee.item_wield_best_all()
		if (tac.count > 0):
			tac.set_strategy(attachee)
		return toee.RUN_DEFAULT

	def enter_combat(self, attachee, triggerer):
		if (not self.get_var("was_surprised")):
			self.vars["was_surprised"] = 1
			attachee.condition_add("SurpriseRound2")
		cs().npc_enter_combat(attachee, self)
		stat_class = toee.stat_level_wizard
		caster_level = 1
		# 1
		#self.spells.add_spell(toee.spell_grease, stat_class, caster_level)
		self.spells.add_spell(toee.spell_sleep, stat_class, caster_level)
		self.spells.add_spell(toee.spell_mage_armor, stat_class, caster_level)
		# 0
		self.spells.add_spell(toee.spell_acid_splash, stat_class, caster_level, 3)

		#item = utils_item.item_create_in_inventory(const_proto_scrolls.PROTO_SCROLL_OF_FIREBALL, attachee)
		return toee.RUN_DEFAULT

class CtrlGuardElite(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14200

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_enter_combat] = KOTS_KEEP_ENCOUNTERS
		npc.scripts[const_toee.sn_will_kos] = KOTS_KEEP_ENCOUNTERS
		npc.scripts[const_toee.sn_will_kos] = KOTS_KEEP_ENCOUNTERS

		npc.feat_add(toee.feat_armor_proficiency_light)
		npc.feat_add(toee.feat_armor_proficiency_medium)
		npc.feat_add(toee.feat_armor_proficiency_heavy)

		utils_npc_build.NPCAbilitiesSetup(ALLY_ABILITY_MIN, ALLY_ABILITY_MAX).generate().focus_melee().npc_setup_random(npc)
		self.generate_hp(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)
		npc.feat_add(toee.feat_power_attack)

		# create inventory
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_CHAINMAIL_GLOVES, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SPLINT_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_SMALL_WOODEN, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, npc)
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_RED, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)
		item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELM_PLUMED_SILVER, npc)
		if (item):
			item.item_flag_set(toee.OIF_NO_LOOT)

		npc.item_wield_best_all()
		return

	def enter_combat(self, attachee, triggerer):
		return toee.RUN_DEFAULT

	def will_kos(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		if (1): return toee.SKIP_DEFAULT
		return toee.RUN_DEFAULT


class CtrlKeepPortalLv1ToLv2(py14764_npc_portal.CtrlPortalUp):
	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		toee.game.fade_and_teleport(
			0, 0, 0, 
			module_consts.MAP_ID_ZMOD_KEEP_LV2, 
			module_consts.ZMOD_KEEP_LV2_ENTRY_COORDS_STAIRS[0], 
			module_consts.ZMOD_KEEP_LV2_ENTRY_COORDS_STAIRS[1]
			)
		return toee.SKIP_DEFAULT

class CtrlKeepPortalLv2ToLv1(py14764_npc_portal.CtrlPortalDown):
	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		toee.game.fade_and_teleport(
			0, 0, 0, 
			module_consts.MAP_ID_ZMOD_KEEP_LV1, 
			module_consts.ZMOD_KEEP_LV1_ENTRY_COORDS_STAIRS[0], 
			module_consts.ZMOD_KEEP_LV1_ENTRY_COORDS_STAIRS[1]
			)
		return toee.SKIP_DEFAULT

class CtrlKeepPortalLv2ToLv3(py14764_npc_portal.CtrlPortalUp):
	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		toee.game.fade_and_teleport(
			0, 0, 0, 
			module_consts.MAP_ID_ZMOD_KEEP_LV3, 
			module_consts.ZMOD_KEEP_LV3_ENTRY_COORDS_STAIRS[0], 
			module_consts.ZMOD_KEEP_LV3_ENTRY_COORDS_STAIRS[1]
			)
		return toee.SKIP_DEFAULT

class CtrlKeepPortalLv3ToLv2(py14764_npc_portal.CtrlPortalDown):
	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		toee.game.fade_and_teleport(
			0, 0, 0, 
			module_consts.MAP_ID_ZMOD_KEEP_LV2, 
			module_consts.ZMOD_KEEP_LV2_ENTRY_COORDS_STAIRS[0], 
			module_consts.ZMOD_KEEP_LV2_ENTRY_COORDS_STAIRS[1]
			)
		return toee.SKIP_DEFAULT
