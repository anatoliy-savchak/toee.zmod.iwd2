import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py06615_daemon_orc_fort, py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, py14764_npc_portal, utils_pc
import const_proto_armor_iwd2

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
		utils_npc.npc_description_set_new(npc, "Hedron Kerdos")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_light_brown # HairColourIndex: 5
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		
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
		# FeatWeaponProPolearm: 2 => feat_martial_weapon_proficiency_halberd skip for fighter

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
		# SLOT_ARMOR: Leather Armor(LeatherArmor) from 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, npc, no_loot = False, wear_on = toee.item_wear_armor) # Leather Armor (00LEAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = False, wear_on = toee.item_wear_boots) # boots for Leather Armor (00LEAT01) OK
		
		# SLOT_WEAPON1: Spear(Spears) from 00SPER01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_SHORTSPEAR, npc, no_loot = False, wear_on = toee.item_wear_weapon_primary) # Spear (00SPER01) at SLOT_WEAPON1 OK
		
		# SLOT_QUICK1: Dagger(Daggers) from 00DAGG01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_DAGGER, npc, no_loot = False, wear_on = None) # Dagger (00DAGG01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Lynx Eye Gem(Gems) from 00GEM02
		# Not found! TODO ITEM
		
		# SLOT_QUICK3: Bottle of Wine(Drink) from 00MISC08
		# Not found! TODO ITEM
		
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		# NumTimesTalkedTo(0)
		if not attachee.has_met(triggerer):
			line_id = 10 # Well, here ye are, straight from Bremen to the scenic shore of Targos herself.  Now that ye be seeing the skeleton of the town ye'll be defendin', ye sure ye don't want me to take ye back?
		
		# GlobalGT("Reig_Quest", "GLOBAL", 0)
		# Global("Dock_Goblin_Quest", "GLOBAL", 0)
		# Global("Hedron_Know_Attack", "GLOBAL", 0)
		if ies.GlobalGT("Reig_Quest", "GLOBAL", 0) \
			and ies.Global("Dock_Goblin_Quest", "GLOBAL", 0) \
			and ies.Global("Hedron_Know_Attack", "GLOBAL", 0):
			line_id = 20 # I was hoping ye might come back - what's the word from the docks?  Not even Magdar's come out to shake me down yet, and he usually sends some half-drunk stumblers to help unload my supplies.
		
		# GlobalGT("Reig_Quest", "GLOBAL", 0)
		# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
		if ies.GlobalGT("Reig_Quest", "GLOBAL", 0) \
			and ies.GlobalLT("Hedron_Know_Attack", "GLOBAL", 2):
			line_id = 30 # What's going on along the shore?  I heard something about an attack on the docks, but no one can tell me anything for certain.
		
		# GlobalGT("Hedron_Know_Attack", "GLOBAL", 0)
		# GlobalGT("Hedron_Quest", "GLOBAL", 0)
		# GlobalLT("Hedron_Quest", "GLOBAL", 4)
		if ies.GlobalGT("Hedron_Know_Attack", "GLOBAL", 0) \
			and ies.GlobalGT("Hedron_Quest", "GLOBAL", 0) \
			and ies.GlobalLT("Hedron_Quest", "GLOBAL", 4):
			line_id = 40 # You're back - any word of me Ma?
		
		# NumTimesTalkedToGT(0)
		# Global("Reig_Quest", "GLOBAL", 0)
		if attachee.has_met(triggerer) \
			and ies.Global("Reig_Quest", "GLOBAL", 0):
			line_id = 50 # Aye, look who's come back aboard - sick of Targos already, are ye?
		
		# Global("Hedron_Know_Attack", "GLOBAL", 2)
		if ies.Global("Hedron_Know_Attack", "GLOBAL", 2):
			line_id = 60 # Aye, look who's come back aboard - the great goblin slayers of Targos.  What can I do for ye?
		
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		return toee.SKIP_DEFAULT
	
