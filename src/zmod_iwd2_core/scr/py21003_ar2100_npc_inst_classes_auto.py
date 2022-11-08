import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting, module_difficulty
#### IMPORTS ####
import py21002_ar2100_npc_classes
#### END IMPORTS ####

#### GVARS ####
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
	
	def setup_bcs(self):
		return

class Ctrl_21WERRAT_AR2100_GTH01_01_Auto(py21002_ar2100_npc_classes.Ctrl_21WERRAT): # 21WERRAT 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21WERRAT_AR2100_GTH01_03_Auto(py21002_ar2100_npc_classes.Ctrl_21WERRAT): # 21WERRAT 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21WERRAT_AR2100_GTH01_09_Auto(py21002_ar2100_npc_classes.Ctrl_21WERRAT): # 21WERRAT 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21WERBGR_AR2100_GTH01_02_Auto(py21002_ar2100_npc_classes.Ctrl_21WERBGR): # 21WERBGR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21WERBGR_AR2100_GTH01_10_Auto(py21002_ar2100_npc_classes.Ctrl_21WERBGR): # 21WERBGR 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21WERBGR_AR2100_GTH01_06_Auto(py21002_ar2100_npc_classes.Ctrl_21WERBGR): # 21WERBGR 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2100_GTH01_07_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2100_GTH01_08_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2100_GTH01_11_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2100_GTH01_05_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2100_GTH01_04_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2100_GTH01_12_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21WERRAT_AR2100_GTH02_10_Auto(py21002_ar2100_npc_classes.Ctrl_21WERRAT): # 21WERRAT 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21WERRAT_AR2100_GTH02_01_Auto(py21002_ar2100_npc_classes.Ctrl_21WERRAT): # 21WERRAT 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21WERBGR_AR2100_GTH02_09_Auto(py21002_ar2100_npc_classes.Ctrl_21WERBGR): # 21WERBGR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21WERBGR_AR2100_GTH02_02_Auto(py21002_ar2100_npc_classes.Ctrl_21WERBGR): # 21WERBGR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2100_GTH02_08_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2100_GTH02_07_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2100_GTH02_06_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2100_GTH02_05_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2100_GTH02_03_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2100_GTH02_04_Auto(py21002_ar2100_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21OGR_AR2100_Ogre_Auto(py21002_ar2100_npc_classes.Ctrl_21OGR): # 21OGR 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21SPDQN_AR2100_Spider_Queen_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDQN): # 21SPDQN 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21SPDSML_AR2100_Spider_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDSML): # 21SPDSML 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21SPDSML_AR2100_Spider_2_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDSML): # 21SPDSML 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21SPDSML_AR2100_Spider_3_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDSML): # 21SPDSML 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21SPDSML_AR2100_Spider_4_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDSML): # 21SPDSML 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21SPDSML_AR2100_Spider_5_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDSML): # 21SPDSML 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21SPDSML_AR2100_Spider_6_Auto(py21002_ar2100_npc_classes.Ctrl_21SPDSML): # 21SPDSML 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_21HGHSNK_AR2100_Highland_Snake_Auto(py21002_ar2100_npc_classes.Ctrl_21HGHSNK): # 21HGHSNK 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_21HGHSNK_AR2100_Highland_Snake_2_Auto(py21002_ar2100_npc_classes.Ctrl_21HGHSNK): # 21HGHSNK 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_21HGHSNK_AR2100_Highland_Snake_3_Auto(py21002_ar2100_npc_classes.Ctrl_21HGHSNK): # 21HGHSNK 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_21HRP_AR2100_Harpy_Auto(py21002_ar2100_npc_classes.Ctrl_21HRP): # 21HRP 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_21HRP_AR2100_Harpy_2_Auto(py21002_ar2100_npc_classes.Ctrl_21HRP): # 21HRP 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_21HRP_AR2100_Harpy_3_Auto(py21002_ar2100_npc_classes.Ctrl_21HRP): # 21HRP 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_21HRP_AR2100_Harpy_4_Auto(py21002_ar2100_npc_classes.Ctrl_21HRP): # 21HRP 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_21VERB_AR2100_Verbeeg_Auto(py21002_ar2100_npc_classes.Ctrl_21VERB): # 21VERB 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_21VERB_AR2100_Verbeeg_2_Auto(py21002_ar2100_npc_classes.Ctrl_21VERB): # 21VERB 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_21VERB_AR2100_Verbeeg_3_Auto(py21002_ar2100_npc_classes.Ctrl_21VERB): # 21VERB 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_21WERRAT_AR2100_Wererat_Scripted_Event_Auto(py21002_ar2100_npc_classes.Ctrl_21WERRAT): # 21WERRAT 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20EMMA_AR2100_Emma_Auto(py21002_ar2100_npc_classes.Ctrl_20EMMA): # 20EMMA 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20KRIS_AR2100_Kristian_Auto(py21002_ar2100_npc_classes.Ctrl_20KRIS): # 20KRIS 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20KNTVIR_AR2100_WarriorofVirtue1_Auto(py21002_ar2100_npc_classes.Ctrl_20KNTVIR): # 20KNTVIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20KNTVIR_AR2100_WarriorofVirtue2_Auto(py21002_ar2100_npc_classes.Ctrl_20KNTVIR): # 20KNTVIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20KNTVIR_AR2100_WarriorofVirtue3_Auto(py21002_ar2100_npc_classes.Ctrl_20KNTVIR): # 20KNTVIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

