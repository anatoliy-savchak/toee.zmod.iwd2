import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting, module_difficulty
#### IMPORTS ####
import py21001_ar2100_npc_classes_auto
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
class Ctrl_21GAERNT(py21001_ar2100_npc_classes_auto.Ctrl_21GAERNT_Auto): # 21GAERNT 
	pass

class Ctrl_21WERRAT(py21001_ar2100_npc_classes_auto.Ctrl_21WERRAT_Auto): # 21WERRAT 
	pass

class Ctrl_21WERBGR(py21001_ar2100_npc_classes_auto.Ctrl_21WERBGR_Auto): # 21WERBGR 
	pass

class Ctrl_20ORCSHM(py21001_ar2100_npc_classes_auto.Ctrl_20ORCSHM_Auto): # 20ORCSHM 
	pass

class Ctrl_20ORCACH(py21001_ar2100_npc_classes_auto.Ctrl_20ORCACH_Auto): # 20ORCACH 
	pass

class Ctrl_20ORCA3(py21001_ar2100_npc_classes_auto.Ctrl_20ORCA3_Auto): # 20ORCA3 
	pass

class Ctrl_21OGR(py21001_ar2100_npc_classes_auto.Ctrl_21OGR_Auto): # 21OGR 
	pass

class Ctrl_21SPDQN(py21001_ar2100_npc_classes_auto.Ctrl_21SPDQN_Auto): # 21SPDQN 
	pass

class Ctrl_21SPDSML(py21001_ar2100_npc_classes_auto.Ctrl_21SPDSML_Auto): # 21SPDSML 
	pass

class Ctrl_21HGHSNK(py21001_ar2100_npc_classes_auto.Ctrl_21HGHSNK_Auto): # 21HGHSNK 
	pass

class Ctrl_21HRP(py21001_ar2100_npc_classes_auto.Ctrl_21HRP_Auto): # 21HRP 
	pass

class Ctrl_21VERB(py21001_ar2100_npc_classes_auto.Ctrl_21VERB_Auto): # 21VERB 
	pass

class Ctrl_20EMMA(py21001_ar2100_npc_classes_auto.Ctrl_20EMMA_Auto): # 20EMMA 
	pass

class Ctrl_20KRIS(py21001_ar2100_npc_classes_auto.Ctrl_20KRIS_Auto): # 20KRIS 
	pass

class Ctrl_20KNTVIR(py21001_ar2100_npc_classes_auto.Ctrl_20KNTVIR_Auto): # 20KNTVIR 
	pass

