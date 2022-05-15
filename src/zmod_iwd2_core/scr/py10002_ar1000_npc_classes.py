import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting
#### IMPORTS ####
import py10001_ar1000_npc_classes_auto
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
class Ctrl_10HEDRON(py10001_ar1000_npc_classes_auto.Ctrl_10HEDRON_Auto): # 10HEDRON 
	pass

class Ctrl_10ELDGUL(py10001_ar1000_npc_classes_auto.Ctrl_10ELDGUL_Auto): # 10ELDGUL 
	pass

class Ctrl_10SCREED(py10001_ar1000_npc_classes_auto.Ctrl_10SCREED_Auto): # 10SCREED 
	pass

class Ctrl_10REIG(py10001_ar1000_npc_classes_auto.Ctrl_10REIG_Auto): # 10REIG 
	pass

class Ctrl_10JON(py10001_ar1000_npc_classes_auto.Ctrl_10JON_Auto): # 10JON 
	pass

class Ctrl_10BROGAN(py10001_ar1000_npc_classes_auto.Ctrl_10BROGAN_Auto): # 10BROGAN 
	pass

class Ctrl_10JORUN(py10001_ar1000_npc_classes_auto.Ctrl_10JORUN_Auto): # 10JORUN 
	pass

class Ctrl_10GOB(py10001_ar1000_npc_classes_auto.Ctrl_10GOB_Auto): # 10GOB 
	pass

class Ctrl_10GOBD(py10001_ar1000_npc_classes_auto.Ctrl_10GOBD_Auto): # 10GOBD 
	pass

class Ctrl_10MALED(py10001_ar1000_npc_classes_auto.Ctrl_10MALED_Auto): # 10MALED 
	pass

class Ctrl_10SOLDRD(py10001_ar1000_npc_classes_auto.Ctrl_10SOLDRD_Auto): # 10SOLDRD 
	pass

class Ctrl_10GOBARD(py10001_ar1000_npc_classes_auto.Ctrl_10GOBARD_Auto): # 10GOBARD 
	pass

class Ctrl_10SAILRD(py10001_ar1000_npc_classes_auto.Ctrl_10SAILRD_Auto): # 10SAILRD 
	pass

class Ctrl_10GOBAR(py10001_ar1000_npc_classes_auto.Ctrl_10GOBAR_Auto): # 10GOBAR 
	pass

class Ctrl_10CRANDA(py10001_ar1000_npc_classes_auto.Ctrl_10CRANDA_Auto): # 10CRANDA 
	pass

class Ctrl_12SWIFTH(py10001_ar1000_npc_classes_auto.Ctrl_12SWIFTH_Auto): # 12SWIFTH 
	pass

class Ctrl_10HINT(py10001_ar1000_npc_classes_auto.Ctrl_10HINT_Auto): # 10HINT 
	pass

class Ctrl_10FIRTHH(py10001_ar1000_npc_classes_auto.Ctrl_10FIRTHH_Auto): # 10FIRTHH 
	pass

