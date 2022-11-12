import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon, const_iwd2, const_proto_weapon_iwd2, utils_npc_spells_inf
import utils_journal as uj, inf_scripting, module_difficulty, const_inf
#### IMPORTS ####
#### END IMPORTS ####

#### GVARS ####
MODULE_SCRIPT_ID = 21001
#### GVARS END ####

def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)
def cs(): return ctrl_daemon.gdc()
#### NPCS ####
class Ctrl_21GAERNT_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 21GAERNT 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WERERAT
	
	@classmethod
	def get_allegiance_default(cls): return 128 # NEUTRAL
	
	def setup_scripts(self, npc):
		super(Ctrl_21GAERNT_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Gaernat Sharptooth")
		
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [10, 23, 14, 10, 12, 4])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 11
		ac_natural_bonus = 11 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 2
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 6
		# stat_level_fighter: 6
		npc.make_class(toee.stat_level_fighter, 6)
		return
	
	def setup_char_feats(self, npc):
		# feats
		npc.feat_add(toee.feat_dodge) # Dodge
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 41) # MaximumHP: 41
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 41
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 0
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		return
	
	def setup_char_cr(self, npc):
		cr = 3 # crnum_iwd2: 5, D&D CR: 3
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 5, 2, 2) # SaveVsDeath: 5, SaveVsWands: 2, SaveVsPolymorph: 2
		return
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D6C
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_MACE_LIGHT, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D6C) at SLOT_WEAPON1 by Wererat
		
		# SLOT_QUICK1: None(Books) from RT03_R
		# junk, skip and forget
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(20, 40)) # Charges1: 20, Charges2: 40, Charges3: 0
		
		return
	
	def setup_spells(self, npc):
		return
	
class Ctrl_21WERRAT_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 21WERRAT 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WERERAT
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_21WERRAT_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Wererat")
		
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [12, 17, 13, 10, 10, 10])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 14
		ac_natural_bonus = 14 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 1
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 3
		# stat_level_fighter: 3
		npc.make_class(toee.stat_level_fighter, 3)
		return
	
	def setup_char_feats(self, npc):
		# feats
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		npc.feat_add(toee.feat_weapon_finesse_short_sword) # Weapon finesse
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 23) # MaximumHP: 23
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 23
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 0
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_NEUTRAL) # 0
		return
	
	def setup_char_cr(self, npc):
		cr = 2 # crnum_iwd2: 4, D&D CR: 2
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 2, 4) # SaveVsDeath: 4, SaveVsWands: 2, SaveVsPolymorph: 4
		return
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D6C
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_MACE_LIGHT, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D6C) at SLOT_WEAPON1 by Wererat
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(20, 40)) # Charges1: 20, Charges2: 40, Charges3: 0
		
		return
	
	def setup_spells(self, npc):
		return
	
class Ctrl_21WERBGR_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 21WERBGR 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WERERAT
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_21WERBGR_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Werebadger")
		
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [10, 17, 13, 10, 10, 10])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 14
		ac_natural_bonus = 14 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 1
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 3
		# stat_level_fighter: 3
		npc.make_class(toee.stat_level_fighter, 3)
		return
	
	def setup_char_feats(self, npc):
		# feats
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		npc.feat_add(toee.feat_weapon_finesse_short_sword) # Weapon finesse
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 21) # MaximumHP: 21
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 21
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 0
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		return
	
	def setup_char_cr(self, npc):
		cr = 2 # crnum_iwd2: 4, D&D CR: 2
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 2, 4) # SaveVsDeath: 4, SaveVsWands: 2, SaveVsPolymorph: 4
		return
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D6C
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_MACE_LIGHT, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D6C) at SLOT_WEAPON1 by Werebadger
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(20, 40)) # Charges1: 20, Charges2: 40, Charges3: 0
		
		return
	
	def setup_spells(self, npc):
		return
	
