import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting
#### IMPORTS ####
from bcs import scr_12cwar2
from bcs import scr_12cwar0
#### END IMPORTS ####

#### GVARS ####
MODULE_SCRIPT_ID = 12011
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
class Ctrl_12SHAWFO_Auto(ctrl_behaviour_ie.CtrlBehaviourIE): # 12SHAWFO 
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN
	
	def setup_scripts(self, npc):
		super(Ctrl_12SHAWFO_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return
	
	def setup_appearance(self, npc):
		utils_npc.npc_description_set_new(npc, "Shawford Crale")
		
		npc.obj_set_int(toee.obj_f_critter_portrait, 8680) # none
		
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_light_brown # HairColourIndex: 5
		hairStyle.update_npc(npc)
		return
	
	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, [17, 16, 14, 13, 11, 14])
		
		# class levels: 6
		# stat_level_fighter: 6
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 4, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 5, toee.stat_level_fighter)
		
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_GOOD) # 0x11 LAWFUL_GOOD
		npc.obj_set_int(toee.obj_f_critter_experience, 270) # XPReward TODO!!!
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # CR: 5 TODO!!!
		
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
		# FeatWeaponProLargeSword: 2 => feat_martial_weapon_proficiency_longsword skip for fighter
		# FeatWeaponProPolearm: 1 => feat_martial_weapon_proficiency_halberd skip for fighter
		
		npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status
		
		# saves
		utils_npc.ensure_saves_natural(npc, 5, 2, 2) # SaveVsDeath: 5, SaveVsWands: 2, SaveVsPolymorph: 2
		
		# HP
		utils_npc.ensure_hp(npc, 28) # MaximumHP: 28
		npc.obj_set_int(toee.obj_f_hp_damage, 0) # CurrentHP: 28
		
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
		# SLOT_ARMOR: Chainmail Armor(ChainMail) from 00CHAN01
		# Not found! TODO ITEM
		
		# SLOT_WEAPON1: Longsword (LongsSwords) from 00SWDL01
		# Not found! TODO ITEM
		
		# SLOT_SHIELD1: Large Shield(MediumShield) from 00SHLD08
		# Not found! TODO ITEM
		
		# SLOT_QUICK1: Dagger(Daggers) from 00DAGG01
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_DAGGER, npc, no_loot = False, wear_on = None) # Dagger (00DAGG01) at SLOT_QUICK1 OK
		
		# SLOT_QUICK2: Potion of Healing(Potions) from 00POTN04
		utils_item.item_create_in_inventory2(const_proto_potions.PROTO_POTION_OF_CURE_LIGHT_WOUNDS, npc, no_loot = False, wear_on = None) # Potion of Healing (00POTN04) at SLOT_QUICK2 base! TODO ITEM
		
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_LEATHER_CLOTHING, npc, no_loot = True, wear_on = toee.item_wear_armor) # 
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc, no_loot = True, wear_on = toee.item_wear_boots)
		return
	
	def script_dialog(self, attachee, triggerer):
		print("script_dialog 12SHAWFO")
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		while True:
			print("STATE 0")
			# NumTimesTalkedTo(0)
			if self.iNumTimesTalkedTo(0):
				line_id = 10 # Ah, you must be the company from Luskan Ulbrec spoke of - I heard of your actions on the Docks, quite impressive.  Never again will I say nothing good ever comes from Luskan.
				print("STATE 0: line_id = 10")
				break
			
			print("STATE 9")
			# GlobalGT("Lumber_Quest", "GLOBAL", 0)
			# Global("Arrow_Quest", "GLOBAL", 0)
			if self.iGlobalGT("'Lumber_Quest'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Arrow_Quest'", "'GLOBAL'", 0):
				line_id = 100 # Have you spoken to Olap yet?
				print("STATE 9: line_id = 100")
				break
			
			print("STATE 16")
			# GlobalGT("Arrow_Quest", "GLOBAL", 0)
			# Global("Dead_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobalGT("'Arrow_Quest'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 0):
				line_id = 170 # Were you able to get Isherwood the arrows he needed?
				print("STATE 16: line_id = 170")
				break
			
			print("STATE 22")
			# GlobalGT("Dead_Goblin_Quest", "GLOBAL", 0)
			# Global("Palisade_Iron_Collar_Quest", "GLOBAL", 0)
			if self.iGlobalGT("'Dead_Goblin_Quest'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 0):
				line_id = 300 # Did you speak to Koluhm?
				print("STATE 22: line_id = 300")
				break
			
			print("STATE 32")
			# GlobalGT("Palisade_Iron_Collar_Quest", "GLOBAL", 0)
			# GlobalLT("Palisade_Iron_Collar_Quest", "GLOBAL", 3)
			if self.iGlobalGT("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 0) \
				 and self.iGlobalLT("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 3):
				line_id = 340 # Any luck on bringing the Iron Collar to the Palisade?
				print("STATE 32: line_id = 340")
				break
			
			print("STATE 33")
			# GlobalGT("Palisade_Iron_Collar_Quest", "GLOBAL", 2)
			# Global("Shawford_Has_No_Pants", "GLOBAL", 0)
			# Global("Shaengarne_Quest", "GLOBAL", 0)
			if self.iGlobalGT("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Shawford_Has_No_Pants'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Shaengarne_Quest'", "'GLOBAL'", 0):
				line_id = 360 # The goblins have been driven back - for the time being.  You've done well, and I have sent one of our runners to tell Lord Ulbrec of our victory... and your part in it.
				print("STATE 33: line_id = 360")
				break
			
			print("STATE 35")
			# GlobalGT("Palisade_Iron_Collar_Quest", "GLOBAL", 2)
			# Global("Shawford_Has_No_Pants", "GLOBAL", 1)
			# Global("Shaengarne_Quest", "GLOBAL", 0)
			if self.iGlobalGT("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Shawford_Has_No_Pants'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Shaengarne_Quest'", "'GLOBAL'", 0):
				line_id = 440 # Welcome back - no sign of any more goblins yet, but we're keeping a close eye out for them.  If you haven't already, you should check with Lord Ulbrec to see if he has any assignments for you.
				print("STATE 35: line_id = 440")
				break
			
			print("STATE 36")
			# Global("Shaengarne_Quest", "GLOBAL", 1)
			if self.iGlobal("'Shaengarne_Quest'", "'GLOBAL'", 1):
				line_id = 450 # I heard about your march upon the Shaengarne.  I wish you luck, and I pray the gods watch over you. 
				print("STATE 36: line_id = 450")
				break
			
			print("STATE 43")
			# GlobalGT("Shaengarne_Quest", "GLOBAL", 1)
			# Global("Shaengarne_Bridge_Cleared", "GLOBAL", 1)Global("31bugGut_Dead", "GLOBAL", 0)
			if self.iGlobalGT("'Shaengarne_Quest'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Shaengarne_Bridge_Cleared'", "'GLOBAL'", 1) \
				 and self.iGlobal("'31bugGut_Dead'", "'GLOBAL'", 0):
				line_id = 460 # I heard about your battle at the Shaengarne - it seems that Ulbrec and Oswald's plans proved true; a small force was more effective than all the Targos Guard.  A heroic feat, indeed.  
				print("STATE 43: line_id = 460")
				break
			
			print("STATE 44")
			# Global("31bugGut_Dead", "GLOBAL", 1)
			if self.iGlobal("'31bugGut_Dead'", "'GLOBAL'", 1):
				line_id = 470 # I heard about your battle at the fortress - your coming to Targos has truly been our salvation.  To think, you have carried the battle from Targos' walls to the walls of the horde itself, then slayed their leader within his own fortress.  Now *that* is a tale that won't be long forgotten.  
				print("STATE 44: line_id = 470")
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
		# 12SHAWFO
		
		if index == 0:
			# Global("10Swift_Dead", "GLOBAL", 0)
			if self.iGlobal("'10Swift_Dead'", "'GLOBAL'", 0):
				return True # 351: Did you hear that?
			
		elif index == 1:
			# Global("10Swift_Dead", "GLOBAL", 1)
			if self.iGlobal("'10Swift_Dead'", "'GLOBAL'", 1):
				return True # 352: Did you hear that?
			
		elif index == 2:
			# GlobalGT("Crane_Wheel", "GLOBAL", 0)
			# Global("Lumber_Quest_Aborted", "GLOBAL", 0)
			if self.iGlobalGT("'Crane_Wheel'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Lumber_Quest_Aborted'", "'GLOBAL'", 0):
				return True # 101: Yes.  We settled the matter of the wood shortage.
			
		elif index == 3:
			# Global("Lumber_Quest_Aborted", "GLOBAL", 1)
			if self.iGlobal("'Lumber_Quest_Aborted'", "'GLOBAL'", 1):
				return True # 102: The problem cannot be solved.  The only one who could fix the crane to get the lumber to the Palisade is dead.
			
		elif index == 4:
			# Global("Know_Olap", "GLOBAL", 0)
			if self.iGlobal("'Know_Olap'", "'GLOBAL'", 0):
				return True # 103: Where can he be found again?
			
		elif index == 5:
			# Global("Crane_Wheel", "GLOBAL", 0)
			# Global("Lumber_Quest_Aborted", "GLOBAL", 0)
			if self.iGlobal("'Crane_Wheel'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Lumber_Quest_Aborted'", "'GLOBAL'", 0):
				return True # 104: We're still working on the matter.  We shall return.
			
		elif index == 6:
			# Global("Arrow_Quest", "GLOBAL", 1)
			if self.iGlobal("'Arrow_Quest'", "'GLOBAL'", 1):
				return True # 171: Not yet.  Where can I find Isherwood again?
			
		elif index == 7:
			# Global("Arrow_Quest", "GLOBAL", 3)
			if self.iGlobal("'Arrow_Quest'", "'GLOBAL'", 3):
				return True # 172: Yes, we came to an... arrangement with Deirdre Gallaway.  Isherwood has the arrows he needs.
			
		elif index == 8:
			# Global("Arrow_Quest", "GLOBAL", 4)
			if self.iGlobal("'Arrow_Quest'", "'GLOBAL'", 4):
				return True # 173: We got Isherwood the arrows he needed - and made some room in our backpack in the process.
			
		elif index == 9:
			# GlobalLT("Arrow_Quest", "GLOBAL", 3)
			if self.iGlobalLT("'Arrow_Quest'", "'GLOBAL'", 3):
				return True # 174: We're still working on it - we'll return when it's done.
			
		elif index == 10:
			# !Global("Koluhm_Dead", "GLOBAL", 1)
			# Global("Know_Koluhm", "GLOBAL", 0)
			if not self.iGlobal("'Koluhm_Dead'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Know_Koluhm'", "'GLOBAL'", 0):
				return True # 191: He speaks to the dead?
			
		elif index == 11:
			# !Global("Koluhm_Dead", "GLOBAL", 1)
			# GlobalGT("Know_Koluhm", "GLOBAL", 0)
			if not self.iGlobal("'Koluhm_Dead'", "'GLOBAL'", 1) \
				 and self.iGlobalGT("'Know_Koluhm'", "'GLOBAL'", 0):
				return True # 192: Koluhm?  I know of him.
			
		elif index == 12:
			# Global("Koluhm_Dead", "GLOBAL", 1)
			if self.iGlobal("'Koluhm_Dead'", "'GLOBAL'", 1):
				return True # 193: Oh, Koluhm?  Yeah, that priest accidentally fell on my... er, someone's weapon and died.
			
		elif index == 13:
			# Global("Koluhm_Dead", "GLOBAL", 1)
			if self.iGlobal("'Koluhm_Dead'", "'GLOBAL'", 1):
				return True # 194: Uh, I think Koluhm had an accident, at least that's what the rumors say.  Probably caught some fast-catching graverot or something.
			
		elif index == 14:
			# Global("Know_Koluhm", "GLOBAL", 0)
			if self.iGlobal("'Know_Koluhm'", "'GLOBAL'", 0):
				return True # 211: Very well.  Where can I find him?
			
		elif index == 15:
			# Global("Know_Koluhm", "GLOBAL", 1)
			if self.iGlobal("'Know_Koluhm'", "'GLOBAL'", 1):
				return True # 212: I'll go hunt down Koluhm, then.
			
		elif index == 16:
			# Global("Koluhm_Dead", "GLOBAL", 1)
			# GlobalLT("Dead_Goblin_Quest", "GLOBAL", 2)
			if self.iGlobal("'Koluhm_Dead'", "'GLOBAL'", 1) \
				 and self.iGlobalLT("'Dead_Goblin_Quest'", "'GLOBAL'", 2):
				return True # 301: Oh, Koluhm?  He accidentally fell on my... er, someone's weapon and died.
			
		elif index == 17:
			# Global("Koluhm_Dead", "GLOBAL", 1)
			# GlobalLT("Dead_Goblin_Quest", "GLOBAL", 2)
			if self.iGlobal("'Koluhm_Dead'", "'GLOBAL'", 1) \
				 and self.iGlobalLT("'Dead_Goblin_Quest'", "'GLOBAL'", 2):
				return True # 302: Uh, I think Koluhm had an accident, at least that's what the rumors say.  Probably caught some fast-catching graverot or something.
			
		elif index == 18:
			# Global("Dead_Goblin_Quest", "GLOBAL", 2)
			if self.iGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 2):
				return True # 303: Yes, he can't speak goblin, so he's sending a scroll with the goblin's "answers" up to the Palisade.  You should expect it soon.
			
		elif index == 19:
			# Global("Dead_Goblin_Quest", "GLOBAL", 5)
			if self.iGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 5):
				return True # 304: Yes, we spoke to him and were able to translate some of the goblin's speech.  Apparently the tribe that attacked Targos is only *one* of the tribes in the region.  They're led by someone named "Caballus," which sounds like some goblin sorcerer.  I'd tell your archers to aim for any goblin sorcerer they can see.
			
		elif index == 20:
			# Global("Dead_Goblin_Quest", "GLOBAL", 4)
			if self.iGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 4):
				return True # 305: Yes, we spoke to him and were able to translate some of the goblin's speech.  Apparently the tribe that attacked Targos is only *one* of the tribes in the region.  They seem to be led by three different leaders, one of them named "Caballus," which sounds like a goblin sorcerer.
			
		elif index == 21:
			# Global("Dead_Goblin_Quest", "GLOBAL", 3)
			if self.iGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 3):
				return True # 306: I'm glad the Palisade is still standing - we spoke to Koluhm and were able to translate the goblin's speech.  It sounds like they intended to do a simultaneous attack on the Palisade and the Docks, which means that we could be attacked at any time.
			
		elif index == 22:
			# Global("Dead_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 1):
				return True # 307: Not yet.  We'll go speak to him soon.
			
		elif index == 23:
			# Global("Know_Iron_Collar", "GLOBAL", 0)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 321: No, I haven't heard of them.
			
		elif index == 24:
			# Global("Know_Iron_Collar", "GLOBAL", 1)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 322: I've... met them, yes.  They were deep into their cups in the Salty Dog.
			
		elif index == 25:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			# Global("Koluhm_Dead", "GLOBAL", 1)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Koluhm_Dead'", "'GLOBAL'", 1):
				return True # 323: Actually, I think Black Geoffrey died in the goblin attacks on the docks... the same attack that claimed poor Koluhm's life.
			
		elif index == 26:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			# Global("Koluhm_Dead", "GLOBAL", 0)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Koluhm_Dead'", "'GLOBAL'", 0):
				return True # 324: Actually, I heard Black Geoffrey died in the goblin attacks on the docks... but I'm just guessing.
			
		elif index == 27:
			# Global("Know_Iron_Collar", "GLOBAL", 0)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 311: No, I haven't heard of them.
			
		elif index == 28:
			# Global("Know_Iron_Collar", "GLOBAL", 1)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 312: I've... met them, yes.  They were deep into their cups in the Salty Dog.
			
		elif index == 29:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			# Global("Koluhm_Dead", "GLOBAL", 1)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Koluhm_Dead'", "'GLOBAL'", 1):
				return True # 313: Actually, I think Black Geoffrey died in the goblin attacks on the docks... the same attack that claimed poor Koluhm's life.
			
		elif index == 30:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			# Global("Koluhm_Dead", "GLOBAL", 0)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Koluhm_Dead'", "'GLOBAL'", 0):
				return True # 314: Actually, I heard Black Geoffrey died in the goblin attacks on the docks... but I'm just guessing.
			
		elif index == 31:
			# Global("Know_Iron_Collar", "GLOBAL", 0)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 231: No, I haven't heard of them.
			
		elif index == 32:
			# Global("Know_Iron_Collar", "GLOBAL", 1)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Know_Iron_Collar'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 232: I've... met them, yes.  They were deep into their cups in the Salty Dog.
			
		elif index == 33:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			# Global("Koluhm_Dead", "GLOBAL", 1)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Koluhm_Dead'", "'GLOBAL'", 1):
				return True # 233: Actually, I think Black Geoffrey died in the goblin attacks on the docks... the same attack that claimed poor Koluhm's life.
			
		elif index == 34:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			# Global("Koluhm_Dead", "GLOBAL", 0)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1) \
				 and self.iGlobal("'Koluhm_Dead'", "'GLOBAL'", 0):
				return True # 234: Actually, I heard Black Geoffrey died in the goblin attacks on the docks... but I'm just guessing.
			
		elif index == 35:
			# Global("10Swift_Dead", "GLOBAL", 0)
			if self.iGlobal("'10Swift_Dead'", "'GLOBAL'", 0):
				return True # 291: Did you hear that?
			
		elif index == 36:
			# Global("10Swift_Dead", "GLOBAL", 1)
			if self.iGlobal("'10Swift_Dead'", "'GLOBAL'", 1):
				return True # 292: Did you hear that?
			
		elif index == 37:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1):
				return True # 341: No, they were too deep in their cups to listen to reason, so I was forced to deal with them.  
			
		elif index == 38:
			# Global("Palisade_Iron_Collar_Quest", "GLOBAL", 2)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 1)
			if self.iGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 1):
				return True # 342: Well, at first it seemed as if they would be coming along peacefully, but then I heard one of them say something... I can't quite remember what... and so we were forced to kill them all.  I'm sure it was all just a misunderstanding.
			
		elif index == 39:
			# Global("Palisade_Iron_Collar_Quest", "GLOBAL", 2)
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			if self.iGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 2) \
				 and self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0):
				return True # 343: Yes - though they proved to be a stubborn bunch.  I don't know how well they'll serve, but they may stop a few goblin axes. 
			
		elif index == 40:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			# GlobalLT("Palisade_Iron_Collar_Quest", "GLOBAL", 2)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0) \
				 and self.iGlobalLT("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 2):
				return True # 344: Where can they be found again?
			
		elif index == 41:
			# Global("Black_Geoffrey_Dead", "GLOBAL", 0)
			# GlobalLT("Palisade_Iron_Collar_Quest", "GLOBAL", 2)
			if self.iGlobal("'Black_Geoffrey_Dead'", "'GLOBAL'", 0) \
				 and self.iGlobalLT("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 2):
				return True # 345: Not yet.  We're still working on it.  We'll return when we've dealt with them.
			
		elif index == 42:
			# Global("S_R_1", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 371: Actually, we came for our payment.  We're not here for our health, Shawford, we're here to earn some coin. 
			
		elif index == 43:
			# Global("S_R_1", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 372: We came to receive payment for the fighting at the Palisade, Shawford.  It was not an easy battle. 
			
		elif index == 44:
			# Global("S_R_1", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 441: Actually, we came for our payment.  We're not here for our health, Shawford, we're here to earn some coin. 
			
		elif index == 45:
			# Global("S_R_1", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 442: We came to receive payment for the fighting at the Palisade, Shawford.  It was not an easy battle. 
			
		elif index == 46:
			# Global("S_R_1", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 451: Actually, we came more for payment than prayer.  We're not here for our health, Shawford, we're here to earn some coin. 
			
		elif index == 47:
			# Global("S_R_1", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 452: We came to receive payment for the fighting at the Palisade, Shawford.  It was not an easy battle. 
			
		elif index == 48:
			# Global("SC_Speech", "GLOBAL", 0)
			if self.iGlobal("'SC_Speech'", "'GLOBAL'", 0):
				return True # 381: Good.  And watch that tone of yours - we didn't travel here from Luskan and past Bremen in flames just to defend your town - we're risking our *lives* here, and the payment should reflect it. 
			
		elif index == 49:
			# Global("SC_Speech", "GLOBAL", 1)
			if self.iGlobal("'SC_Speech'", "'GLOBAL'", 1):
				return True # 382: Good.  And watch that tone of yours - we didn't travel here from Luskan and past Bremen in flames just to defend your town - we're risking our *lives* here, and the payment should reflect it. 
			
		elif index == 50:
			# Global("SC_Speech", "GLOBAL", 0)
			if self.iGlobal("'SC_Speech'", "'GLOBAL'", 0):
				return True # 383: This'll do, then.  Farewell. 
			
		elif index == 51:
			# Global("SC_Speech", "GLOBAL", 1)
			if self.iGlobal("'SC_Speech'", "'GLOBAL'", 1):
				return True # 384: This'll do, then.  Farewell. 
			
		elif index == 52:
			# Global("S_R_1", "GLOBAL", 1)
			# Global("S_R_2", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 1) \
				 and self.iGlobal("'S_R_2'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 461: It was a suicide mission, and we expect to be rewarded accordingly.  We're here for gold, Shawford, not compliments. 
			
		elif index == 53:
			# Global("S_R_1", "GLOBAL", 0)
			# Global("S_R_2", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 0) \
				 and self.iGlobal("'S_R_2'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 462: It was a suicide mission, and we expect to be rewarded accordingly, both for Shaengarne and the Palisade battle.  We're here for gold, Shawford, not compliments. 
			
		elif index == 54:
			# Global("S_R_1", "GLOBAL", 1)
			# Global("S_R_2", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 1) \
				 and self.iGlobal("'S_R_2'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 463: We came for payment for our battle at the Shaengarne, Shawford.  
			
		elif index == 55:
			# Global("S_R_1", "GLOBAL", 0)
			# Global("S_R_2", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 0) \
				 and self.iGlobal("'S_R_2'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 464: We came for payment for our battle at the Shaengarne, Shawford... and for our battle at the Palisade.   
			
		elif index == 56:
			# Global("S_R_1", "GLOBAL", 0)
			# Global("S_R_2", "GLOBAL", 0)
			# Global("S_R_3", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 0) \
				 and self.iGlobal("'S_R_2'", "'GLOBAL'", 0) \
				 and self.iGlobal("'S_R_3'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 471: I consider it Ulbrec's attempt to keep from paying us our due.  We're here for all the gold owed us, Shawford, not words. 
			
		elif index == 57:
			# Global("S_R_1", "GLOBAL", 1)
			# Global("S_R_2", "GLOBAL", 0)
			# Global("S_R_3", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 1) \
				 and self.iGlobal("'S_R_2'", "'GLOBAL'", 0) \
				 and self.iGlobal("'S_R_3'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 472: I consider it Ulbrec's attempt to keep from paying us our due.  We're here for all the gold owed us, Shawford, not words. 
			
		elif index == 58:
			# Global("S_R_1", "GLOBAL", 1)
			# Global("S_R_2", "GLOBAL", 1)
			# Global("S_R_3", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 1) \
				 and self.iGlobal("'S_R_2'", "'GLOBAL'", 1) \
				 and self.iGlobal("'S_R_3'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 473: I consider it Ulbrec's attempt to keep from paying us our due.  We're here for all the gold owed us, Shawford, not words. 
			
		elif index == 59:
			# Global("S_R_1", "GLOBAL", 0)
			# Global("S_R_2", "GLOBAL", 0)
			# Global("S_R_3", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 0) \
				 and self.iGlobal("'S_R_2'", "'GLOBAL'", 0) \
				 and self.iGlobal("'S_R_3'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 474: We came for payment for our battle at the fortress, Shawford... and any of the other missions you have yet to pay us for.   
			
		elif index == 60:
			# Global("S_R_1", "GLOBAL", 1)
			# Global("S_R_2", "GLOBAL", 0)
			# Global("S_R_3", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 1) \
				 and self.iGlobal("'S_R_2'", "'GLOBAL'", 0) \
				 and self.iGlobal("'S_R_3'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 475: We came for payment for our battle at the fortress, Shawford... and any of the other missions you have yet to pay us for.   
			
		elif index == 61:
			# Global("S_R_1", "GLOBAL", 1)
			# Global("S_R_2", "GLOBAL", 1)
			# Global("S_R_3", "GLOBAL", 0)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'S_R_1'", "'GLOBAL'", 1) \
				 and self.iGlobal("'S_R_2'", "'GLOBAL'", 1) \
				 and self.iGlobal("'S_R_3'", "'GLOBAL'", 0) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 476: We came for payment for our battle at the fortress, Shawford... and any of the other missions you have yet to pay us for.   
			
		return False # dialog_test_do
	
	def dialog_action_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		if index == 0:
			# GiveItemCreate("Misc07", Protagonist, 250, 0, 0)
			utils_pc.pc_party_receive_money_and_print(250 * const_toee.gp)
			# 12: We were told that you were the watch commander... and the paymaster.
			
		elif index == 1:
			# GiveItemCreate("Misc07", Protagonist, 250, 0, 0)
			utils_pc.pc_party_receive_money_and_print(250 * const_toee.gp)
			# 21: Continue
			
		elif index == 2:
			# SetGlobal("Goblins_Attack_Palisade", "GLOBAL", 1)
			self.iSetGlobal("'Goblins_Attack_Palisade'", "'GLOBAL'", 1)
			# StartCutSceneMode()
			self.iStartCutSceneMode()
			# StartCutScene("12cWar2")
			self.iStartCutScenePost(scr_12cwar2.Script_12cWar2)
			# 351: Did you hear that?
			
		elif index == 3:
			# SetGlobal("Goblins_Attack_Palisade", "GLOBAL", 1)
			self.iSetGlobal("'Goblins_Attack_Palisade'", "'GLOBAL'", 1)
			# StartCutSceneMode()
			self.iStartCutSceneMode()
			# StartCutScene("12cWar0")
			self.iStartCutScenePost(scr_12cwar0.Script_12cWar0)
			# 352: Did you hear that?
			
		elif index == 4:
			# SetGlobal("Lumber_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Lumber_Quest'", "'GLOBAL'", 1)
			# 91: Very well.  We will go find Olap, then.
			
		elif index == 5:
			# AddXpVar("Level_2_Average",10785)
			self.iAddXpVar("'Level_2_Average'", 10785)
			# 101: Yes.  We settled the matter of the wood shortage.
			
		elif index == 6:
			# AddXpVar("Level_2_Easy",10794)
			self.iAddXpVar("'Level_2_Easy'", 10794)
			# 102: The problem cannot be solved.  The only one who could fix the crane to get the lumber to the Palisade is dead.
			
		elif index == 7:
			# SetGlobal("Arrow_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Arrow_Quest'", "'GLOBAL'", 1)
			# 121: Continue
			
		elif index == 8:
			# AddXpVar("Level_2_Average",10785)
			self.iAddXpVar("'Level_2_Average'", 10785)
			# 172: Yes, we came to an... arrangement with Deirdre Gallaway.  Isherwood has the arrows he needs.
			
		elif index == 9:
			# AddXpVar("Level_2_Average",10785)
			self.iAddXpVar("'Level_2_Average'", 10785)
			# 173: We got Isherwood the arrows he needed - and made some room in our backpack in the process.
			
		elif index == 10:
			# SetGlobal("Dead_Goblin_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 1)
			# 191: He speaks to the dead?
			
		elif index == 11:
			# SetGlobal("Dead_Goblin_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 1)
			# 192: Koluhm?  I know of him.
			
		elif index == 12:
			# SetGlobal("Dead_Goblin_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 1)
			# 193: Oh, Koluhm?  Yeah, that priest accidentally fell on my... er, someone's weapon and died.
			
		elif index == 13:
			# SetGlobal("Dead_Goblin_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 1)
			# 194: Uh, I think Koluhm had an accident, at least that's what the rumors say.  Probably caught some fast-catching graverot or something.
			
		elif index == 14:
			# AddXpVar("Level_2_Easy",10785)
			self.iAddXpVar("'Level_2_Easy'", 10785)
			# SetGlobal("Dead_Goblin_Quest", "GLOBAL", 6)
			self.iSetGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 6)
			# 303: Yes, he can't speak goblin, so he's sending a scroll with the goblin's "answers" up to the Palisade.  You should expect it soon.
			
		elif index == 15:
			# AddXpVar("Level_2_Easy",10785)
			self.iAddXpVar("'Level_2_Easy'", 10785)
			# SetGlobal("Dead_Goblin_Quest", "GLOBAL", 6)
			self.iSetGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 6)
			# 304: Yes, we spoke to him and were able to translate some of the goblin's speech.  Apparently the tribe that attacked Targos is only *one* of the tribes in the region.  They're led by someone named "Caballus," which sounds like some goblin sorcerer.  I'd tell your archers to aim for any goblin sorcerer they can see.
			
		elif index == 16:
			# AddXpVar("Level_2_Average",10785)
			self.iAddXpVar("'Level_2_Average'", 10785)
			# SetGlobal("Dead_Goblin_Quest", "GLOBAL", 6)
			self.iSetGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 6)
			# 305: Yes, we spoke to him and were able to translate some of the goblin's speech.  Apparently the tribe that attacked Targos is only *one* of the tribes in the region.  They seem to be led by three different leaders, one of them named "Caballus," which sounds like a goblin sorcerer.
			
		elif index == 17:
			# AddXpVar("Level_2_Hard",10795)
			self.iAddXpVar("'Level_2_Hard'", 10795)
			# SetGlobal("Dead_Goblin_Quest", "GLOBAL", 6)
			self.iSetGlobal("'Dead_Goblin_Quest'", "'GLOBAL'", 6)
			# 331: That's not all.  They should expect a three-pronged assault, one from a sorcerer named "Caballus," and two others - uh, "Ghotrag" and "Vgh..." er, "Houndstooth," or something.
			
		elif index == 18:
			# SetGlobal("Palisade_Iron_Collar_Quest", "GLOBAL", 3)
			self.iSetGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 3)
			# 323: Actually, I think Black Geoffrey died in the goblin attacks on the docks... the same attack that claimed poor Koluhm's life.
			
		elif index == 19:
			# SetGlobal("Palisade_Iron_Collar_Quest", "GLOBAL", 3)
			self.iSetGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 3)
			# 324: Actually, I heard Black Geoffrey died in the goblin attacks on the docks... but I'm just guessing.
			
		elif index == 20:
			# SetGlobal("Palisade_Iron_Collar_Quest", "GLOBAL", 3)
			self.iSetGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 3)
			# 313: Actually, I think Black Geoffrey died in the goblin attacks on the docks... the same attack that claimed poor Koluhm's life.
			
		elif index == 21:
			# SetGlobal("Palisade_Iron_Collar_Quest", "GLOBAL", 3)
			self.iSetGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 3)
			# 314: Actually, I heard Black Geoffrey died in the goblin attacks on the docks... but I'm just guessing.
			
		elif index == 22:
			# SetGlobal("Palisade_Iron_Collar_Quest", "GLOBAL", 3)
			self.iSetGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 3)
			# 233: Actually, I think Black Geoffrey died in the goblin attacks on the docks... the same attack that claimed poor Koluhm's life.
			
		elif index == 23:
			# SetGlobal("Palisade_Iron_Collar_Quest", "GLOBAL", 3)
			self.iSetGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 3)
			# 234: Actually, I heard Black Geoffrey died in the goblin attacks on the docks... but I'm just guessing.
			
		elif index == 24:
			# SetGlobal("Palisade_Iron_Collar_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 1)
			# 261: Where can I find them?
			
		elif index == 25:
			# SetGlobal("Palisade_Iron_Collar_Quest", "GLOBAL", 1)
			self.iSetGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 1)
			# 262: I'm on it.  I'll return with them... or without them... shortly.
			
		elif index == 26:
			# SetGlobal("Goblins_Attack_Palisade", "GLOBAL", 1)
			self.iSetGlobal("'Goblins_Attack_Palisade'", "'GLOBAL'", 1)
			# StartCutSceneMode()
			self.iStartCutSceneMode()
			# StartCutScene("12cWar2")
			self.iStartCutScenePost(scr_12cwar2.Script_12cWar2)
			# 291: Did you hear that?
			
		elif index == 27:
			# SetGlobal("Goblins_Attack_Palisade", "GLOBAL", 1)
			self.iSetGlobal("'Goblins_Attack_Palisade'", "'GLOBAL'", 1)
			# StartCutSceneMode()
			self.iStartCutSceneMode()
			# StartCutScene("12cWar0")
			self.iStartCutScenePost(scr_12cwar0.Script_12cWar0)
			# 292: Did you hear that?
			
		elif index == 28:
			# AddXpVar("Level_2_Average",10785)
			self.iAddXpVar("'Level_2_Average'", 10785)
			# SetGlobal("Palisade_Iron_Collar_Quest", "GLOBAL", 4)
			self.iSetGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 4)
			# 341: No, they were too deep in their cups to listen to reason, so I was forced to deal with them.  
			
		elif index == 29:
			# AddXpVar("Level_2_Average",10785)
			self.iAddXpVar("'Level_2_Average'", 10785)
			# SetGlobal("Palisade_Iron_Collar_Quest", "GLOBAL", 3)
			self.iSetGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 3)
			# 342: Well, at first it seemed as if they would be coming along peacefully, but then I heard one of them say something... I can't quite remember what... and so we were forced to kill them all.  I'm sure it was all just a misunderstanding.
			
		elif index == 30:
			# AddXpVar("Level_2_Hard",10796)
			self.iAddXpVar("'Level_2_Hard'", 10796)
			# SetGlobal("Palisade_Iron_Collar_Quest", "GLOBAL", 3)
			self.iSetGlobal("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 3)
			# SetGlobal("IC_Good", "GLOBAL", 1)
			self.iSetGlobal("'IC_Good'", "'GLOBAL'", 1)
			# 343: Yes - though they proved to be a stubborn bunch.  I don't know how well they'll serve, but they may stop a few goblin axes. 
			
		elif index == 31:
			# SetGlobal("S_R_1", "GLOBAL", 1)
			self.iSetGlobal("'S_R_1'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 1000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(1000 * const_toee.gp)
			# 371: Actually, we came for our payment.  We're not here for our health, Shawford, we're here to earn some coin. 
			
		elif index == 32:
			# SetGlobal("S_R_1", "GLOBAL", 1)
			self.iSetGlobal("'S_R_1'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 1000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(1000 * const_toee.gp)
			# 372: We came to receive payment for the fighting at the Palisade, Shawford.  It was not an easy battle. 
			
		elif index == 33:
			# SetGlobal("Shawford_Has_No_Pants", "GLOBAL", 1)
			self.iSetGlobal("'Shawford_Has_No_Pants'", "'GLOBAL'", 1)
			# 373: I will seek him out, then.  Farewell.
			
		elif index == 34:
			# SetGlobal("S_R_1", "GLOBAL", 1)
			self.iSetGlobal("'S_R_1'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 1000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(1000 * const_toee.gp)
			# 441: Actually, we came for our payment.  We're not here for our health, Shawford, we're here to earn some coin. 
			
		elif index == 35:
			# SetGlobal("S_R_1", "GLOBAL", 1)
			self.iSetGlobal("'S_R_1'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 1000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(1000 * const_toee.gp)
			# 442: We came to receive payment for the fighting at the Palisade, Shawford.  It was not an easy battle. 
			
		elif index == 36:
			# SetGlobal("S_R_1", "GLOBAL", 1)
			self.iSetGlobal("'S_R_1'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 1000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(1000 * const_toee.gp)
			# 451: Actually, we came more for payment than prayer.  We're not here for our health, Shawford, we're here to earn some coin. 
			
		elif index == 37:
			# SetGlobal("S_R_1", "GLOBAL", 1)
			self.iSetGlobal("'S_R_1'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 1000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(1000 * const_toee.gp)
			# 452: We came to receive payment for the fighting at the Palisade, Shawford.  It was not an easy battle. 
			
		elif index == 38:
			# SetGlobal("SC_Speech", "GLOBAL", 1)
			self.iSetGlobal("'SC_Speech'", "'GLOBAL'", 1)
			# 381: Good.  And watch that tone of yours - we didn't travel here from Luskan and past Bremen in flames just to defend your town - we're risking our *lives* here, and the payment should reflect it. 
			
		elif index == 39:
			# SetGlobal("SC_Speech", "GLOBAL", 1)
			self.iSetGlobal("'SC_Speech'", "'GLOBAL'", 1)
			# 383: This'll do, then.  Farewell. 
			
		elif index == 40:
			# SetGlobal("S_R_2", "GLOBAL", 1)
			self.iSetGlobal("'S_R_2'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 3000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(3000 * const_toee.gp)
			# 461: It was a suicide mission, and we expect to be rewarded accordingly.  We're here for gold, Shawford, not compliments. 
			
		elif index == 41:
			# SetGlobal("S_R_1", "GLOBAL", 1)
			self.iSetGlobal("'S_R_1'", "'GLOBAL'", 1)
			# SetGlobal("S_R_2", "GLOBAL", 1)
			self.iSetGlobal("'S_R_2'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 4000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(4000 * const_toee.gp)
			# 462: It was a suicide mission, and we expect to be rewarded accordingly, both for Shaengarne and the Palisade battle.  We're here for gold, Shawford, not compliments. 
			
		elif index == 42:
			# SetGlobal("S_R_2", "GLOBAL", 1)
			self.iSetGlobal("'S_R_2'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 3000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(3000 * const_toee.gp)
			# 463: We came for payment for our battle at the Shaengarne, Shawford.  
			
		elif index == 43:
			# SetGlobal("S_R_1", "GLOBAL", 1)
			self.iSetGlobal("'S_R_1'", "'GLOBAL'", 1)
			# SetGlobal("S_R_2", "GLOBAL", 1)
			self.iSetGlobal("'S_R_2'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 4000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(4000 * const_toee.gp)
			# 464: We came for payment for our battle at the Shaengarne, Shawford... and for our battle at the Palisade.   
			
		elif index == 44:
			# SetGlobal("S_R_1", "GLOBAL", 1)
			self.iSetGlobal("'S_R_1'", "'GLOBAL'", 1)
			#  SetGlobal("S_R_2", "GLOBAL", 1)
			self.iSetGlobal("'S_R_2'", "'GLOBAL'", 1)
			# SetGlobal("S_R_3", "GLOBAL", 1)
			self.iSetGlobal("'S_R_3'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 10000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(10000 * const_toee.gp)
			# 471: I consider it Ulbrec's attempt to keep from paying us our due.  We're here for all the gold owed us, Shawford, not words. 
			
		elif index == 45:
			# SetGlobal("S_R_2", "GLOBAL", 1)
			self.iSetGlobal("'S_R_2'", "'GLOBAL'", 1)
			# SetGlobal("S_R_3", "GLOBAL", 1)
			self.iSetGlobal("'S_R_3'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 9000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(9000 * const_toee.gp)
			# 472: I consider it Ulbrec's attempt to keep from paying us our due.  We're here for all the gold owed us, Shawford, not words. 
			
		elif index == 46:
			# SetGlobal("S_R_3", "GLOBAL", 1)
			self.iSetGlobal("'S_R_3'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 6000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(6000 * const_toee.gp)
			# 473: I consider it Ulbrec's attempt to keep from paying us our due.  We're here for all the gold owed us, Shawford, not words. 
			
		elif index == 47:
			# SetGlobal("S_R_1", "GLOBAL", 1)
			self.iSetGlobal("'S_R_1'", "'GLOBAL'", 1)
			#  SetGlobal("S_R_2", "GLOBAL", 1)
			self.iSetGlobal("'S_R_2'", "'GLOBAL'", 1)
			# SetGlobal("S_R_3", "GLOBAL", 1)
			self.iSetGlobal("'S_R_3'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 10000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(10000 * const_toee.gp)
			# 474: We came for payment for our battle at the fortress, Shawford... and any of the other missions you have yet to pay us for.   
			
		elif index == 48:
			# SetGlobal("S_R_2", "GLOBAL", 1)
			self.iSetGlobal("'S_R_2'", "'GLOBAL'", 1)
			# SetGlobal("S_R_3", "GLOBAL", 1)
			self.iSetGlobal("'S_R_3'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 9000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(9000 * const_toee.gp)
			# 475: We came for payment for our battle at the fortress, Shawford... and any of the other missions you have yet to pay us for.   
			
		elif index == 49:
			# SetGlobal("S_R_3", "GLOBAL", 1)
			self.iSetGlobal("'S_R_3'", "'GLOBAL'", 1)
			# GiveItemCreate("Misc07", Protagonist, 6000, 0, 0)
			utils_pc.pc_party_receive_money_and_print(6000 * const_toee.gp)
			# 476: We came for payment for our battle at the fortress, Shawford... and any of the other missions you have yet to pay us for.   
			
		return # dialog_action_do
		
	def get_dialog_trigger_max_index(self): return 61
	
	def get_state_to_line(self, state):
		if state==0: return 10
		if state==1: return 20
		if state==2: return 30
		if state==3: return 350
		if state==4: return 40
		if state==5: return 60
		if state==6: return 70
		if state==7: return 80
		if state==8: return 90
		if state==9: return 100
		if state==10: return 160
		if state==11: return 150
		if state==12: return 110
		if state==13: return 120
		if state==14: return 130
		if state==15: return 140
		if state==16: return 170
		if state==17: return 180
		if state==18: return 190
		if state==19: return 200
		if state==20: return 210
		if state==21: return 220
		if state==22: return 300
		if state==23: return 330
		if state==24: return 320
		if state==25: return 310
		if state==26: return 230
		if state==27: return 240
		if state==28: return 250
		if state==29: return 260
		if state==30: return 270
		if state==31: return 290
		if state==32: return 340
		if state==33: return 360
		if state==34: return 370
		if state==35: return 440
		if state==36: return 450
		if state==37: return 380
		if state==38: return 390
		if state==39: return 400
		if state==40: return 410
		if state==41: return 420
		if state==42: return 430
		if state==43: return 460
		if state==44: return 470
		if state==45: return 280
		if state==46: return 50
		return
	
