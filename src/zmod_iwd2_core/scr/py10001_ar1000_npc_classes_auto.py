import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2
import utils_journal as uj, inf_scripting
#### IMPORT ####
#### IMPORT END ####


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
		base(self, Ctrl_10HEDRON_Auto).setup_scripts(npc)
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
		