class Ctrl_20ORCSHM_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCSHM 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCSHM_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Orc Shaman")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 4930) # Orc Shaman_Orc Shaman_14751
		
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 14, 12])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 14
		ac_natural_bonus = 14 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 1
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 4
		# stat_level_cleric: 4
		npc.make_class(toee.stat_level_cleric, 4)
		return
	
	def setup_char_feats(self, npc):
		# feats
		npc.feat_add(toee.feat_combat_casting) # Combat casting
		# shield proficiency:  => feat_shield_proficiency skip for cleric
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for cleric
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for cleric
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for cleric
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 22) # MaximumHP: 22
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 22
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 4
		utils_npc.npc_skill_ensure(npc, toee.skill_concentration, 4)
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		return
	
	def setup_char_cr(self, npc):
		cr = 1 # crnum_iwd2: 3, D&D CR: 1
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 1, 4) # SaveVsDeath: 4, SaveVsWands: 1, SaveVsPolymorph: 4
		return
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D6C
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_QUARTERSTAFF, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D6C) at SLOT_WEAPON1
		
		# SLOT_QUICK1: None(Books) from RT02_M
		# junk, skip and forget
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20)) # Charges1: 10, Charges2: 20, Charges3: 0
		
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_ROBES_BROWN_TEMPLE_EARTH, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc, no_loot = True, wear_on = toee.item_wear_helmet)
		return
	
	def setup_spells(self, npc):
		stat_level = toee.stat_level_cleric # CLR
		#Level: 1
		utils_npc_spells_inf.ctrl_add_spell(self, "Command", 1, 1, stat_level, 1) # Command
		utils_npc_spells_inf.ctrl_add_spell(self, "Cure Light Wounds", 1, 1, stat_level, 1) # Cure Light Wounds
		utils_npc_spells_inf.ctrl_add_spell(self, "Frost Fingers", 1, 1, stat_level, 1) # Frost Fingers
		utils_npc_spells_inf.ctrl_add_spell(self, "Magic Stone", 1, 1, stat_level, 1) # Magic Stone
		
		#Level: 2
		utils_npc_spells_inf.ctrl_add_spell(self, "Cure Moderate Wounds", 1, 1, stat_level, 2) # Cure Moderate Wounds
		utils_npc_spells_inf.ctrl_add_spell(self, "Hold Person", 1, 1, stat_level, 2) # Hold Person
		utils_npc_spells_inf.ctrl_add_spell(self, "Bull's Strength", 3, 3, stat_level, 2) # Bull's Strength
		utils_npc_spells_inf.ctrl_add_spell(self, "Aid", 1, 1, stat_level, 2) # Aid
		utils_npc_spells_inf.ctrl_add_spell(self, "Chant", 1, 1, stat_level, 2) # Chant
		utils_npc_spells_inf.ctrl_add_spell(self, "Summon Monster II", 1, 1, stat_level, 2) # Summon Monster II
		
		return
	
class Ctrl_20ORCACH_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCACH 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCACH_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Orc Archer")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 5510) # Orc Bowman_Orc Bowman_14467
		
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 8, 8])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 14
		ac_natural_bonus = 14 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 1
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 1
		# stat_level_fighter: 1
		npc.make_class(toee.stat_level_fighter, 1)
		return
	
	def setup_char_feats(self, npc):
		# feats
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 8) # MaximumHP: 8
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 8
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 0
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		return
	
	def setup_char_cr(self, npc):
		cr = 0 # crnum_iwd2: 2, D&D CR: 1/2
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 2, 0, 0) # SaveVsDeath: 2, SaveVsWands: 0, SaveVsPolymorph: 0
		return
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: Longbow(Bows) from 00CWBOWG
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_LONGBOW, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # Longbow (00CWBOWG) at SLOT_WEAPON1 OK
		
		# SLOT_WEAPON2: None(Books) from 001D8S
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_BATTLEAXE, npc, no_loot = True, wear_on = None) # None (001D8S) at SLOT_WEAPON2
		
		# SLOT_AMMO1: Arrows(Arrows) from 00AROW01
		quiver = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc, no_loot = False, wear_on = toee.item_wear_ammo) # Arrows (00AROW01) at SLOT_AMMO1 OK
		quiver.obj_set_int(toee.obj_f_ammo_quantity, 15)
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20)) # Charges1: 10, Charges2: 20, Charges3: 0
		
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MASTERWORK_BARBARIAN, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return
	
	def setup_spells(self, npc):
		return
	
