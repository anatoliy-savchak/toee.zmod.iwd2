import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting
#### IMPORTS ####
#### END IMPORTS ####

#### GVARS ####
MODULE_SCRIPT_ID = 20001
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
class Ctrl_20ORCACH_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCACH 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCACH_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Orc Archer")
		
		# npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 8, 8])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = 0 # crnum_iwd2: 2, D&D CR: 1/2
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
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
		
		# saves
		utils_npc.ensure_saves_natural(npc, 2, 0, 0) # SaveVsDeath: 2, SaveVsWands: 0, SaveVsPolymorph: 0
		
		# HP
		utils_npc.ensure_hp(npc, 8) # MaximumHP: 8
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 8
		
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
	
class Ctrl_20ORCWAR_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCWAR 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCWAR_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Orc")
		
		# npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 8, 8])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = 0 # crnum_iwd2: 2, D&D CR: 1/2
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
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
		
		# saves
		utils_npc.ensure_saves_natural(npc, 2, 0, 0) # SaveVsDeath: 2, SaveVsWands: 0, SaveVsPolymorph: 0
		
		# HP
		utils_npc.ensure_hp(npc, 8) # MaximumHP: 8
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 8
		
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
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D8S
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_BATTLEAXE, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D8S) at SLOT_WEAPON1
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20)) # Charges1: 10, Charges2: 20, Charges3: 0
		
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MASTERWORK_BARBARIAN, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return
	
class Ctrl_20ORCSHM_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCSHM 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCSHM_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Orc Shaman")
		
		# npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 14, 12])
		
		# class levels: 4
		# stat_level_cleric: 4
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_cleric)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_cleric)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_cleric)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_cleric)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = 1 # crnum_iwd2: 3, D&D CR: 3
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
		# feats
		npc.feat_add(toee.feat_combat_casting) # Combat casting
		# shield proficiency:  => feat_shield_proficiency skip for cleric
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for cleric
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for cleric
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for cleric
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 1, 4) # SaveVsDeath: 4, SaveVsWands: 1, SaveVsPolymorph: 4
		
		# HP
		utils_npc.ensure_hp(npc, 22) # MaximumHP: 22
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 22
		
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
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D6C
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_QUARTERSTAFF, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D6C) at SLOT_WEAPON1
		
		# SLOT_QUICK1: None(Books) from RT02_M
		# junk, skip and forget
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20)) # Charges1: 10, Charges2: 20, Charges3: 0
		
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_ROBES_BROWN_TEMPLE_EARTH, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return
	
class Ctrl_20ORCA3_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCA3 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCA3_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Orc Archer")
		
		# npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 8, 8])
		
		# class levels: 3
		# stat_level_fighter: 3
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = 1 # crnum_iwd2: 3, D&D CR: 3
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
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
		
		# saves
		utils_npc.ensure_saves_natural(npc, 3, 1, 1) # SaveVsDeath: 3, SaveVsWands: 1, SaveVsPolymorph: 1
		
		# HP
		utils_npc.ensure_hp(npc, 18) # MaximumHP: 18
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 18
		
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
	
class Ctrl_20ORCW3_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCW3 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCW3_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Orc Warrior")
		
		# npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 8, 8])
		
		# class levels: 3
		# stat_level_fighter: 3
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = 1 # crnum_iwd2: 3, D&D CR: 3
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
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
		
		# saves
		utils_npc.ensure_saves_natural(npc, 3, 1, 1) # SaveVsDeath: 3, SaveVsWands: 1, SaveVsPolymorph: 1
		
		# HP
		utils_npc.ensure_hp(npc, 18) # MaximumHP: 18
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 18
		
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
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D8S
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_BATTLEAXE, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D8S) at SLOT_WEAPON1
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20)) # Charges1: 10, Charges2: 20, Charges3: 0
		
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MASTERWORK_BARBARIAN, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return
	
class Ctrl_20ORCA4_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCA4 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCA4_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Orc Archer")
		
		# npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 8, 8])
		
		# class levels: 4
		# stat_level_fighter: 4
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = 2 # crnum_iwd2: 4, D&D CR: 4
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
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
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 1, 1) # SaveVsDeath: 4, SaveVsWands: 1, SaveVsPolymorph: 1
		
		# HP
		utils_npc.ensure_hp(npc, 22) # MaximumHP: 22
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 22
		
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
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: Longbow(Bows) from 00CWBOWG
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_LONGBOW, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # Longbow (00CWBOWG) at SLOT_WEAPON1 OK
		
		# SLOT_WEAPON2: None(Books) from 001D8S
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_BATTLEAXE, npc, no_loot = True, wear_on = None) # None (001D8S) at SLOT_WEAPON2
		
		# SLOT_AMMO1: Arrows(Arrows) from 00AROW01
		quiver = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc, no_loot = False, wear_on = toee.item_wear_ammo) # Arrows (00AROW01) at SLOT_AMMO1 OK
		quiver.obj_set_int(toee.obj_f_ammo_quantity, 15)
		
		# SLOT_QUICK1: None(Books) from RT02_L
		# junk, skip and forget
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20)) # Charges1: 10, Charges2: 20, Charges3: 0
		
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MASTERWORK_BARBARIAN, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return
	
