import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### GVARS ####
MODULE_SCRIPT_ID = 10001
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
class Ctrl_10HEDRON_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10HEDRON 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	def setup_scripts(self, npc):
		super(Ctrl_10HEDRON_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Hedron Kerdos")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
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
		npc.obj_set_int(toee.obj_f_critter_experience, 270) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # CR: 5 TODO!!!
		
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
		utils_item.item_create_in_inventory2(const_proto_items_iwd2.PROTO_GENERIC_LYNX_EYE_GEM, npc, no_loot = False, wear_on = None) # Lynx Eye Gem (00GEM02) at SLOT_QUICK2 OK
		
		# SLOT_QUICK3: Bottle of Wine(Drink) from 00MISC08
		# Not found! TODO ITEM
		
		return
	
	def script_dialog(self, attachee, triggerer):
		print("script_dialog 10HEDRON")
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		while True:
			print("STATE 0")
			# NumTimesTalkedTo(0)
			if self.iNumTimesTalkedTo(0):
				line_id = 10 # Well, here ye are, straight from Bremen to the scenic shore of Targos herself.  Now that ye be seeing the skeleton of the town ye'll be defendin', ye sure ye don't want me to take ye back?
				print("STATE 0: line_id = 10")
				break
			
			print("STATE 21")
			# GlobalGT("Reig_Quest", "GLOBAL", 0)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			# Global("Hedron_Know_Attack", "GLOBAL", 0)
			if self.iGlobalGT("'Reig_Quest'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Hedron_Know_Attack'", "'GLOBAL'", 0):
				line_id = 220 # I was hoping ye might come back - what's the word from the docks?  Not even Magdar's come out to shake me down yet, and he usually sends some half-drunk stumblers to help unload my supplies.
				print("STATE 21: line_id = 220")
				break
			
			print("STATE 30")
			# GlobalGT("Reig_Quest", "GLOBAL", 0)
			# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
			if self.iGlobalGT("'Reig_Quest'", "'GLOBAL'", 0) \
				 and self.iGlobalLT("'Hedron_Know_Attack'", "'GLOBAL'", 2):
				line_id = 310 # What's going on along the shore?  I heard something about an attack on the docks, but no one can tell me anything for certain.
				print("STATE 30: line_id = 310")
				break
			
			print("STATE 33")
			# GlobalGT("Hedron_Know_Attack", "GLOBAL", 0)
			# GlobalGT("Hedron_Quest", "GLOBAL", 0)
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			if self.iGlobalGT("'Hedron_Know_Attack'", "'GLOBAL'", 0) \
				 and self.iGlobalGT("'Hedron_Quest'", "'GLOBAL'", 0) \
				 and self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 4):
				line_id = 360 # You're back - any word of me Ma?
				print("STATE 33: line_id = 360")
				break
			
			print("STATE 34")
			# NumTimesTalkedToGT(0)
			# Global("Reig_Quest", "GLOBAL", 0)
			if self.iNumTimesTalkedToGT(0) \
				 and self.iGlobal("'Reig_Quest'", "'GLOBAL'", 0):
				line_id = 370 # Aye, look who's come back aboard - sick of Targos already, are ye?
				print("STATE 34: line_id = 370")
				break
			
			print("STATE 38")
			# Global("Hedron_Know_Attack", "GLOBAL", 2)
			if self.iGlobal("'Hedron_Know_Attack'", "'GLOBAL'", 2):
				line_id = 390 # Aye, look who's come back aboard - the great goblin slayers of Targos.  What can I do for ye?
				print("STATE 38: line_id = 390")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return line_id # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		# 10HEDRON
		
		if index == 0:
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 42: Mostly decent folk?
			
		elif index == 1:
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 4):
				return True # 171: If your mother lives in Targos, why are you staying on the ship?
			
		elif index == 2:
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 401: You named your ship after your *mother?*
			
		elif index == 3:
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 191: You named your ship after your mother?
			
		elif index == 4:
			# GlobalGT("Know_Hedron", "GLOBAL", 0)
			if self.iGlobalGT("'Know_Hedron'", "'GLOBAL'", 0):
				return True # 193: I see.  I must take my leave.  Farewell.
			
		elif index == 5:
			# Global("Know_Hedron", "GLOBAL", 0)
			if self.iGlobal("'Know_Hedron'", "'GLOBAL'", 0):
				return True # 121: All right.  Thanks for your help, Hedron.
			
		elif index == 6:
			# Global("Know_Hedron", "GLOBAL", 1)
			if self.iGlobal("'Know_Hedron'", "'GLOBAL'", 1):
				return True # 122: All right.  Thanks for your help, Hedron.
			
		elif index == 7:
			# Global("Firtha_Dead", "GLOBAL", 1)
			if self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 1):
				return True # 241: I'm afraid she didn't make it, Hedron... she, uh, was killed by goblins in her home.
			
		elif index == 8:
			# GlobalGT("Hedron_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalGT("'Hedron_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 4) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 242: We already checked on her, Hedron.  Some goblins had broken into her house, but we took them out and rescued her.
			
		elif index == 9:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("AR1004_GOBLINS_CLEAR", "GLOBAL", 1)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'AR1004_GOBLINS_CLEAR'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 243: We encountered an old woman being menaced by goblins - I don't know whether it was your mother or not.
			
		elif index == 10:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 244: Your mother?  Which house is hers?
			
		elif index == 11:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 245: We'll see what we can do - but we need someplace safe to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 12:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 246: We'll go check on her, Hedron.  We'll return when she's safe.
			
		elif index == 13:
			# ClassEx(Protagonist, Paladin)
			if self.iClassEx("Protagonist", "Paladin"):
				return True # 261: It is likely the goblin attack merely frightened her.  Any harsh words she spoke probably stemmed from fear, not anger.
			
		elif index == 14:
			# ClassEx(Protagonist, Monk)
			if self.iClassEx("Protagonist", "Monk"):
				return True # 262: It is likely the goblin attack merely frightened her.  Any harsh words she spoke probably stemmed from fear, not anger.
			
		elif index == 15:
			# CheckStatLT(Protagonist, 12, CHR)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iCheckStatLT("Protagonist", 12, "CHR") \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 263: She's certainly got a tongue on her, no doubt.
			
		elif index == 16:
			# CheckStatGT(Protagonist, 11, CHR)
			# CheckStatLT(Protagonist, 16, CHR)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iCheckStatGT("Protagonist", 11, "CHR") \
				 and self.iCheckStatLT("Protagonist", 16, "CHR") \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 264: She's certainly got a tongue on her, no doubt.
			
		elif index == 17:
			# CheckStatGT(Protagonist, 15, CHR)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iCheckStatGT("Protagonist", 15, "CHR") \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 265: She's certainly got a tongue on her, no doubt.
			
		elif index == 18:
			# CheckStatLT(Protagonist, 12, CHR)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iCheckStatLT("Protagonist", 12, "CHR") \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 266: She was somewhat sparse with her gratitude, Hedron.  Perhaps you could remedy that.
			
		elif index == 19:
			# CheckStatGT(Protagonist, 11, CHR)
			# CheckStatLT(Protagonist,16, CHR)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iCheckStatGT("Protagonist", 11, "CHR") \
				 and self.iCheckStatLT("Protagonist", 16, "CHR") \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 267: She was somewhat sparse with her gratitude, Hedron.  Perhaps you could remedy that.
			
		elif index == 20:
			# CheckStatGT(Protagonist, 15, CHR)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iCheckStatGT("Protagonist", 15, "CHR") \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 268: She was somewhat sparse with her gratitude, Hedron.  Perhaps you could remedy that.
			
		elif index == 21:
			# ClassEx(Protagonist, Paladin)
			if self.iClassEx("Protagonist", "Paladin"):
				return True # 281: The tenets of my faith preclude me from accepting this much wealth.  Your gratitude is enough.  Farewell.
			
		elif index == 22:
			# ClassEx(Protagonist, Monk)
			if self.iClassEx("Protagonist", "Monk"):
				return True # 282: The tenets of my order preclude the acceptance of this much wealth.  Your gratitude is enough.  Farewell.
			
		elif index == 23:
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 283: Glad we could help.  Take care, Hedron.
			
		elif index == 24:
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 284: She tested our patience, but this should serve to make up for it.  Farewell, Hedron.
			
		elif index == 25:
			# ClassEx(Protagonist, Paladin)
			if self.iClassEx("Protagonist", "Paladin"):
				return True # 271: The tenets of my faith preclude me from accepting this much wealth.  We were pleased to help you, and let us leave it at that.  Farewell.
			
		elif index == 26:
			# ClassEx(Protagonist, Monk)
			if self.iClassEx("Protagonist", "Monk"):
				return True # 272: The tenets of my order preclude the acceptance of this much wealth.  We were pleased to help you, and let us leave it at that.  Farewell.
			
		elif index == 27:
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 273: Glad we could help.  Take care, Hedron.
			
		elif index == 28:
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 274: She tested our patience, but this should serve to make up for it.  Farewell, Hedron.
			
		elif index == 29:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobalLT("'Hedron_Know_Attack'", "'GLOBAL'", 2) \
				 and self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 4):
				return True # 311: The town was attacked by goblins.  We managed to drive them off and retake the docks.
			
		elif index == 30:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobalLT("'Hedron_Know_Attack'", "'GLOBAL'", 2) \
				 and self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 4):
				return True # 312: There's been an attack on the docks.  If this keeps up, I suspect Targos is going to be the new home of the goblin horde in the near future.
			
		elif index == 31:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
			# GlobalGT("Hedron_Quest", "GLOBAL", 3)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobalLT("'Hedron_Know_Attack'", "'GLOBAL'", 2) \
				 and self.iGlobalGT("'Hedron_Quest'", "'GLOBAL'", 3):
				return True # 313: We've managed to drive off the goblins, though it was a near thing.  Could you put us up for the night, Hedron?
			
		elif index == 32:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
			# GlobalGT("Hedron_Quest", "GLOBAL", 3)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobalLT("'Hedron_Know_Attack'", "'GLOBAL'", 2) \
				 and self.iGlobalGT("'Hedron_Quest'", "'GLOBAL'", 3):
				return True # 314: The goblins have been taken care of... but if you caught word of the goblin attack, how come you haven't left yet?
			
		elif index == 33:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
			# GlobalGT("Hedron_Quest", "GLOBAL", 3)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobalLT("'Hedron_Know_Attack'", "'GLOBAL'", 2) \
				 and self.iGlobalGT("'Hedron_Quest'", "'GLOBAL'", 3):
				return True # 315: The docks are safe, and the attacking goblins are dead.  Just returned to the ship to let you know - we'll speak again later.
			
		elif index == 34:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				return True # 316: There's still goblins about, and we need someplace safe to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 35:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				return True # 317: We're still figuring out the extent of the goblin attack.  We'll return when we know more.  Farewell.
			
		elif index == 36:
			# Global("Firtha_Dead", "GLOBAL", 1)
			if self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 1):
				return True # 331: I'm afraid she didn't make it, Hedron... she, uh, was killed by goblins in her home.
			
		elif index == 37:
			# GlobalGT("Hedron_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalGT("'Hedron_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 4) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 332: We already checked on her, Hedron.  Some goblins had broken into her house, but we took them out and rescued her.
			
		elif index == 38:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("AR1004_GOBLINS_CLEAR", "GLOBAL", 1)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'AR1004_GOBLINS_CLEAR'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 333: We encountered an old woman being menaced by goblins - I don't know whether it was your mother or not.
			
		elif index == 39:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 334: Your mother?  Which house is hers?
			
		elif index == 40:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 335: We'll see what we can do - but we need someplace safe to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 41:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 336: We'll go check on her, Hedron.  We'll return when she's safe.
			
		elif index == 42:
			# Global("Firtha_Dead", "GLOBAL", 1)
			if self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 1):
				return True # 361: I'm afraid she didn't make it, Hedron... she, uh, was killed by goblins in her home.
			
		elif index == 43:
			# GlobalGT("Hedron_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalGT("'Hedron_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 4) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 362: We already checked on her, Hedron.  Some goblins had broken into her house, but we took them out and rescued her.
			
		elif index == 44:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("AR1004_GOBLINS_CLEAR", "GLOBAL", 1)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'AR1004_GOBLINS_CLEAR'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 363: We encountered an old woman being menaced by goblins - I don't know whether it was your mother or not.
			
		elif index == 45:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 364: Which house is hers again?
			
		elif index == 46:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 365: We'll see what we can do - but we need someplace safe to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 47:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Firtha_Dead'", "'GLOBAL'", 0):
				return True # 366: We'll go check on her, Hedron.  We'll return when she's safe.
			
		elif index == 48:
			# Global("Reig_Quest", "GLOBAL", 0)
			if self.iGlobal("'Reig_Quest'", "'GLOBAL'", 0):
				return True # 375: Nothing today, thanks.  Farewell.
			
		elif index == 49:
			# GlobalGT("Reig_Quest", "GLOBAL", 0)
			if self.iGlobalGT("'Reig_Quest'", "'GLOBAL'", 0):
				return True # 376: Nothing today, thanks.  Farewell.
			
		elif index == 50:
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			if self.iGlobalLT("'Hedron_Quest'", "'GLOBAL'", 4):
				return True # 351: If your mother's here why are you still aboard the ship?
			
		return False # dialog_test_do
	
	def dialog_action_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		if index == 0:
			# SetGlobal("Know_Hedron", "GLOBAL", 1)
			self.iSetGlobal("'Know_Hedron'", "'GLOBAL'", 1)
			# 141: We'll be careful.  Farewell, Hedron.
			
		elif index == 1:
			# SetGlobal("Hedron_Know_Attack", "GLOBAL", 1)
			self.iSetGlobal("'Hedron_Know_Attack'", "'GLOBAL'", 1)
			# 221: The town's been attacked by goblins.  You'd best stay on the ship.
			
		elif index == 2:
			# SetGlobal("Hedron_Know_Attack", "GLOBAL", 1)
			self.iSetGlobal("'Hedron_Know_Attack'", "'GLOBAL'", 1)
			# 222: There's been an attack on the docks, and Targos has gained a number of bloodthirsty goblin citizens.
			
		elif index == 3:
			# SetGlobal("Hedron_Quest", "GLOBAL", 5)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 5)
			# 241: I'm afraid she didn't make it, Hedron... she, uh, was killed by goblins in her home.
			
		elif index == 4:
			# AddXpVar("Level_1_Easy",2578)
			self.iAddXpVar("'Level_1_Easy'", 2578)
			# SetGlobal("Hedron_Quest", "GLOBAL", 4)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 4)
			# 242: We already checked on her, Hedron.  Some goblins had broken into her house, but we took them out and rescued her.
			
		elif index == 5:
			# SetGlobal("Hedron_Quest", "GLOBAL", 4)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 4)
			# 243: We encountered an old woman being menaced by goblins - I don't know whether it was your mother or not.
			
		elif index == 6:
			# SetGlobal("Hedron_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 1)
			# 244: Your mother?  Which house is hers?
			
		elif index == 7:
			# SetGlobal("Hedron_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 1)
			# FadeToColor([0.0],0)
			self.iFadeToColor("[0.0]", 0)
			# FadeFromColor([0.0],0)
			self.iFadeFromColor("[0.0]", 0)
			# RestUntilHealed()
			self.iRestUntilHealed()
			# 245: We'll see what we can do - but we need someplace safe to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 8:
			# SetGlobal("Hedron_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 1)
			# 246: We'll go check on her, Hedron.  We'll return when she's safe.
			
		elif index == 9:
			# AddXpVar("Level_1_Easy",2578)
			self.iAddXpVar("'Level_1_Easy'", 2578)
			# 291: That's her.  Some goblin attackers had broken into her home, but we took care of them.  She's safe.
			
		elif index == 10:
			# FadeToColor([0.0],0)
			self.iFadeToColor("[0.0]", 0)
			# FadeFromColor([0.0],0)
			self.iFadeFromColor("[0.0]", 0)
			# RestUntilHealed()
			self.iRestUntilHealed()
			# 301: The town's in danger, but we need someplace safe to rest - can you watch over us while we catch our second wind?
			
		elif index == 11:
			# GiveItemCreate("Misc07", Protagonist, 73, 0, 0)
			utils_pc.pc_party_receive_money_and_print(73 * const_toee.gp)
			# 263: She's certainly got a tongue on her, no doubt.
			
		elif index == 12:
			# GiveItemCreate("Misc07", Protagonist, 123, 0, 0)
			utils_pc.pc_party_receive_money_and_print(123 * const_toee.gp)
			# GiveItem("00Gem02", Protagonist)
			self.iGiveItem(const_proto_items_iwd2.PROTO_GENERIC_LYNX_EYE_GEM, "Protagonist")
			# 264: She's certainly got a tongue on her, no doubt.
			
		elif index == 13:
			# GiveItemCreate("Misc07", Protagonist, 173, 0, 0)
			utils_pc.pc_party_receive_money_and_print(173 * const_toee.gp)
			# GiveItem("00Gem02", Protagonist)
			self.iGiveItem(const_proto_items_iwd2.PROTO_GENERIC_LYNX_EYE_GEM, "Protagonist")
			# 265: She's certainly got a tongue on her, no doubt.
			
		elif index == 14:
			# GiveItemCreate("Misc07", Protagonist, 73, 0, 0)
			utils_pc.pc_party_receive_money_and_print(73 * const_toee.gp)
			# 266: She was somewhat sparse with her gratitude, Hedron.  Perhaps you could remedy that.
			
		elif index == 15:
			# GiveItemCreate("Misc07", Protagonist, 123, 0, 0)
			utils_pc.pc_party_receive_money_and_print(123 * const_toee.gp)
			# GiveItem("00Gem02", Protagonist)
			self.iGiveItem(const_proto_items_iwd2.PROTO_GENERIC_LYNX_EYE_GEM, "Protagonist")
			# 267: She was somewhat sparse with her gratitude, Hedron.  Perhaps you could remedy that.
			
		elif index == 16:
			# GiveItemCreate("Misc07", Protagonist, 173, 0, 0)
			utils_pc.pc_party_receive_money_and_print(173 * const_toee.gp)
			# GiveItem("00Gem02", Protagonist)
			self.iGiveItem(const_proto_items_iwd2.PROTO_GENERIC_LYNX_EYE_GEM, "Protagonist")
			# 268: She was somewhat sparse with her gratitude, Hedron.  Perhaps you could remedy that.
			
		elif index == 17:
			# SetGlobal("Hedron_Know_Attack", "GLOBAL", 2)
			self.iSetGlobal("'Hedron_Know_Attack'", "'GLOBAL'", 2)
			# 311: The town was attacked by goblins.  We managed to drive them off and retake the docks.
			
		elif index == 18:
			# SetGlobal("Hedron_Know_Attack", "GLOBAL", 2)
			self.iSetGlobal("'Hedron_Know_Attack'", "'GLOBAL'", 2)
			# 312: There's been an attack on the docks.  If this keeps up, I suspect Targos is going to be the new home of the goblin horde in the near future.
			
		elif index == 19:
			# SetGlobal("Hedron_Know_Attack", "GLOBAL", 2)
			self.iSetGlobal("'Hedron_Know_Attack'", "'GLOBAL'", 2)
			# FadeToColor([0.0],0)
			self.iFadeToColor("[0.0]", 0)
			# FadeFromColor([0.0],0)
			self.iFadeFromColor("[0.0]", 0)
			# RestUntilHealed()
			self.iRestUntilHealed()
			# 313: We've managed to drive off the goblins, though it was a near thing.  Could you put us up for the night, Hedron?
			
		elif index == 20:
			# SetGlobal("Hedron_Know_Attack", "GLOBAL", 2)
			self.iSetGlobal("'Hedron_Know_Attack'", "'GLOBAL'", 2)
			# 314: The goblins have been taken care of... but if you caught word of the goblin attack, how come you haven't left yet?
			
		elif index == 21:
			# SetGlobal("Hedron_Know_Attack", "GLOBAL", 2)
			self.iSetGlobal("'Hedron_Know_Attack'", "'GLOBAL'", 2)
			# 315: The docks are safe, and the attacking goblins are dead.  Just returned to the ship to let you know - we'll speak again later.
			
		elif index == 22:
			# FadeToColor([0.0],0)
			self.iFadeToColor("[0.0]", 0)
			# FadeFromColor([0.0],0)
			self.iFadeFromColor("[0.0]", 0)
			# RestUntilHealed()
			self.iRestUntilHealed()
			# 316: There's still goblins about, and we need someplace safe to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 23:
			# SetGlobal("Hedron_Quest", "GLOBAL", 5)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 5)
			# 331: I'm afraid she didn't make it, Hedron... she, uh, was killed by goblins in her home.
			
		elif index == 24:
			# AddXpVar("Level_1_Easy",2578)
			self.iAddXpVar("'Level_1_Easy'", 2578)
			# SetGlobal("Hedron_Quest", "GLOBAL", 4)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 4)
			# 332: We already checked on her, Hedron.  Some goblins had broken into her house, but we took them out and rescued her.
			
		elif index == 25:
			# SetGlobal("Hedron_Quest", "GLOBAL", 4)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 4)
			# 333: We encountered an old woman being menaced by goblins - I don't know whether it was your mother or not.
			
		elif index == 26:
			# SetGlobal("Hedron_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 1)
			# 334: Your mother?  Which house is hers?
			
		elif index == 27:
			# SetGlobal("Hedron_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 1)
			# FadeToColor([0.0],0)
			self.iFadeToColor("[0.0]", 0)
			# FadeFromColor([0.0],0)
			self.iFadeFromColor("[0.0]", 0)
			# RestUntilHealed()
			self.iRestUntilHealed()
			# 335: We'll see what we can do - but we need someplace safe to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 28:
			# SetGlobal("Hedron_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 1)
			# 336: We'll go check on her, Hedron.  We'll return when she's safe.
			
		elif index == 29:
			# SetGlobal("Hedron_Quest", "GLOBAL", 5)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 5)
			# 361: I'm afraid she didn't make it, Hedron... she, uh, was killed by goblins in her home.
			
		elif index == 30:
			# AddXpVar("Level_1_Easy",2578)
			self.iAddXpVar("'Level_1_Easy'", 2578)
			# SetGlobal("Hedron_Quest", "GLOBAL", 4)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 4)
			# 362: We already checked on her, Hedron.  Some goblins had broken into her house, but we took them out and rescued her.
			
		elif index == 31:
			# SetGlobal("Hedron_Quest", "GLOBAL", 4)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 4)
			# 363: We encountered an old woman being menaced by goblins - I don't know whether it was your mother or not.
			
		elif index == 32:
			# SetGlobal("Hedron_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 1)
			# 364: Which house is hers again?
			
		elif index == 33:
			# SetGlobal("Hedron_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 1)
			# FadeToColor([0.0],0)
			self.iFadeToColor("[0.0]", 0)
			# FadeFromColor([0.0],0)
			self.iFadeFromColor("[0.0]", 0)
			# RestUntilHealed()
			self.iRestUntilHealed()
			# 365: We'll see what we can do - but we need someplace safe to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 34:
			# SetGlobal("Hedron_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Hedron_Quest'", "'GLOBAL'", 1)
			# 366: We'll go check on her, Hedron.  We'll return when she's safe.
			
		elif index == 35:
			# FadeToColor([0.0],0)
			self.iFadeToColor("[0.0]", 0)
			# FadeFromColor([0.0],0)
			self.iFadeFromColor("[0.0]", 0)
			# RestUntilHealed()
			self.iRestUntilHealed()
			# 373: Could you put us up for the night, Hedron?
			
		elif index == 36:
			# FadeToColor([0.0],0)
			self.iFadeToColor("[0.0]", 0)
			# FadeFromColor([0.0],0)
			self.iFadeFromColor("[0.0]", 0)
			# RestUntilHealed()
			self.iRestUntilHealed()
			# 393: Could you put us up for the night, Hedron?
			
		return # dialog_action_do
		
	def get_dialog_trigger_max_index(self): return 50
	
	def get_state_to_line(self, state):
		if state==0: return 10
		if state==1: return 20
		if state==2: return 210
		if state==3: return 30
		if state==4: return 40
		if state==5: return 160
		if state==6: return 170
		if state==7: return 50
		if state==8: return 150
		if state==9: return 80
		if state==10: return 90
		if state==11: return 100
		if state==12: return 400
		if state==13: return 180
		if state==14: return 190
		if state==15: return 200
		if state==16: return 410
		if state==17: return 110
		if state==18: return 120
		if state==19: return 130
		if state==20: return 140
		if state==21: return 220
		if state==22: return 230
		if state==23: return 240
		if state==24: return 250
		if state==25: return 290
		if state==26: return 300
		if state==27: return 260
		if state==28: return 280
		if state==29: return 270
		if state==30: return 310
		if state==31: return 320
		if state==32: return 330
		if state==33: return 360
		if state==34: return 370
		if state==35: return 340
		if state==36: return 350
		if state==37: return 380
		if state==38: return 390
		if state==39: return 60
		if state==40: return 70
		return
	