class Ctrl_20ORCA3_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCA3 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCA3_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Orc Archer")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 5510) # Orc Bowman_Orc Bowman_14467
		
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 8, 8])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 14
		ac_natural_bonus = 14 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 1
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 3
		# stat_level_fighter: 3
		npc.make_class(toee.stat_level_fighter, 3)
		return
	
	def setup_char_feats(self, npc):
		# feats
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 18) # MaximumHP: 18
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 18
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 0
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		return
	
	def setup_char_cr(self, npc):
		cr = 1 # crnum_iwd2: 3, D&D CR: 1
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 3, 1, 1) # SaveVsDeath: 3, SaveVsWands: 1, SaveVsPolymorph: 1
		return
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: Longbow(Bows) from 00CWBOWG
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_LONGBOW, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # Longbow (00CWBOWG) at SLOT_WEAPON1 OK
		
		# SLOT_WEAPON2: None(Books) from 001D8S
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_BATTLEAXE, npc, no_loot = True, wear_on = None) # None (001D8S) at SLOT_WEAPON2
		
		# SLOT_AMMO1: Arrows(Arrows) from 00AROW01
		quiver = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc, no_loot = False, wear_on = toee.item_wear_ammo) # Arrows (00AROW01) at SLOT_AMMO1 OK
		quiver.obj_set_int(toee.obj_f_ammo_quantity, 15)
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20)) # Charges1: 10, Charges2: 20, Charges3: 0
		
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MASTERWORK_BARBARIAN, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return
	
	def setup_spells(self, npc):
		return
	
class Ctrl_21OGR_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 21OGR 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_OGRE
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_21OGR_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Ogre")
		
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [21, 8, 15, 6, 10, 7])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 16
		ac_natural_bonus = 16 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		
		# from None(001D10C) at SLOT_WEAPON1 by ItemMiscMeleeNatural1d10C
		utils_npc.npc_natural_attack(npc, index = 0, attack_type = const_toee.nwt_slap, attack_bonus = 0, number = 1, damage_str = "1d10")
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 1
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 4
		# stat_level_fighter: 4
		npc.make_class(toee.stat_level_fighter, 4)
		return
	
	def setup_char_feats(self, npc):
		# feats
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 24) # MaximumHP: 24
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 24
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 0
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_EVIL) # 0x33 CHAOTIC_EVIL
		return
	
	def setup_char_cr(self, npc):
		cr = 2 # crnum_iwd2: 4, D&D CR: 2
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 1, 1) # SaveVsDeath: 4, SaveVsWands: 1, SaveVsPolymorph: 1
		return
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D10C
		# see natural
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(20, 40)) # Charges1: 20, Charges2: 40, Charges3: 0
		
		return
	
	def setup_spells(self, npc):
		return
	
class Ctrl_21SPDQN_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 21SPDQN 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_SPIDER_PHASE
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_21SPDQN_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Spider Queen")
		
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [15, 17, 12, 3, 10, 3])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 11
		ac_natural_bonus = 11 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 2
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 6
		# stat_level_fighter: 6
		npc.make_class(toee.stat_level_fighter, 6)
		return
	
	def setup_char_feats(self, npc):
		# feats
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 48) # MaximumHP: 48
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 48
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 0
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_NEUTRAL) # 0
		return
	
	def setup_char_cr(self, npc):
		cr = 3 # crnum_iwd2: 5, D&D CR: 3
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 1, 1) # SaveVsDeath: 4, SaveVsWands: 1, SaveVsPolymorph: 1
		return
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 00CWPOIS
		# Not found! TODO ITEM
		
		return
	
	def setup_spells(self, npc):
		return
	
class Ctrl_21SPDSML_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 21SPDSML 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_SPIDER_SMALL
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_21SPDSML_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Spider")
		
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [11, 17, 12, 3, 10, 3])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 11
		ac_natural_bonus = 11 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 1
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 2
		# stat_level_fighter: 2
		npc.make_class(toee.stat_level_fighter, 2)
		return
	
	def setup_char_feats(self, npc):
		# feats
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		npc.feat_add(toee.feat_weapon_finesse_short_sword) # Weapon finesse
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 14) # MaximumHP: 14
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 14
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 0
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		return
	
	def setup_char_cr(self, npc):
		cr = 1 # crnum_iwd2: 3, D&D CR: 1
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 3, 0, 0) # SaveVsDeath: 3, SaveVsWands: 0, SaveVsPolymorph: 0
		return
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D2P
		# Not found! TODO ITEM
		
		return
	
	def setup_spells(self, npc):
		return
	
