import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py06615_daemon_orc_fort, py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, py14764_npc_portal, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie

MODULE_SCRIPT_ID = 1001

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

class Ctrl10HEDRON(ctrl_behaviour_ie.CtrlBehaviourIE): # 10HEDRON 
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
			if self.iGlobalGT("Reig_Quest", "GLOBAL", 0) \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 0) \
				 and self.iGlobal("Hedron_Know_Attack", "GLOBAL", 0):
				line_id = 230 # I was hoping ye might come back - what's the word from the docks?  Not even Magdar's come out to shake me down yet, and he usually sends some half-drunk stumblers to help unload my supplies.
				print("STATE 21: line_id = 230")
				break
			
			print("STATE 30")
			# GlobalGT("Reig_Quest", "GLOBAL", 0)
			# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
			if self.iGlobalGT("Reig_Quest", "GLOBAL", 0) \
				 and self.iGlobalLT("Hedron_Know_Attack", "GLOBAL", 2):
				line_id = 330 # What's going on along the shore?  I heard something about an attack on the docks, but no one can tell me anything for certain.
				print("STATE 30: line_id = 330")
				break
			
			print("STATE 33")
			# GlobalGT("Hedron_Know_Attack", "GLOBAL", 0)
			# GlobalGT("Hedron_Quest", "GLOBAL", 0)
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			if self.iGlobalGT("Hedron_Know_Attack", "GLOBAL", 0) \
				 and self.iGlobalGT("Hedron_Quest", "GLOBAL", 0) \
				 and self.iGlobalLT("Hedron_Quest", "GLOBAL", 4):
				line_id = 390 # You're back - any word of me Ma?
				print("STATE 33: line_id = 390")
				break
			
			print("STATE 34")
			# NumTimesTalkedToGT(0)
			# Global("Reig_Quest", "GLOBAL", 0)
			if self.iNumTimesTalkedToGT(0) \
				 and self.iGlobal("Reig_Quest", "GLOBAL", 0):
				line_id = 400 # Aye, look who's come back aboard - sick of Targos already, are ye?
				print("STATE 34: line_id = 400")
				break
			
			print("STATE 38")
			# Global("Hedron_Know_Attack", "GLOBAL", 2)
			if self.iGlobal("Hedron_Know_Attack", "GLOBAL", 2):
				line_id = 420 # Aye, look who's come back aboard - the great goblin slayers of Targos.  What can I do for ye?
				print("STATE 38: line_id = 420")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		if index == 0:
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 156: Mostly decent folk?
			
		elif index == 1:
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 4):
				return True # 171: If your mother lives in Targos, why are you staying on the ship?
			
		elif index == 3:
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 191: You named your ship after your mother?
			
		elif index == 4:
			# GlobalGT("Know_Hedron", "GLOBAL", 0)
			if self.iGlobalGT("Know_Hedron", "GLOBAL", 0):
				return True # 204: I see.  I must take my leave.  Farewell.
			
		elif index == 5:
			# Global("Know_Hedron", "GLOBAL", 0)
			if self.iGlobal("Know_Hedron", "GLOBAL", 0):
				return True # 121: All right.  Thanks for your help, Hedron.
			
		elif index == 6:
			# Global("Know_Hedron", "GLOBAL", 1)
			if self.iGlobal("Know_Hedron", "GLOBAL", 1):
				return True # 142: All right.  Thanks for your help, Hedron.
			
		elif index == 7:
			# Global("Firtha_Dead", "GLOBAL", 1)
			if self.iGlobal("Firtha_Dead", "GLOBAL", 1):
				return True # 251: I'm afraid she didn't make it, Hedron... she, uh, was killed by goblins in her home.
			
		elif index == 8:
			# GlobalGT("Hedron_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalGT("Hedron_Quest", "GLOBAL", 1) \
				 and self.iGlobalLT("Hedron_Quest", "GLOBAL", 4) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 262: We already checked on her, Hedron.  Some goblins had broken into her house, but we took them out and rescued her.
			
		elif index == 9:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("AR1004_GOBLINS_CLEAR", "GLOBAL", 1)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 2) \
				 and self.iGlobal("AR1004_GOBLINS_CLEAR", "GLOBAL", 1) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 300: We encountered an old woman being menaced by goblins - I don't know whether it was your mother or not.
			
		elif index == 10:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 2) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 312: Your mother?  Which house is hers?
			
		elif index == 11:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 2) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 323: We'll see what we can do - but we need someplace safe to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 12:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 2) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 324: We'll go check on her, Hedron.  We'll return when she's safe.
			
		elif index == 13:
			# ClassEx(Protagonist, Paladin)
			if self.iClassEx("Protagonist", "Paladin"):
				return True # 271: It is likely the goblin attack merely frightened her.  Any harsh words she spoke probably stemmed from fear, not anger.
			
		elif index == 14:
			# ClassEx(Protagonist, Monk)
			if self.iClassEx("Protagonist", "Monk"):
				return True # 285: It is likely the goblin attack merely frightened her.  Any harsh words she spoke probably stemmed from fear, not anger.
			
		elif index == 15:
			# CheckStatLT(Protagonist, 12, CHR)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iCheckStatLT("Protagonist", 12, "CHR") \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 286: She's certainly got a tongue on her, no doubt.
			
		elif index == 16:
			# CheckStatGT(Protagonist, 11, CHR)
			# CheckStatLT(Protagonist, 16, CHR)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iCheckStatGT("Protagonist", 11, "CHR") \
				 and self.iCheckStatLT("Protagonist", 16, "CHR") \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 295: She's certainly got a tongue on her, no doubt.
			
		elif index == 17:
			# CheckStatGT(Protagonist, 15, CHR)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iCheckStatGT("Protagonist", 15, "CHR") \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 296: She's certainly got a tongue on her, no doubt.
			
		elif index == 18:
			# CheckStatLT(Protagonist, 12, CHR)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iCheckStatLT("Protagonist", 12, "CHR") \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 297: She was somewhat sparse with her gratitude, Hedron.  Perhaps you could remedy that.
			
		elif index == 19:
			# CheckStatGT(Protagonist, 11, CHR)
			# CheckStatLT(Protagonist,16, CHR)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iCheckStatGT("Protagonist", 11, "CHR") \
				 and self.iCheckStatLT("Protagonist", 16, "CHR") \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 298: She was somewhat sparse with her gratitude, Hedron.  Perhaps you could remedy that.
			
		elif index == 20:
			# CheckStatGT(Protagonist, 15, CHR)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iCheckStatGT("Protagonist", 15, "CHR") \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 299: She was somewhat sparse with her gratitude, Hedron.  Perhaps you could remedy that.
			
		elif index == 21:
			# ClassEx(Protagonist, Paladin)
			if self.iClassEx("Protagonist", "Paladin"):
				return True # 291: The tenets of my faith preclude me from accepting this much wealth.  Your gratitude is enough.  Farewell.
			
		elif index == 22:
			# ClassEx(Protagonist, Monk)
			if self.iClassEx("Protagonist", "Monk"):
				return True # 292: The tenets of my order preclude the acceptance of this much wealth.  Your gratitude is enough.  Farewell.
			
		elif index == 23:
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 293: Glad we could help.  Take care, Hedron.
			
		elif index == 24:
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 294: She tested our patience, but this should serve to make up for it.  Farewell, Hedron.
			
		elif index == 25:
			# ClassEx(Protagonist, Paladin)
			if self.iClassEx("Protagonist", "Paladin"):
				return True # 281: The tenets of my faith preclude me from accepting this much wealth.  We were pleased to help you, and let us leave it at that.  Farewell.
			
		elif index == 26:
			# ClassEx(Protagonist, Monk)
			if self.iClassEx("Protagonist", "Monk"):
				return True # 282: The tenets of my order preclude the acceptance of this much wealth.  We were pleased to help you, and let us leave it at that.  Farewell.
			
		elif index == 27:
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 283: Glad we could help.  Take care, Hedron.
			
		elif index == 28:
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 284: She tested our patience, but this should serve to make up for it.  Farewell, Hedron.
			
		elif index == 29:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			if self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1) \
				 and self.iGlobalLT("Hedron_Know_Attack", "GLOBAL", 2) \
				 and self.iGlobalLT("Hedron_Quest", "GLOBAL", 4):
				return True # 331: The town was attacked by goblins.  We managed to drive them off and retake the docks.
			
		elif index == 30:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			if self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1) \
				 and self.iGlobalLT("Hedron_Know_Attack", "GLOBAL", 2) \
				 and self.iGlobalLT("Hedron_Quest", "GLOBAL", 4):
				return True # 358: There's been an attack on the docks.  If this keeps up, I suspect Targos is going to be the new home of the goblin horde in the near future.
			
		elif index == 31:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
			# GlobalGT("Hedron_Quest", "GLOBAL", 3)
			if self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1) \
				 and self.iGlobalLT("Hedron_Know_Attack", "GLOBAL", 2) \
				 and self.iGlobalGT("Hedron_Quest", "GLOBAL", 3):
				return True # 359: We've managed to drive off the goblins, though it was a near thing.  Could you put us up for the night, Hedron?
			
		elif index == 32:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
			# GlobalGT("Hedron_Quest", "GLOBAL", 3)
			if self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1) \
				 and self.iGlobalLT("Hedron_Know_Attack", "GLOBAL", 2) \
				 and self.iGlobalGT("Hedron_Quest", "GLOBAL", 3):
				return True # 360: The goblins have been taken care of... but if you caught word of the goblin attack, how come you haven't left yet?
			
		elif index == 33:
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Know_Attack", "GLOBAL", 2)
			# GlobalGT("Hedron_Quest", "GLOBAL", 3)
			if self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1) \
				 and self.iGlobalLT("Hedron_Know_Attack", "GLOBAL", 2) \
				 and self.iGlobalGT("Hedron_Quest", "GLOBAL", 3):
				return True # 384: The docks are safe, and the attacking goblins are dead.  Just returned to the ship to let you know - we'll speak again later.
			
		elif index == 34:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 0):
				return True # 385: There's still goblins about, and we need someplace safe to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 35:
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 0):
				return True # 386: We're still figuring out the extent of the goblin attack.  We'll return when we know more.  Farewell.
			
		elif index == 36:
			# Global("Firtha_Dead", "GLOBAL", 1)
			if self.iGlobal("Firtha_Dead", "GLOBAL", 1):
				return True # 351: I'm afraid she didn't make it, Hedron... she, uh, was killed by goblins in her home.
			
		elif index == 37:
			# GlobalGT("Hedron_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalGT("Hedron_Quest", "GLOBAL", 1) \
				 and self.iGlobalLT("Hedron_Quest", "GLOBAL", 4) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 352: We already checked on her, Hedron.  Some goblins had broken into her house, but we took them out and rescued her.
			
		elif index == 38:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("AR1004_GOBLINS_CLEAR", "GLOBAL", 1)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 2) \
				 and self.iGlobal("AR1004_GOBLINS_CLEAR", "GLOBAL", 1) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 353: We encountered an old woman being menaced by goblins - I don't know whether it was your mother or not.
			
		elif index == 39:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 2) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 354: Your mother?  Which house is hers?
			
		elif index == 40:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 2) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 355: We'll see what we can do - but we need someplace safe to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 41:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 2) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 356: We'll go check on her, Hedron.  We'll return when she's safe.
			
		elif index == 42:
			# Global("Firtha_Dead", "GLOBAL", 1)
			if self.iGlobal("Firtha_Dead", "GLOBAL", 1):
				return True # 391: I'm afraid she didn't make it, Hedron... she, uh, was killed by goblins in her home.
			
		elif index == 43:
			# GlobalGT("Hedron_Quest", "GLOBAL", 1)
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalGT("Hedron_Quest", "GLOBAL", 1) \
				 and self.iGlobalLT("Hedron_Quest", "GLOBAL", 4) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 392: We already checked on her, Hedron.  Some goblins had broken into her house, but we took them out and rescued her.
			
		elif index == 44:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("AR1004_GOBLINS_CLEAR", "GLOBAL", 1)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 2) \
				 and self.iGlobal("AR1004_GOBLINS_CLEAR", "GLOBAL", 1) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 393: We encountered an old woman being menaced by goblins - I don't know whether it was your mother or not.
			
		elif index == 45:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 2) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 394: Which house is hers again?
			
		elif index == 46:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 2) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 395: We'll see what we can do - but we need someplace safe to rest.  Can you watch over us while we catch our second wind?
			
		elif index == 47:
			# GlobalLT("Hedron_Quest", "GLOBAL", 2)
			# Global("Firtha_Dead", "GLOBAL", 0)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 2) \
				 and self.iGlobal("Firtha_Dead", "GLOBAL", 0):
				return True # 396: We'll go check on her, Hedron.  We'll return when she's safe.
			
		elif index == 48:
			# Global("Reig_Quest", "GLOBAL", 0)
			if self.iGlobal("Reig_Quest", "GLOBAL", 0):
				return True # 405: Nothing today, thanks.  Farewell.
			
		elif index == 49:
			# GlobalGT("Reig_Quest", "GLOBAL", 0)
			if self.iGlobalGT("Reig_Quest", "GLOBAL", 0):
				return True # 412: Nothing today, thanks.  Farewell.
			
		elif index == 50:
			# GlobalLT("Hedron_Quest", "GLOBAL", 4)
			if self.iGlobalLT("Hedron_Quest", "GLOBAL", 4):
				return True # 381: If your mother's here why are you still aboard the ship?
			
		return False # dialog_test_do
	
