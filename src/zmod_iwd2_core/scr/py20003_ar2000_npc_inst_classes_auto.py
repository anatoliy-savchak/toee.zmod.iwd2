import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting, module_difficulty
#### IMPORTS ####
import py20002_ar2000_npc_classes
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
class Ctrl_20ORCACH_AR2000_T1_Arch_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T1_Arch_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T1_Arch_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T1_Arch_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T1_Orc_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T1_Orc_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T1_Orc_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2000_T1_Shaman_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T1_Arch_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T1_Arch_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T1_Arch_7_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T1_Arch_8_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T1_Orc_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2000_T1_Shaman_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T1_Arch_9_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T1_Arch_10_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T1_Arch_11_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T1_Arch_12_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T1_Orc_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T1_Orc_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T1_Orc_7_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 1 # SetTeamBit(TEAM_1_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T2_Arch_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T2_Arch_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T2_Arch_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T2_Orch_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T2_Orc_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T2_Orc_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T2_Arch_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T2_Arch_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T2_Arch_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T2_Arch_7_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T2_Arch_8_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T2_Arch_9_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T2_Orc_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T2_Orc_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T2_Orc_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 2 # SetTeamBit(TEAM_2_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T3_Arch_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T3_Arch_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T3_Arch_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T3_Arch_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T3_Orc_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T3_Orc_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T3_Orc_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2000_T3_Shaman_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T3_Arch_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T3_Arch_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T3_Arch_7_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T3_Arch_8_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T3_Orc_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T3_Orc_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T3_Orc_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T3_Arch_9_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T3_Arch_10_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T3_Arch_11_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T3_Arch_12_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T3_Orc_7_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T3_Orc_8_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T3_Orc_9_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2000_T3_Shaman_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCFIR_AR2000_T3_Firestarter_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCFIR): # 20ORCFIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 3 # SetTeamBit(TEAM_3_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T4_Arch_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T4_Arch_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T4_Arch_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2000_T4_Shaman_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T4_Orc_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T4_Orc_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T4_Orc_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T4_Arch_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T4_Arch_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T4_Arch_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T4_Orc_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T4_Orc_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 4 # SetTeamBit(TEAM_4_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T5_Arch_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 10 # SetTeamBit(TEAM_10_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T5_Arch_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 10 # SetTeamBit(TEAM_10_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2000_T5_Shaman_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 10 # SetTeamBit(TEAM_10_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T5_Orc_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 10 # SetTeamBit(TEAM_10_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T5_Orc_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T5_Orc_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T5_Orc_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2000_T5_Shaman_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T5_Orc_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T5_Orc_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T5_Orc_7_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T5_Arch_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T5_Arch_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T5_Arch_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 10 # SetTeamBit(TEAM_10_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T5_Arch_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 10 # SetTeamBit(TEAM_10_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T5_Orc_8_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 10 # SetTeamBit(TEAM_10_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T5_Orc_9_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T5_Orc_10_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T5_Orc_11_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCFIR_AR2000_T5_Firestarter_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCFIR): # 20ORCFIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 5 # SetTeamBit(TEAM_5_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCFIR_AR2000_T9_Firestarter_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCFIR): # 20ORCFIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20ORCRUN_AR2000_T9_Runner_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCRUN): # 20ORCRUN 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T9_Archer_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T9_Archer_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T9_Archer_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T9_Archer_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T9_Archer_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T9_Archer_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T9_Archer_7_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T9_Archer_8_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T9_Archer_9_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 9 # SetTeamBit(TEAM_9_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T6_Orc_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T6_Orc_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T6_Orc_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T6_Arch_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T6_Arch_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2000_T6_Shaman_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T6_Arch_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T6_Arch_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T6_Orc_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T6_Orc_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T6_Orc_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T6_Arch_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA3_AR2000_T6_Arch_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA3): # 20ORCA3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T6_Orc_7_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T6_Orc_8_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T6_Orc_9_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T6_Arch_7_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T6_Arch_8_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T6_Arch_9_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T6_Arch_10_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 6 # SetTeamBit(TEAM_6_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCFIR_AR2000_T6_Firestarter_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCFIR): # 20ORCFIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20ORCRUN_AR2000_T6_Runner_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCRUN): # 20ORCRUN 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20ORCFIR_AR2000_T7_Firestarter_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCFIR): # 20ORCFIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 7 # SetTeamBit(TEAM_7_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCFIR_AR2000_T7_Firestarter_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCFIR): # 20ORCFIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 7 # SetTeamBit(TEAM_7_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2000_T7_Shaman_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 7 # SetTeamBit(TEAM_7_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T7_Orc_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 7 # SetTeamBit(TEAM_7_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T7_Orc_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 7 # SetTeamBit(TEAM_7_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T7_Orc_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 7 # SetTeamBit(TEAM_7_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T7_Orc_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 7 # SetTeamBit(TEAM_7_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T7_Orc_5_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 7 # SetTeamBit(TEAM_7_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T8_Orc_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T8_Orc_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T8_Orc_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 3
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T8_Arch_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCACH_AR2000_T8_Arch_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCACH): # 20ORCACH 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T8_Arch_3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCA4_AR2000_T8_Arch_4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCA4): # 20ORCA4 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2000_T8_Shaman_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 6
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW3_AR2000_T8_Orc_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW3): # 20ORCW3 
	@classmethod
	def get_difficulty_mask(cls):
		return 2
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T8_Orc_7_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T8_Orc_8_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T8_Orc_9_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCW4_AR2000_T8_Orc_10_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCW4): # 20ORCW4 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCSHM_AR2000_T8_Shaman_2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCSHM): # 20ORCSHM 
	@classmethod
	def get_difficulty_mask(cls):
		return 4
	
	@classmethod
	def get_team_number(cls):
		return 8 # SetTeamBit(TEAM_8_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCFIR_AR2000_T8_Firestarter_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCFIR): # 20ORCFIR 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20ORCRUN_AR2000_T8_Runner_1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCRUN): # 20ORCRUN 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T7_Orc_6_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 7 # SetTeamBit(TEAM_7_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T7_Orc_7_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 7 # SetTeamBit(TEAM_7_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCWAR_AR2000_T7_Orc_8_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCWAR): # 20ORCWAR 
	@classmethod
	def get_difficulty_mask(cls):
		return 1
	
	@classmethod
	def get_team_number(cls):
		return 7 # SetTeamBit(TEAM_7_BIT,TRUE)
	
	def setup_bcs(self):
		return

class Ctrl_20ORCCHF_AR2000_Torak1_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCCHF): # 20ORCCHF 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20ORCCHF_AR2000_Torak2_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCCHF): # 20ORCCHF 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20ORCCHF_AR2000_Torak3_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCCHF): # 20ORCCHF 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20ORCCHF_AR2000_Torak4_Auto(py20002_ar2000_npc_classes.Ctrl_20ORCCHF): # 20ORCCHF 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20DERETH_AR2000_Dereth_Auto(py20002_ar2000_npc_classes.Ctrl_20DERETH): # 20DERETH 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

class Ctrl_20SABRIN_AR2000_Sabrina_Auto(py20002_ar2000_npc_classes.Ctrl_20SABRIN): # 20SABRIN 
	@classmethod
	def get_difficulty_mask(cls):
		return 7
	
	@classmethod
	def get_team_number(cls):
		return 0 # no team script
	
	def setup_bcs(self):
		return

