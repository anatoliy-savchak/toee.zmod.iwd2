import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting
#### IMPORTS ####
import py20001_ar2000_npc_classes_auto
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
class Ctrl_20ORCACH(py20001_ar2000_npc_classes_auto.Ctrl_20ORCACH_Auto): # 20ORCACH 
	pass

class Ctrl_20ORCWAR(py20001_ar2000_npc_classes_auto.Ctrl_20ORCWAR_Auto): # 20ORCWAR 
	pass

class Ctrl_20ORCSHM(py20001_ar2000_npc_classes_auto.Ctrl_20ORCSHM_Auto): # 20ORCSHM 
	pass

class Ctrl_20ORCA3(py20001_ar2000_npc_classes_auto.Ctrl_20ORCA3_Auto): # 20ORCA3 
	pass

class Ctrl_20ORCW3(py20001_ar2000_npc_classes_auto.Ctrl_20ORCW3_Auto): # 20ORCW3 
	pass

class Ctrl_20ORCA4(py20001_ar2000_npc_classes_auto.Ctrl_20ORCA4_Auto): # 20ORCA4 
	pass

class Ctrl_20ORCW4(py20001_ar2000_npc_classes_auto.Ctrl_20ORCW4_Auto): # 20ORCW4 
	pass

class Ctrl_20ORCFIR(py20001_ar2000_npc_classes_auto.Ctrl_20ORCFIR_Auto): # 20ORCFIR 
	pass

class Ctrl_20ORCRUN(py20001_ar2000_npc_classes_auto.Ctrl_20ORCRUN_Auto): # 20ORCRUN 
	pass

class Ctrl_20ORCCHF(py20001_ar2000_npc_classes_auto.Ctrl_20ORCCHF_Auto): # 20ORCCHF 
	pass

class Ctrl_20DERETH(py20001_ar2000_npc_classes_auto.Ctrl_20DERETH_Auto): # 20DERETH 
	pass

class Ctrl_20SABRIN(py20001_ar2000_npc_classes_auto.Ctrl_20SABRIN_Auto): # 20SABRIN 
	pass