class Ctrl_10ELDGUL_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10ELDGUL 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	def setup_scripts(self, npc):
		super(Ctrl_10ELDGUL_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Eldgull")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
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
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
	
	def script_dialog(self, attachee, triggerer):
		print("script_dialog 10ELDGUL")
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		while True:
			print("STATE 0")
			# True()
			if True:
				line_id = 420 # Can't stop t'bandy words with ye; Hedron be findin' *more* work for me after I finish this bit.  Fare thee well.
				print("STATE 0: line_id = 420")
				break
			
			print("STATE 3")
			# GlobalGT("Reig_Quest", "GLOBAL", 0)
			if self.iGlobalGT("'Reig_Quest'", "'GLOBAL'", 0):
				line_id = 450 # Is it true?  I hear th'town's bein' attacked by the goblins!
				print("STATE 3: line_id = 450")
				break
			
			print("STATE 5")
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1):
				line_id = 470 # Caught word 'bout the battle - looks like ye pulled through - good for ye.
				print("STATE 5: line_id = 470")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return line_id # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		# 10ELDGUL
		
		return False # dialog_test_do
	
	def dialog_action_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		return # dialog_action_do
		
	def get_dialog_trigger_max_index(self): return 0
	
	def get_state_to_line(self, state):
		if state==0: return 420
		if state==1: return 430
		if state==2: return 440
		if state==3: return 450
		if state==4: return 460
		if state==5: return 470
		return
	
class Ctrl_10SCREED_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10SCREED 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	def setup_scripts(self, npc):
		super(Ctrl_10SCREED_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Screed")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
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
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
	
	def script_dialog(self, attachee, triggerer):
		print("script_dialog 10SCREED")
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		while True:
			print("STATE 0")
			# True()
			if True:
				line_id = 480 # Was good havin' ye with us, even for only a short time.  Hope fortune's wind fills yer sails, friend.
				print("STATE 0: line_id = 480")
				break
			
			print("STATE 3")
			# GlobalGT("Reig_Quest", "GLOBAL", 0)
			if self.iGlobalGT("'Reig_Quest'", "'GLOBAL'", 0):
				line_id = 510 # I hear the town's being attacked again - the Wicked Wench's all ready to set sail if ye need to fall back.
				print("STATE 3: line_id = 510")
				break
			
			print("STATE 4")
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1):
				line_id = 520 # Heard th' fightin' up along the docks was fierce - drove those goblins back, did ye?
				print("STATE 4: line_id = 520")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return line_id # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		# 10SCREED
		
		return False # dialog_test_do
	
	def dialog_action_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		return # dialog_action_do
		
	def get_dialog_trigger_max_index(self): return 0
	
	def get_state_to_line(self, state):
		if state==0: return 480
		if state==1: return 490
		if state==2: return 500
		if state==3: return 510
		if state==4: return 520
		return
	