class Ctrl10ELDGUL(ctrl_behaviour_ie.CtrlBehaviourIE): # 10ELDGUL 
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
				line_id = 10 # None
				print("STATE 0: line_id = 10")
				break
			
			print("STATE 3")
			# GlobalGT("Reig_Quest", "GLOBAL", 0)
			if self.iGlobalGT("Reig_Quest", "GLOBAL", 0):
				line_id = 30 # None
				print("STATE 3: line_id = 30")
				break
			
			print("STATE 5")
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1):
				line_id = 160 # None
				print("STATE 5: line_id = 160")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		return False # dialog_test_do
	
class Ctrl10SCREED(ctrl_behaviour_ie.CtrlBehaviourIE): # 10SCREED 
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
				line_id = 10 # None
				print("STATE 0: line_id = 10")
				break
			
			print("STATE 3")
			# GlobalGT("Reig_Quest", "GLOBAL", 0)
			if self.iGlobalGT("Reig_Quest", "GLOBAL", 0):
				line_id = 30 # None
				print("STATE 3: line_id = 30")
				break
			
			print("STATE 4")
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1):
				line_id = 40 # None
				print("STATE 4: line_id = 40")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		return False # dialog_test_do
	
class Ctrl10REIG(ctrl_behaviour_ie.CtrlBehaviourIE): # 10REIG 
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
				line_id = 10 # None
				print("STATE 0: line_id = 10")
				break
			
			print("STATE 15")
			# Global("Reig_Quest", "GLOBAL", 1)
			if self.iGlobal("Reig_Quest", "GLOBAL", 1):
				line_id = 200 # None
				print("STATE 15: line_id = 200")
				break
			
			print("STATE 16")
			# HPGT(Myself, 3)
			# Global("Reig_Quest", "GLOBAL", 1)
			# Global("Reig_Heal_Priest", "GLOBAL", 0)
			if self.iHPGT("Myself", 3) \
				 and self.iGlobal("Reig_Quest", "GLOBAL", 1) \
				 and self.iGlobal("Reig_Heal_Priest", "GLOBAL", 0):
				line_id = 430 # My arm's better, thanks for your help.  Looks like you're praying to the right gods.
				print("STATE 16: line_id = 430")
				break
			
			print("STATE 17")
			# Global("Reig_Quest", "GLOBAL", 1)
			# Global("Reig_Heal_Priest", "GLOBAL", 1)
			if self.iGlobal("Reig_Quest", "GLOBAL", 1) \
				 and self.iGlobal("Reig_Heal_Priest", "GLOBAL", 1):
				line_id = 110 # None
				print("STATE 17: line_id = 110")
				break
			
			print("STATE 19")
			# Global("Reig_Quest", "GLOBAL", 2)
			if self.iGlobal("Reig_Quest", "GLOBAL", 2):
				line_id = 130 # None
				print("STATE 19: line_id = 130")
				break
			
			print("STATE 21")
			# Global("Told_Reig", "GLOBAL", 1)
			if self.iGlobal("Told_Reig", "GLOBAL", 1):
				line_id = 230 # None
				print("STATE 21: line_id = 230")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		if index == 35:
			# Global("Reig_Heal_Priest", "GLOBAL", 0)
			if self.iGlobal("Reig_Heal_Priest", "GLOBAL", 0):
				return True # 431: The wound's closed, but there may be more damage.  You still don't look too good.
			
		elif index == 36:
			# Global("Reig_Heal_Priest", "GLOBAL", 1)
			if self.iGlobal("Reig_Heal_Priest", "GLOBAL", 1):
				return True # 432: The wound's closed, but there may be more damage.  You still don't look too good.
			
		return False # dialog_test_do
	
