import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting
#### IMPORTS ####
import py12013_ar1201_npc_inst_classes_auto
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
class Ctrl_12SHAWFO_AR1201_Shawford_Crale(py12013_ar1201_npc_inst_classes_auto.Ctrl_12SHAWFO_AR1201_Shawford_Crale_Auto): # 12SHAWFO 

	def setup_appearance(self, npc):
		super(Ctrl_12SHAWFO_AR1201_Shawford_Crale, self).setup_appearance(npc)
		npc.obj_set_int(toee.obj_f_critter_portrait, 7470) # NPC_7472_s_Tarim, NPC_7132_s_RomagCommander, NPC_7062_s_JarvisHann
		return 
	
class Ctrl_12MESS_AR1201_Messenger_Hidden(py12013_ar1201_npc_inst_classes_auto.Ctrl_12MESS_AR1201_Messenger_Hidden_Auto): # 12MESS 

	def setup_appearance(self, npc):
		super(Ctrl_12MESS_AR1201_Messenger_Hidden, self).setup_appearance(npc)
		npc.obj_set_int(toee.obj_f_critter_portrait, 7770) # NPC_7772_s_Courier
		return 
class Ctrl_12SWIFTH_AR1201_Swift_Thomas_Hidden(py12013_ar1201_npc_inst_classes_auto.Ctrl_12SWIFTH_AR1201_Swift_Thomas_Hidden_Auto): # 12SWIFTH 
	pass

class Ctrl_12NOLAN_AR1201_Nolan(py12013_ar1201_npc_inst_classes_auto.Ctrl_12NOLAN_AR1201_Nolan_Auto): # 12NOLAN 
	pass