class Ctrl_10REIG_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10REIG 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	def setup_scripts(self, npc):
		super(Ctrl_10REIG_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Reig Redwaters")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
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
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
	
	def script_dialog(self, attachee, triggerer):
		print("script_dialog 10REIG")
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		while True:
			print("STATE 0")
			# NumTimesTalkedTo(0)
			if self.iNumTimesTalkedTo(0):
				line_id = 530 # Halt!  Who goes there?  Step forward and identify yourself!
				print("STATE 0: line_id = 530")
				break
			
			print("STATE 15")
			# Global("Reig_Quest", "GLOBAL", 1)
			if self.iGlobal("'Reig_Quest'", "'GLOBAL'", 1):
				line_id = 600 # Did you find Magdar?  My damned arm's getting worse, and I need that potion he's got.
				print("STATE 15: line_id = 600")
				break
			
			print("STATE 16")
			# HPGT(Myself, 3)
			# Global("Reig_Quest", "GLOBAL", 1)
			# Global("Reig_Heal_Priest", "GLOBAL", 0)
			if self.iHPGT("Myself", 3) \
				 and self.iGlobal("'Reig_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Reig_Heal_Priest'", "'GLOBAL'", 0):
				line_id = 670 # My arm's better, thanks for your help.  Looks like you're praying to the right gods.
				print("STATE 16: line_id = 670")
				break
			
			print("STATE 17")
			# Global("Reig_Quest", "GLOBAL", 1)
			# Global("Reig_Heal_Priest", "GLOBAL", 1)
			if self.iGlobal("'Reig_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Reig_Heal_Priest'", "'GLOBAL'", 1):
				line_id = 680 # None
				print("STATE 17: line_id = 680")
				break
			
			print("STATE 19")
			# Global("Reig_Quest", "GLOBAL", 2)
			if self.iGlobal("'Reig_Quest'", "'GLOBAL'", 2):
				line_id = 640 # None
				print("STATE 19: line_id = 640")
				break
			
			print("STATE 21")
			# Global("Told_Reig", "GLOBAL", 1)
			if self.iGlobal("'Told_Reig'", "'GLOBAL'", 1):
				line_id = 690 # Now that the raiders have been taken care of, we should be all right.  You should report to Lord Ulbrec up in the main town - he'll be glad to know we have reinforcements.
				print("STATE 21: line_id = 690")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return line_id # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		# 10REIG
		
		if index == 0:
			# !SubRace(Protagonist, ELF_DROW)
			if not self.iSubRace("Protagonist", "ELF_DROW"):
				return True # 531: I'm @pcname@ .  What happened here?
			
		elif index == 1:
			# !SubRace(Protagonist, ELF_DROW)
			if not self.iSubRace("Protagonist", "ELF_DROW"):
				return True # 532: Calm down - what's wrong with your arm?
			
		elif index == 2:
			# SubRace(Protagonist, ELF_DROW)
			if self.iSubRace("Protagonist", "ELF_DROW"):
				return True # 533: I'm @pcname@ .  What happened here?
			
		elif index == 3:
			# SubRace(Protagonist, ELF_DROW)
			if self.iSubRace("Protagonist", "ELF_DROW"):
				return True # 534: Calm down - what's wrong with your arm?
			
		elif index == 4:
			# CheckSkillGT(Protagonist, 0, Diplomacy)
			if self.iCheckSkillGT("Protagonist", 0, "Diplomacy"):
				return True # 711: Thanks for the blade - but we could also use some armor if we're going to be hunting goblins.
			
		elif index == 5:
			# CheckSkillLT(Protagonist, 1, Diplomacy)
			# CheckStatGT(Protagonist, 11, INT)
			if self.iCheckSkillLT("Protagonist", 1, "Diplomacy") \
				 and self.iCheckStatGT("Protagonist", 11, "INT"):
				return True # 712: Thanks for the blade - but we could also use some armor if we're going to be hunting goblins.
			
		elif index == 6:
			# Global("Know_Goblin_Reig", "GLOBAL", 0)
			if self.iGlobal("'Know_Goblin_Reig'", "'GLOBAL'", 0):
				return True # 713: Very well.  How did the goblins get into town?
			
		elif index == 7:
			# Global("Know_Arm", "GLOBAL", 0)
			if self.iGlobal("'Know_Arm'", "'GLOBAL'", 0):
				return True # 714: What's wrong with your arm?
			
		elif index == 8:
			# Global("Know_Arm", "GLOBAL", 1)
			if self.iGlobal("'Know_Arm'", "'GLOBAL'", 1):
				return True # 715: Your arm looks in pretty bad shape - your bandages are almost soaked through.
			
		elif index == 9:
			# Kit(Protagonist, CLERIC_ILMATER)
			if self.iKit("Protagonist", "CLERIC_ILMATER"):
				return True # 781: I'm an Ilmatari, a Painbearer of Ilmater.  My healing magic may be able to draw the pain from your wound and end your suffering.
			
		elif index == 10:
			# Kit(Protagonist, CLERIC_LATHANDER)
			if self.iKit("Protagonist", "CLERIC_LATHANDER"):
				return True # 782: Come the dawn, all things may be healed, Lathander teaches us.  I can aid you with my healing magic, if you wish. 
			
		elif index == 11:
			# Kit(Protagonist, CLERIC_SELUNE)
			if self.iKit("Protagonist", "CLERIC_SELUNE"):
				return True # 783: Let Selune's light fall upon you, guardsman, and her healing magic shall seal your wound.
			
		elif index == 12:
			# Kit(Protagonist, CLERIC_HELM)
			if self.iKit("Protagonist", "CLERIC_HELM"):
				return True # 784: Wounds are the price of a strong defense, guardsman, so the teachings of Helm tell us.  Let a Watcher's healing magic aid you. 
			
		elif index == 13:
			# Kit(Protagonist, CLERIC_OGHMA)
			if self.iKit("Protagonist", "CLERIC_OGHMA"):
				return True # 785: Much blood is shed in the pursuit of knowledge, Oghma teaches us.  As a Lorekeeper, I may call upon his healing magic to aid you, if you wish. 
			
		elif index == 14:
			# Kit(Protagonist, CLERIC_TEMPUS)
			if self.iKit("Protagonist", "CLERIC_TEMPUS"):
				return True # 786: Wounds are the price of battle - and an inspiration to others.  Let a Battleguard call upon Tempus' magics to seal your wound. 
			
		elif index == 15:
			# Kit(Protagonist, CLERIC_BANE)
			if self.iKit("Protagonist", "CLERIC_BANE"):
				return True # 787: Dreadmasters know much of the ways of pain.  Perhaps I could return strength to your arm... if it is Bane's will that you live.  
			
		elif index == 16:
			# Kit(Protagonist, CLERIC_MASK)
			if self.iKit("Protagonist", "CLERIC_MASK"):
				return True # 788: Ah, a supply of healing draughts may be found close by, you say?  Hmm... first, let a Demarch of Mask attend to your wound. 
			
		elif index == 17:
			# Kit(Protagonist, CLERIC_TALOS)
			if self.iKit("Protagonist", "CLERIC_TALOS"):
				return True # 789: A rain of blood follows the storms, so teaches Talos.  We Stormlords know much of pain... and how to end it.   
			
		elif index == 18:
			# ClassEx(Protagonist, Druid)
			if self.iClassEx("Protagonist", "Druid"):
				return True # 790: I'm a druid.  I may be able to call upon nature's power to heal your arm.
			
		elif index == 19:
			# ClassEx(Protagonist, Paladin)
			if self.iClassEx("Protagonist", "Paladin"):
				return True # 791: I'm a paladin.  I may be able to use my healing magics to help your arm.
			
		elif index == 20:
			# PartyHasItem("00Potn04")
			if self.iPartyHasItem(const_proto_potions.PROTO_POTION_OF_CURE_LIGHT_WOUNDS):
				return True # 792: I already found a healing potion.  It should help - drink it down.
			
		elif index == 21:
			# !Alignment(Protagonist, 3)
			if not self.iAlignment("Protagonist", 3):
				return True # 621: Let me see what I can do.
			
		elif index == 22:
			# Alignment(Protagonist, 3)
			if self.iAlignment("Protagonist", 3):
				return True # 622: I wouldn't call myself a healer...  but let me see what I can do.
			
		elif index == 23:
			# Kit(Protagonist, CLERIC_ILMATER)
			if self.iKit("Protagonist", "CLERIC_ILMATER"):
				return True # 601: I'm an Ilmatari, a Painbearer of Ilmater.  My healing magic may be able to draw the pain from your wound and end your suffering.
			
		elif index == 24:
			# Kit(Protagonist, CLERIC_LATHANDER)
			if self.iKit("Protagonist", "CLERIC_LATHANDER"):
				return True # 602: Come the dawn, all things may be healed, Lathander teaches us.  I can aid you with my healing magic, if you wish. 
			
		elif index == 25:
			# Kit(Protagonist, CLERIC_SELUNE)
			if self.iKit("Protagonist", "CLERIC_SELUNE"):
				return True # 603: Let Selune's light fall upon you, guardsman, and her healing magic shall seal your wound.
			
		elif index == 26:
			# Kit(Protagonist, CLERIC_HELM)
			if self.iKit("Protagonist", "CLERIC_HELM"):
				return True # 604: Wounds are the price of a strong defense, guardsman, so the teachings of Helm tell us.  Let a Watcher's healing magic aid you. 
			
		elif index == 27:
			# Kit(Protagonist, CLERIC_OGHMA)
			if self.iKit("Protagonist", "CLERIC_OGHMA"):
				return True # 605: Much blood is shed in the pursuit of knowledge, Oghma teaches us.  As a Lorekeeper, I may call upon his healing magic to aid you, if you wish. 
			
		elif index == 28:
			# Kit(Protagonist, CLERIC_TEMPUS)
			if self.iKit("Protagonist", "CLERIC_TEMPUS"):
				return True # 606: Wounds are the price of battle - and an inspiration to others.  Let a Battleguard call upon Tempus' magics to seal your wound. 
			
		elif index == 29:
			# Kit(Protagonist, CLERIC_BANE)
			if self.iKit("Protagonist", "CLERIC_BANE"):
				return True # 607: Dreadmasters know much of the ways of pain.  Perhaps I could return strength to your arm... if it is Bane's will that you live.  
			
		elif index == 30:
			# Kit(Protagonist, CLERIC_MASK)
			if self.iKit("Protagonist", "CLERIC_MASK"):
				return True # 608: Ah, a supply of healing draughts may be found close by, you say?  Hmm... first, let a Demarch of Mask attend to your wound. 
			
		elif index == 31:
			# Kit(Protagonist, CLERIC_TALOS)
			if self.iKit("Protagonist", "CLERIC_TALOS"):
				return True # 609: A rain of blood follows the storms, so teaches Talos.  We Stormlords know much of pain... and how to end it.   
			
		elif index == 32:
			# ClassEx(Protagonist, Druid)
			if self.iClassEx("Protagonist", "Druid"):
				return True # 610: I'm a druid.  I may be able to call upon nature's power to heal you.
			
		elif index == 33:
			# ClassEx(Protagonist, Paladin)
			if self.iClassEx("Protagonist", "Paladin"):
				return True # 611: I'm a paladin.  I may be able to use my healing magics to help your arm.
			
		elif index == 34:
			# PartyHasItem("00Potn04")
			if self.iPartyHasItem(const_proto_potions.PROTO_POTION_OF_CURE_LIGHT_WOUNDS):
				return True # 612: Here's the healing potion.  It should help - drink it down.
			
		elif index == 35:
			# Global("Reig_Heal_Priest", "GLOBAL", 0)
			if self.iGlobal("'Reig_Heal_Priest'", "'GLOBAL'", 0):
				return True # 671: The wound's closed, but there may be more damage.  You still don't look too good.
			
		elif index == 36:
			# Global("Reig_Heal_Priest", "GLOBAL", 1)
			if self.iGlobal("'Reig_Heal_Priest'", "'GLOBAL'", 1):
				return True # 672: The wound's closed, but there may be more damage.  You still don't look too good.
			
		elif index == 37:
			# PartyHasItem("00Potn04")
			if self.iPartyHasItem(const_proto_potions.PROTO_POTION_OF_CURE_LIGHT_WOUNDS):
				return True # 681: Here's the healing potion.  It should help - drink it down.
			
		elif index == 38:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				return True # 641: We need to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 39:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				return True # 642: I'll see what I can do.
			
		elif index == 40:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1):
				return True # 643: We've wiped out the last of the goblins along the docks.
			
		elif index == 41:
			# CheckSkillGT(Protagonist, 2, Intimidate)
			# !Alignment(Protagonist,1)
			if self.iCheckSkillGT("Protagonist", 2, "Intimidate") \
				 and not self.iAlignment("Protagonist", 1):
				return True # 721: Also, your dead friend here, Brohn, shouldn't be needing his equipment any longer, so pass that along as well.
			
		elif index == 42:
			# CheckSkillLT(Protagonist, 3, Intimidate)
			# CheckStatGT(Protagonist, 14, INT)
			# !Alignment(Protagonist,1)
			if self.iCheckSkillLT("Protagonist", 3, "Intimidate") \
				 and self.iCheckStatGT("Protagonist", 14, "INT") \
				 and not self.iAlignment("Protagonist", 1):
				return True # 722: Also, your dead friend here, Brohn, shouldn't be needing his equipment any longer, so pass that along as well.
			
		elif index == 43:
			# CheckSkillGT(Protagonist, 2, Diplomacy)
			# !Alignment(Protagonist,3)
			if self.iCheckSkillGT("Protagonist", 2, "Diplomacy") \
				 and not self.iAlignment("Protagonist", 3):
				return True # 723: I mean no disrespect to your fellow soldier, but we could also use any of the equipment your fallen comrade Brohn had, if any.
			
		elif index == 44:
			# CheckSkillLT(Protagonist, 3, Diplomacy)
			# CheckStatGT(Protagonist, 14, INT)
			# !Alignment(Protagonist,3)
			if self.iCheckSkillLT("Protagonist", 3, "Diplomacy") \
				 and self.iCheckStatGT("Protagonist", 14, "INT") \
				 and not self.iAlignment("Protagonist", 3):
				return True # 724: I mean no disrespect to your fallen friend, but we could also use any of the equipment your fallen comrade Brohn had, if any.
			
		return False # dialog_test_do
	
	def dialog_action_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		if index == 0:
			# SetGlobal("Reig_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Reig_Quest'", "'GLOBAL'", 1)
			# 531: I'm @pcname@ .  What happened here?
			
		elif index == 1:
			# SetGlobal("Reig_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Reig_Quest'", "'GLOBAL'", 1)
			# 532: Calm down - what's wrong with your arm?
			
		elif index == 2:
			# SetGlobal("Reig_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Reig_Quest'", "'GLOBAL'", 1)
			# 533: I'm @pcname@ .  What happened here?
			
		elif index == 3:
			# SetGlobal("Reig_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Reig_Quest'", "'GLOBAL'", 1)
			# 534: Calm down - what's wrong with your arm?
			
		elif index == 4:
			# SetGlobal("Know_Arm", "GLOBAL", 1)
			self.iSetGlobal("'Know_Arm'", "'GLOBAL'", 1)
			# 591: We've come from Luskan to aid Targos.  Perhaps we can help you stop these raiders.
			
		elif index == 5:
			# SetGlobal("Know_Arm", "GLOBAL", 1)
			self.iSetGlobal("'Know_Arm'", "'GLOBAL'", 1)
			# 592: Goblins?  How did they get into town?
			
		elif index == 6:
			# SetGlobal("Know_Arm", "GLOBAL", 1)
			self.iSetGlobal("'Know_Arm'", "'GLOBAL'", 1)
			# 581: We've come from Luskan to aid Targos.  Perhaps we can help you stop these raiders.
			
		elif index == 7:
			# SetGlobal("Know_Arm", "GLOBAL", 1)
			self.iSetGlobal("'Know_Arm'", "'GLOBAL'", 1)
			# 582: Goblins?  How did they get into town?
			
		elif index == 8:
			# SetCriticalPathObject("Reig",FALSE)
			self.iSetCriticalPathObject("'Reig'", False)
			# 551: Continue
			
		elif index == 9:
			# GiveItemCreate("00Swds01", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_weapon.PROTO_WEAPON_SHORTSWORD, "Protagonist", 0, 0, 0)
			# 701: Continue
			
		elif index == 10:
			# GiveItem("00Leat01", Protagonist)
			self.iGiveItem(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, "Protagonist")
			# 711: Thanks for the blade - but we could also use some armor if we're going to be hunting goblins.
			
		elif index == 11:
			# GiveItem("00Leat01", Protagonist)
			self.iGiveItem(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, "Protagonist")
			# 712: Thanks for the blade - but we could also use some armor if we're going to be hunting goblins.
			
		elif index == 12:
			# SetGlobal("Know_Goblin_Reig", "GLOBAL", 1)
			self.iSetGlobal("'Know_Goblin_Reig'", "'GLOBAL'", 1)
			# 571: We've come from Luskan to aid Targos.  Perhaps we can help you stop these raiders.
			
		elif index == 13:
			# AddXpVar("Level_1_Average",1484)
			self.iAddXpVar("'Level_1_Average'", 1484)
			# TakePartyItemNum("00Potn04", 1)
			self.iTakePartyItemNum(const_proto_potions.PROTO_POTION_OF_CURE_LIGHT_WOUNDS, 1)
			# DestroyItem("00Potn04")
			self.iDestroyItem(const_proto_potions.PROTO_POTION_OF_CURE_LIGHT_WOUNDS)
			# SetGlobal("Reig_Quest", "GLOBAL", 2)
			self.iSetGlobal("'Reig_Quest'", "'GLOBAL'", 2)
			# 792: I already found a healing potion.  It should help - drink it down.
			
		elif index == 14:
			# AddXpVar("Level_1_Average",1484)
			self.iAddXpVar("'Level_1_Average'", 1484)
			# TakePartyItemNum("00Potn04", 1)
			self.iTakePartyItemNum(const_proto_potions.PROTO_POTION_OF_CURE_LIGHT_WOUNDS, 1)
			# DestroyItem("00Potn04")
			self.iDestroyItem(const_proto_potions.PROTO_POTION_OF_CURE_LIGHT_WOUNDS)
			# SetGlobal("Reig_Quest", "GLOBAL", 2)
			self.iSetGlobal("'Reig_Quest'", "'GLOBAL'", 2)
			# 612: Here's the healing potion.  It should help - drink it down.
			
		elif index == 15:
			# AddXpVar("Level_1_Easy",1483)
			self.iAddXpVar("'Level_1_Easy'", 1483)
			# SetGlobal("Reig_Heal_Priest", "GLOBAL", 1)
			self.iSetGlobal("'Reig_Heal_Priest'", "'GLOBAL'", 1)
			# 671: The wound's closed, but there may be more damage.  You still don't look too good.
			
		elif index == 16:
			# AddXpVar("Level_1_Easy",1483)
			self.iAddXpVar("'Level_1_Easy'", 1483)
			# 672: The wound's closed, but there may be more damage.  You still don't look too good.
			
		elif index == 17:
			# AddXpVar("Level_1_Average",1484)
			self.iAddXpVar("'Level_1_Average'", 1484)
			# TakePartyItemNum("00Potn04", 1)
			self.iTakePartyItemNum(const_proto_potions.PROTO_POTION_OF_CURE_LIGHT_WOUNDS, 1)
			# DestroyItem("00Potn04")
			self.iDestroyItem(const_proto_potions.PROTO_POTION_OF_CURE_LIGHT_WOUNDS)
			# SetGlobal("Reig_Quest", "GLOBAL", 2)
			self.iSetGlobal("'Reig_Quest'", "'GLOBAL'", 2)
			# 681: Here's the healing potion.  It should help - drink it down.
			
		elif index == 18:
			# SetGlobal("Told_Reig", "GLOBAL", 1)
			self.iSetGlobal("'Told_Reig'", "'GLOBAL'", 1)
			# 643: We've wiped out the last of the goblins along the docks.
			
		elif index == 19:
			# GiveItemCreate("00Leat01", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, "Protagonist", 0, 0, 0)
			# GiveItemCreate("00Helm01", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_cloth.PROTO_CLOTH_HELM_DRUIDIC, "Protagonist", 0, 0, 0)
			# GiveItemCreate("00Dagg01", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_weapon.PROTO_WEAPON_DAGGER, "Protagonist", 0, 0, 0)
			# GiveItemCreate("00ax1h11", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_weapon.PROTO_WEAPON_HANDAXE, "Protagonist", 0, 0, 0)
			# 723: I mean no disrespect to your fellow soldier, but we could also use any of the equipment your fallen comrade Brohn had, if any.
			
		elif index == 20:
			# GiveItemCreate("00Leat01", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, "Protagonist", 0, 0, 0)
			# GiveItemCreate("00Helm01", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_cloth.PROTO_CLOTH_HELM_DRUIDIC, "Protagonist", 0, 0, 0)
			# GiveItemCreate("00Dagg01", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_weapon.PROTO_WEAPON_DAGGER, "Protagonist", 0, 0, 0)
			# GiveItemCreate("00ax1h11", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_weapon.PROTO_WEAPON_HANDAXE, "Protagonist", 0, 0, 0)
			# 724: I mean no disrespect to your fallen friend, but we could also use any of the equipment your fallen comrade Brohn had, if any.
			
		elif index == 21:
			# GiveItemCreate("00Leat01", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, "Protagonist", 0, 0, 0)
			# GiveItemCreate("00Helm01", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_cloth.PROTO_CLOTH_HELM_DRUIDIC, "Protagonist", 0, 0, 0)
			# GiveItemCreate("00Dagg01", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_weapon.PROTO_WEAPON_DAGGER, "Protagonist", 0, 0, 0)
			# GiveItemCreate("00ax1h11", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_weapon.PROTO_WEAPON_HANDAXE, "Protagonist", 0, 0, 0)
			# 731: Without arms and armor, both our corpses will lie next to his soon enough.  Brohn's equipment may give us the... edge... we need to drive the goblins back, so make your choice.
			
		return # dialog_action_do
		
	def get_dialog_trigger_max_index(self): return 44
	
	def get_state_to_line(self, state):
		if state==0: return 530
		if state==1: return 540
		if state==2: return 590
		if state==3: return 580
		if state==4: return 550
		if state==5: return 700
		if state==6: return 710
		if state==7: return 750
		if state==8: return 760
		if state==9: return 560
		if state==10: return 570
		if state==11: return 770
		if state==12: return 780
		if state==13: return 800
		if state==14: return 620
		if state==15: return 600
		if state==16: return 670
		if state==17: return 680
		if state==18: return 630
		if state==19: return 640
		if state==20: return 660
		if state==21: return 690
		if state==22: return 720
		if state==23: return 730
		if state==24: return 740
		if state==25: return 810
		if state==26: return 820
		if state==27: return 650
		return
	
