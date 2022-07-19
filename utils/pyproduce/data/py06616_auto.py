import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py06615_daemon_orc_fort, py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, py14764_npc_portal, utils_pc, module_difficulty

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
class Ctrl10HEDRON(NPCBase):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		utils_npc.npc_description_set_new(npc, "Hedron Kerdos")
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [13, 16, 12, 13, 14, 12])
		
		# class levels: 6
		# stat_level_fighter: 6
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 4, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 5, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_GOOD) # 0x31 CHAOTIC_GOOD
		npc.obj_set_int(toee.obj_f_critter_experience, 270) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 5)

		# feats
		npc.feat_add(toee.feat_shield_proficiency) # Shield proficiency
		
		# FeatArmorPreficiency: 3
		npc.feat_add(toee.feat_armor_proficiency_light)
		npc.feat_add(toee.feat_armor_proficiency_medium)
		npc.feat_add(toee.feat_armor_proficiency_heavy)
		
		# FeatWeaponProAxe: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_throwing_axe)
		npc.feat_add(toee.feat_martial_weapon_proficiency_handaxe)
		npc.feat_add(toee.feat_martial_weapon_proficiency_battleaxe)
		npc.feat_add(toee.feat_martial_weapon_proficiency_greataxe)
		
		# FeatWeaponProBow: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_shortbow)
		npc.feat_add(toee.feat_martial_weapon_proficiency_composite_shortbow)
		npc.feat_add(toee.feat_martial_weapon_proficiency_longbow)
		npc.feat_add(toee.feat_martial_weapon_proficiency_composite_longbow)
		
		# FeatWeaponProFlail: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_light_flail)
		npc.feat_add(toee.feat_martial_weapon_proficiency_heavy_flail)
		
		# FeatWeaponProGreatsword: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_greatsword)
		
		# FeatWeaponProHammer: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_light_hammer)
		npc.feat_add(toee.feat_martial_weapon_proficiency_warhammer)
		
		# FeatWeaponProLargeSword: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_longsword)
		npc.feat_add(toee.feat_martial_weapon_proficiency_scimitar)
		
		# FeatWeaponProPolearm: 2
		npc.feat_add(toee.feat_martial_weapon_proficiency_halberd)
		npc.feat_add(toee.feat_weapon_focus_halberd)

		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		
		# saves
		utils_npc.ensure_saves_natural(npc, 5, 2, 2) # SaveVsDeath: 5, SaveVsWands: 2, SaveVsPolymorph: 2
		
		# HP
		utils_npc.ensure_hp(npc, 31) # MaximumHP: 31
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 31

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
		
		# items
		# SLOT_ARMOR: Leather Armor(LeatherArmor) at 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, npc, False, toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, False, toee.item_wear_boots) # 
		
		# SLOT_WEAPON1: Spear(Spears) at 00SPER01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_SHORTSPEAR, npc, False, toee.item_wear_weapon_primary) # 
		
		# SLOT_QUICK1: Dagger(Daggers) at 00DAGG01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_DAGGER, npc, False, None) # 
		
		# SLOT_QUICK2: Lynx Eye Gem(Gems) at 00GEM02
		# SLOT_QUICK3: Bottle of Wine(Drink) at 00MISC08
		return

class Ctrl10ELDGUL(NPCBase):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		utils_npc.npc_description_set_new(npc, "Eldgull")
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [9, 15, 9, 9, 9, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_NEUTRAL) # 0x32 CHAOTIC_NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 1)

		# feats
		npc.feat_add(toee.feat_shield_proficiency) # Shield proficiency
		
		# FeatArmorPreficiency: 3
		npc.feat_add(toee.feat_armor_proficiency_light)
		npc.feat_add(toee.feat_armor_proficiency_medium)
		npc.feat_add(toee.feat_armor_proficiency_heavy)
		
		# FeatWeaponProAxe: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_throwing_axe)
		npc.feat_add(toee.feat_martial_weapon_proficiency_handaxe)
		npc.feat_add(toee.feat_martial_weapon_proficiency_battleaxe)
		npc.feat_add(toee.feat_martial_weapon_proficiency_greataxe)
		
		# FeatWeaponProBow: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_shortbow)
		npc.feat_add(toee.feat_martial_weapon_proficiency_composite_shortbow)
		npc.feat_add(toee.feat_martial_weapon_proficiency_longbow)
		npc.feat_add(toee.feat_martial_weapon_proficiency_composite_longbow)
		
		# FeatWeaponProFlail: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_light_flail)
		npc.feat_add(toee.feat_martial_weapon_proficiency_heavy_flail)
		
		# FeatWeaponProGreatsword: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_greatsword)
		
		# FeatWeaponProHammer: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_light_hammer)
		npc.feat_add(toee.feat_martial_weapon_proficiency_warhammer)
		
		# FeatWeaponProLargeSword: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_longsword)
		npc.feat_add(toee.feat_martial_weapon_proficiency_scimitar)
		
		# FeatWeaponProPolearm: 1
		npc.feat_add(toee.feat_martial_weapon_proficiency_halberd)

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
		
		# items
		# SLOT_QUICK1: Club(Club) at 00CLUB01
		# SLOT_QUICK2: Gold(Gold) at MISC07
		return

