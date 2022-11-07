import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting, module_difficulty
#### IMPORTS ####
import py21003_ar2100_npc_inst_classes_auto
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
class Ctrl_21GAERNT_AR2100_Gaernat_Sharptooth(py21003_ar2100_npc_inst_classes_auto.Ctrl_21GAERNT_AR2100_Gaernat_Sharptooth_Auto): # 21GAERNT 
	pass

class Ctrl_21WERRAT_AR2100_GTH01_01(py21003_ar2100_npc_inst_classes_auto.Ctrl_21WERRAT_AR2100_GTH01_01_Auto): # 21WERRAT 
	pass

class Ctrl_21WERRAT_AR2100_GTH01_03(py21003_ar2100_npc_inst_classes_auto.Ctrl_21WERRAT_AR2100_GTH01_03_Auto): # 21WERRAT 
	pass

class Ctrl_21WERRAT_AR2100_GTH01_09(py21003_ar2100_npc_inst_classes_auto.Ctrl_21WERRAT_AR2100_GTH01_09_Auto): # 21WERRAT 
	pass

class Ctrl_21WERBGR_AR2100_GTH01_02(py21003_ar2100_npc_inst_classes_auto.Ctrl_21WERBGR_AR2100_GTH01_02_Auto): # 21WERBGR 
	pass

class Ctrl_21WERBGR_AR2100_GTH01_10(py21003_ar2100_npc_inst_classes_auto.Ctrl_21WERBGR_AR2100_GTH01_10_Auto): # 21WERBGR 
	pass

class Ctrl_21WERBGR_AR2100_GTH01_06(py21003_ar2100_npc_inst_classes_auto.Ctrl_21WERBGR_AR2100_GTH01_06_Auto): # 21WERBGR 
	pass

class Ctrl_20ORCSHM_AR2100_GTH01_07(py21003_ar2100_npc_inst_classes_auto.Ctrl_20ORCSHM_AR2100_GTH01_07_Auto): # 20ORCSHM 
	pass

class Ctrl_20ORCSHM_AR2100_GTH01_08(py21003_ar2100_npc_inst_classes_auto.Ctrl_20ORCSHM_AR2100_GTH01_08_Auto): # 20ORCSHM 
	pass

class Ctrl_20ORCSHM_AR2100_GTH01_11(py21003_ar2100_npc_inst_classes_auto.Ctrl_20ORCSHM_AR2100_GTH01_11_Auto): # 20ORCSHM 
	pass

class Ctrl_20ORCACH_AR2100_GTH01_05(py21003_ar2100_npc_inst_classes_auto.Ctrl_20ORCACH_AR2100_GTH01_05_Auto): # 20ORCACH 
	pass

class Ctrl_20ORCACH_AR2100_GTH01_04(py21003_ar2100_npc_inst_classes_auto.Ctrl_20ORCACH_AR2100_GTH01_04_Auto): # 20ORCACH 
	pass

class Ctrl_20ORCACH_AR2100_GTH01_12(py21003_ar2100_npc_inst_classes_auto.Ctrl_20ORCACH_AR2100_GTH01_12_Auto): # 20ORCACH 
	pass

class Ctrl_21WERRAT_AR2100_GTH02_10(py21003_ar2100_npc_inst_classes_auto.Ctrl_21WERRAT_AR2100_GTH02_10_Auto): # 21WERRAT 
	pass

class Ctrl_21WERRAT_AR2100_GTH02_01(py21003_ar2100_npc_inst_classes_auto.Ctrl_21WERRAT_AR2100_GTH02_01_Auto): # 21WERRAT 
	pass

class Ctrl_21WERBGR_AR2100_GTH02_09(py21003_ar2100_npc_inst_classes_auto.Ctrl_21WERBGR_AR2100_GTH02_09_Auto): # 21WERBGR 
	pass

class Ctrl_21WERBGR_AR2100_GTH02_02(py21003_ar2100_npc_inst_classes_auto.Ctrl_21WERBGR_AR2100_GTH02_02_Auto): # 21WERBGR 
	pass