class Ctrl10JON(ctrl_behaviour_ie.CtrlBehaviourIE): # 10JON 
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

	def script_dialog(self, attachee, triggerer):
		print("script_dialog 10JON")
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		while True:
			print("STATE 0")
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 0):
				line_id = 10 # None
				print("STATE 0: line_id = 10")
				break
			
			print("STATE 8")
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1):
				line_id = 150 # None
				print("STATE 8: line_id = 150")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		return False # dialog_test_do
	
class Ctrl10BROGAN(ctrl_behaviour_ie.CtrlBehaviourIE): # 10BROGAN 
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
				line_id = 10 # None
				print("STATE 0: line_id = 10")
				break
			
			print("STATE 6")
			# GlobalGT("Iron_Collar_Quest", "GLOBAL", 0)
			# GlobalLT("Iron_Collar_Quest", "GLOBAL", 3)
			# Global("Brogan_Quest", "GLOBAL", 0)
			# Global("AR1002_Visited", "GLOBAL", 0)
			if self.iGlobalGT("Iron_Collar_Quest", "GLOBAL", 0) \
				 and self.iGlobalLT("Iron_Collar_Quest", "GLOBAL", 3) \
				 and self.iGlobal("Brogan_Quest", "GLOBAL", 0) \
				 and self.iGlobal("AR1002_Visited", "GLOBAL", 0):
				line_id = 170 # None
				print("STATE 6: line_id = 170")
				break
			
			print("STATE 10")
			# Global("Brogan_Quest", "GLOBAL", 1)
			if self.iGlobal("Brogan_Quest", "GLOBAL", 1):
				line_id = 90 # None
				print("STATE 10: line_id = 90")
				break
			
			print("STATE 13")
			# Global("Brogan_Quest", "GLOBAL", 1)
			# Global("AR1002_Visited", "GLOBAL", 1)
			# Global("AR1007_Visited", "GLOBAL", 1)
			if self.iGlobal("Brogan_Quest", "GLOBAL", 1) \
				 and self.iGlobal("AR1002_Visited", "GLOBAL", 1) \
				 and self.iGlobal("AR1007_Visited", "GLOBAL", 1):
				line_id = 180 # None
				print("STATE 13: line_id = 180")
				break
			
			print("STATE 18")
			# Global("AR1002_Visited", "GLOBAL", 1)
			# Global("Know_Brogan", "GLOBAL", 0)
			if self.iGlobal("AR1002_Visited", "GLOBAL", 1) \
				 and self.iGlobal("Know_Brogan", "GLOBAL", 0):
				line_id = 120 # None
				print("STATE 18: line_id = 120")
				break
			
			print("STATE 19")
			# Global("Brogan_Leave", "GLOBAL", 1)
			if self.iGlobal("Brogan_Leave", "GLOBAL", 1):
				line_id = 130 # None
				print("STATE 19: line_id = 130")
				break
			
			print("STATE 20")
			# GlobalGT("Iron_Collar_Quest", "GLOBAL", 0)
			# GlobalLT("Iron_Collar_Quest", "GLOBAL", 3)
			# Global("Brogan_Quest", "GLOBAL", 0)
			# Global("AR1002_Visited", "GLOBAL", 1)
			if self.iGlobalGT("Iron_Collar_Quest", "GLOBAL", 0) \
				 and self.iGlobalLT("Iron_Collar_Quest", "GLOBAL", 3) \
				 and self.iGlobal("Brogan_Quest", "GLOBAL", 0) \
				 and self.iGlobal("AR1002_Visited", "GLOBAL", 1):
				line_id = 140 # None
				print("STATE 20: line_id = 140")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		return False # dialog_test_do
	