class Ctrl_20ORCW4_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCW4 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCW4_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Orc Warrior")
		
		# npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 8, 8])
		
		# class levels: 4
		# stat_level_fighter: 4
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = 2 # crnum_iwd2: 4, D&D CR: 4
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
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
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 1, 1) # SaveVsDeath: 4, SaveVsWands: 1, SaveVsPolymorph: 1
		
		# HP
		utils_npc.ensure_hp(npc, 22) # MaximumHP: 22
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 22
		
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
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: None(Books) from 001D8S
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_BATTLEAXE, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D8S) at SLOT_WEAPON1
		
		# SLOT_QUICK1: None(Books) from RT02_L
		# junk, skip and forget
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20)) # Charges1: 10, Charges2: 20, Charges3: 0
		
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MASTERWORK_BARBARIAN, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return
	
class Ctrl_20ORCFIR_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCFIR 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCFIR_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Orc Firestarter")
		
		# npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 8, 8])
		
		# class levels: 4
		# stat_level_fighter: 4
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = 2 # crnum_iwd2: 4, D&D CR: 4
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
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
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 1, 1) # SaveVsDeath: 4, SaveVsWands: 1, SaveVsPolymorph: 1
		
		# HP
		utils_npc.ensure_hp(npc, 18) # MaximumHP: 18
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 18
		
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
	
	def setup_gear(self, npc):
		# SLOT_WEAPON1: Longbow(Bows) from 00CWBOWG
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_LONGBOW, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # Longbow (00CWBOWG) at SLOT_WEAPON1 OK
		
		# SLOT_WEAPON2: None(Books) from 001D8S
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_BATTLEAXE, npc, no_loot = True, wear_on = None) # None (001D8S) at SLOT_WEAPON2
		
		# SLOT_AMMO1: Arrow of Flame +1(Arrows) from 00CWARWB
		quiver = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc, no_loot = True, wear_on = toee.item_wear_ammo) # Arrow of Flame +1 (00CWARWB) at SLOT_AMMO1 OK
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20)) # Charges1: 10, Charges2: 20, Charges3: 0
		
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MASTERWORK_BARBARIAN, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return
	
class Ctrl_20ORCRUN_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCRUN 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCRUN_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Orc Runner")
		
		# npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 8, 8])
		
		# class levels: 4
		# stat_level_barbarian: 4
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_barbarian)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_barbarian)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_barbarian)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_barbarian)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = 1 # crnum_iwd2: 3, D&D CR: 3
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
		# feats
		# shield proficiency:  => feat_shield_proficiency skip for barbarian
		# FeatArmorPreficiency: 2 => feat_armor_proficiency_light skip for barbarian
		# FeatArmorPreficiency: 2 => feat_armor_proficiency_medium skip for barbarian
		# FeatWeaponProAxe: 1 => feat_martial_weapon_proficiency_throwing_axe skip for barbarian
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for barbarian
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for barbarian
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for barbarian
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for barbarian
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for barbarian
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for barbarian
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 1, 1) # SaveVsDeath: 4, SaveVsWands: 1, SaveVsPolymorph: 1
		
		# HP
		utils_npc.ensure_hp(npc, 18) # MaximumHP: 18
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 18
		
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
	
	def setup_gear(self, npc):
		# SLOT_BOOTS: Boots of Speed(Boots) from 10CICAT1
		# Not found! TODO ITEM
		
		# SLOT_WEAPON1: None(Books) from 001D8S
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_BATTLEAXE, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D8S) at SLOT_WEAPON1
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20)) # Charges1: 10, Charges2: 20, Charges3: 0
		
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MASTERWORK_BARBARIAN, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return
	
class Ctrl_20ORCCHF_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20ORCCHF 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ORC
	
	@classmethod
	def get_allegiance(cls): return 128
	
	def setup_scripts(self, npc):
		super(Ctrl_20ORCCHF_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Torak")
		
		# npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [15, 10, 11, 9, 8, 8])
		
		# class levels: 5
		# stat_level_fighter: 5
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 4, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = 3 # crnum_iwd2: 5, D&D CR: 5
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
		# feats
		npc.feat_add(toee.feat_power_attack) # Power attack
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
		
		# saves
		utils_npc.ensure_saves_natural(npc, 4, 1, 1) # SaveVsDeath: 4, SaveVsWands: 1, SaveVsPolymorph: 1
		
		# HP
		utils_npc.ensure_hp(npc, 43) # MaximumHP: 43
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 43
		
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
	
	def setup_gear(self, npc):
		# SLOT_ARMOR: Leather Armor +1(LeatherArmor) from 00LEAT02
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, npc, no_loot = False, wear_on = toee.item_wear_armor) # Leather Armor +1 (00LEAT02) at SLOT_ARMOR default TODO ITEM
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = False, wear_on = toee.item_wear_boots) # boots for Leather Armor +1 (00LEAT02) default
		
		# SLOT_WEAPON1: Battleaxe +1(Axes) from 00AX1H03
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_BATTLEAXE_PLUS_1, npc, no_loot = False, wear_on = toee.item_wear_weapon_primary) # Battleaxe +1 (00AX1H03) at SLOT_WEAPON1 OK
		
		# SLOT_QUICK1: None(Books) from RT02_R
		# junk, skip and forget
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(10, 20)) # Charges1: 10, Charges2: 20, Charges3: 0
		
		# SLOT_QUICK3: Highland Gate Key(Keys) from 22KEYHG1
		# Not found! TODO ITEM
		
		return
	
