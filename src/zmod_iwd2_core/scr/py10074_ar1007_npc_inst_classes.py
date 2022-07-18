import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting
#### IMPORTS ####
import py10073_ar1007_npc_inst_classes_auto
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
class Ctrl_10GOBC_AR1007_Goblin_1(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_1_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_2(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_2_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_3(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_3_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_4(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_4_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_5(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_5_Auto): # 10GOBC 
	pass

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_1(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBSC_AR1007_Goblin_Sapper_1_Auto): # 10GOBSC 
	pass

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_2(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBSC_AR1007_Goblin_Sapper_2_Auto): # 10GOBSC 
	pass

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_3(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBSC_AR1007_Goblin_Sapper_3_Auto): # 10GOBSC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_6(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_6_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_7(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_7_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_8(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_8_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_9(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_9_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_10(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_10_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_11(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_11_Auto): # 10GOBC 
	pass

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_4(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBSC_AR1007_Goblin_Sapper_4_Auto): # 10GOBSC 
	pass

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_5(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBSC_AR1007_Goblin_Sapper_5_Auto): # 10GOBSC 
	pass

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_6(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBSC_AR1007_Goblin_Sapper_6_Auto): # 10GOBSC 
	pass

class Ctrl_10GOBD_AR1007_Dead_Goblin(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBD_AR1007_Dead_Goblin_Auto): # 10GOBD 
	pass

class Ctrl_10GOBC_AR1007_Goblin_12(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_12_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_13(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_13_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_14(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_14_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_15(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_15_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_16(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_16_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_17(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_17_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_18(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_18_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_19(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_19_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_20(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_20_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_21(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_21_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_22(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_22_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_23(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_23_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_24(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_24_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_25(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_25_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_26(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_26_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_27(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_27_Auto): # 10GOBC 
	pass

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_7(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBSC_AR1007_Goblin_Sapper_7_Auto): # 10GOBSC 
	pass

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_8(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBSC_AR1007_Goblin_Sapper_8_Auto): # 10GOBSC 
	pass

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_9(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBSC_AR1007_Goblin_Sapper_9_Auto): # 10GOBSC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_28(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_28_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_29(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_29_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_30(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_30_Auto): # 10GOBC 
	pass

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_10(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBSC_AR1007_Goblin_Sapper_10_Auto): # 10GOBSC 
	pass

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_11(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBSC_AR1007_Goblin_Sapper_11_Auto): # 10GOBSC 
	pass

class Ctrl_10GOBSC_AR1007_Goblin_Sapper_12(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBSC_AR1007_Goblin_Sapper_12_Auto): # 10GOBSC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_31(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_31_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_32(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_32_Auto): # 10GOBC 
	pass

class Ctrl_10GOBC_AR1007_Goblin_33(py10073_ar1007_npc_inst_classes_auto.Ctrl_10GOBC_AR1007_Goblin_33_Auto): # 10GOBC 
	pass

class Ctrl_10RUKWU_AR1007_Rukwurm(py10073_ar1007_npc_inst_classes_auto.Ctrl_10RUKWU_AR1007_Rukwurm_Auto): # 10RUKWU 
	pass

class Ctrl_10ULEK_AR1007_Ulek(py10073_ar1007_npc_inst_classes_auto.Ctrl_10ULEK_AR1007_Ulek_Auto): # 10ULEK 
	pass