class Ctrl10JORUN(ctrl_behaviour_ie.CtrlBehaviourIE): # 10JORUN 
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
			if self.iGlobal("Know_Jorun", "GLOBAL", 0) \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 0):
				line_id = 10 # None
				print("STATE 0: line_id = 10")
				break
			
			print("STATE 13")
			# Global("Know_Jorun", "GLOBAL", 1)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iGlobal("Know_Jorun", "GLOBAL", 1) \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 0):
				line_id = 180 # None
				print("STATE 13: line_id = 180")
				break
			
			print("STATE 14")
			# Global("Know_Jorun", "GLOBAL", 0)
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("Know_Jorun", "GLOBAL", 0) \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1):
				line_id = 190 # None
				print("STATE 14: line_id = 190")
				break
			
			print("STATE 20")
			# Global("Know_Jorun", "GLOBAL", 1)
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iGlobal("Know_Jorun", "GLOBAL", 1) \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1):
				line_id = 140 # None
				print("STATE 20: line_id = 140")
				break
			
			print("STATE 31")
			# NumTimesTalkedTo(0)
			# Subrace(Protagonist, Dwarf_Gray)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iNumTimesTalkedTo(0) \
				 and self.iSubrace("Protagonist", "Dwarf_Gray") \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 0):
				line_id = 340 # None
				print("STATE 31: line_id = 340")
				break
			
			print("STATE 32")
			# NumTimesTalkedTo(0)
			# Subrace(Protagonist, Elf_Drow)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iNumTimesTalkedTo(0) \
				 and self.iSubrace("Protagonist", "Elf_Drow") \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 0):
				line_id = 350 # None
				print("STATE 32: line_id = 350")
				break
			
			print("STATE 35")
			# NumTimesTalkedTo(0)
			# Subrace(Protagonist, Gnome_Deep)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iNumTimesTalkedTo(0) \
				 and self.iSubrace("Protagonist", "Gnome_Deep") \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 0):
				line_id = 370 # None
				print("STATE 35: line_id = 370")
				break
			
			print("STATE 37")
			# NumTimesTalkedTo(0)
			# Subrace(Protagonist, Dwarf_Gray)
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iNumTimesTalkedTo(0) \
				 and self.iSubrace("Protagonist", "Dwarf_Gray") \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1):
				line_id = 410 # None
				print("STATE 37: line_id = 410")
				break
			
			print("STATE 38")
			# NumTimesTalkedTo(0)
			# Subrace(Protagonist, Elf_Drow)
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iNumTimesTalkedTo(0) \
				 and self.iSubrace("Protagonist", "Elf_Drow") \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1):
				line_id = 420 # None
				print("STATE 38: line_id = 420")
				break
			
			print("STATE 39")
			# NumTimesTalkedTo(0)
			# Subrace(Protagonist, Gnome_Deep)
			# Global("Dock_Goblin_Quest", "GLOBAL", 1)
			if self.iNumTimesTalkedTo(0) \
				 and self.iSubrace("Protagonist", "Gnome_Deep") \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 1):
				line_id = 60 # None
				print("STATE 39: line_id = 60")
				break
			
			print("STATE 40")
			# NumTimesTalkedTo(0)
			# Race(Protagonist, Dwarf)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iNumTimesTalkedTo(0) \
				 and self.iRace("Protagonist", "Dwarf") \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 0):
				line_id = 70 # None
				print("STATE 40: line_id = 70")
				break
			
			print("STATE 41")
			# NumTimesTalkedTo(0)
			# Race(Protagonist, Dwarf)
			# Global("Dock_Goblin_Quest", "GLOBAL", 0)
			if self.iNumTimesTalkedTo(0) \
				 and self.iRace("Protagonist", "Dwarf") \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 0):
				line_id = 440 # Well, now, a dwarf is a sight for sore eyes in these windswept lands... especially one who can cleave goblins as well as ye can.  Something this ol' shipbuilder can help ye with?  
				print("STATE 41: line_id = 440")
				break
			
			break # while
			
		print("script_dialog line_id: {}".format(line_id))
		if line_id >= 0:
			triggerer.begin_dialog(attachee, line_id)
		
		return # script_dialog
	
	def dialog_test_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		return False # dialog_test_do
	
class Ctrl10MALED(ctrl_behaviour_ie.CtrlBehaviourIE): # 10MALED 
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

class Ctrl10SOLDRD(ctrl_behaviour_ie.CtrlBehaviourIE): # 10SOLDRD 
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

class Ctrl10GOB(ctrl_behaviour_ie.CtrlBehaviourIE): # 10GOB 
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

class Ctrl10GOBD(ctrl_behaviour_ie.CtrlBehaviourIE): # 10GOBD 
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

class Ctrl10GOBAR(ctrl_behaviour_ie.CtrlBehaviourIE): # 10GOBAR 
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

class Ctrl10GOBARD(ctrl_behaviour_ie.CtrlBehaviourIE): # 10GOBARD 
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

class Ctrl10SAILRD(ctrl_behaviour_ie.CtrlBehaviourIE): # 10SAILRD 
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

