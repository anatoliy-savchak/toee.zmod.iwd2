import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting
#### IMPORTS ####
import py10002_ar1000_npc_classes
from bcs import scr_00t01m
from bcs import scr_00aatgn
from bcs import scr_10onboat
from bcs import scr_00amvr
from bcs import scr_00t00det
from bcs import scr_10hedro0
from bcs import scr_10eldgum
from bcs import scr_10screem
from bcs import scr_10reig0
from bcs import scr_10agobc0
from bcs import scr_00t02m
from bcs import scr_00t02et
from bcs import scr_00townid
from bcs import scr_10jon0
from bcs import scr_10broga0
from bcs import scr_10jorun0
from bcs import scr_00t03m
from bcs import scr_10gobf0
from bcs import scr_10gobm0
from bcs import scr_00amvw05
from bcs import scr_00t03t
from bcs import scr_00t04m
from bcs import scr_00t04t
from bcs import scr_00t05m
from bcs import scr_00t05t
from bcs import scr_00t06m
from bcs import scr_00t06t
from bcs import scr_10gobr0
from bcs import scr_00t07m
from bcs import scr_00t07t
from bcs import scr_00t08m
from bcs import scr_00t08t
from bcs import scr_10crand0
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
class Ctrl_10HEDRON_AR1000_Hedron_Auto(py10002_ar1000_npc_classes.Ctrl_10HEDRON): # 10HEDRON 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t01m.Script_00T01M
		self.vars["bcs_class"] = scr_00aatgn.Script_00AATGN
		self.vars["bcs_combat"] = scr_10onboat.Script_10ONBOAT
		self.vars["bcs_movement"] = scr_00amvr.Script_00AMVR
		self.vars["bcs_team"] = scr_00t00det.Script_00T00DET
		self.vars["bcs_special_one"] = scr_10hedro0.Script_10HEDRO0
		return

class Ctrl_10ELDGUL_AR1000_Eldgull_Auto(py10002_ar1000_npc_classes.Ctrl_10ELDGUL): # 10ELDGUL 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t01m.Script_00T01M
		self.vars["bcs_class"] = scr_00aatgn.Script_00AATGN
		self.vars["bcs_combat"] = scr_10onboat.Script_10ONBOAT
		self.vars["bcs_movement"] = scr_10eldgum.Script_10ELDGUM
		self.vars["bcs_team"] = scr_00t00det.Script_00T00DET
		return

class Ctrl_10SCREED_AR1000_Screed_Auto(py10002_ar1000_npc_classes.Ctrl_10SCREED): # 10SCREED 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t01m.Script_00T01M
		self.vars["bcs_class"] = scr_00aatgn.Script_00AATGN
		self.vars["bcs_combat"] = scr_10onboat.Script_10ONBOAT
		self.vars["bcs_movement"] = scr_10screem.Script_10SCREEM
		self.vars["bcs_team"] = scr_00t00det.Script_00T00DET
		return

class Ctrl_10REIG_AR1000_Reig_Auto(py10002_ar1000_npc_classes.Ctrl_10REIG): # 10REIG 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_10reig0.Script_10REIG0
		self.vars["bcs_class"] = scr_00aatgn.Script_00AATGN
		self.vars["bcs_combat"] = scr_10agobc0.Script_10AGOBC0
		self.vars["bcs_movement"] = scr_00t02m.Script_00T02M
		self.vars["bcs_team"] = scr_00t02et.Script_00T02ET
		self.vars["bcs_special_one"] = scr_00townid.Script_00TOWNID
		return

class Ctrl_10JON_AR1000_Jon_Auto(py10002_ar1000_npc_classes.Ctrl_10JON): # 10JON 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t02et.Script_00T02ET
		self.vars["bcs_class"] = scr_00aatgn.Script_00AATGN
		self.vars["bcs_combat"] = scr_10agobc0.Script_10AGOBC0
		self.vars["bcs_movement"] = scr_10jon0.Script_10JON0
		self.vars["bcs_team"] = scr_00t02et.Script_00T02ET
		self.vars["bcs_special_one"] = scr_00townid.Script_00TOWNID
		return