class Ctrl_21HGHSNK_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 21HGHSNK 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_SNAKE_GIANT
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_21HGHSNK_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Highland Snake")
		
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [10, 19, 13, 3, 12, 3])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 11
		ac_natural_bonus = 11 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		
		# from None(001D10C) at SLOT_WEAPON1 by ItemMiscMeleeNatural1d10C
		utils_npc.npc_natural_attack(npc, index = 0, attack_type = const_toee.nwt_slap, attack_bonus = 0, number = 1, damage_str = "1d10")
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 2
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 6
		# stat_level_fighter: 6
		npc.make_class(toee.stat_level_fighter, 6)
		return
	
	def setup_char_feats(self, npc):
		# feats
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 34) # MaximumHP: 34
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 34
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 0
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		return
	
	def setup_char_cr(self, npc):
		cr = 3 # crnum_iwd2: 5, D&D CR: 3
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 4, 1) # SaveVsDeath: 4, SaveVsWands: 4, SaveVsPolymorph: 1
		return
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D10C
		# see natural
		
		return
	
	def setup_spells(self, npc):
		return
	
class Ctrl_21HRP_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 21HRP 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_HARPY
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_21HRP_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Harpy")
		
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [10, 15, 10, 7, 10, 15])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 11
		ac_natural_bonus = 11 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		
		# from None(001D3S) at SLOT_WEAPON1 by ItemMiscMeleeNatural1d3s
		utils_npc.npc_natural_attack(npc, index = 0, attack_type = const_toee.nwt_bite, attack_bonus = 0, number = self.get_attacks_per_round(npc), damage_str = "1d3")
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 2
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 7
		# stat_level_fighter: 7
		npc.make_class(toee.stat_level_fighter, 7)
		return
	
	def setup_char_feats(self, npc):
		# feats
		npc.feat_add(toee.feat_dodge) # Dodge
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 41) # MaximumHP: 41
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 41
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 0
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_EVIL) # 0x33 CHAOTIC_EVIL
		return
	
	def setup_char_cr(self, npc):
		cr = 3 # crnum_iwd2: 5, D&D CR: 3
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 2, 5, 5) # SaveVsDeath: 2, SaveVsWands: 5, SaveVsPolymorph: 5
		return
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D3S
		# see natural
		
		# SLOT_QUICK1: None(Books) from RT03_L
		# junk, skip and forget
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20)) # Charges1: 10, Charges2: 20, Charges3: 0
		
		return
	
	def setup_spells(self, npc):
		return
	
class Ctrl_21VERB_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 21VERB 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GIANT_VERBEEG
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_21VERB_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Verbeeg")
		
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [21, 8, 15, 6, 10, 7])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 16
		ac_natural_bonus = 16 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 2
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 5
		# stat_level_fighter: 5
		npc.make_class(toee.stat_level_fighter, 5)
		return
	
	def setup_char_feats(self, npc):
		# feats
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 27) # MaximumHP: 27
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 27
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 0
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_NEUTRAL_EVIL) # 0x23 NEUTRAL_EVIL
		return
	
	def setup_char_cr(self, npc):
		cr = 2 # crnum_iwd2: 4, D&D CR: 2
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 0, 1) # SaveVsDeath: 4, SaveVsWands: 0, SaveVsPolymorph: 1
		return
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D6P
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_SHORTSPEAR, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D6P) at SLOT_WEAPON1
		
		# SLOT_QUICK1: None(Books) from RT03_V
		# junk, skip and forget
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(20, 40)) # Charges1: 20, Charges2: 40, Charges3: 0
		
		return
	
	def setup_spells(self, npc):
		return
	
