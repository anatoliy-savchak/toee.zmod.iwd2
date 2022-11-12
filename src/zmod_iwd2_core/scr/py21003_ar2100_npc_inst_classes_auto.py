import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon, const_iwd2, const_proto_weapon_iwd2, utils_npc_spells_inf
import utils_journal as uj, inf_scripting, module_difficulty, const_inf
#### IMPORTS ####
import py21002_ar2100_npc_classes
from bcs import scr_00aatgn
from bcs import scr_20orcsh1
from bcs import scr_00aatkn
from bcs import scr_21emmac
from bcs import scr_20cemma2
from bcs import scr_21krisc
from bcs import scr_21wovc
#### END IMPORTS ####

#### GVARS ####
MODULE_SCRIPT_ID = 21003
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
class Ctrl_21GAERNT_AR2100_Gaernat_Sharptooth_Auto(py21002_ar2100_npc_classes.Ctrl_21GAERNT): # 21GAERNT 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

	def script_dialog(self, attachee, triggerer):
		print("script_dialog 21GAERNT")
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		while True:
			print("STATE 0")
			# NumTimesTalkedTo(0)
			if self.iNumTimesTalkedTo(0):
				line_id = 10 # Look who stands before me, brethren!  It is the mighty adventurer of the logging village.  So, tell me.  Why are you here?
				print("STATE 0: line_id = 10")
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
		# 21GAERNT
		
		return False # dialog_test_do
	
	def dialog_action_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		if index == 0:
			# Enemy()
			self.iEnemy()
			# 31: If it is a battle you want, then you shall have it.
			
		elif index == 1:
			# Enemy()
			self.iEnemy()
			# 41: If it is a battle you want, then you shall have it.
			
		return # dialog_action_do
		
	def get_dialog_trigger_max_index(self): return 0
	
	def get_state_to_line(self, state):
		if state==0: return 10
		if state==1: return 20
		if state==2: return 30
		if state==3: return 40
		if state==4: return 50
		return
	
	def setup_scripts(self, npc):
		super(Ctrl_21GAERNT_AR2100_Gaernat_Sharptooth_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		self.enable_dialog(npc)
		return
	
class Ctrl_21WERRAT_AR2100_GTH01_01_Auto(py21002_ar2100_npc_classes.Ctrl_21WERRAT): # 21WERRAT 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21WERRAT_AR2100_GTH01_03_Auto(py21002_ar2100_npc_classes.Ctrl_21WERRAT): # 21WERRAT 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21WERRAT_AR2100_GTH01_09_Auto(py21002_ar2100_npc_classes.Ctrl_21WERRAT): # 21WERRAT 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21WERBGR_AR2100_GTH01_02_Auto(py21002_ar2100_npc_classes.Ctrl_21WERBGR): # 21WERBGR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21WERBGR_AR2100_GTH01_10_Auto(py21002_ar2100_npc_classes.Ctrl_21WERBGR): # 21WERBGR 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21WERBGR_AR2100_GTH01_06_Auto(py21002_ar2100_npc_classes.Ctrl_21WERBGR): # 21WERBGR 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_20ORCSHM_AR2100_GTH01_07_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_20orcsh1.Script_20ORCSH1

class Ctrl_20ORCSHM_AR2100_GTH01_08_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_20orcsh1.Script_20ORCSH1

class Ctrl_20ORCSHM_AR2100_GTH01_11_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_20orcsh1.Script_20ORCSH1

class Ctrl_20ORCACH_AR2100_GTH01_05_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatkn.Script_00AATKN

class Ctrl_20ORCACH_AR2100_GTH01_04_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatkn.Script_00AATKN

class Ctrl_20ORCACH_AR2100_GTH01_12_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatkn.Script_00AATKN

class Ctrl_21WERRAT_AR2100_GTH02_10_Auto(py21002_ar2100_npc_classes.Ctrl_21WERRAT): # 21WERRAT 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21WERRAT_AR2100_GTH02_01_Auto(py21002_ar2100_npc_classes.Ctrl_21WERRAT): # 21WERRAT 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21WERBGR_AR2100_GTH02_09_Auto(py21002_ar2100_npc_classes.Ctrl_21WERBGR): # 21WERBGR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21WERBGR_AR2100_GTH02_02_Auto(py21002_ar2100_npc_classes.Ctrl_21WERBGR): # 21WERBGR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_20ORCSHM_AR2100_GTH02_08_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_20orcsh1.Script_20ORCSH1

class Ctrl_20ORCSHM_AR2100_GTH02_07_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_20orcsh1.Script_20ORCSH1

class Ctrl_20ORCACH_AR2100_GTH02_06_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatkn.Script_00AATKN

class Ctrl_20ORCACH_AR2100_GTH02_05_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatkn.Script_00AATKN

class Ctrl_20ORCA3_AR2100_GTH02_03_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatkn.Script_00AATKN

class Ctrl_20ORCA3_AR2100_GTH02_04_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatkn.Script_00AATKN

class Ctrl_21OGR_AR2100_Ogre_Auto(py21002_ar2100_npc_classes.Ctrl_21OGR): # 21OGR 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21SPDQN_AR2100_Spider_Queen_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDQN): # 21SPDQN 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21SPDSML_AR2100_Spider_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDSML): # 21SPDSML 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21SPDSML_AR2100_Spider_2_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDSML): # 21SPDSML 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21SPDSML_AR2100_Spider_3_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDSML): # 21SPDSML 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21SPDSML_AR2100_Spider_4_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDSML): # 21SPDSML 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21SPDSML_AR2100_Spider_5_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDSML): # 21SPDSML 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21SPDSML_AR2100_Spider_6_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDSML): # 21SPDSML 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21HGHSNK_AR2100_Highland_Snake_Auto(py21002_ar2100_npc_classes.Ctrl_21HGHSNK): # 21HGHSNK 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21HGHSNK_AR2100_Highland_Snake_2_Auto(py21002_ar2100_npc_classes.Ctrl_21HGHSNK): # 21HGHSNK 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21HGHSNK_AR2100_Highland_Snake_3_Auto(py21002_ar2100_npc_classes.Ctrl_21HGHSNK): # 21HGHSNK 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21HRP_AR2100_Harpy_Auto(py21002_ar2100_npc_classes.Ctrl_21HRP): # 21HRP 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21HRP_AR2100_Harpy_2_Auto(py21002_ar2100_npc_classes.Ctrl_21HRP): # 21HRP 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21HRP_AR2100_Harpy_3_Auto(py21002_ar2100_npc_classes.Ctrl_21HRP): # 21HRP 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21HRP_AR2100_Harpy_4_Auto(py21002_ar2100_npc_classes.Ctrl_21HRP): # 21HRP 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21VERB_AR2100_Verbeeg_Auto(py21002_ar2100_npc_classes.Ctrl_21VERB): # 21VERB 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21VERB_AR2100_Verbeeg_2_Auto(py21002_ar2100_npc_classes.Ctrl_21VERB): # 21VERB 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21VERB_AR2100_Verbeeg_3_Auto(py21002_ar2100_npc_classes.Ctrl_21VERB): # 21VERB 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def get_bcs_combat(self):
		return scr_00aatgn.Script_00AATGN

class Ctrl_21WERRAT_AR2100_Wererat_Scripted_Event_Auto(py21002_ar2100_npc_classes.Ctrl_21WERRAT): # 21WERRAT 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def get_bcs_combat(self):
		return

class Ctrl_20EMMA_AR2100_Emma_Auto(py21002_ar2100_npc_classes.Ctrl_20EMMA): # 20EMMA 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def get_bcs_combat(self):
		return scr_21emmac.Script_21EMMAC

	def script_dialog(self, attachee, triggerer):
		print("script_dialog 20NEWEMM")
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		attachee.turn_towards(triggerer)
		
		line_id = -1
		while True:
			print("STATE 0")
			# NumTimesTalkedTo(0)
			if self.iNumTimesTalkedTo(0):
				line_id = 60 # Well met, adventurer.  I am Emma Moonblade, priestess of Selune.  It seems I chose an interesting moment to arrive.
				print("STATE 0: line_id = 60")
				break
			
			print("STATE 14")
			# NumTimesTalkedToGT(0)
			if self.iNumTimesTalkedToGT(0):
				line_id = 290 # You have returned.  How may I aid you?
				print("STATE 14: line_id = 290")
				break
			
			print("STATE 22")
			# GlobalLT( "SR_Orcs_Dead", "GLOBAL", 2 )
			if self.iGlobalLT("'SR_Orcs_Dead'", "'GLOBAL'", 2):
				line_id = 320 # Continue the battle!  Do not let them get the upper hand!
				print("STATE 22: line_id = 320")
				break
			
			print("STATE 23")
			# Global("SR_Emma_Revenge","GLOBAL", 1)
			if self.iGlobal("'SR_Emma_Revenge'", "'GLOBAL'", 1):
				line_id = 330 # I warned you that we would meet again, pig.  Now you shall pay for your threats!
				print("STATE 23: line_id = 330")
				break
			
			print("STATE 24")
			# Global("SR_Emma_Revenge","GLOBAL", 2)
			if self.iGlobal("'SR_Emma_Revenge'", "'GLOBAL'", 2):
				line_id = 340 # I warned you that we would meet again, pig.  Now you shall pay for what you did to Kaitlin!
				print("STATE 24: line_id = 340")
				break
			
			print("STATE 25")
			# Global("SR_Emma_Revenge","GLOBAL", 3)
			if self.iGlobal("'SR_Emma_Revenge'", "'GLOBAL'", 3):
				line_id = 350 # I warned you that we would meet again, pig.  Now you shall pay for slaying Kaitlin!
				print("STATE 25: line_id = 350")
				break
			
			print("STATE 26")
			# Global("SR_Emma_Revenge","GLOBAL", 4)
			if self.iGlobal("'SR_Emma_Revenge'", "'GLOBAL'", 4):
				line_id = 360 # I warned you that we would meet again, pig.  Now you shall pay for attacking me!
				print("STATE 26: line_id = 360")
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
		# 20NEWEMM
		
		if index == 0:
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 72: I may have seen something.  What is it worth to you?
			
		elif index == 1:
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 282: I may have seen something.  What is it worth to you?
			
		elif index == 2:
			# !PartyHasItem("00SWDL09")
			if not self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE):
				return True # 81: It is only a sword, priestess.
			
		elif index == 3:
			# !PartyHasItem("00SWDL09")
			if not self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE):
				return True # 82: Why not recover the blade yourself?
			
		elif index == 4:
			# !Global("SR_Emma_Heal","GLOBAL", 1)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			# !PartyHasItem("00SWDL09")
			if not self.iGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk") \
				 and not self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE):
				return True # 83: I could be convinced to recover it for you... for a price.
			
		elif index == 5:
			# Global("SR_Emma_Heal","GLOBAL", 1)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			# !PartyHasItem("00SWDL09")
			if self.iGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk") \
				 and not self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE):
				return True # 84: I could be convinced to recover if for you... if you were to continue healing me for but a gold.
			
		elif index == 6:
			# ClassEx(Protagonist, Paladin)
			# !PartyHasItem("00SWDL09")
			if self.iClassEx("Protagonist", "Paladin") \
				 and not self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE):
				return True # 85: You have my word, priestess.  I shall recover your blade from the creature!
			
		elif index == 7:
			# PartyHasItem("00SWDL09")
			# !Global("SR_Kaitlin_Fled","GLOBAL", 1)
			# !Global("SR_Kaitlin_Dead","GLOBAL", 1)
			if self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE) \
				 and not self.iGlobal("'SR_Kaitlin_Fled'", "'GLOBAL'", 1) \
				 and not self.iGlobal("'SR_Kaitlin_Dead'", "'GLOBAL'", 1):
				return True # 86: I have already recovered your blade, priestess.
			
		elif index == 8:
			# PartyHasItem("00SWDL09")
			# Global("SR_Kaitlin_Fled","GLOBAL", 1)
			if self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE) \
				 and self.iGlobal("'SR_Kaitlin_Fled'", "'GLOBAL'", 1):
				return True # 87: I have already recovered your blade, priestess.
			
		elif index == 9:
			# PartyHasItem("00SWDL09")
			# Global("SR_Kaitlin_Dead","GLOBAL", 1)
			if self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE) \
				 and self.iGlobal("'SR_Kaitlin_Dead'", "'GLOBAL'", 1):
				return True # 88: I have already recovered your blade, priestess.
			
		elif index == 10:
			# !Global("SR_Emma_Heal","GLOBAL", 1)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 102: I could be convinced to recover it for you... for a price.
			
		elif index == 11:
			# Global("SR_Emma_Heal","GLOBAL", 1)
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1) \
				 and not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 103: I could be convinced to recover if for you... if you were to continue healing me for but a gold.
			
		elif index == 12:
			# ClassEx(Protagonist, Paladin)
			if self.iClassEx("Protagonist", "Paladin"):
				return True # 104: You have my word, priestess.  I shall recover your blade from the creature!
			
		elif index == 13:
			# !ClassEx(Protagonist, Paladin)
			if not self.iClassEx("Protagonist", "Paladin"):
				return True # 105: Feeling a bit weak are we?  Seems to me I could slay you now, recover your blade at my leisure, and keep it for myself.
			
		elif index == 14:
			# Global("SR_Kaitlin_Fled","GLOBAL", 1)
			# !PartyHasItem("00SWDL09")
			if self.iGlobal("'SR_Kaitlin_Fled'", "'GLOBAL'", 1) \
				 and not self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE):
				return True # 291: I have been to the village, priestess.
			
		elif index == 15:
			# Global("SR_Kaitlin_Dead","GLOBAL", 1)
			#  !PartyHasItem("00SWDL09")
			if self.iGlobal("'SR_Kaitlin_Dead'", "'GLOBAL'", 1) \
				 and not self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE):
				return True # 292: I have been to the village, priestess.
			
		elif index == 16:
			# Global("SR_Recover_Blade","GLOBAL", 3)
			# PartyHasItem("00SWDL09")
			# !Global("SR_Kaitlin_Fled","GLOBAL", 1)
			# !Global("SR_Kaitlin_Dead","GLOBAL", 1)
			if self.iGlobal("'SR_Recover_Blade'", "'GLOBAL'", 3) \
				 and self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE) \
				 and not self.iGlobal("'SR_Kaitlin_Fled'", "'GLOBAL'", 1) \
				 and not self.iGlobal("'SR_Kaitlin_Dead'", "'GLOBAL'", 1):
				return True # 293: I have recovered your blade, priestess.
			
		elif index == 17:
			# Global("SR_Recover_Blade","GLOBAL", 3)
			# PartyHasItem("00SWDL09")
			# Global("SR_Kaitlin_Fled","GLOBAL", 1)
			if self.iGlobal("'SR_Recover_Blade'", "'GLOBAL'", 3) \
				 and self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE) \
				 and self.iGlobal("'SR_Kaitlin_Fled'", "'GLOBAL'", 1):
				return True # 294: I have recovered your blade, priestess.
			
		elif index == 18:
			# Global("SR_Recover_Blade","GLOBAL", 3)
			# PartyHasItem("00SWDL09")
			# Global("SR_Kaitlin_Dead","GLOBAL", 1)
			if self.iGlobal("'SR_Recover_Blade'", "'GLOBAL'", 3) \
				 and self.iPartyHasItem(const_proto_weapon_iwd2.PROTO_LONGSWORD_MOONBLADE_OF_SELUNE) \
				 and self.iGlobal("'SR_Kaitlin_Dead'", "'GLOBAL'", 1):
				return True # 295: I have recovered your blade, priestess.
			
		elif index == 19:
			# !Global("SR_Emma_Heal","GLOBAL", 1)
			if not self.iGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1):
				return True # 296: I am in need of healing.
			
		elif index == 20:
			# Global("SR_Emma_Heal","GLOBAL", 1)
			if self.iGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1):
				return True # 297: I am in need of healing.
			
		elif index == 21:
			# !ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 181: I am grateful, priestess.
			
		elif index == 22:
			# !ClassEx(Protagonist, Paladin)
			# ClassEx(Protagonist, Monk)
			if not self.iClassEx("Protagonist", "Paladin") \
				 and self.iClassEx("Protagonist", "Monk"):
				return True # 182: I am grateful, priestess, but I cannot accept a reward.  The tenets of my faith do not allow it.
			
		elif index == 23:
			# ClassEx(Protagonist, Paladin)
			# !ClassEx(Protagonist, Monk)
			if self.iClassEx("Protagonist", "Paladin") \
				 and not self.iClassEx("Protagonist", "Monk"):
				return True # 183: I am grateful, priestess, but I cannot accept a reward.  The tenets of my faith do not allow it.
			
		elif index == 24:
			# Global("SR_Dereth_Freed","GLOBAL", 4)
			# Global("SR_Sabrina_Freed","GLOBAL", 4)
			# GlobalGT("SR_Rescue_Villagers","GLOBAL", 3)
			# !Global("SR_Dereth_Dead","GLOBAL", 1)
			# !Global("SR_Sabrina_Dead","GLOBAL", 1)
			# !Global("SR_Kaitlin_Dead","GLOBAL", 1)
			if self.iGlobal("'SR_Dereth_Freed'", "'GLOBAL'", 4) \
				 and self.iGlobal("'SR_Sabrina_Freed'", "'GLOBAL'", 4) \
				 and self.iGlobalGT("'SR_Rescue_Villagers'", "'GLOBAL'", 3) \
				 and not self.iGlobal("'SR_Dereth_Dead'", "'GLOBAL'", 1) \
				 and not self.iGlobal("'SR_Sabrina_Dead'", "'GLOBAL'", 1) \
				 and not self.iGlobal("'SR_Kaitlin_Dead'", "'GLOBAL'", 1):
				return True # 184: No reward is necessary, Priestess.  I am glad to have been of aid to those in need.
			
		elif index == 25:
			# !Global("SR_Emma_Heal","GLOBAL", 1)
			if not self.iGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1):
				return True # 191: I am in need of healing.
			
		elif index == 26:
			# Global("SR_Emma_Heal","GLOBAL", 1)
			if self.iGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1):
				return True # 192: I am in need of healing.
			
		elif index == 27:
			# Global("SR_Emma_Heal","GLOBAL", 1)
			if self.iGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1):
				return True # 201: I am in need of healing.
			
		return False # dialog_test_do
	
	def dialog_action_do(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		if index == 0:
			# SetGlobal("SR_Emma_Heal","GLOBAL", 1)
			self.iSetGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1)
			# 271: Very well.  The troll had to flee east, priestess.  It did not pass by us and travel is blocked any other way.
			
		elif index == 1:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 3)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 3)
			# 83: I could be convinced to recover it for you... for a price.
			
		elif index == 2:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 3)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 3)
			# 84: I could be convinced to recover if for you... if you were to continue healing me for but a gold.
			
		elif index == 3:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 3)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 3)
			# 85: You have my word, priestess.  I shall recover your blade from the creature!
			
		elif index == 4:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 4)
			# SetGlobal("SR_Emma_Has_Blade","GLOBAL", 1)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 4)
			self.iSetGlobal("'SR_Emma_Has_Blade'", "'GLOBAL'", 1)
			# 86: I have already recovered your blade, priestess.
			
		elif index == 5:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 4)
			# SetGlobal("SR_Emma_Revenge","GLOBAL", 2)
			# SetGlobal("SR_Emma_Has_Blade","GLOBAL", 1)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 4)
			self.iSetGlobal("'SR_Emma_Revenge'", "'GLOBAL'", 2)
			self.iSetGlobal("'SR_Emma_Has_Blade'", "'GLOBAL'", 1)
			# 87: I have already recovered your blade, priestess.
			
		elif index == 6:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 4)
			# SetGlobal("SR_Emma_Revenge","GLOBAL", 3)
			# SetGlobal("SR_Emma_Has_Blade","GLOBAL", 1)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 4)
			self.iSetGlobal("'SR_Emma_Revenge'", "'GLOBAL'", 3)
			self.iSetGlobal("'SR_Emma_Has_Blade'", "'GLOBAL'", 1)
			# 88: I have already recovered your blade, priestess.
			
		elif index == 7:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 3)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 3)
			# 101: Very well, I shall recover the blade.
			
		elif index == 8:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 3)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 3)
			# 102: I could be convinced to recover it for you... for a price.
			
		elif index == 9:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 3)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 3)
			# 103: I could be convinced to recover if for you... if you were to continue healing me for but a gold.
			
		elif index == 10:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 3)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 3)
			# 104: You have my word, priestess.  I shall recover your blade from the creature!
			
		elif index == 11:
			# SetGlobal("SR_Emma_Revenge","GLOBAL", 1)
			self.iSetGlobal("'SR_Emma_Revenge'", "'GLOBAL'", 1)
			# 105: Feeling a bit weak are we?  Seems to me I could slay you now, recover your blade at my leisure, and keep it for myself.
			
		elif index == 12:
			# SetGlobal("SR_Emma_Heal","GLOBAL", 1)
			self.iSetGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1)
			# 141: Very well, I shall recover your blade for you.
			
		elif index == 13:
			# StartCutScene("20cEmma2")
			self.iStartCutScenePost(scr_20cemma2.Script_20cEmma2, self.locus_make())
			# 171: You will not escape me, priestess!
			
		elif index == 14:
			# GiveItemCreate("00Misc32", Protagonist,3,0,0)
			self.iGiveItemCreate("'00Misc32'", "Protagonist", 3, 0, 0)
			# 111: I shall do so.
			
		elif index == 15:
			# SetGlobal("SR_Emma_Revenge","GLOBAL", 2)
			self.iSetGlobal("'SR_Emma_Revenge'", "'GLOBAL'", 2)
			# 291: I have been to the village, priestess.
			
		elif index == 16:
			# SetGlobal("SR_Emma_Revenge","GLOBAL", 3)
			self.iSetGlobal("'SR_Emma_Revenge'", "'GLOBAL'", 3)
			# 292: I have been to the village, priestess.
			
		elif index == 17:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 4)
			# SetGlobal("SR_Emma_Has_Blade","GLOBAL", 1)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 4)
			self.iSetGlobal("'SR_Emma_Has_Blade'", "'GLOBAL'", 1)
			# 293: I have recovered your blade, priestess.
			
		elif index == 18:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 4)
			# SetGlobal("SR_Emma_Revenge","GLOBAL", 2)
			# SetGlobal("SR_Emma_Has_Blade","GLOBAL", 1)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 4)
			self.iSetGlobal("'SR_Emma_Revenge'", "'GLOBAL'", 2)
			self.iSetGlobal("'SR_Emma_Has_Blade'", "'GLOBAL'", 1)
			# 294: I have recovered your blade, priestess.
			
		elif index == 19:
			# SetGlobal("SR_Recover_Blade","GLOBAL", 4)
			# SetGlobal("SR_Emma_Revenge","GLOBAL", 3)
			# SetGlobal("SR_Emma_Has_Blade","GLOBAL", 1)
			self.iSetGlobal("'SR_Recover_Blade'", "'GLOBAL'", 4)
			self.iSetGlobal("'SR_Emma_Revenge'", "'GLOBAL'", 3)
			self.iSetGlobal("'SR_Emma_Has_Blade'", "'GLOBAL'", 1)
			# 295: I have recovered your blade, priestess.
			
		elif index == 20:
			# StartStore("20Emma", Protagonist)
			self.iStartStore("'20Emma'", "Protagonist")
			# 296: I am in need of healing.
			
		elif index == 21:
			# StartStore("20EmDis", Protagonist)
			self.iStartStore("'20EmDis'", "Protagonist")
			# 297: I am in need of healing.
			
		elif index == 22:
			# FadeToColor([0.0],0)
			# RestUntilHealed()
			# FadeFromColor([0.0],0)
			self.iFadeToColor("[0.0]", 0)
			self.iRestUntilHealed()
			self.iFadeFromColor("[0.0]", 0)
			# 298: Would you mind if I rested here?
			
		elif index == 23:
			# StartCutScene("20cEmma2")
			self.iStartCutScenePost(scr_20cemma2.Script_20cEmma2, self.locus_make())
			# 301: You will not escape me, priestess!
			
		elif index == 24:
			# StartCutScene("20cEmma2")
			self.iStartCutScenePost(scr_20cemma2.Script_20cEmma2, self.locus_make())
			# 311: You will not escape me, priestess!
			
		elif index == 25:
			# AddXpVar("Level_3_Hard",36407)
			# TakePartyItem("00SWDL09")
			# GiveItemCreate("Misc07", Protagonist, 2000, 0, 0)
			self.iAddXpVar("'Level_3_Hard'", 36407)
			self.iTakePartyItem("'00SWDL09'")
			utils_pc.pc_party_receive_money_and_print(2000 * const_toee.gp)
			# 181: I am grateful, priestess.
			
		elif index == 26:
			# AddXpVar("Level_3_Hard",36407)
			# TakePartyItem("00SWDL09")
			# SetGlobal("SR_Emma_Heal","GLOBAL", 1)
			self.iAddXpVar("'Level_3_Hard'", 36407)
			self.iTakePartyItem("'00SWDL09'")
			self.iSetGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1)
			# 182: I am grateful, priestess, but I cannot accept a reward.  The tenets of my faith do not allow it.
			
		elif index == 27:
			# AddXpVar("Level_3_Hard",36407)
			# TakePartyItem("00SWDL09")
			# SetGlobal("SR_Emma_Heal","GLOBAL", 1)
			self.iAddXpVar("'Level_3_Hard'", 36407)
			self.iTakePartyItem("'00SWDL09'")
			self.iSetGlobal("'SR_Emma_Heal'", "'GLOBAL'", 1)
			# 183: I am grateful, priestess, but I cannot accept a reward.  The tenets of my faith do not allow it.
			
		elif index == 28:
			# AddXpVar("Level_4_Hard",36408)
			self.iAddXpVar("'Level_4_Hard'", 36408)
			# 184: No reward is necessary, Priestess.  I am glad to have been of aid to those in need.
			
		elif index == 29:
			# StartStore("20Emma", Protagonist)
			self.iStartStore("'20Emma'", "Protagonist")
			# 191: I am in need of healing.
			
		elif index == 30:
			# StartStore("20EmDis", Protagonist)
			self.iStartStore("'20EmDis'", "Protagonist")
			# 192: I am in need of healing.
			
		elif index == 31:
			# FadeToColor([0.0],0)
			# RestUntilHealed()
			# FadeFromColor([0.0],0)
			self.iFadeToColor("[0.0]", 0)
			self.iRestUntilHealed()
			self.iFadeFromColor("[0.0]", 0)
			# 193: Would you mind if I rested here?
			
		elif index == 32:
			# StartStore("20EmDis", Protagonist)
			self.iStartStore("'20EmDis'", "Protagonist")
			# 201: I am in need of healing.
			
		elif index == 33:
			# FadeToColor([0.0],0)
			# RestUntilHealed()
			# FadeFromColor([0.0],0)
			self.iFadeToColor("[0.0]", 0)
			self.iRestUntilHealed()
			self.iFadeFromColor("[0.0]", 0)
			# 202: Would you mind if I rested here?
			
		elif index == 34:
			# SetNumTimesTalkedTo(0)
			self.iSetNumTimesTalkedTo(0)
			# 321: Continue
			
		elif index == 35:
			# Enemy()
			self.iEnemy()
			# 331: We shall see who pays, Emma!
			
		elif index == 36:
			# Enemy()
			self.iEnemy()
			# 341: We shall see who pays, Emma!
			
		elif index == 37:
			# Enemy()
			self.iEnemy()
			# 351: We shall see who pays, Emma!
			
		elif index == 38:
			# Enemy()
			self.iEnemy()
			# 361: We shall see who pays, Emma!
			
		elif index == 39:
			# TakePartyItem("00SWDL09")
			self.iTakePartyItem("'00SWDL09'")
			# 231: Here it is.
			
		elif index == 40:
			# StartCutScene("20cEmma2")
			self.iStartCutScenePost(scr_20cemma2.Script_20cEmma2, self.locus_make())
			# 241: You will not escape me, priestess!
			
		elif index == 41:
			# TakePartyItem("00SWDL09")
			self.iTakePartyItem("'00SWDL09'")
			# 251: Here it is.
			
		elif index == 42:
			# StartCutScene("20cEmma2")
			self.iStartCutScenePost(scr_20cemma2.Script_20cEmma2, self.locus_make())
			# 261: You will not escape me, priestess!
			
		return # dialog_action_do
		
	def get_dialog_trigger_max_index(self): return 27
	
	def get_state_to_line(self, state):
		if state==0: return 60
		if state==1: return 70
		if state==2: return 280
		if state==3: return 270
		if state==4: return 80
		if state==5: return 90
		if state==6: return 100
		if state==7: return 140
		if state==8: return 150
		if state==9: return 160
		if state==10: return 170
		if state==11: return 110
		if state==12: return 120
		if state==13: return 130
		if state==14: return 290
		if state==15: return 300
		if state==16: return 310
		if state==17: return 180
		if state==18: return 190
		if state==19: return 200
		if state==20: return 210
		if state==21: return 220
		if state==22: return 320
		if state==23: return 330
		if state==24: return 340
		if state==25: return 350
		if state==26: return 360
		if state==27: return 230
		if state==28: return 240
		if state==29: return 250
		if state==30: return 260
		return
	
	def setup_scripts(self, npc):
		super(Ctrl_20EMMA_AR2100_Emma_Auto, self).setup_scripts(npc)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		self.enable_dialog(npc)
		return
	
class Ctrl_20KRIS_AR2100_Kristian_Auto(py21002_ar2100_npc_classes.Ctrl_20KRIS): # 20KRIS 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_21krisc.Script_21KRISC

class Ctrl_20KNTVIR_AR2100_WarriorofVirtue1_Auto(py21002_ar2100_npc_classes.Ctrl_20KNTVIR): # 20KNTVIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_21wovc.Script_21WOVC

class Ctrl_20KNTVIR_AR2100_WarriorofVirtue2_Auto(py21002_ar2100_npc_classes.Ctrl_20KNTVIR): # 20KNTVIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_21wovc.Script_21WOVC

class Ctrl_20KNTVIR_AR2100_WarriorofVirtue3_Auto(py21002_ar2100_npc_classes.Ctrl_20KNTVIR): # 20KNTVIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def get_bcs_combat(self):
		return scr_21wovc.Script_21WOVC