class Ctrl_10JON_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10JON 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	def setup_scripts(self, npc):
		super(Ctrl_10JON_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Honest Jon")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
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
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
	
	def script_dialog(self, attachee, triggerer):
		print("script_dialog 10JON")
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		while True:
			print("STATE 0")
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				line_id = 830 # No idea where those goblins came from - one moment we're stepping out of the Salty Dog, and suddenly there's a mess of them running through town.  We sounded the alarm, but...
				print("STATE 0: line_id = 830")
				break
			
			print("STATE 8")
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1):
				line_id = 890 # Tymora must have been smiling on us when you sailed into town.  Without you to drive back the goblins, the docks might have been burning now, and Targos overrun.
				print("STATE 8: line_id = 890")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return line_id # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		# 10JON
		
		if index == 0:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			# CheckSkillGT(Protagonist, 0, Diplomacy)
			# Global("Jon_Has_No_Pants", "GLOBAL", 0)
			# HasItem("00Dagg01", "Jon")
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0) \
				 and self.iCheckSkillGT("Protagonist", 0, "Diplomacy") \
				 and self.iGlobal("'Jon_Has_No_Pants'", "'GLOBAL'", 0) \
				 and self.iHasItem(const_proto_weapon.PROTO_WEAPON_DAGGER, "'Jon'"):
				return True # 841: We'll see what we can do.  In the meantime, do you have an extra blade you can spare?
			
		elif index == 1:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			# CheckStatGT(Protagonist, 12, INT)
			# CheckSkillLT(Protagonist, 1, Diplomacy)
			# Global("Jon_Has_No_Pants", "GLOBAL", 0)
			# HasItem("00Dagg01", "Jon")
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0) \
				 and self.iCheckStatGT("Protagonist", 12, "INT") \
				 and self.iCheckSkillLT("Protagonist", 1, "Diplomacy") \
				 and self.iGlobal("'Jon_Has_No_Pants'", "'GLOBAL'", 0) \
				 and self.iHasItem(const_proto_weapon.PROTO_WEAPON_DAGGER, "'Jon'"):
				return True # 842: We'll see what we can do.  In the meantime, do you have an extra blade you can spare?
			
		elif index == 2:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			# CheckSkillGT(Protagonist, 0, Diplomacy)
			# Global("Jon_Has_No_Pants", "GLOBAL", 0)
			# !HasItem("00Dagg01", "Jon")
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0) \
				 and self.iCheckSkillGT("Protagonist", 0, "Diplomacy") \
				 and self.iGlobal("'Jon_Has_No_Pants'", "'GLOBAL'", 0) \
				 and not self.iHasItem(const_proto_weapon.PROTO_WEAPON_DAGGER, "'Jon'"):
				return True # 843: We'll see what we can do.  In the meantime, do you have an extra blade you can spare?
			
		elif index == 3:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			# CheckStatGT(Protagonist, 12, INT)
			# CheckSkillLT(Protagonist, 1, Diplomacy)
			# Global("Jon_Has_No_Pants", "GLOBAL", 0)
			# !HasItem("00Dagg01", "Jon")
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0) \
				 and self.iCheckStatGT("Protagonist", 12, "INT") \
				 and self.iCheckSkillLT("Protagonist", 1, "Diplomacy") \
				 and self.iGlobal("'Jon_Has_No_Pants'", "'GLOBAL'", 0) \
				 and not self.iHasItem(const_proto_weapon.PROTO_WEAPON_DAGGER, "'Jon'"):
				return True # 844: We'll see what we can do.  In the meantime, do you have an extra blade you can spare?
			
		return False # dialog_test_do
	
	def dialog_action_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		if index == 0:
			# GiveItem("00Dagg01", Protagonist)
			self.iGiveItem(const_proto_weapon.PROTO_WEAPON_DAGGER, "Protagonist")
			# SetGlobal("Jon_Has_No_Pants", "GLOBAL", 1)
			self.iSetGlobal("'Jon_Has_No_Pants'", "'GLOBAL'", 1)
			# 841: We'll see what we can do.  In the meantime, do you have an extra blade you can spare?
			
		elif index == 1:
			# GiveItem("00Dagg01", Protagonist)
			self.iGiveItem(const_proto_weapon.PROTO_WEAPON_DAGGER, "Protagonist")
			# SetGlobal("Jon_Has_No_Pants", "GLOBAL", 1)
			self.iSetGlobal("'Jon_Has_No_Pants'", "'GLOBAL'", 1)
			# 842: We'll see what we can do.  In the meantime, do you have an extra blade you can spare?
			
		elif index == 2:
			# SetGlobal("Jon_Has_No_Pants", "GLOBAL", 1)
			self.iSetGlobal("'Jon_Has_No_Pants'", "'GLOBAL'", 1)
			# 843: We'll see what we can do.  In the meantime, do you have an extra blade you can spare?
			
		elif index == 3:
			# SetGlobal("Jon_Has_No_Pants", "GLOBAL", 1)
			self.iSetGlobal("'Jon_Has_No_Pants'", "'GLOBAL'", 1)
			# 844: We'll see what we can do.  In the meantime, do you have an extra blade you can spare?
			
		return # dialog_action_do
		
	def get_dialog_trigger_max_index(self): return 3
	
	def get_state_to_line(self, state):
		if state==0: return 830
		if state==1: return 840
		if state==2: return 920
		if state==3: return 850
		if state==4: return 880
		if state==5: return 930
		if state==6: return 860
		if state==7: return 870
		if state==8: return 890
		if state==9: return 900
		if state==10: return 910
		return
	