class Ctrl_10BROGAN_AR1000_Brogan_Auto(py10002_ar1000_npc_classes.Ctrl_10BROGAN): # 10BROGAN 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_10broga0.Script_10BROGA0
		self.vars["bcs_class"] = scr_00aatgn.Script_00AATGN
		self.vars["bcs_combat"] = scr_10agobc0.Script_10AGOBC0
		self.vars["bcs_movement"] = scr_00amvr.Script_00AMVR
		self.vars["bcs_special_one"] = scr_00townid.Script_00TOWNID
		return

class Ctrl_10JORUN_AR1000_Jorun_Auto(py10002_ar1000_npc_classes.Ctrl_10JORUN): # 10JORUN 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_10jorun0.Script_10JORUN0
		self.vars["bcs_class"] = scr_00aatgn.Script_00AATGN
		self.vars["bcs_combat"] = scr_10agobc0.Script_10AGOBC0
		self.vars["bcs_movement"] = scr_00amvr.Script_00AMVR
		self.vars["bcs_special_one"] = scr_00townid.Script_00TOWNID
		return

class Ctrl_10GOB_AR1000_1000_Goblin_01_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t03m.Script_00T03M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t03t.Script_00T03T
		return

class Ctrl_10GOBD_AR1000_Dead_Goblin_0_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBD): # 10GOBD 
	def setup_bcs(self):
		return

class Ctrl_10MALED_AR1000_Dead_Townsperson_0_Auto(py10002_ar1000_npc_classes.Ctrl_10MALED): # 10MALED 
	def setup_bcs(self):
		return

class Ctrl_10SOLDRD_AR1000_Brohn_Dead_Auto(py10002_ar1000_npc_classes.Ctrl_10SOLDRD): # 10SOLDRD 
	def setup_bcs(self):
		return

class Ctrl_10GOBD_AR1000_Dead_Goblin_1_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBD): # 10GOBD 
	def setup_bcs(self):
		return

class Ctrl_10GOBD_AR1000_Dead_Goblin_2_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBD): # 10GOBD 
	def setup_bcs(self):
		return

class Ctrl_10GOBD_AR1000_Dead_Goblin_3_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBD): # 10GOBD 
	def setup_bcs(self):
		return

class Ctrl_10SOLDRD_AR1000_Dead_Soldier_0_Auto(py10002_ar1000_npc_classes.Ctrl_10SOLDRD): # 10SOLDRD 
	def setup_bcs(self):
		return

class Ctrl_10GOBD_AR1000_Dead_Goblin_J1_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBD): # 10GOBD 
	def setup_bcs(self):
		return

class Ctrl_10GOBD_AR1000_Dead_Goblin_J2_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBD): # 10GOBD 
	def setup_bcs(self):
		return

class Ctrl_10GOBD_AR1000_Dead_Goblin_6_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBD): # 10GOBD 
	def setup_bcs(self):
		return

class Ctrl_10GOB_AR1000_1000_Goblin_02_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t04m.Script_00T04M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t04t.Script_00T04T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_03_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t04m.Script_00T04M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t04t.Script_00T04T
		return

class Ctrl_10MALED_AR1000_Dead_Townsperson_1_Auto(py10002_ar1000_npc_classes.Ctrl_10MALED): # 10MALED 
	def setup_bcs(self):
		return

class Ctrl_10GOBARD_AR1000_Dead_Goblin_7_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBARD): # 10GOBARD 
	def setup_bcs(self):
		return

class Ctrl_10SOLDRD_AR1000_Dead_Soldier_1_Auto(py10002_ar1000_npc_classes.Ctrl_10SOLDRD): # 10SOLDRD 
	def setup_bcs(self):
		return

class Ctrl_10SAILRD_AR1000_Dead_Sailor_Auto(py10002_ar1000_npc_classes.Ctrl_10SAILRD): # 10SAILRD 
	def setup_bcs(self):
		return

