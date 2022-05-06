import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2
import utils_journal as uj, inf_scripting
#### IMPORT ####
import py10001_ar1000_npcs_auto
#### IMPORT END ####


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
MODULE_SCRIPT_ID = 10002
 
class Ctrl10HEDRON(py10001_ar1000_npcs_auto.Ctrl10HEDRONAuto): # 10HEDRON 
	pass

class Ctrl10ELDGUL(py10001_ar1000_npcs_auto.Ctrl10ELDGULAuto): # 10ELDGUL 
	pass

class Ctrl10SCREED(py10001_ar1000_npcs_auto.Ctrl10SCREEDAuto): # 10SCREED 
	pass

class Ctrl10REIG(py10001_ar1000_npcs_auto.Ctrl10REIGAuto): # 10REIG 
	pass

class Ctrl10JON(py10001_ar1000_npcs_auto.Ctrl10JONAuto): # 10JON 
	pass

class Ctrl10BROGAN(py10001_ar1000_npcs_auto.Ctrl10BROGANAuto): # 10BROGAN 
	pass

class Ctrl10JORUN(py10001_ar1000_npcs_auto.Ctrl10JORUNAuto): # 10JORUN 
	pass

class Ctrl10MALED(py10001_ar1000_npcs_auto.Ctrl10MALEDAuto): # 10MALED 
	pass

class Ctrl10SOLDRD(py10001_ar1000_npcs_auto.Ctrl10SOLDRDAuto): # 10SOLDRD 
	pass

class Ctrl10GOB(py10001_ar1000_npcs_auto.Ctrl10GOBAuto): # 10GOB 
	pass

class Ctrl10GOBD(py10001_ar1000_npcs_auto.Ctrl10GOBDAuto): # 10GOBD 
	pass

class Ctrl10GOBAR(py10001_ar1000_npcs_auto.Ctrl10GOBARAuto): # 10GOBAR 
	pass

class Ctrl10GOBARD(py10001_ar1000_npcs_auto.Ctrl10GOBARDAuto): # 10GOBARD 
	pass

class Ctrl10SAILRD(py10001_ar1000_npcs_auto.Ctrl10SAILRDAuto): # 10SAILRD 
	pass

class Ctrl10CRANDA(py10001_ar1000_npcs_auto.Ctrl10CRANDAAuto): # 10CRANDA 
	pass