class Ctrl_10BROGAN_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10BROGAN 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	def setup_scripts(self, npc):
		super(Ctrl_10BROGAN_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Brogan")
		
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
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
	
	def script_dialog(self, attachee, triggerer):
		print("script_dialog 10BROGAN")
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		while True:
			print("STATE 0")
			# True()
			if True:
				line_id = 940 # Halt!  Identify yourself!
				print("STATE 0: line_id = 940")
				break
			
			print("STATE 6")
			# GlobalGT("Iron_Collar_Quest", "GLOBAL", 0)
			# GlobalLT("Iron_Collar_Quest", "GLOBAL", 3)
			# Global("Brogan_Quest", "GLOBAL", 0)
			# Global("AR1002_Visited", "GLOBAL", 0)
			if self.iGlobalGT("'Iron_Collar_Quest'", "'GLOBAL'", 0) \
				 and self.iGlobalLT("'Iron_Collar_Quest'", "'GLOBAL'", 3) \
				 and self.iGlobal("'Brogan_Quest'", "'GLOBAL'", 0) \
				 and self.iGlobal("'AR1002_Visited'", "'GLOBAL'", 0):
				line_id = 1050 # You're back!  Did you bring the Iron Collar Band with you?
				print("STATE 6: line_id = 1050")
				break
			
			print("STATE 10")
			# Global("Brogan_Quest", "GLOBAL", 1)
			if self.iGlobal("'Brogan_Quest'", "'GLOBAL'", 1):
				line_id = 1060 # Did you take out those goblins yet?  Time's running short.
				print("STATE 10: line_id = 1060")
				break
			
			print("STATE 13")
			# Global("Brogan_Quest", "GLOBAL", 1)
			# Global("AR1002_Visited", "GLOBAL", 1)
			# Global("AR1007_Visited", "GLOBAL", 1)
			if self.iGlobal("'Brogan_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobal("'AR1002_Visited'", "'GLOBAL'", 1) \
				 and self.iGlobal("'AR1007_Visited'", "'GLOBAL'", 1):
				line_id = 1090 # Where in Tempus' name have you *been?*  I heard the fighting, and then everything went silent.  Thought you were dead.
				print("STATE 13: line_id = 1090")
				break
			
			print("STATE 18")
			# Global("AR1002_Visited", "GLOBAL", 1)
			# Global("Know_Brogan", "GLOBAL", 0)
			if self.iGlobal("'AR1002_Visited'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Know_Brogan'", "'GLOBAL'", 0):
				line_id = 1150 # Are you mad?  That was a foolish thing for you to do - breaking into that warehouse!  You could have been killed!
				print("STATE 18: line_id = 1150")
				break
			
			print("STATE 19")
			# Global("Brogan_Leave", "GLOBAL", 1)
			if self.iGlobal("'Brogan_Leave'", "'GLOBAL'", 1):
				line_id = 1160 # I respect your courage.  If you tell of your deeds to Lord Ulbrec, he is sure to reward you.
				print("STATE 19: line_id = 1160")
				break
			
			print("STATE 20")
			# GlobalGT("Iron_Collar_Quest", "GLOBAL", 0)
			# GlobalLT("Iron_Collar_Quest", "GLOBAL", 3)
			# Global("Brogan_Quest", "GLOBAL", 0)
			# Global("AR1002_Visited", "GLOBAL", 1)
			if self.iGlobalGT("'Iron_Collar_Quest'", "'GLOBAL'", 0) \
				 and self.iGlobalLT("'Iron_Collar_Quest'", "'GLOBAL'", 3) \
				 and self.iGlobal("'Brogan_Quest'", "'GLOBAL'", 0) \
				 and self.iGlobal("'AR1002_Visited'", "'GLOBAL'", 1):
				line_id = 1170 # Are you mad?  That was a foolish thing for you to do - breaking into that warehouse!  You could have been killed!
				print("STATE 20: line_id = 1170")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return line_id # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		# 10BROGAN
		
		if index == 0:
			# Global("Know_Iron_Collar", "GLOBAL", 0)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1):
				return True # 961: Uh, the sell-swords from the Salty Dog?
			
		elif index == 1:
			# Global("Know_Iron_Collar", "GLOBAL", 0)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 962: The sell-swords from the Salty Dog?
			
		elif index == 2:
			# Global("Know_Iron_Collar", "GLOBAL", 1)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1):
				return True # 963: Uh, the sell-swords from the Salty Dog?  You mean the Iron Collar mercenaries?
			
		elif index == 3:
			# Global("Know_Iron_Collar", "GLOBAL", 1)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 964: The sell-swords from the Salty Dog?  You mean the Iron Collar mercenaries?
			
		elif index == 4:
			# Global("Know_Iron_Collar", "GLOBAL", 1)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 965: If you're waiting for the Iron Collar mercenaries, I wouldn't bet on them showing up any time soon... at least until the kegs in the Salty Dog are empty.
			
		elif index == 5:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1):
				return True # 981: There was an altercation at the Salty Dog, and the Iron Collar Mercenaries refused to back down - they won't be coming.  We can take out those goblins for you.
			
		elif index == 6:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1):
				return True # 982: Actually, uh, I think the goblins may have already killed them.  It might be best if you let us go in and take out those goblins ourselves.
			
		elif index == 7:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 983: Look, there's no reason to wait for those mercenaries.  Let me go in and take those goblins out for you.
			
		elif index == 8:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 984: Where's the Salty Dog Tavern?  I could go find those sell-swords you're waiting for and bring them here.
			
		elif index == 9:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 985: I'll go grab the Iron Collar company from the Salty Dog, and perhaps between the three groups of us we can dispatch these goblins.
			
		elif index == 10:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1):
				return True # 1051: There was an altercation at the Salty Dog, and the Iron Collar Mercenaries refused to back down - they won't be coming.  We can take out those goblins for you.
			
		elif index == 11:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1):
				return True # 1052: Actually, uh, I think the goblins may have already killed them.  It might be best if you let us go in and take out those goblins ourselves.
			
		elif index == 12:
			# Global("Iron_Collar_Quest", "GLOBAL", 2)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Iron_Collar_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 1053: They're not coming.  They've too many kegs to slaughter in the Salty Dog to come to Targos' aid.  Let us handle the goblins.
			
		elif index == 13:
			# Global("Iron_Collar_Quest", "GLOBAL", 2)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Iron_Collar_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 1054: The Iron Collar mercenaries will not be coming.  It's just us.
			
		elif index == 14:
			# GlobalLT("Iron_Collar_Quest", "GLOBAL", 2)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Iron_Collar_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 1055: Forget the Iron Collar - let me go in and take out those goblins for you.
			
		elif index == 15:
			# GlobalLT("Iron_Collar_Quest", "GLOBAL", 2)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobalLT("'Iron_Collar_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 1056: No, I haven't found them yet.  I'll return when I do.
			
		elif index == 16:
			# CheckSkillGT(Protagonist, 0, Intimidate)
			if self.iCheckSkillGT("Protagonist", 0, "Intimidate"):
				return True # 1031: Let me in that warehouse, and you'll see how good we play at being soldiers.
			
		elif index == 17:
			# Global("Iron_Collar_Quest", "GLOBAL", 0)
			if self.iGlobal("'Iron_Collar_Quest'", "'GLOBAL'", 0):
				return True # 1032: Where's the Salty Dog Tavern?  I could go find those sell-swords you're waiting for and bring them here.
			
		elif index == 18:
			# Global("Iron_Collar_Quest", "GLOBAL", 1)
			if self.iGlobal("'Iron_Collar_Quest'", "'GLOBAL'", 1):
				return True # 1033: Where's the Salty Dog Tavern again?  I could go find those sell-swords you're waiting for and bring them here.
			
		elif index == 19:
			# Global("Know_Iron_Collar", "GLOBAL", 1)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 1):
				return True # 1035: But the Iron Collar mercenaries might not be able to get here in time.
			
		elif index == 20:
			# Global("Know_Iron_Collar", "GLOBAL", 1)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 1):
				return True # 1036: If you want soldiers, then you shouldn't be waiting for those Iron Collar drunks - if you want those goblins dead, then talk to *me.*
			
		elif index == 21:
			# ClassEx(Protagonist, Thief)
			if self.iClassEx("Protagonist", "Thief"):
				return True # 991: Hmmm. I might be able to pick the lock as well. Stand back.
			
		elif index == 22:
			# Global("AR1002_Visited", "GLOBAL", 0)
			if self.iGlobal("'AR1002_Visited'", "'GLOBAL'", 0):
				return True # 1061: Not yet - we're about ready to storm the warehouse, though.  Stand back.
			
		elif index == 23:
			# Global("AR1002_Visited", "GLOBAL", 1)
			# Global("AR1002_GOBLINS_CLEAR", "GLOBAL", 0)
			if self.iGlobal("'AR1002_Visited'", "'GLOBAL'", 1) \
				 and self.iGlobal("'AR1002_GOBLINS_CLEAR'", "'GLOBAL'", 0):
				return True # 1062: Not yet - there's still some left in the warehouse.  We're going back in shortly to take care of the rest.
			
		elif index == 24:
			# Global("AR1002_GOBLINS_CLEAR", "GLOBAL", 1)
			if self.iGlobal("'AR1002_GOBLINS_CLEAR'", "'GLOBAL'", 1):
				return True # 1063: We wiped out the ones inside, but there seems to be a passage leading below the warehouse - it looks like that's how they got into town in the first place.
			
		elif index == 25:
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 1071: There's no way in the nine hells I'm serving as a tunnel worm for you or for Targos... without some coin to show for my trouble.
			
		elif index == 26:
			# Global("AR1007_GOBLINS_CLEAR", "GLOBAL", 1)
			if self.iGlobal("'AR1007_GOBLINS_CLEAR'", "'GLOBAL'", 1):
				return True # 1091: We found a passage running beneath the warehouse - it led into some caves in the cliff.  It looks like goblin sappers tunneled through there to get into Targos.
			
		elif index == 27:
			# Global("AR1007_GOBLINS_CLEAR", "GLOBAL", 0)
			if self.iGlobal("'AR1007_GOBLINS_CLEAR'", "'GLOBAL'", 0):
				return True # 1092: We found a passage running beneath the warehouse - found more goblins down there, but I haven't taken them all out yet.  When they're taken care of, I'll be back.
			
		elif index == 28:
			# Global("AR1007_GOBLINS_CLEAR", "GLOBAL", 0)
			if self.iGlobal("'AR1007_GOBLINS_CLEAR'", "'GLOBAL'", 0):
				return True # 1093: Well, it's good you came to check on us, then.  As it stands, there are still some more goblins down below; we'll return when they're dead.
			
		elif index == 29:
			# !PartyHasItem("10Vellum")
			if not self.iPartyHasItem(const_proto_items_iwd2.PROTO_GENERIC_EXPENDED_TELEPORTATION_SCROLL):
				return True # 1101: Well, there were some collapsed passages - could be the goblins accidentally sealed themselves in.
			
		elif index == 30:
			# PartyHasItem("10Vellum")
			if self.iPartyHasItem(const_proto_items_iwd2.PROTO_GENERIC_EXPENDED_TELEPORTATION_SCROLL):
				return True # 1102: Well, there were some collapsed passages - could be the goblins accidentally sealed themselves in.  Found this scroll on one of the goblins, however, and it looks magical... or was, at least.
			
		elif index == 31:
			# Global("AR1002_GOBLINS_CLEAR", "GLOBAL", 0)
			if self.iGlobal("'AR1002_GOBLINS_CLEAR'", "'GLOBAL'", 0):
				return True # 1151: Swift action was called for.  There are still some goblins in the warehouse.  We're going back in shortly to take care of them.
			
		elif index == 32:
			# Global("AR1002_GOBLINS_CLEAR", "GLOBAL", 1)
			# Global("AR1007_Visited", "GLOBAL", 0)
			if self.iGlobal("'AR1002_GOBLINS_CLEAR'", "'GLOBAL'", 1) \
				 and self.iGlobal("'AR1007_Visited'", "'GLOBAL'", 0):
				return True # 1152: Swift action was called for.  We wiped out the ones in the warehouse, but there seems to be a passage leading below the warehouse - it looks like that's how they got into town in the first place.
			
		elif index == 33:
			# Global("AR1007_Visited", "GLOBAL", 1)
			# Global("AR1007_GOBLINS_CLEAR", "GLOBAL", 0)
			if self.iGlobal("'AR1007_Visited'", "'GLOBAL'", 1) \
				 and self.iGlobal("'AR1007_GOBLINS_CLEAR'", "'GLOBAL'", 0):
				return True # 1153: Swift action was called for.  We found a passage running beneath the warehouse - there were more goblins down there, but we haven't taken them all out yet.  When we've driven them out, we'll be back.
			
		elif index == 34:
			# Global("AR1007_GOBLINS_CLEAR", "GLOBAL", 1)
			if self.iGlobal("'AR1007_GOBLINS_CLEAR'", "'GLOBAL'", 1):
				return True # 1154: Swift action was called for.  We found a passage running beneath the warehouse - it led into some caves in the cliff.  It looks like goblin sappers tunneled through there to get into Targos.
			
		elif index == 35:
			# Global("AR1002_GOBLINS_CLEAR", "GLOBAL", 0)
			if self.iGlobal("'AR1002_GOBLINS_CLEAR'", "'GLOBAL'", 0):
				return True # 1171: We couldn't wait for the Iron Collar mercenaries - plus, there's still some goblins left in the warehouse.  We're going back in shortly to take care of them.
			
		elif index == 36:
			# Global("AR1002_GOBLINS_CLEAR", "GLOBAL", 1)
			# Global("AR1007_Visited", "GLOBAL", 0)
			if self.iGlobal("'AR1002_GOBLINS_CLEAR'", "'GLOBAL'", 1) \
				 and self.iGlobal("'AR1007_Visited'", "'GLOBAL'", 0):
				return True # 1172: We couldn't wait for the Iron Collar mercenaries  and swift action was called for.  We wiped out the goblins in the warehouse, but there seems to be a passage leading below the warehouse - it looks like that's how they got into town in the first place.
			
		elif index == 37:
			# Global("AR1007_Visited", "GLOBAL", 1)
			# Global("AR1007_GOBLINS_CLEAR", "GLOBAL", 0)
			if self.iGlobal("'AR1007_Visited'", "'GLOBAL'", 1) \
				 and self.iGlobal("'AR1007_GOBLINS_CLEAR'", "'GLOBAL'", 0):
				return True # 1173: Swift action was called for.  We found a passage running beneath the warehouse - there were more goblins down there, but we haven't taken them all out yet.  When they're taken care of, we'll be back.
			
		elif index == 38:
			# Global("AR1007_GOBLINS_CLEAR", "GLOBAL", 1)
			if self.iGlobal("'AR1007_GOBLINS_CLEAR'", "'GLOBAL'", 1):
				return True # 1174: Swift action was called for.  We found a passage running beneath the warehouse - it led into some caves in the cliff.  It looks like goblin sappers tunneled through there to get into Targos.
			
		elif index == 39:
			# ClassEx(Protagonist, Mage)
			# !Class(Protagonist, SORCERER)
			if self.iClassEx("Protagonist", "Mage") \
				 and not self.iClass("Protagonist", "SORCERER"):
				return True # 1021: Hmm.  Sound advice.  Still, we wizards are a lot stronger than we appear.  We'll see about getting this door open.
			
		elif index == 40:
			# Class(Protagonist, SORCERER)
			if self.iClass("Protagonist", "SORCERER"):
				return True # 1022: Watch it.  We sorcerers are a lot stronger than we appear - but perhaps we'll heed your advice this time.  We'll see about getting this door open, then.
			
		elif index == 41:
			# !ClassEx(Protagonist, Mage)
			# !ClassEx(Protagonist, Sorcerer)
			if not self.iClassEx("Protagonist", "Mage") \
				 and not self.iClassEx("Protagonist", "Sorcerer"):
				return True # 1023: All right, then - we'll see about getting this door open.  Stand back.
			
		return False # dialog_test_do
	
	def dialog_action_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		if index == 0:
			# SetGlobal("Know_Brogan", "GLOBAL", 1)
			self.iSetGlobal("'Know_Brogan'", "'GLOBAL'", 1)
			# 941: We're adventurers from Luskan.  What's going on here?
			
		elif index == 1:
			# SetGlobal("Know_Brogan", "GLOBAL", 1)
			self.iSetGlobal("'Know_Brogan'", "'GLOBAL'", 1)
			# 942: Calm yourself - what's the problem?
			
		elif index == 2:
			# SetGlobal("Iron_Collar_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Iron_Collar_Quest'", "'GLOBAL'", 1)
			# 984: Where's the Salty Dog Tavern?  I could go find those sell-swords you're waiting for and bring them here.
			
		elif index == 3:
			# SetGlobal("Iron_Collar_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Iron_Collar_Quest'", "'GLOBAL'", 1)
			# 985: I'll go grab the Iron Collar company from the Salty Dog, and perhaps between the three groups of us we can dispatch these goblins.
			
		elif index == 4:
			# AddXpVar("Level_1_Easy",27693)
			self.iAddXpVar("'Level_1_Easy'", 27693)
			# SetGlobal("Iron_Collar_Quest", "GLOBAL", 3)
			self.iSetGlobal("'Iron_Collar_Quest'", "'GLOBAL'", 3)
			# 1053: They're not coming.  They've too many kegs to slaughter in the Salty Dog to come to Targos' aid.  Let us handle the goblins.
			
		elif index == 5:
			# AddXpVar("Level_1_Easy",27693)
			self.iAddXpVar("'Level_1_Easy'", 27693)
			# SetGlobal("Iron_Collar_Quest", "GLOBAL", 3)
			self.iSetGlobal("'Iron_Collar_Quest'", "'GLOBAL'", 3)
			# 1054: The Iron Collar mercenaries will not be coming.  It's just us.
			
		elif index == 6:
			# AddXpVar("Level_1_Easy",27695)
			self.iAddXpVar("'Level_1_Easy'", 27695)
			# 1031: Let me in that warehouse, and you'll see how good we play at being soldiers.
			
		elif index == 7:
			# SetGlobal("Iron_Collar_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Iron_Collar_Quest'", "'GLOBAL'", 1)
			# 1032: Where's the Salty Dog Tavern?  I could go find those sell-swords you're waiting for and bring them here.
			
		elif index == 8:
			# SetGlobal("Iron_Collar_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Iron_Collar_Quest'", "'GLOBAL'", 1)
			# 1033: Where's the Salty Dog Tavern again?  I could go find those sell-swords you're waiting for and bring them here.
			
		elif index == 9:
			# SetGlobal("Iron_Collar_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Iron_Collar_Quest'", "'GLOBAL'", 1)
			# 1034: I'll go grab the Iron Collar company from the Salty Dog, and perhaps between the three groups of us we can dispatch these goblins.
			
		elif index == 10:
			# AddXpVar("Level_1_Easy",27695)
			self.iAddXpVar("'Level_1_Easy'", 27695)
			# 1035: But the Iron Collar mercenaries might not be able to get here in time.
			
		elif index == 11:
			# AddXpVar("Level_1_Easy",27695)
			self.iAddXpVar("'Level_1_Easy'", 27695)
			# 1036: If you want soldiers, then you shouldn't be waiting for those Iron Collar drunks - if you want those goblins dead, then talk to *me.*
			
		elif index == 12:
			# SetGlobal("Brogan_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Brogan_Quest'", "'GLOBAL'", 1)
			# 991: Hmmm. I might be able to pick the lock as well. Stand back.
			
		elif index == 13:
			# SetGlobal("Brogan_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Brogan_Quest'", "'GLOBAL'", 1)
			# 1001: How many do you figure are in the warehouse?
			
		elif index == 14:
			# SetGlobal("Brogan_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Brogan_Quest'", "'GLOBAL'", 1)
			# 1002: All right, then.  Stand back.
			
		elif index == 15:
			# AddXpVar("Level_1_Average",27697)
			self.iAddXpVar("'Level_1_Average'", 27697)
			# 1111: Continue
			
		elif index == 16:
			# SetGlobal("Brogan_Quest", "GLOBAL", 2)
			self.iSetGlobal("'Brogan_Quest'", "'GLOBAL'", 2)
			# 1121: I hope so.  Where can I find him?
			
		elif index == 17:
			# SetGlobal("Brogan_Quest", "GLOBAL", 2)
			self.iSetGlobal("'Brogan_Quest'", "'GLOBAL'", 2)
			# 1122: No reward is necessary... as long as Targos is safe, that is enough.  I would speak to Lord Ulbrec about employment, however.
			
		elif index == 18:
			# SetGlobal("Brogan_Leave", "GLOBAL", 1)
			self.iSetGlobal("'Brogan_Leave'", "'GLOBAL'", 1)
			# 1131: I will seek him out, then.  Farewell.
			
		elif index == 19:
			# SetGlobal("Brogan_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Brogan_Quest'", "'GLOBAL'", 1)
			# 1171: We couldn't wait for the Iron Collar mercenaries - plus, there's still some goblins left in the warehouse.  We're going back in shortly to take care of them.
			
		elif index == 20:
			# SetGlobal("Brogan_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Brogan_Quest'", "'GLOBAL'", 1)
			# 1172: We couldn't wait for the Iron Collar mercenaries  and swift action was called for.  We wiped out the goblins in the warehouse, but there seems to be a passage leading below the warehouse - it looks like that's how they got into town in the first place.
			
		elif index == 21:
			# SetGlobal("Brogan_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Brogan_Quest'", "'GLOBAL'", 1)
			# 1173: Swift action was called for.  We found a passage running beneath the warehouse - there were more goblins down there, but we haven't taken them all out yet.  When they're taken care of, we'll be back.
			
		elif index == 22:
			# SetGlobal("Brogan_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Brogan_Quest'", "'GLOBAL'", 1)
			# 1174: Swift action was called for.  We found a passage running beneath the warehouse - it led into some caves in the cliff.  It looks like goblin sappers tunneled through there to get into Targos.
			
		elif index == 23:
			# AddXpVar("Level_1_Average",27697)
			self.iAddXpVar("'Level_1_Average'", 27697)
			# 1141: Continue
			
		return # dialog_action_do
		
	def get_dialog_trigger_max_index(self): return 41
	
	def get_state_to_line(self, state):
		if state==0: return 940
		if state==1: return 950
		if state==2: return 960
		if state==3: return 970
		if state==4: return 980
		if state==5: return 1040
		if state==6: return 1050
		if state==7: return 1030
		if state==8: return 990
		if state==9: return 1000
		if state==10: return 1060
		if state==11: return 1070
		if state==12: return 1080
		if state==13: return 1090
		if state==14: return 1100
		if state==15: return 1110
		if state==16: return 1120
		if state==17: return 1130
		if state==18: return 1150
		if state==19: return 1160
		if state==20: return 1170
		if state==21: return 1010
		if state==22: return 1020
		if state==23: return 1140
		return
	