class Ctrl_10GOB_AR1000_1000_Goblin_04_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t05m.Script_00T05M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t05t.Script_00T05T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_05_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t05m.Script_00T05M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t05t.Script_00T05T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_06_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t06m.Script_00T06M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t06t.Script_00T06T
		return

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_01_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBAR): # 10GOBAR 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t06m.Script_00T06M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobr0.Script_10GOBR0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t06t.Script_00T06T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_07_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t06m.Script_00T06M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t06t.Script_00T06T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_19_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t06m.Script_00T06M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t06t.Script_00T06T
		return

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_02_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBAR): # 10GOBAR 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t06m.Script_00T06M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobr0.Script_10GOBR0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t06t.Script_00T06T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_08_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t06m.Script_00T06M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t06t.Script_00T06T
		return

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_03_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBAR): # 10GOBAR 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t06m.Script_00T06M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobr0.Script_10GOBR0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t04t.Script_00T04T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_09_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t04m.Script_00T04M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t04t.Script_00T04T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_10_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t04m.Script_00T04M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t04t.Script_00T04T
		return

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_04_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBAR): # 10GOBAR 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t04m.Script_00T04M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobr0.Script_10GOBR0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t04t.Script_00T04T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_11_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t03m.Script_00T03M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t03t.Script_00T03T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_12_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t03m.Script_00T03M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t03t.Script_00T03T
		return

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_05_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBAR): # 10GOBAR 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t03m.Script_00T03M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobr0.Script_10GOBR0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t03t.Script_00T03T
		return

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_06_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBAR): # 10GOBAR 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t03m.Script_00T03M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobr0.Script_10GOBR0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t03t.Script_00T03T
		return

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_07_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBAR): # 10GOBAR 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t05m.Script_00T05M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobr0.Script_10GOBR0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t05t.Script_00T05T
		return

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_08_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBAR): # 10GOBAR 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t05m.Script_00T05M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobr0.Script_10GOBR0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t05t.Script_00T05T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_13_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t05m.Script_00T05M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t05t.Script_00T05T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_14_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t07m.Script_00T07M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t07t.Script_00T07T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_15_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t07m.Script_00T07M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t07t.Script_00T07T
		return

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_09_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBAR): # 10GOBAR 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t07m.Script_00T07M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobr0.Script_10GOBR0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t07t.Script_00T07T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_16_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t08m.Script_00T08M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t08t.Script_00T08T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_17_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t08m.Script_00T08M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t08t.Script_00T08T
		return

class Ctrl_10GOB_AR1000_1000_Goblin_18_Auto(py10002_ar1000_npc_classes.Ctrl_10GOB): # 10GOB 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t08m.Script_00T08M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobm0.Script_10GOBM0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t08t.Script_00T08T
		return

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_10_Auto(py10002_ar1000_npc_classes.Ctrl_10GOBAR): # 10GOBAR 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_00t08m.Script_00T08M
		self.vars["bcs_class"] = scr_10gobf0.Script_10GOBF0
		self.vars["bcs_combat"] = scr_10gobr0.Script_10GOBR0
		self.vars["bcs_movement"] = scr_00amvw05.Script_00AMVW05
		self.vars["bcs_team"] = scr_00t08t.Script_00T08T
		return

class Ctrl_10CRANDA_AR1000_Crandall_Auto(py10002_ar1000_npc_classes.Ctrl_10CRANDA): # 10CRANDA 
	def setup_bcs(self):
		self.vars["bcs_general"] = scr_10agobc0.Script_10AGOBC0
		self.vars["bcs_class"] = scr_00aatgn.Script_00AATGN
		self.vars["bcs_movement"] = scr_10crand0.Script_10CRAND0
		self.vars["bcs_special_one"] = scr_00townid.Script_00TOWNID
		return

class Ctrl_10MALED_AR1000_Dead_Townsperson_2_Auto(py10002_ar1000_npc_classes.Ctrl_10MALED): # 10MALED 
	def setup_bcs(self):
		return

