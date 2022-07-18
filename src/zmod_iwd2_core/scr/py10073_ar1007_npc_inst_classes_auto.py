import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting
#### IMPORTS ####
import py10072_ar1007_npc_classes
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
class Ctrl_10GOBC_AR1007_Goblin_1_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_2_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_3_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_4_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_5_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_1_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBSC): # 10GOBSC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_2_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBSC): # 10GOBSC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_3_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBSC): # 10GOBSC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_6_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_7_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_8_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_9_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_10_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_11_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_4_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBSC): # 10GOBSC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_5_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBSC): # 10GOBSC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_6_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBSC): # 10GOBSC 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBD_AR1007_Dead_Goblin_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBD): # 10GOBD 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_12_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_13_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_14_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_15_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_16_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_17_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_18_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_19_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_20_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_21_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_22_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_23_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_24_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_25_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_26_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_27_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_7_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBSC): # 10GOBSC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_8_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBSC): # 10GOBSC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_9_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBSC): # 10GOBSC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_28_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_29_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_30_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_10_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBSC): # 10GOBSC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_11_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBSC): # 10GOBSC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_12_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBSC): # 10GOBSC 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_31_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_32_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10GOBC_AR1007_Goblin_33_Auto(py10072_ar1007_npc_classes.Ctrl_10GOBC): # 10GOBC 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10RUKWU_AR1007_Rukwurm_Auto(py10072_ar1007_npc_classes.Ctrl_10RUKWU): # 10RUKWU 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_10ULEK_AR1007_Ulek_Auto(py10072_ar1007_npc_classes.Ctrl_10ULEK): # 10ULEK 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