class Ctrl_10JORUN_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10JORUN 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN
	
	def setup_scripts(self, npc):
		super(Ctrl_10JORUN_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Jorun Tamewater")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
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
		npc.obj_set_int(toee.obj_f_critter_experience, 65) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # CR: 2 TODO!!!
		
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
	
	def script_dialog(self, attachee, triggerer):
		print("script_dialog 10JORUN")
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		while True:
			print("STATE 0")
			# Global("Know_Jorun", "GLOBAL", 0)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("'Know_Jorun'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				line_id = 1180 # Damnable goblins... it seems no matter what corners o' the world y'go, they're always there.  Who are ye?  Do ye stand with Targos?
				print("STATE 0: line_id = 1180")
				break
			
			print("STATE 13")
			# Global("Know_Jorun", "GLOBAL", 1)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("'Know_Jorun'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				line_id = 1390 # Have ye spilled any more goblin blood?  Ye better not be greedy - make ye sure ye save a handful for me.
				print("STATE 13: line_id = 1390")
				break
			
			print("STATE 14")
			# Global("Know_Jorun", "GLOBAL", 0)
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("'Know_Jorun'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1):
				line_id = 1400 # Well, now, something I can help ye with?  I'm not doing business with the attacks an' all, and there's not much call for building ships as much as taking them down.
				print("STATE 14: line_id = 1400")
				break
			
			print("STATE 20")
			# Global("Know_Jorun", "GLOBAL", 1)
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("'Know_Jorun'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1):
				line_id = 1490 # More than once ye've crossed my path; if ye plan on makin' a habit of it, the least ye could do is bring a winecask with ye... or two. Somethin' I can do for ye?
				print("STATE 20: line_id = 1490")
				break
			
			print("STATE 31")
			# NumTimesTalkedTo(0)
			# Subrace(Protagonist, Dwarf_Gray)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iNumTimesTalkedTo(0) \
				 and self.iSubrace("Protagonist", "Dwarf_Gray") \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				line_id = 1500 # Eh?!  A duergar in Targos?  Ye were the last beast I expected to see in league with these goblins, but it'll give me pleasure to bury yer black heart alongside them.
				print("STATE 31: line_id = 1500")
				break
			
			print("STATE 32")
			# NumTimesTalkedTo(0)
			# Subrace(Protagonist, Elf_Drow)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iNumTimesTalkedTo(0) \
				 and self.iSubrace("Protagonist", "Elf_Drow") \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				line_id = 1530 # Eh?!  A drow in Targos?  Ye were the last beast I expected to see in league with these goblins, but it'll give me pleasure to bury yer black heart alongside them.
				print("STATE 32: line_id = 1530")
				break
			
			print("STATE 35")
			# NumTimesTalkedTo(0)
			# Subrace(Protagonist, Gnome_Deep)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iNumTimesTalkedTo(0) \
				 and self.iSubrace("Protagonist", "Gnome_Deep") \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				line_id = 1540 # Damn me eyes... are ye a deep gnome?  What in the hells are ye doing in Targos?
				print("STATE 35: line_id = 1540")
				break
			
			print("STATE 37")
			# NumTimesTalkedTo(0)
			# Subrace(Protagonist, Dwarf_Gray)
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iNumTimesTalkedTo(0) \
				 and self.iSubrace("Protagonist", "Dwarf_Gray") \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1):
				line_id = 1550 # I heard talk of a duergar around town... didn't put much stock in it 'til now.  I hear ye done a good job splitting goblins in half, but ye've still got a long way to go to earning my trust... and Targos' trust.  Now what did ye want with this ol' shipbuilder?
				print("STATE 37: line_id = 1550")
				break
			
			print("STATE 38")
			# NumTimesTalkedTo(0)
			# Subrace(Protagonist, Elf_Drow)
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iNumTimesTalkedTo(0) \
				 and self.iSubrace("Protagonist", "Elf_Drow") \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1):
				line_id = 1560 # I heard talk of a drow around town... didn't put much stock in it 'til now.  I hear ye done a good job splitting goblins in half, but ye've still got a long way to go to earning my trust... and Targos' trust.  Now what did ye want with this ol' shipbuilder?
				print("STATE 38: line_id = 1560")
				break
			
			print("STATE 39")
			# NumTimesTalkedTo(0)
			# Subrace(Protagonist, Gnome_Deep)
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iNumTimesTalkedTo(0) \
				 and self.iSubrace("Protagonist", "Gnome_Deep") \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1):
				line_id = 1570 # Damn me eyes... ye're the deep gnome everyone's going on about.  I was hoping ye might be crossing me path - something this ol' shipbuilder can help ye with? 
				print("STATE 39: line_id = 1570")
				break
			
			print("STATE 40")
			# NumTimesTalkedTo(0)
			# Race(Protagonist, Dwarf)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iNumTimesTalkedTo(0) \
				 and self.iRace("Protagonist", "Dwarf") \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				line_id = 1580 # It's good to see another dwarf on the shore of Maer Dualdon especially with these damnable goblins about... it seems no matter what corners o' the world y'go, they're always there.  Who are ye?  Do ye come to add yer axe and hammer to Targos? 
				print("STATE 40: line_id = 1580")
				break
			
			print("STATE 41")
			# NumTimesTalkedTo(0)
			# Race(Protagonist, Dwarf)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iNumTimesTalkedTo(0) \
				 and self.iRace("Protagonist", "Dwarf") \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				line_id = 1590 # Well, now, a dwarf is a sight for sore eyes in these windswept lands... especially one who can cleave goblins as well as ye can.  Something this ol' shipbuilder can help ye with?  
				print("STATE 41: line_id = 1590")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return line_id # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		# 10JORUN
		
		if index == 0:
			# Global("Jorun_Rest", "GLOBAL", 0)
			if self.iGlobal("'Jorun_Rest'", "'GLOBAL'", 0):
				return True # 1211: Do you know of any place we can rest?
			
		elif index == 1:
			# Global("Jorun_Help", "GLOBAL", 0)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 0):
				return True # 1213: Agreed.  Watch yourself, Jorun.
			
		elif index == 2:
			# Global("Jorun_Help", "GLOBAL", 1)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 1):
				return True # 1214: Agreed.  Farewell, Jorun.
			
		elif index == 3:
			# Global("Brogan_Quest", "GLOBAL", 2)
			if self.iGlobal("'Brogan_Quest'", "'GLOBAL'", 2):
				return True # 1291: It looks like they tunneled into some old caves in the Targos cliffs and used them to get to the docks.
			
		elif index == 4:
			# Global("Jorun_Rest", "GLOBAL", 0)
			if self.iGlobal("'Jorun_Rest'", "'GLOBAL'", 0):
				return True # 1341: Do you know of any place we can rest?
			
		elif index == 5:
			# Global("Jorun_Rest", "GLOBAL", 0)
			if self.iGlobal("'Jorun_Rest'", "'GLOBAL'", 0):
				return True # 1371: Do you know of any place we can rest?
			
		elif index == 6:
			# Global("Ask_Caves", "GLOBAL", 0)
			if self.iGlobal("'Ask_Caves'", "'GLOBAL'", 0):
				return True # 1372: Where did these caves come from?
			
		elif index == 7:
			# Global("Jorun_Help", "GLOBAL", 0)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 0):
				return True # 1373: We'll be on our guard.  Watch yourself, Jorun.
			
		elif index == 8:
			# Global("Jorun_Help", "GLOBAL", 1)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 1):
				return True # 1374: All right - we'll be on our guard.  Farewell, Jorun.
			
		elif index == 9:
			# Global("Jorun_Rest", "GLOBAL", 0)
			if self.iGlobal("'Jorun_Rest'", "'GLOBAL'", 0):
				return True # 1331: Do you know of any place we can rest?
			
		elif index == 10:
			# Global("Jorun_Help", "GLOBAL", 0)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 0):
				return True # 1332: Hmm.  Good point.  We'll see what we can find out - watch yourself.
			
		elif index == 11:
			# Global("Jorun_Help", "GLOBAL", 1)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 1):
				return True # 1333: Hmm.  Good point.  Farewell, Jorun.
			
		elif index == 12:
			# Global("Jorun_Rest", "GLOBAL", 0)
			if self.iGlobal("'Jorun_Rest'", "'GLOBAL'", 0):
				return True # 1391: Do you know of any place we can rest?
			
		elif index == 13:
			# Global("Lumber_Quest", "GLOBAL", 3)
			if self.iGlobal("'Lumber_Quest'", "'GLOBAL'", 3):
				return True # 1411: Jorun Tamewater?  I spoke with your son, Olap, at the Palisade.  It seems the crane broke, and it needs to be fixed.
			
		elif index == 14:
			# Global("Lumber_Quest", "GLOBAL", 3)
			if self.iGlobal("'Lumber_Quest'", "'GLOBAL'", 3):
				return True # 1481: I spoke with your son, Olap, at the Palisade.  It seems the crane broke, and it needs to be fixed.
			
		elif index == 15:
			# Global("Lumber_Quest", "GLOBAL", 3)
			if self.iGlobal("'Lumber_Quest'", "'GLOBAL'", 3):
				return True # 1491: I spoke with your son, Olap, at the Palisade.  It seems the crane broke, and it needs to be fixed.
			
		elif index == 16:
			# PartyHasItem("00helm05")
			if self.iPartyHasItem(const_proto_cloth.PROTO_CLOTH_HELM_GREAT):
				return True # 1231: We already opened your chest - do you mind if we put your equipment to use?
			
		elif index == 17:
			# PartyHasItem("00helm05")
			# !ClassEx(Protagonist, Paladin)
			if self.iPartyHasItem(const_proto_cloth.PROTO_CLOTH_HELM_GREAT) \
				 and not self.iClassEx("Protagonist", "Paladin"):
				return True # 1232: Uh, the goblins may have looted it already.  That would be terrible. What's in this chest of yours?
			
		elif index == 18:
			# !PartyHasItem("00helm05")
			if not self.iPartyHasItem(const_proto_cloth.PROTO_CLOTH_HELM_GREAT):
				return True # 1233: What's in the chest?
			
		elif index == 19:
			# Global("Jorun_Help", "GLOBAL", 0)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 0):
				return True # 1241: All right, then.  Watch yourself, Jorun.
			
		elif index == 20:
			# Global("Jorun_Help", "GLOBAL", 1)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 1):
				return True # 1242: All right, then.  Watch yourself, Jorun.
			
		elif index == 21:
			# !PartyHasItem("00helm05")
			if not self.iPartyHasItem(const_proto_cloth.PROTO_CLOTH_HELM_GREAT):
				return True # 1261: If we could get your chest open, would you mind if we used your equipment?
			
		elif index == 22:
			# PartyHasItem("00helm05")
			# !ClassEx(Protagonist, Paladin)
			if self.iPartyHasItem(const_proto_cloth.PROTO_CLOTH_HELM_GREAT) \
				 and not self.iClassEx("Protagonist", "Paladin"):
				return True # 1262: Uh, if we could, say, get your chest open, would you mind if we used your equipment?
			
		elif index == 23:
			# !ClassEx(Protagonist, Paladin)
			if not self.iClassEx("Protagonist", "Paladin"):
				return True # 1263: If someone were to, say, pick the lock, would the trap go off?
			
		elif index == 24:
			# !ClassEx(Protagonist, Paladin)
			if not self.iClassEx("Protagonist", "Paladin"):
				return True # 1271: Will the trap go off if someone picks the lock?
			
		elif index == 25:
			# Global("Jorun_Help", "GLOBAL", 0)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 0):
				return True # 1273: All right, then.  Watch yourself, Jorun.
			
		elif index == 26:
			# Global("Jorun_Help", "GLOBAL", 1)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 1):
				return True # 1274: All right, then.  Watch yourself, Jorun.
			
		elif index == 27:
			# Global("Jorun_Help", "GLOBAL", 0)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 0):
				return True # 1282: All right, then.  Watch yourself, Jorun.
			
		elif index == 28:
			# Global("Jorun_Help", "GLOBAL", 1)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 1):
				return True # 1283: All right, then.  Watch yourself, Jorun.
			
		elif index == 29:
			# Global("Jorun_Help", "GLOBAL", 0)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 0):
				return True # 1382: All right, then.  Watch yourself, Jorun.
			
		elif index == 30:
			# Global("Jorun_Help", "GLOBAL", 1)
			if self.iGlobal("'Jorun_Help'", "'GLOBAL'", 1):
				return True # 1383: All right, then.  Watch yourself, Jorun.
			
		elif index == 31:
			# Global("Lumber_Quest", "GLOBAL", 3)
			if self.iGlobal("'Lumber_Quest'", "'GLOBAL'", 3):
				return True # 1551: Are you Jorun Tamewater?  I spoke with your son, Olap, at the Palisade.  It seems the crane broke, and it needs to be fixed.
			
		elif index == 32:
			# Global("Lumber_Quest", "GLOBAL", 3)
			if self.iGlobal("'Lumber_Quest'", "'GLOBAL'", 3):
				return True # 1561: Are you Jorun Tamewater?  I spoke with your son, Olap, at the Palisade.  It seems the crane broke, and it needs to be fixed.
			
		return False # dialog_test_do
	
	def dialog_action_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		if index == 0:
			# SetGlobal("Know_Jorun", "GLOBAL", 1)
			self.iSetGlobal("'Know_Jorun'", "'GLOBAL'", 1)
			# 1181: We're adventurers from Luskan.  We just came in on the Wicked Wench and found Targos being attacked.
			
		elif index == 1:
			# SetGlobal("Jorun_Help", "GLOBAL", 1)
			self.iSetGlobal("'Jorun_Help'", "'GLOBAL'", 1)
			# 1213: Agreed.  Watch yourself, Jorun.
			
		elif index == 2:
			# SetGlobal("Ask_Caves", "GLOBAL", 1)
			self.iSetGlobal("'Ask_Caves'", "'GLOBAL'", 1)
			# 1342: What old caves?
			
		elif index == 3:
			# SetGlobal("Ask_Caves", "GLOBAL", 1)
			self.iSetGlobal("'Ask_Caves'", "'GLOBAL'", 1)
			# 1372: Where did these caves come from?
			
		elif index == 4:
			# SetGlobal("Ask_Caves", "GLOBAL", 0)
			self.iSetGlobal("'Ask_Caves'", "'GLOBAL'", 0)
			# SetGlobal("Jorun_Help", "GLOBAL", 1)
			self.iSetGlobal("'Jorun_Help'", "'GLOBAL'", 1)
			# 1373: We'll be on our guard.  Watch yourself, Jorun.
			
		elif index == 5:
			# SetGlobal("Ask_Caves", "GLOBAL", 0)
			self.iSetGlobal("'Ask_Caves'", "'GLOBAL'", 0)
			# 1374: All right - we'll be on our guard.  Farewell, Jorun.
			
		elif index == 6:
			# SetGlobal("Jorun_Help", "GLOBAL", 1)
			self.iSetGlobal("'Jorun_Help'", "'GLOBAL'", 1)
			# 1332: Hmm.  Good point.  We'll see what we can find out - watch yourself.
			
		elif index == 7:
			# SetGlobal("Know_Jorun", "GLOBAL", 1)
			self.iSetGlobal("'Know_Jorun'", "'GLOBAL'", 1)
			# 1401: My name is @pcname@ .  Who are you?
			
		elif index == 8:
			# SetGlobal("Lumber_Quest", "GLOBAL", 4)
			self.iSetGlobal("'Lumber_Quest'", "'GLOBAL'", 4)
			# GiveItemCreate("10GenCrW ", Protagonist, 0, 0, 0)
			self.iGiveItemCreate(const_proto_items_iwd2.PROTO_SCROLL_WOODEN_CRANE_WHEEL, "Protagonist", 0, 0, 0)
			# 1431: How?
			
		elif index == 9:
			# SetGlobal("Jorun_Help", "GLOBAL", 1)
			self.iSetGlobal("'Jorun_Help'", "'GLOBAL'", 1)
			# SetGlobal("Ask_Caves", "GLOBAL", 0)
			self.iSetGlobal("'Ask_Caves'", "'GLOBAL'", 0)
			# 1251: Sounds good to me.  Farewell, Jorun.
			
		elif index == 10:
			# SetGlobal("Jorun_Rest", "GLOBAL", 1)
			self.iSetGlobal("'Jorun_Rest'", "'GLOBAL'", 1)
			# SetGlobal("Ask_Caves", "GLOBAL", 0)
			self.iSetGlobal("'Ask_Caves'", "'GLOBAL'", 0)
			# 1221: Why is that?
			
		elif index == 11:
			# SetGlobal("Jorun_Help", "GLOBAL", 1)
			self.iSetGlobal("'Jorun_Help'", "'GLOBAL'", 1)
			# 1241: All right, then.  Watch yourself, Jorun.
			
		elif index == 12:
			# SetGlobal("Jorun_Help", "GLOBAL", 1)
			self.iSetGlobal("'Jorun_Help'", "'GLOBAL'", 1)
			# 1273: All right, then.  Watch yourself, Jorun.
			
		elif index == 13:
			# SetGlobal("Jorun_Help", "GLOBAL", 1)
			self.iSetGlobal("'Jorun_Help'", "'GLOBAL'", 1)
			# 1282: All right, then.  Watch yourself, Jorun.
			
		elif index == 14:
			# SetGlobal("Jorun_Dwarf", "GLOBAL", 1)
			self.iSetGlobal("'Jorun_Dwarf'", "'GLOBAL'", 1)
			# SetGlobal("Know_Jorun", "GLOBAL", 1)
			self.iSetGlobal("'Know_Jorun'", "'GLOBAL'", 1)
			# 1511: What gain would there be in me even talking to you?  If I were with the goblins, I would be attacking you right now.
			
		elif index == 15:
			# SetGlobal("Jorun_Dwarf", "GLOBAL", 1)
			self.iSetGlobal("'Jorun_Dwarf'", "'GLOBAL'", 1)
			# SetGlobal("Know_Jorun", "GLOBAL", 1)
			self.iSetGlobal("'Know_Jorun'", "'GLOBAL'", 1)
			# 1512: We sailed in on the Wicked Wench, you idiot!  We're from Luskan - either you trust us or you don't.  I have no more time to waste talking to you.
			
		elif index == 16:
			# SetGlobal("Know_Jorun", "GLOBAL", 1)
			self.iSetGlobal("'Know_Jorun'", "'GLOBAL'", 1)
			# 1541: We're adventurers from Luskan.  We just came in on the Wicked Wench and found Targos being attacked.
			
		elif index == 17:
			# SetGlobal("Jorun_Help", "GLOBAL", 1)
			self.iSetGlobal("'Jorun_Help'", "'GLOBAL'", 1)
			# 1382: All right, then.  Watch yourself, Jorun.
			
		elif index == 18:
			# SetGlobal("Know_Jorun", "GLOBAL", 1)
			self.iSetGlobal("'Know_Jorun'", "'GLOBAL'", 1)
			# 1551: Are you Jorun Tamewater?  I spoke with your son, Olap, at the Palisade.  It seems the crane broke, and it needs to be fixed.
			
		elif index == 19:
			# SetGlobal("Know_Jorun", "GLOBAL", 1)
			self.iSetGlobal("'Know_Jorun'", "'GLOBAL'", 1)
			# 1552: We're looking to spill some goblin blood... and earn a few coins for our trouble, but the coinage so far has been somewhat light. 
			
		elif index == 20:
			# SetGlobal("Know_Jorun", "GLOBAL", 1)
			self.iSetGlobal("'Know_Jorun'", "'GLOBAL'", 1)
			# 1561: Are you Jorun Tamewater?  I spoke with your son, Olap, at the Palisade.  It seems the crane broke, and it needs to be fixed.
			
		elif index == 21:
			# SetGlobal("Know_Jorun", "GLOBAL", 1)
			self.iSetGlobal("'Know_Jorun'", "'GLOBAL'", 1)
			# 1562: We're looking to spill some goblin blood... and earn a few coins for our trouble, but the coinage so far has been somewhat light. 
			
		elif index == 22:
			# SetGlobal("Know_Jorun", "GLOBAL", 1)
			self.iSetGlobal("'Know_Jorun'", "'GLOBAL'", 1)
			# 1571: My name is @pcname@ .  Who are you?
			
		elif index == 23:
			# SetGlobal("Know_Jorun", "GLOBAL", 1)
			self.iSetGlobal("'Know_Jorun'", "'GLOBAL'", 1)
			# 1581: We're adventurers from Luskan.  We just came in on the Wicked Wench and found Targos being attacked. 
			
		elif index == 24:
			# SetGlobal("Know_Jorun", "GLOBAL", 1)
			self.iSetGlobal("'Know_Jorun'", "'GLOBAL'", 1)
			# 1591: My name is @pcname@ .  Who are you?
			
		return # dialog_action_do
		
	def get_dialog_trigger_max_index(self): return 32
	
	def get_state_to_line(self, state):
		if state==0: return 1180
		if state==1: return 1190
		if state==2: return 1200
		if state==3: return 1210
		if state==4: return 1290
		if state==5: return 1340
		if state==6: return 1350
		if state==7: return 1360
		if state==8: return 1370
		if state==9: return 1300
		if state==10: return 1310
		if state==11: return 1320
		if state==12: return 1330
		if state==13: return 1390
		if state==14: return 1400
		if state==15: return 1410
		if state==16: return 1450
		if state==17: return 1460
		if state==18: return 1470
		if state==19: return 1480
		if state==20: return 1490
		if state==21: return 1420
		if state==22: return 1430
		if state==23: return 1440
		if state==24: return 1250
		if state==25: return 1220
		if state==26: return 1230
		if state==27: return 1240
		if state==28: return 1260
		if state==29: return 1270
		if state==30: return 1280
		if state==31: return 1500
		if state==32: return 1530
		if state==33: return 1510
		if state==34: return 1520
		if state==35: return 1540
		if state==36: return 1380
		if state==37: return 1550
		if state==38: return 1560
		if state==39: return 1570
		if state==40: return 1580
		if state==41: return 1590
		return
	