class Ctrl_20ORCSHM_AR2100_GTH02_08(py21003_ar2100_npc_inst_classes_auto.Ctrl_20ORCSHM_AR2100_GTH02_08_Auto): # 20ORCSHM 
	pass

class Ctrl_20ORCSHM_AR2100_GTH02_07(py21003_ar2100_npc_inst_classes_auto.Ctrl_20ORCSHM_AR2100_GTH02_07_Auto): # 20ORCSHM 
	pass

class Ctrl_20ORCACH_AR2100_GTH02_06(py21003_ar2100_npc_inst_classes_auto.Ctrl_20ORCACH_AR2100_GTH02_06_Auto): # 20ORCACH 
	pass

class Ctrl_20ORCACH_AR2100_GTH02_05(py21003_ar2100_npc_inst_classes_auto.Ctrl_20ORCACH_AR2100_GTH02_05_Auto): # 20ORCACH 
	pass

class Ctrl_20ORCA3_AR2100_GTH02_03(py21003_ar2100_npc_inst_classes_auto.Ctrl_20ORCA3_AR2100_GTH02_03_Auto): # 20ORCA3 
	pass

class Ctrl_20ORCA3_AR2100_GTH02_04(py21003_ar2100_npc_inst_classes_auto.Ctrl_20ORCA3_AR2100_GTH02_04_Auto): # 20ORCA3 
	pass

class Ctrl_21OGR_AR2100_Ogre(py21003_ar2100_npc_inst_classes_auto.Ctrl_21OGR_AR2100_Ogre_Auto): # 21OGR 
	pass

class Ctrl_21SPDQN_AR2100_Spider_Queen(py21003_ar2100_npc_inst_classes_auto.Ctrl_21SPDQN_AR2100_Spider_Queen_Auto): # 21SPDQN 
	pass

class Ctrl_21SPDSML_AR2100_Spider(py21003_ar2100_npc_inst_classes_auto.Ctrl_21SPDSML_AR2100_Spider_Auto): # 21SPDSML 
	pass

class Ctrl_21HGHSNK_AR2100_Highland_Snake(py21003_ar2100_npc_inst_classes_auto.Ctrl_21HGHSNK_AR2100_Highland_Snake_Auto): # 21HGHSNK 
	pass

class Ctrl_21HRP_AR2100_Harpy(py21003_ar2100_npc_inst_classes_auto.Ctrl_21HRP_AR2100_Harpy_Auto): # 21HRP 
	pass

class Ctrl_21VERB_AR2100_Verbeeg(py21003_ar2100_npc_inst_classes_auto.Ctrl_21VERB_AR2100_Verbeeg_Auto): # 21VERB 
	pass

class Ctrl_21WERRAT_AR2100_Wererat_Scripted_Event(py21003_ar2100_npc_inst_classes_auto.Ctrl_21WERRAT_AR2100_Wererat_Scripted_Event_Auto): # 21WERRAT 
	pass

class Ctrl_20EMMA_AR2100_Emma(py21003_ar2100_npc_inst_classes_auto.Ctrl_20EMMA_AR2100_Emma_Auto): # 20EMMA 
	pass

class Ctrl_20KRIS_AR2100_Kristian(py21003_ar2100_npc_inst_classes_auto.Ctrl_20KRIS_AR2100_Kristian_Auto): # 20KRIS 
	pass

class Ctrl_20KNTVIR_AR2100_WarriorofVirtue1(py21003_ar2100_npc_inst_classes_auto.Ctrl_20KNTVIR_AR2100_WarriorofVirtue1_Auto): # 20KNTVIR 
	pass

class Ctrl_20KNTVIR_AR2100_WarriorofVirtue2(py21003_ar2100_npc_inst_classes_auto.Ctrl_20KNTVIR_AR2100_WarriorofVirtue2_Auto): # 20KNTVIR 
	pass

class Ctrl_20KNTVIR_AR2100_WarriorofVirtue3(py21003_ar2100_npc_inst_classes_auto.Ctrl_20KNTVIR_AR2100_WarriorofVirtue3_Auto): # 20KNTVIR 
	pass

