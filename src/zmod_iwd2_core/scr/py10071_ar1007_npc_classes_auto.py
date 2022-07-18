import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting
#### IMPORTS ####
#### END IMPORTS ####

#### GVARS ####
MODULE_SCRIPT_ID = 10071
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
class Ctrl_10GOBC_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10GOBC 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GOBLIN
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_10GOBC_Auto, self).setup_scripts(npc)
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Goblin")
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [8, 13, 11, 10, 11, 8])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = -2 # crnum_iwd2: 1, D&D CR: 1/4
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
		utils_npc.ensure_hp(npc, 5) # MaximumHP: 5
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 5
		
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
		# SLOT_WEAPON1: None(Books) from 001D6S
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_HANDAXE, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D6S) at SLOT_WEAPON1
		
		# SLOT_QUICK1: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(1, 3)) # Charges1: 1, Charges2: 3, Charges3: 0
		
		# SLOT_QUICK2: None(Books) from 00RTGOB1
		# junk, skip and forget
		
		utils_item.item_create_in_inventory2(const_proto_armor_iwd2.PROTO_SHIELD_SMALL_WOODEN_EMPTY, npc, no_loot = True, wear_on = toee.item_wear_shield) # anim: Goblin_w_Axe
		return
	
class Ctrl_10GOBSC_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10GOBSC 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GOBLIN
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_10GOBSC_Auto, self).setup_scripts(npc)
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Goblin Sapper")
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [8, 13, 11, 10, 11, 8])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = -2 # crnum_iwd2: 1, D&D CR: 1/4
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
		utils_npc.ensure_hp(npc, 5) # MaximumHP: 5
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 5
		
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
		# SLOT_WEAPON1: None(Books) from 001D6S
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_HANDAXE, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D6S) at SLOT_WEAPON1
		
		# SLOT_QUICK1: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(1, 3)) # Charges1: 1, Charges2: 3, Charges3: 0
		
		# SLOT_QUICK2: None(Books) from 00RTFIRE
		# junk, skip and forget
		
		utils_item.item_create_in_inventory2(const_proto_armor_iwd2.PROTO_SHIELD_SMALL_WOODEN_EMPTY, npc, no_loot = True, wear_on = toee.item_wear_shield) # anim: Goblin_w_Axe
		return
	
class Ctrl_10GOBD_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10GOBD 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GOBLIN
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_10GOBD_Auto, self).setup_scripts(npc)
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Goblin")
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [8, 13, 11, 10, 11, 8])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = -2 # crnum_iwd2: 1, D&D CR: 1/4
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
		utils_npc.ensure_hp(npc, 4) # MaximumHP: 4
		npc.obj_set_int(toee.obj_f_hp_damage, 14) # CurrentHP: 4, STATE_DEAD
		
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
		utils_item.item_create_in_inventory2(const_proto_armor_iwd2.PROTO_SHIELD_SMALL_WOODEN_EMPTY, npc, no_loot = True, wear_on = toee.item_wear_shield) # anim: Goblin_w_Axe
		return
	
class Ctrl_10RUKWU_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10RUKWU 
	@classmethod
	def get_proto_id(cls): return 14192
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_10RUKWU_Auto, self).setup_scripts(npc)
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Rukwurm")
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [13, 13, 12, 10, 11, 9])
		
		# class levels: 2
		# stat_level_fighter: 2
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = 0 # crnum_iwd2: 2, D&D CR: 1/2
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
		# feats
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 2 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		
		# saves
		utils_npc.ensure_saves_natural(npc, 3, 0, 0) # SaveVsDeath: 3, SaveVsWands: 0, SaveVsPolymorph: 0
		
		# HP
		utils_npc.ensure_hp(npc, 12) # MaximumHP: 12
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 12
		
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
		
		# SLOT_INV4: Expended Teleportation Scroll(Notes) from 10VELLUM
		utils_item.item_create_in_inventory2(const_proto_items_iwd2.PROTO_GENERIC_EXPENDED_TELEPORTATION_SCROLL, npc, no_loot = False, wear_on = None) # Expended Teleportation Scroll (10VELLUM) at SLOT_INV4 OK
		
		# SLOT_INV5: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(9, 21)) # Charges1: 9, Charges2: 21, Charges3: 0
		
		# SLOT_INV6: None(Books) from 00RG05
		# junk, skip and forget
		
		# SLOT_INV7: None(Books) from RT01_M
		# junk, skip and forget
		
		utils_item.item_create_in_inventory2(const_proto_armor_iwd2.PROTO_SHIELD_SMALL_WOODEN_EMPTY, npc, no_loot = True, wear_on = toee.item_wear_shield) # anim: Goblin Elite w/ Axe
		return
	
class Ctrl_10ULEK_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10ULEK 
	@classmethod
	def get_proto_id(cls): return 14192
	
	@classmethod
	def get_allegiance(cls): return 255
	
	def setup_scripts(self, npc):
		super(Ctrl_10ULEK_Auto, self).setup_scripts(npc)
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Ulek the Burrower")
		
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [13, 13, 12, 10, 11, 9])
		
		# class levels: 2
		# stat_level_fighter: 2
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		cr = 0 # crnum_iwd2: 2, D&D CR: 1/2
		cr_bonus = cr - npc.stat_level_get(toee.stat_level)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)
		
		# feats
		# shield proficiency:  => feat_shield_proficiency skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_light skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_medium skip for fighter
		# FeatArmorPreficiency: 3 => feat_armor_proficiency_heavy skip for fighter
		# FeatWeaponProAxe: 2 => feat_martial_weapon_proficiency_throwing_axe skip for fighter
		# FeatWeaponProBow: 1 => feat_martial_weapon_proficiency_shortbow skip for fighter
		# FeatWeaponProFlail: 1 => feat_martial_weapon_proficiency_light_flail skip for fighter
		# FeatWeaponProGreatsword: 1 => feat_martial_weapon_proficiency_greatsword skip for fighter
		# FeatWeaponProHammer: 1 => feat_martial_weapon_proficiency_light_hammer skip for fighter
		# FeatWeaponProLargeSword: 1 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		
		# saves
		utils_npc.ensure_saves_natural(npc, 3, 0, 0) # SaveVsDeath: 3, SaveVsWands: 0, SaveVsPolymorph: 0
		
		# HP
		utils_npc.ensure_hp(npc, 12) # MaximumHP: 12
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 12
		
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
		
		# SLOT_QUICK1: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(9, 21)) # Charges1: 9, Charges2: 21, Charges3: 0
		
		# SLOT_QUICK2: None(Books) from 00RG05
		# junk, skip and forget
		
		# SLOT_QUICK3: None(Books) from RT01_M
		# junk, skip and forget
		
		utils_item.item_create_in_inventory2(const_proto_armor_iwd2.PROTO_SHIELD_SMALL_WOODEN_EMPTY, npc, no_loot = True, wear_on = toee.item_wear_shield) # anim: Goblin Elite w/ Axe
		return
	