class Ctrl_10GOB_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10GOB 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GOBLIN
	
	def setup_scripts(self, npc):
		super(Ctrl_10GOB_Auto, self).setup_scripts(npc)
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
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
	
class Ctrl_10GOBD_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10GOBD 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GOBLIN
	
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
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
	
class Ctrl_10MALED_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10MALED 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	def setup_scripts(self, npc):
		super(Ctrl_10MALED_Auto, self).setup_scripts(npc)
		return
	
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
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
	
class Ctrl_10SOLDRD_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10SOLDRD 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	def setup_scripts(self, npc):
		super(Ctrl_10SOLDRD_Auto, self).setup_scripts(npc)
		return
	
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
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
	
class Ctrl_10GOBARD_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10GOBARD 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GOBLIN
	
	def setup_scripts(self, npc):
		super(Ctrl_10GOBARD_Auto, self).setup_scripts(npc)
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
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
	
class Ctrl_10SAILRD_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10SAILRD 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	def setup_scripts(self, npc):
		super(Ctrl_10SAILRD_Auto, self).setup_scripts(npc)
		return
	
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
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
	
class Ctrl_10GOBAR_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10GOBAR 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GOBLIN
	
	def setup_scripts(self, npc):
		super(Ctrl_10GOBAR_Auto, self).setup_scripts(npc)
		return
	
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
		npc.obj_set_int(toee.obj_f_critter_experience, 25) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
	