class Ctrl_20EMMA_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20EMMA 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	@classmethod
	def get_allegiance_default(cls): return 128 # NEUTRAL
	
	def setup_scripts(self, npc):
		super(Ctrl_20EMMA_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Emma Moonblade")
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_red # HairColourIndex: 4
		hairStyle.update_npc(npc)
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		self.hide_creature(npc, True)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [12, 14, 12, 12, 17, 14])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 15
		ac_natural_bonus = 15 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 2
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 8
		# stat_level_cleric: 8
		npc.make_class(toee.stat_level_cleric, 8)
		return
	
	def setup_char_feats(self, npc):
		# feats
		npc.feat_add(toee.feat_combat_casting) # Combat casting
		# shield proficiency:  => feat_shield_proficiency skip for cleric
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for cleric
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for cleric
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for cleric
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 49) # MaximumHP: 49
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 49
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 8
		utils_npc.npc_skill_ensure(npc, toee.skill_concentration, 8)
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_GOOD) # 0x31 CHAOTIC_GOOD
		return
	
	def setup_char_cr(self, npc):
		cr = 4 # crnum_iwd2: 6, D&D CR: 4
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 6, 2, 6) # SaveVsDeath: 6, SaveVsWands: 2, SaveVsPolymorph: 6
		return
	
	def setup_gear(self, npc):
		# SLOT_QUICK1: None(Books) from RT02_M
		# junk, skip and forget
		
		# SLOT_SELECTED_WEAPON: None(None) from None
		# Not found! TODO ITEM
		
		# SLOT_SELECTED_WEAPON_ABILITY: None(None) from None
		# Not found! TODO ITEM
		
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_GARB_FARMER_BLACK, npc, no_loot = True, wear_on = toee.item_wear_armor) # CLOTH BLACK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return
	
	def setup_spells(self, npc):
		stat_level = toee.stat_level_cleric # CLR
		#Level: 1
		utils_npc_spells_inf.ctrl_add_spell(self, "Magic Stone", 1, 1, stat_level, 1) # Magic Stone
		
		#Level: 2
		utils_npc_spells_inf.ctrl_add_spell(self, "Cure Moderate Wounds", 1, 1, stat_level, 2) # Cure Moderate Wounds
		utils_npc_spells_inf.ctrl_add_spell(self, "Silence", 1, 1, stat_level, 2) # Silence
		utils_npc_spells_inf.ctrl_add_spell(self, "Hold Person", 1, 1, stat_level, 2) # Hold Person
		
		#Level: 3
		utils_npc_spells_inf.ctrl_add_spell(self, "Cure Serious Wounds", 1, 1, stat_level, 3) # Cure Serious Wounds
		utils_npc_spells_inf.ctrl_add_spell(self, "Dispel Magic", 1, 1, stat_level, 3) # Dispel Magic
		utils_npc_spells_inf.ctrl_add_spell(self, "Miscast Magic", 1, 1, stat_level, 3) # Miscast Magic
		utils_npc_spells_inf.ctrl_add_spell(self, "Contagion", 1, 1, stat_level, 3) # Contagion
		utils_npc_spells_inf.ctrl_add_spell(self, "Circle of Bones", 1, 1, stat_level, 3) # Circle of Bones
		
		#Level: 4
		utils_npc_spells_inf.ctrl_add_spell(self, "Cure Critical Wounds", 2, 2, stat_level, 4) # Cure Critical Wounds
		
		return
	
class Ctrl_20KRIS_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20KRIS 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_20KRIS_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Kristian Deylore")
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_blonde # HairColourIndex: 3
		hairStyle.update_npc(npc)
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		self.hide_creature(npc, True)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [18, 12, 14, 10, 14, 14])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 15
		ac_natural_bonus = 15 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 1
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 8
		# stat_level_paladin: 8
		npc.make_class(toee.stat_level_paladin, 8)
		return
	
	def setup_char_feats(self, npc):
		# feats
		npc.feat_add(toee.feat_combat_casting) # Combat casting
		npc.feat_add("Extra Smiting") # Extra smiting
		npc.feat_add(toee.feat_power_attack) # Power attack
		# shield proficiency:  => feat_shield_proficiency skip for paladin
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for paladin
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for paladin
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for paladin
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for paladin
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for paladin
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for paladin
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for paladin
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for paladin
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for paladin
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for paladin
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 54) # MaximumHP: 54
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 54
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 8
		utils_npc.npc_skill_ensure(npc, toee.skill_concentration, 8)
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_GOOD) # 0x11 LAWFUL_GOOD
		return
	
	def setup_char_cr(self, npc):
		cr = 3 # crnum_iwd2: 5, D&D CR: 3
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 6, 2, 2) # SaveVsDeath: 6, SaveVsWands: 2, SaveVsPolymorph: 2
		return
	
	def setup_gear(self, npc):
		# SLOT_ARMOR: Half-plate Armor(HalfPlate) from 00PLAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_HALF_PLATE, npc, no_loot = False, wear_on = toee.item_wear_armor) # Half-plate Armor (00PLAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_SILVER_PLATE_BOOTS, npc, no_loot = False, wear_on = toee.item_wear_boots) # boots for Half-plate Armor (00PLAT01) OK
		
		# SLOT_WEAPON1: Bastard Sword +1(GreatSword) from 00CWSWDF
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD_PLUS_1, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # Bastard Sword +1 (00CWSWDF) at SLOT_WEAPON1 OK
		
		return
	
	def setup_spells(self, npc):
		return
	
