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

class Ctrl10HEDRON(ctrl_behaviour.CtrlBehaviourAI): # 10HEDRON 
	@classmethod
	def get_name(cls): "10Hedron"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		utils_npc.npc_description_set_new(npc, "Hedron Kerdos")
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_light_brown # HairColourIndex: 5
		hairStyle.update_npc(npc)
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
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # CR: 5

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
		return

	def setup_gear(self, npc):
		# SLOT_ARMOR: Leather Armor(LeatherArmor) at 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, npc, False, toee.item_wear_armor) # Leather Armor (00LEAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, False, toee.item_wear_boots) # boots for Leather Armor (00LEAT01) OK
		
		# SLOT_WEAPON1: Spear(Spears) at 00SPER01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_SHORTSPEAR, npc, False, toee.item_wear_weapon_primary) # Spear (00SPER01) at SLOT_WEAPON1 OK
		
		# SLOT_QUICK1: Dagger(Daggers) at 00DAGG01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_DAGGER, npc, False, None) # Dagger (00DAGG01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Lynx Eye Gem(Gems) at 00GEM02
		# Not found! TODO ITEM
		
		# SLOT_QUICK3: Bottle of Wine(Drink) at 00MISC08
		# Not found! TODO ITEM
		
		return

class Ctrl10ELDGUL(ctrl_behaviour.CtrlBehaviourAI): # 10ELDGUL 
	@classmethod
	def get_name(cls): "10Eldgul"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		utils_npc.npc_description_set_new(npc, "Eldgull")
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_light_brown # HairColourIndex: 5
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [9, 15, 9, 9, 9, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_NEUTRAL) # 0x32 CHAOTIC_NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		return

	def setup_gear(self, npc):
		# SLOT_QUICK1: Club(Club) at 00CLUB01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_CLUB, npc, False, None) # Club (00CLUB01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Gold(Gold) at MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 2, 0) # Charges1: 1, Charges2: 2, Charges3: 0
		
		
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_LEATHER_CLOTHING, npc, False, toee.item_wear_armor) # default
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, False, toee.item_wear_boots) # default
		return

class Ctrl10SCREED(ctrl_behaviour.CtrlBehaviourAI): # 10SCREED 
	@classmethod
	def get_name(cls): "10Screed"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		utils_npc.npc_description_set_new(npc, "Screed")
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black # HairColourIndex: 0
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [12, 12, 9, 9, 9, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		utils_npc.ensure_hp(npc, 6) # MaximumHP: 6
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 6

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
		# SLOT_QUICK1: Dagger(Daggers) at 00DAGG01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_DAGGER, npc, False, None) # Dagger (00DAGG01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Gold(Gold) at MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 2, 0) # Charges1: 1, Charges2: 2, Charges3: 0
		
		
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_LEATHER_CLOTHING, npc, False, toee.item_wear_armor) # default
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, False, toee.item_wear_boots) # default
		return

class Ctrl10REIG(ctrl_behaviour.CtrlBehaviourAI): # 10REIG 
	@classmethod
	def get_name(cls): "10Reig"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		utils_npc.npc_description_set_new(npc, "Reig Redwaters")
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown # HairColourIndex: 2
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [12, 11, 10, 9, 9, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		utils_npc.ensure_hp(npc, 6) # MaximumHP: 6
		npc.obj_set_int(toee.obj_f_hp_damage, 3) # CurrentHP: 3

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
		# SLOT_ARMOR: Leather Armor(LeatherArmor) at 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, npc, False, toee.item_wear_armor) # Leather Armor (00LEAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, False, toee.item_wear_boots) # boots for Leather Armor (00LEAT01) OK
		
		# SLOT_QUICK1: Dagger(Daggers) at 00DAGG01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_DAGGER, npc, False, None) # Dagger (00DAGG01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Gold(Gold) at MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 2, 0) # Charges1: 1, Charges2: 2, Charges3: 0
		
		return

class Ctrl10JON(ctrl_behaviour.CtrlBehaviourAI): # 10JON 
	@classmethod
	def get_name(cls): "10Jon"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		utils_npc.npc_description_set_new(npc, "Honest Jon")
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_blonde # HairColourIndex: 3
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [12, 11, 12, 9, 9, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		utils_npc.ensure_hp(npc, 6) # MaximumHP: 6
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 6

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
		# SLOT_HELMET: Helmet(HelmsHats) at 00HELM01
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELM_DRUIDIC, npc, False, toee.item_wear_helmet) # Helmet (00HELM01) at SLOT_HELMET OK
		
		# SLOT_ARMOR: Leather Armor(LeatherArmor) at 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, npc, False, toee.item_wear_armor) # Leather Armor (00LEAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, False, toee.item_wear_boots) # boots for Leather Armor (00LEAT01) OK
		
		# SLOT_WEAPON1: Spear(Spears) at 00SPER01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_SHORTSPEAR, npc, False, toee.item_wear_weapon_primary) # Spear (00SPER01) at SLOT_WEAPON1 OK
		
		# SLOT_QUICK1: Dagger(Daggers) at 00DAGG01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_DAGGER, npc, False, None) # Dagger (00DAGG01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Gold(Gold) at MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 2, 0) # Charges1: 1, Charges2: 2, Charges3: 0
		
		return

class Ctrl10BROGAN(ctrl_behaviour.CtrlBehaviourAI): # 10BROGAN 
	@classmethod
	def get_name(cls): "10Brogan"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		utils_npc.npc_description_set_new(npc, "Brogan")
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown # HairColourIndex: 2
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [12, 11, 12, 9, 9, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		utils_npc.ensure_hp(npc, 6) # MaximumHP: 6
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 6

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
		# SLOT_HELMET: Helmet(HelmsHats) at 00HELM01
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELM_DRUIDIC, npc, False, toee.item_wear_helmet) # Helmet (00HELM01) at SLOT_HELMET OK
		
		# SLOT_ARMOR: Leather Armor(LeatherArmor) at 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, npc, False, toee.item_wear_armor) # Leather Armor (00LEAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, False, toee.item_wear_boots) # boots for Leather Armor (00LEAT01) OK
		
		# SLOT_WEAPON1: Battleaxe(Axes) at 00AX1H01
		# Not found! TODO ITEM
		
		# SLOT_QUICK1: Dagger(Daggers) at 00DAGG01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_DAGGER, npc, False, None) # Dagger (00DAGG01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Gold(Gold) at MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 2, 0) # Charges1: 1, Charges2: 2, Charges3: 0
		
		return

class Ctrl10JORUN(ctrl_behaviour.CtrlBehaviourAI): # 10JORUN 
	@classmethod
	def get_name(cls): "10Jorun"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		utils_npc.npc_description_set_new(npc, "Jorun Tamewater")
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black # HairColourIndex: 0
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [13, 12, 16, 15, 12, 9])
		
		# class levels: 3
		# stat_level_fighter: 3
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_NEUTRAL) # 0x12 LAWFUL_NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 65) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # CR: 2

		# feats
		npc.feat_add(toee.feat_iron_will) # Bullheaded
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
		# SLOT_ARMOR: Leather Armor(LeatherArmor) at 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, npc, False, toee.item_wear_armor) # Leather Armor (00LEAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, False, toee.item_wear_boots) # boots for Leather Armor (00LEAT01) OK
		
		# SLOT_WEAPON1: Warhammer(Hammers) at 00HAMM01
		# Not found! TODO ITEM
		
		return