class Ctrl_10CRANDA_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 10CRANDA 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	def setup_scripts(self, npc):
		super(Ctrl_10CRANDA_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Crandall")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_red # HairColourIndex: 4
		hairStyle.update_npc(npc)
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [12, 11, 12, 9, 9, 9])
		
		# class levels: 1
		# stat_level_fighter: 1
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_TRUE_NEUTRAL) # 0x22 NEUTRAL
		npc.obj_set_int(toee.obj_f_critter_experience, 15) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0) # CR: 1 TODO!!!
		
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
		# SLOT_ARMOR: Leather Armor(LeatherArmor) from 00LEAT01
		utils_item.item_create_in_inventory2(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN, npc, no_loot = False, wear_on = toee.item_wear_armor) # Leather Armor (00LEAT01) at SLOT_ARMOR OK
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = False, wear_on = toee.item_wear_boots) # boots for Leather Armor (00LEAT01) OK
		
		# SLOT_WEAPON1: Spear(Spears) from 00SPER01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_SHORTSPEAR, npc, no_loot = False, wear_on = toee.item_wear_weapon_primary) # Spear (00SPER01) at SLOT_WEAPON1 OK
		
		# SLOT_QUICK2: Gold(Gold) from MISC07
		utils_item.item_money_create_in_inventory(npc, 0, 1, 2, 0) # Charges1: 1, Charges2: 2, Charges3: 0
		
		return
	
	def script_dialog(self, attachee, triggerer):
		print("script_dialog 10CRANDA")
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		while True:
			print("STATE 0")
			# NumTimesTalkedTo(0)
			if self.iNumTimesTalkedTo(0):
				line_id = 1600 # Hold!  Do you stand with Targos or against her?
				print("STATE 0: line_id = 1600")
				break
			
			print("STATE 8")
			# NumTimesTalkedToGT(0)
			if self.iNumTimesTalkedToGT(0):
				line_id = 1700 # Any word of goblins or the guard?
				print("STATE 8: line_id = 1700")
				break
			
			print("STATE 9")
			# Global("Crandall_Leave", "GLOBAL", 1)
			if self.iGlobal("'Crandall_Leave'", "'GLOBAL'", 1):
				line_id = 1710 # If you haven't already, you should tell of your efforts to our Lord Ulbrec - we are in dire need of blades such as yours in the days to come.
				print("STATE 9: line_id = 1710")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return line_id # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		# 10CRANDA
		
		if index == 0:
			# Global("Reig_Quest", "GLOBAL", 1)
			# Global("Know_Magdar", "GLOBAL", 0)
			if self.iGlobal("'Reig_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Know_Magdar'", "'GLOBAL'", 0):
				return True # 1621: Do you know where I can find a man named Magdar Shenlen?  One of the soldiers by the docks has been wounded and is in need of a potion that Magdar is said to have.
			
		elif index == 1:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1):
				return True # 1622: Have no fear of that.  We've dispatched the goblin attackers - the docks belong to Targos again.
			
		elif index == 2:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				return True # 1623: Have you seen any goblins?
			
		elif index == 3:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				return True # 1624: Stay here and watch the docks - we'll see about taking care of the goblins in the town.
			
		elif index == 4:
			# Global("Reig_Quest", "GLOBAL", 1)
			# Global("Know_Magdar", "GLOBAL", 0)
			if self.iGlobal("'Reig_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Know_Magdar'", "'GLOBAL'", 0):
				return True # 1701: Do you know where I can find a man named Magdar Shenlen?  One of the soldiers by the docks has been wounded and is in need of a potion that Magdar is said to have.
			
		elif index == 5:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				return True # 1702: Have you seen any goblins in the area?
			
		elif index == 6:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1):
				return True # 1703: Have no fear of goblins.  We've dispatched them - the docks belong to Targos again.
			
		elif index == 7:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				return True # 1704: No word yet - keep to your post.  If we hear of anything, we will summon you.
			
		elif index == 8:
			# Global("Reig_Quest", "GLOBAL", 1)
			# Global("Know_Magdar", "GLOBAL", 0)
			if self.iGlobal("'Reig_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Know_Magdar'", "'GLOBAL'", 0):
				return True # 1652: Do you know where I can find a man named Magdar Shenlen?  One of the soldiers by the docks has been wounded and is in need of a potion that Magdar is said to have.
			
		elif index == 9:
			# ClassEx(Protagonist, Thief)
			if self.iClassEx("Protagonist", "Thief"):
				return True # 1653: Not a bad idea.  Maybe a little hide in shadows and scouting could prove useful.  Farewell.
			
		elif index == 10:
			# ClassEx(Protagonist, Monk)
			# !ClassEx(Protagonist, Thief)
			if self.iClassEx("Protagonist", "Monk") \
				 and not self.iClassEx("Protagonist", "Thief"):
				return True # 1654: Indeed.  Scouting Targos unseen could prove useful to us - and detrimental to our foes.  Farewell.
			
		elif index == 11:
			# !ClassEx(Protagonist, Thief)
			# !ClassEx(Protagonist, Monk)
			# ClassEx(Protagonist, Ranger)
			if not self.iClassEx("Protagonist", "Thief") \
				 and not self.iClassEx("Protagonist", "Monk") \
				 and self.iClassEx("Protagonist", "Ranger"):
				return True # 1655: Not a bad idea.  Maybe a little scouting could prove useful.  Farewell.
			
		elif index == 12:
			# !ClassEx(Protagonist, Thief)
			# !ClassEx(Protagonist, Monk)
			# !ClassEx(Protagonist, Ranger)
			if not self.iClassEx("Protagonist", "Thief") \
				 and not self.iClassEx("Protagonist", "Monk") \
				 and not self.iClassEx("Protagonist", "Ranger"):
				return True # 1656: Thanks for the advice - stay here and watch the docks.  We'll return.
			
		elif index == 13:
			# Global("Reig_Quest", "GLOBAL", 1)
			# Global("Know_Magdar", "GLOBAL", 0)
			if self.iGlobal("'Reig_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Know_Magdar'", "'GLOBAL'", 0):
				return True # 1661: Do you know where I can find a man named Magdar Shenlen?  One of the soldiers by the docks has been wounded and is in need of a potion that Magdar is said to have.
			
		elif index == 14:
			# ClassEx(Protagonist, Thief)
			if self.iClassEx("Protagonist", "Thief"):
				return True # 1662: Hells, a sneak attack's worked for *me* on more than one occasion.  No reason not to use it now.  Farewell.
			
		elif index == 15:
			# ClassEx(Protagonist, Monk)
			if self.iClassEx("Protagonist", "Monk"):
				return True # 1663: A backstab is a thieves' trick - a monk has no need of such things.  Farewell.
			
		elif index == 16:
			# !ClassEx(Protagonist, Thief)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Thief") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 1664: Thanks for the advice - stay here and watch the docks.  We'll return.
			
		return False # dialog_test_do
	
	def dialog_action_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		if index == 0:
			# SetGlobal("Know_Crandall", "GLOBAL", 1)
			self.iSetGlobal("'Know_Crandall'", "'GLOBAL'", 1)
			# 1601: We stand with Targos.  We just sailed in on the Wicked Wench.
			
		elif index == 1:
			# SetGlobal("Know_Crandall", "GLOBAL", 1)
			self.iSetGlobal("'Know_Crandall'", "'GLOBAL'", 1)
			# 1602: Put down your damned weapon, boy, or we'll cleave it from your wrist.  It's plain we're not goblins.
			
		elif index == 2:
			# SetGlobal("Crandall_Leave", "GLOBAL", 1)
			self.iSetGlobal("'Crandall_Leave'", "'GLOBAL'", 1)
			# 1672: I will speak to him, then.  Farewell.
			
		elif index == 3:
			# SetGlobal("Crandall_Leave", "GLOBAL", 1)
			self.iSetGlobal("'Crandall_Leave'", "'GLOBAL'", 1)
			# 1681: I will speak to him, then.  Farewell.
			
		elif index == 4:
			# SetGlobal("Crandall_Leave", "GLOBAL", 1)
			self.iSetGlobal("'Crandall_Leave'", "'GLOBAL'", 1)
			# 1712: I will speak to him, then.  Farewell.
			
		return # dialog_action_do
		
	def get_dialog_trigger_max_index(self): return 16
	
	def get_state_to_line(self, state):
		if state==0: return 1600
		if state==1: return 1610
		if state==2: return 1620
		if state==3: return 1690
		if state==4: return 1630
		if state==5: return 1640
		if state==6: return 1670
		if state==7: return 1680
		if state==8: return 1700
		if state==9: return 1710
		if state==10: return 1650
		if state==11: return 1660
		return
	