class Ctrl_20KNTVIR_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20KNTVIR 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	@classmethod
	def get_allegiance_default(cls): return 255 # ENEMY
	
	def setup_scripts(self, npc):
		super(Ctrl_20KNTVIR_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Warrior of Virtue")
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black # HairColourIndex: 0
		hairStyle.update_npc(npc)
		return
	
	def setup_char(self, npc):
		self.setup_char_abilities(npc)
		self.setup_char_classes(npc)
		self.setup_char_natural(npc)
		self.setup_char_cr(npc)
		self.setup_char_feats(npc)
		self.setup_char_saves(npc)
		self.setup_char_hp(npc)
		self.setup_char_skills(npc)
		self.setup_char_alignment(npc)
		self.setup_spells(npc)
		self.hide_creature(npc, True)
		return
	
	def setup_char_abilities(self, npc):
		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		utils_npc.npc_abilities_set(npc, [16, 16, 10, 10, 12, 10])
		return
	
	def setup_char_natural(self, npc):
		# ArmorClassNatural: 13
		ac_natural_bonus = 13 - 10 - utils_npc.npc_size_penalty(npc)
		if ac_natural_bonus > 0:
			npc.obj_set_int(toee.obj_f_npc_ac_bonus, ac_natural_bonus)
		return
	
	def get_attacks_per_round(self, npc):
		# NumberOfAttacks: 1
		return npc.get_base_attack_bonus() // 5 + 1
	
	def setup_char_classes(self, npc):
		# class levels: 4
		# stat_level_paladin: 4
		npc.make_class(toee.stat_level_paladin, 4)
		return
	
	def setup_char_feats(self, npc):
		# feats
		npc.feat_add(toee.feat_power_attack) # Power attack
		# shield proficiency:  => feat_shield_proficiency skip for paladin
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for paladin
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for paladin
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for paladin
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for paladin
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for paladin
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for paladin
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for paladin
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for paladin
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for paladin
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for paladin
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		return
	
	def setup_char_hp(self, npc):
		
		# HP
		utils_npc.ensure_hp(npc, 48) # MaximumHP: 48
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 48
		return
	
	def setup_char_skills(self, npc):
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 4
		utils_npc.npc_skill_ensure(npc, toee.skill_concentration, 4)
		# SkillDiplomacy: 0
		# SkillDisableDevice: 0
		# SkillHide: 0
		# SkillIntimidate: 0
		# SkillKnowledgeArcana: 0
		# SkillMoveSilently: 0
		# SkillOpenLock: 0
		# SkillPickPocket: 0
		# SkillSearch: 0
		# SkillSpellcraft: 0
		# SkillUseMagicDevice: 0
		# SkillWildernessLaw: 0
		return
	
	def setup_char_alignment(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_GOOD) # 0x11 LAWFUL_GOOD
		return
	
	def setup_char_cr(self, npc):
		cr = 3 # crnum_iwd2: 5, D&D CR: 3
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		return
	
	def setup_char_saves(self, npc):
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 1, 1) # SaveVsDeath: 4, SaveVsWands: 1, SaveVsPolymorph: 1
		return
	
	def setup_gear(self, npc):
		# SLOT_HELMET: Helmet(HelmsHats) from 00HELM02
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELM_BARBARIAN, npc, no_loot = False, wear_on = toee.item_wear_helmet) # Helmet (00HELM02) at SLOT_HELMET OK
		
		# SLOT_ARMOR: Chainmail Armor(ChainMail) from 00CHAN01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_CHAINMAIL, npc, no_loot = False, wear_on = toee.item_wear_armor) # Chainmail Armor (00CHAN01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc, no_loot = False, wear_on = toee.item_wear_boots) # boots for Chainmail Armor (00CHAN01) OK
		
		# SLOT_WEAPON1: Masterwork Bastard Sword(GreatSword) from 00CWSWDE
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD_MASTERWORK, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # Masterwork Bastard Sword (00CWSWDE) at SLOT_WEAPON1 OK
		
		# SLOT_SHIELD1: None(Books) from 00SHIELD
		# Not found! TODO ITEM
		
		return
	
	def setup_spells(self, npc):
		return
	