class Ctrl10ELDGUL(ctrl_behaviour.CtrlBehaviourAI): # 10ELDGUL 
	@classmethod
	def get_name(cls): "10Eldgul"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Eldgull")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_light_brown # HairColourIndex: 5
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		
		utils_npc.npc_abilities_set(npc, [9, 15, 9, 9, 9, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_NEUTRAL) # 0x32 CHAOTIC_NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		# SLOT_QUICK1: Club(Club) from 00CLUB01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_CLUB, npc, no_loot = False, wear_on = None) # Club (00CLUB01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 2, 0) # Charges1: 1, Charges2: 2, Charges3: 0
		
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_LEATHER_CLOTHING, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		# True()
		if ies.True():
			line_id = 70 # Can't stop t'bandy words with ye; Hedron be findin' *more* work for me after I finish this bit.  Fare thee well.
		
		# GlobalGT("Reig_Quest", "GLOBAL", 0)
		if ies.GlobalGT("Reig_Quest", "GLOBAL", 0):
			line_id = 80 # Is it true?  I hear th'town's bein' attacked by the goblins!
		
		# Global("Dock_Goblin_Quest", "GLOBAL", 1)
		if ies.Global("Dock_Goblin_Quest", "GLOBAL", 1):
			line_id = 90 # Caught word 'bout the battle - looks like ye pulled through - good for ye.
		
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		return toee.SKIP_DEFAULT
	
class Ctrl10SCREED(ctrl_behaviour.CtrlBehaviourAI): # 10SCREED 
	@classmethod
	def get_name(cls): "10Screed"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Screed")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black # HairColourIndex: 0
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		
		utils_npc.npc_abilities_set(npc, [12, 12, 9, 9, 9, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		# SLOT_QUICK1: Dagger(Daggers) from 00DAGG01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_DAGGER, npc, no_loot = False, wear_on = None) # Dagger (00DAGG01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 2, 0) # Charges1: 1, Charges2: 2, Charges3: 0
		
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_LEATHER_CLOTHING, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		# True()
		if ies.True():
			line_id = 100 # Was good havin' ye with us, even for only a short time.  Hope fortune's wind fills yer sails, friend.
		
		# GlobalGT("Reig_Quest", "GLOBAL", 0)
		if ies.GlobalGT("Reig_Quest", "GLOBAL", 0):
			line_id = 110 # I hear the town's being attacked again - the Wicked Wench's all ready to set sail if ye need to fall back.
		
		# Global("Dock_Goblin_Quest", "GLOBAL", 1)
		if ies.Global("Dock_Goblin_Quest", "GLOBAL", 1):
			line_id = 120 # Heard th' fightin' up along the docks was fierce - drove those goblins back, did ye?
		
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		return toee.SKIP_DEFAULT
	
class Ctrl10REIG(ctrl_behaviour.CtrlBehaviourAI): # 10REIG 
	@classmethod
	def get_name(cls): "10Reig"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Reig Redwaters")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown # HairColourIndex: 2
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		
		utils_npc.npc_abilities_set(npc, [12, 11, 10, 9, 9, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		# SLOT_ARMOR: Leather Armor(LeatherArmor) from 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, npc, no_loot = False, wear_on = toee.item_wear_armor) # Leather Armor (00LEAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = False, wear_on = toee.item_wear_boots) # boots for Leather Armor (00LEAT01) OK
		
		# SLOT_QUICK1: Dagger(Daggers) from 00DAGG01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_DAGGER, npc, no_loot = False, wear_on = None) # Dagger (00DAGG01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 2, 0) # Charges1: 1, Charges2: 2, Charges3: 0
		
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		# NumTimesTalkedTo(0)
		if not attachee.has_met(triggerer):
			line_id = 130 # Halt!  Who goes there?  Step forward and identify yourself!
		
		# Global("Reig_Quest", "GLOBAL", 1)
		if ies.Global("Reig_Quest", "GLOBAL", 1):
			line_id = 140 # Did you find Magdar?  My damned arm's getting worse, and I need that potion he's got.
		
		# HPGT(Myself, 3)
		# Global("Reig_Quest", "GLOBAL", 1)
		# Global("Reig_Heal_Priest", "GLOBAL", 0)
		if ies.HPGT(Myself, 3) \
			and ies.Global("Reig_Quest", "GLOBAL", 1) \
			and ies.Global("Reig_Heal_Priest", "GLOBAL", 0):
			line_id = 150 # My arm's better, thanks for your help.  Looks like you're praying to the right gods.
		
		# Global("Reig_Quest", "GLOBAL", 1)
		# Global("Reig_Heal_Priest", "GLOBAL", 1)
		if ies.Global("Reig_Quest", "GLOBAL", 1) \
			and ies.Global("Reig_Heal_Priest", "GLOBAL", 1):
			line_id = 160 # I could still use that healing draught from Magdar if you can find him.  Hope the goblins haven't got him yet.
		
		# Global("Reig_Quest", "GLOBAL", 2)
		if ies.Global("Reig_Quest", "GLOBAL", 2):
			line_id = 170 # Looks like you sailed into Targos at the right time.  If you can help us hunt down any of those goblins, we'd welcome your help.
		
		# Global("Told_Reig", "GLOBAL", 1)
		if ies.Global("Told_Reig", "GLOBAL", 1):
			line_id = 180 # Now that the raiders have been taken care of, we should be all right.  You should report to Lord Ulbrec up in the main town - he'll be glad to know we have reinforcements.
		
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		return toee.SKIP_DEFAULT
	
class Ctrl10JON(ctrl_behaviour.CtrlBehaviourAI): # 10JON 
	@classmethod
	def get_name(cls): "10Jon"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Honest Jon")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_blonde # HairColourIndex: 3
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		
		utils_npc.npc_abilities_set(npc, [12, 11, 12, 9, 9, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		# SLOT_HELMET: Helmet(HelmsHats) from 00HELM01
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELM_DRUIDIC, npc, no_loot = False, wear_on = toee.item_wear_helmet) # Helmet (00HELM01) at SLOT_HELMET OK
		
		# SLOT_ARMOR: Leather Armor(LeatherArmor) from 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, npc, no_loot = False, wear_on = toee.item_wear_armor) # Leather Armor (00LEAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = False, wear_on = toee.item_wear_boots) # boots for Leather Armor (00LEAT01) OK
		
		# SLOT_WEAPON1: Spear(Spears) from 00SPER01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_SHORTSPEAR, npc, no_loot = False, wear_on = toee.item_wear_weapon_primary) # Spear (00SPER01) at SLOT_WEAPON1 OK
		
		# SLOT_QUICK1: Dagger(Daggers) from 00DAGG01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_DAGGER, npc, no_loot = False, wear_on = None) # Dagger (00DAGG01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 2, 0) # Charges1: 1, Charges2: 2, Charges3: 0
		
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		# Global("Dock_Goblin_Quest", "GLOBAL", 0)
		if ies.Global("Dock_Goblin_Quest", "GLOBAL", 0):
			line_id = 190 # No idea where those goblins came from - one moment we're stepping out of the Salty Dog, and suddenly there's a mess of them running through town.  We sounded the alarm, but...
		
		# Global("Dock_Goblin_Quest", "GLOBAL", 1)
		if ies.Global("Dock_Goblin_Quest", "GLOBAL", 1):
			line_id = 200 # Tymora must have been smiling on us when you sailed into town.  Without you to drive back the goblins, the docks might have been burning now, and Targos overrun.
		
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		return toee.SKIP_DEFAULT
	
class Ctrl10BROGAN(ctrl_behaviour.CtrlBehaviourAI): # 10BROGAN 
	@classmethod
	def get_name(cls): "10Brogan"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Brogan")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown # HairColourIndex: 2
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		
		utils_npc.npc_abilities_set(npc, [12, 11, 12, 9, 9, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		# SLOT_HELMET: Helmet(HelmsHats) from 00HELM01
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELM_DRUIDIC, npc, no_loot = False, wear_on = toee.item_wear_helmet) # Helmet (00HELM01) at SLOT_HELMET OK
		
		# SLOT_ARMOR: Leather Armor(LeatherArmor) from 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, npc, no_loot = False, wear_on = toee.item_wear_armor) # Leather Armor (00LEAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = False, wear_on = toee.item_wear_boots) # boots for Leather Armor (00LEAT01) OK
		
		# SLOT_WEAPON1: Battleaxe(Axes) from 00AX1H01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_BATTLEAXE, npc, no_loot = False, wear_on = toee.item_wear_weapon_primary) # Battleaxe (00AX1H01) at SLOT_WEAPON1 OK
		
		# SLOT_QUICK1: Dagger(Daggers) from 00DAGG01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_DAGGER, npc, no_loot = False, wear_on = None) # Dagger (00DAGG01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 2, 0) # Charges1: 1, Charges2: 2, Charges3: 0
		
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		# True()
		if ies.True():
			line_id = 210 # Halt!  Identify yourself!
		
		# GlobalGT("Iron_Collar_Quest", "GLOBAL", 0)
		# GlobalLT("Iron_Collar_Quest", "GLOBAL", 3)
		# Global("Brogan_Quest", "GLOBAL", 0)
		# Global("AR1002_Visited", "GLOBAL", 0)
		if ies.GlobalGT("Iron_Collar_Quest", "GLOBAL", 0) \
			and ies.GlobalLT("Iron_Collar_Quest", "GLOBAL", 3) \
			and ies.Global("Brogan_Quest", "GLOBAL", 0) \
			and ies.Global("AR1002_Visited", "GLOBAL", 0):
			line_id = 220 # You're back!  Did you bring the Iron Collar Band with you?
		
		# Global("Brogan_Quest", "GLOBAL", 1)
		if ies.Global("Brogan_Quest", "GLOBAL", 1):
			line_id = 230 # Did you take out those goblins yet?  Time's running short.
		
		# Global("Brogan_Quest", "GLOBAL", 1)
		# Global("AR1002_Visited", "GLOBAL", 1)
		# Global("AR1007_Visited", "GLOBAL", 1)
		if ies.Global("Brogan_Quest", "GLOBAL", 1) \
			and ies.Global("AR1002_Visited", "GLOBAL", 1) \
			and ies.Global("AR1007_Visited", "GLOBAL", 1):
			line_id = 240 # Where in Tempus' name have you *been?*  I heard the fighting, and then everything went silent.  Thought you were dead.
		
		# Global("AR1002_Visited", "GLOBAL", 1)
		# Global("Know_Brogan", "GLOBAL", 0)
		if ies.Global("AR1002_Visited", "GLOBAL", 1) \
			and ies.Global("Know_Brogan", "GLOBAL", 0):
			line_id = 250 # Are you mad?  That was a foolish thing for you to do - breaking into that warehouse!  You could have been killed!
		
		# Global("Brogan_Leave", "GLOBAL", 1)
		if ies.Global("Brogan_Leave", "GLOBAL", 1):
			line_id = 260 # I respect your courage.  If you tell of your deeds to Lord Ulbrec, he is sure to reward you.
		
		# GlobalGT("Iron_Collar_Quest", "GLOBAL", 0)
		# GlobalLT("Iron_Collar_Quest", "GLOBAL", 3)
		# Global("Brogan_Quest", "GLOBAL", 0)
		# Global("AR1002_Visited", "GLOBAL", 1)
		if ies.GlobalGT("Iron_Collar_Quest", "GLOBAL", 0) \
			and ies.GlobalLT("Iron_Collar_Quest", "GLOBAL", 3) \
			and ies.Global("Brogan_Quest", "GLOBAL", 0) \
			and ies.Global("AR1002_Visited", "GLOBAL", 1):
			line_id = 270 # Are you mad?  That was a foolish thing for you to do - breaking into that warehouse!  You could have been killed!
		
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		return toee.SKIP_DEFAULT
	
class Ctrl10JORUN(ctrl_behaviour.CtrlBehaviourAI): # 10JORUN 
	@classmethod
	def get_name(cls): "10Jorun"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Jorun Tamewater")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black # HairColourIndex: 0
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		
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
		# SLOT_ARMOR: Leather Armor(LeatherArmor) from 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, npc, no_loot = False, wear_on = toee.item_wear_armor) # Leather Armor (00LEAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = False, wear_on = toee.item_wear_boots) # boots for Leather Armor (00LEAT01) OK
		
		# SLOT_WEAPON1: Warhammer(Hammers) from 00HAMM01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_WARHAMMER, npc, no_loot = False, wear_on = toee.item_wear_weapon_primary) # Warhammer (00HAMM01) at SLOT_WEAPON1 OK
		
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		# Global("Know_Jorun", "GLOBAL", 0)
		# Global("Dock_Goblin_Quest", "GLOBAL", 0)
		if ies.Global("Know_Jorun", "GLOBAL", 0) \
			and ies.Global("Dock_Goblin_Quest", "GLOBAL", 0):
			line_id = 280 # Damnable goblins... it seems no matter what corners o' the world y'go, they're always there.  Who are ye?  Do ye stand with Targos?
		
		# Global("Know_Jorun", "GLOBAL", 1)
		# Global("Dock_Goblin_Quest", "GLOBAL", 0)
		if ies.Global("Know_Jorun", "GLOBAL", 1) \
			and ies.Global("Dock_Goblin_Quest", "GLOBAL", 0):
			line_id = 290 # Have ye spilled any more goblin blood?  Ye better not be greedy - make ye sure ye save a handful for me.
		
		# Global("Know_Jorun", "GLOBAL", 0)
		# Global("Dock_Goblin_Quest", "GLOBAL", 1)
		if ies.Global("Know_Jorun", "GLOBAL", 0) \
			and ies.Global("Dock_Goblin_Quest", "GLOBAL", 1):
			line_id = 300 # Well, now, something I can help ye with?  I'm not doing business with the attacks an' all, and there's not much call for building ships as much as taking them down.
		
		# Global("Know_Jorun", "GLOBAL", 1)
		# Global("Dock_Goblin_Quest", "GLOBAL", 1)
		if ies.Global("Know_Jorun", "GLOBAL", 1) \
			and ies.Global("Dock_Goblin_Quest", "GLOBAL", 1):
			line_id = 310 # More than once ye've crossed my path; if ye plan on makin' a habit of it, the least ye could do is bring a winecask with ye... or two. Somethin' I can do for ye?
		
		# NumTimesTalkedTo(0)
		# Subrace(Protagonist, Dwarf_Gray)
		# Global("Dock_Goblin_Quest", "GLOBAL", 0)
		if not attachee.has_met(triggerer) \
			and ies.Subrace(Protagonist, Dwarf_Gray) \
			and ies.Global("Dock_Goblin_Quest", "GLOBAL", 0):
			line_id = 320 # Eh?!  A duergar in Targos?  Ye were the last beast I expected to see in league with these goblins, but it'll give me pleasure to bury yer black heart alongside them.
		
		# NumTimesTalkedTo(0)
		# Subrace(Protagonist, Elf_Drow)
		# Global("Dock_Goblin_Quest", "GLOBAL", 0)
		if not attachee.has_met(triggerer) \
			and ies.Subrace(Protagonist, Elf_Drow) \
			and ies.Global("Dock_Goblin_Quest", "GLOBAL", 0):
			line_id = 330 # Eh?!  A drow in Targos?  Ye were the last beast I expected to see in league with these goblins, but it'll give me pleasure to bury yer black heart alongside them.
		
		# NumTimesTalkedTo(0)
		# Subrace(Protagonist, Gnome_Deep)
		# Global("Dock_Goblin_Quest", "GLOBAL", 0)
		if not attachee.has_met(triggerer) \
			and ies.Subrace(Protagonist, Gnome_Deep) \
			and ies.Global("Dock_Goblin_Quest", "GLOBAL", 0):
			line_id = 340 # Damn me eyes... are ye a deep gnome?  What in the hells are ye doing in Targos?
		
		# NumTimesTalkedTo(0)Subrace(Protagonist, Dwarf_Gray)Global("Dock_Goblin_Quest", "GLOBAL", 1)
		if ies.NumTimesTalkedTo(0)Subrace(Protagonist, Dwarf_Gray)Global("Dock_Goblin_Quest", "GLOBAL", 1):
			line_id = 350 # I heard talk of a duergar around town... didn't put much stock in it 'til now.  I hear ye done a good job splitting goblins in half, but ye've still got a long way to go to earning my trust... and Targos' trust.  Now what did ye want with this ol' shipbuilder?
		
		# NumTimesTalkedTo(0)Subrace(Protagonist, Elf_Drow)Global("Dock_Goblin_Quest", "GLOBAL", 1)
		if ies.NumTimesTalkedTo(0)Subrace(Protagonist, Elf_Drow)Global("Dock_Goblin_Quest", "GLOBAL", 1):
			line_id = 360 # I heard talk of a drow around town... didn't put much stock in it 'til now.  I hear ye done a good job splitting goblins in half, but ye've still got a long way to go to earning my trust... and Targos' trust.  Now what did ye want with this ol' shipbuilder?
		
		# NumTimesTalkedTo(0)Subrace(Protagonist, Gnome_Deep)Global("Dock_Goblin_Quest", "GLOBAL", 1)
		if ies.NumTimesTalkedTo(0)Subrace(Protagonist, Gnome_Deep)Global("Dock_Goblin_Quest", "GLOBAL", 1):
			line_id = 370 # Damn me eyes... ye're the deep gnome everyone's going on about.  I was hoping ye might be crossing me path - something this ol' shipbuilder can help ye with? 
		
		# NumTimesTalkedTo(0)Race(Protagonist, Dwarf)Global("Dock_Goblin_Quest", "GLOBAL", 0)
		if ies.NumTimesTalkedTo(0)Race(Protagonist, Dwarf)Global("Dock_Goblin_Quest", "GLOBAL", 0):
			line_id = 380 # It's good to see another dwarf on the shore of Maer Dualdon especially with these damnable goblins about... it seems no matter what corners o' the world y'go, they're always there.  Who are ye?  Do ye come to add yer axe and hammer to Targos? 
		
		# NumTimesTalkedTo(0)Race(Protagonist, Dwarf)Global("Dock_Goblin_Quest", "GLOBAL", 0)
		if ies.NumTimesTalkedTo(0)Race(Protagonist, Dwarf)Global("Dock_Goblin_Quest", "GLOBAL", 0):
			line_id = 390 # Well, now, a dwarf is a sight for sore eyes in these windswept lands... especially one who can cleave goblins as well as ye can.  Something this ol' shipbuilder can help ye with?  
		
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		return toee.SKIP_DEFAULT
	
class Ctrl10MALED(ctrl_behaviour.CtrlBehaviourAI): # 10MALED 
	@classmethod
	def get_name(cls): "10MaleD"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Townsperson")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black # HairColourIndex: 0
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [11, 9, 12, 9, 10, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		npc.obj_set_int(toee.obj_f_hp_damage, 15) # CurrentHP: 5, STATE_DEAD

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
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_GARB_MYSTIC_TEAL, npc, no_loot = True, wear_on = toee.item_wear_armor) # CLOTH LT INDIGO
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return

class Ctrl10SOLDRD(ctrl_behaviour.CtrlBehaviourAI): # 10SOLDRD 
	@classmethod
	def get_name(cls): "10SoldrD"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Targos Soldier")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
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
		utils_npc.ensure_hp(npc, 6) # MaximumHP: 6
		npc.obj_set_int(toee.obj_f_hp_damage, 16) # CurrentHP: 6, STATE_DEAD

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
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_LEATHER_CLOTHING, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return

class Ctrl10GOB(ctrl_behaviour.CtrlBehaviourAI): # 10GOB 
	@classmethod
	def get_name(cls): "10gob"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GOBLIN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_ENEMY # allegiance: 255
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Goblin")
		
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [8, 13, 11, 10, 11, 8])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 4

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
		# SLOT_WEAPON1: None(Books) from 001D4S
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_HANDAXE, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # None (001D4S) at SLOT_WEAPON1 # TODO CHECK if condition to lower 1d6=>1d4 is needed!!
		weapon.obj_set_int(toee.obj_f_weapon_damage_dice, toee.dice_new("1d4").packed)
		
		# SLOT_QUICK1: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 3, 0) # Charges1: 1, Charges2: 3, Charges3: 0
		
		# SLOT_QUICK2: None(Books) from 00RTGOB1
		# junk, skip and forget
		
		utils_item.item_create_in_inventory2(const_proto_armor_iwd2.PROTO_SHIELD_SMALL_WOODEN_EMPTY, npc, no_loot = True, wear_on = toee.item_wear_shield) # anim: Goblin_w_Axe
		return

class Ctrl10GOBD(ctrl_behaviour.CtrlBehaviourAI): # 10GOBD 
	@classmethod
	def get_name(cls): "10gobd"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GOBLIN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_ENEMY # allegiance: 255
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Goblin")
		
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [8, 13, 11, 10, 11, 8])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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

class Ctrl10GOBAR(ctrl_behaviour.CtrlBehaviourAI): # 10GOBAR 
	@classmethod
	def get_name(cls): "10gobar"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GOBLIN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_ENEMY # allegiance: 255
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Goblin Archer")
		
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [8, 13, 11, 10, 11, 8])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		# from None(001D3P) at SLOT_WEAPON2 by ItemMiscMeleeNatural1d3
		utils_npc.npc_natural_attack(npc, index = 0, attack_type = const_toee.nwt_bite, attack_bonus = 0, number = 1, damage_str = "1d3") # TODO check BAB here
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		npc.obj_set_int(toee.obj_f_critter_experience, 25) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 4

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
		# SLOT_WEAPON1: Shortbow(Bows) from 00CWBOWK
		weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_SHORTBOW, npc, no_loot = True, wear_on = toee.item_wear_weapon_primary) # Shortbow (00CWBOWK) at SLOT_WEAPON1 OK
		weapon.obj_set_int(toee.obj_f_weapon_damage_dice, toee.dice_new("1d6-4").packed)
		
		# SLOT_WEAPON2: None(Books) from 001D3P
		# see natural
		
		# SLOT_AMMO1: Arrows(Arrows) from 00AROW01
		quiver = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc, no_loot = False, wear_on = toee.item_wear_ammo) # Arrows (00AROW01) at SLOT_AMMO1 OK
		quiver.obj_set_int(toee.obj_f_ammo_quantity, 10)
		
		# SLOT_QUICK1: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 3, 0) # Charges1: 1, Charges2: 3, Charges3: 0
		
		# SLOT_QUICK2: None(Books) from 00RTGOB1
		# junk, skip and forget
		
		return

class Ctrl10GOBARD(ctrl_behaviour.CtrlBehaviourAI): # 10GOBARD 
	@classmethod
	def get_name(cls): "10gobArD"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GOBLIN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_ENEMY # allegiance: 255
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Goblin")
		
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [8, 13, 11, 10, 11, 8])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		return

class Ctrl10SAILRD(ctrl_behaviour.CtrlBehaviourAI): # 10SAILRD 
	@classmethod
	def get_name(cls): "10SailrD"
	
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_class_faction(cls): return factions_zmod.FACTION_NEUTRAL_NPC # allegiance: 128
		
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Sailor")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black # HairColourIndex: 0
		hairStyle.update_npc(npc)
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [11, 12, 12, 9, 10, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1

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
		utils_npc.ensure_hp(npc, 6) # MaximumHP: 6
		npc.obj_set_int(toee.obj_f_hp_damage, 16) # CurrentHP: 6, STATE_DEAD

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
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_LEATHER_CLOTHING, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return