class Ctrl_20DERETH_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20DERETH 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	@classmethod
	def get_allegiance(cls): return 128
	
	def setup_scripts(self, npc):
		super(Ctrl_20DERETH_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Dereth Springsong")
		
		# npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_blonde # HairColourIndex: 3
		hairStyle.update_npc(npc)
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [10, 10, 12, 16, 18, 12])
		
		# class levels: 9
		# stat_level_druid: 9
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 4, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 5, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 6, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 7, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 8, toee.stat_level_druid)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		cr = 6 # crnum_iwd2: 8, D&D CR: 8
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
		# feats
		npc.feat_add(toee.feat_combat_casting) # Combat casting
		# shield proficiency:  => feat_shield_proficiency skip for druid
		# FeatArmorPreficiency: 2 => feat_armor_proficiency_light skip for druid
		# FeatArmorPreficiency: 2 => feat_armor_proficiency_medium skip for druid
		
		# FeatWeaponProLargeSword: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_longsword)
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_scimitar skip for druid
		
		# FeatWeaponProPolearm: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_halberd)
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		
		# saves
		utils_npc.ensure_saves_natural(npc, 6, 2, 6) # SaveVsDeath: 6, SaveVsWands: 2, SaveVsPolymorph: 6
		
		# HP
		utils_npc.ensure_hp(npc, 56) # MaximumHP: 56
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 56
		
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
	
	def setup_gear(self, npc):
		# SLOT_ARMOR: Studded Leather Armor +2(StuddedLeatherArmor) from 00LEAT07
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_PLUS_2, npc, no_loot = False, wear_on = toee.item_wear_armor) # Studded Leather Armor +2 (00LEAT07) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = False, wear_on = toee.item_wear_boots) # boots for Studded Leather Armor +2 (00LEAT07) OK
		
		# SLOT_WEAPON1: None(Books) from 001D8S
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_BATTLEAXE, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D8S) at SLOT_WEAPON1
		
		# SLOT_QUICK1: None(Books) from RT02_R
		# junk, skip and forget
		
		return
	
class Ctrl_20SABRIN_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 20SABRIN 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	@classmethod
	def get_allegiance(cls): return 128
	
	def setup_scripts(self, npc):
		super(Ctrl_20SABRIN_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Sabrina Fairwynd")
		
		# npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_red # HairColourIndex: 4
		hairStyle.update_npc(npc)
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [10, 12, 12, 12, 16, 16])
		
		# class levels: 7
		# stat_level_druid: 7
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 4, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 5, toee.stat_level_druid)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 6, toee.stat_level_druid)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		cr = 8 # crnum_iwd2: 10, D&D CR: 10
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
		# feats
		npc.feat_add(toee.feat_combat_casting) # Combat casting
		# shield proficiency:  => feat_shield_proficiency skip for druid
		# FeatArmorPreficiency: 2 => feat_armor_proficiency_light skip for druid
		# FeatArmorPreficiency: 2 => feat_armor_proficiency_medium skip for druid
		
		# FeatWeaponProLargeSword: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_longsword)
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_scimitar skip for druid
		
		# FeatWeaponProPolearm: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_halberd)
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		
		# saves
		utils_npc.ensure_saves_natural(npc, 5, 2, 5) # SaveVsDeath: 5, SaveVsWands: 2, SaveVsPolymorph: 5
		
		# HP
		utils_npc.ensure_hp(npc, 42) # MaximumHP: 42
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 42
		
		# skills
		# SkillAlchemy: 0
		# SkillAnimalEmpathy: 0
		# SkillBluff: 0
		# SkillConcentration: 7
		utils_npc.npc_skill_ensure(npc, toee.skill_concentration, 7)
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
	
	def setup_gear(self, npc):
		# SLOT_ARMOR: Leather Armor(LeatherArmor) from 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, npc, no_loot = False, wear_on = toee.item_wear_armor) # Leather Armor (00LEAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = False, wear_on = toee.item_wear_boots) # boots for Leather Armor (00LEAT01) OK
		
		# SLOT_WEAPON1: Scimitar(LongsSwords) from 00SWDC01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_SCIMITAR, npc, no_loot = False, wear_on = toee.item_wear_weapon_primary) # Scimitar (00SWDC01) at SLOT_WEAPON1 OK
		
		# SLOT_QUICK1: None(Books) from RT02_R
		# junk, skip and forget
		
		return
	
