import toee, debug
import module_consts, utils_storage, ctrl_daemon2, ctrl_daemon_ie, ctrl_ambients, inf_scripting, utils_obj
import const_toee
from bcs import scr_000test_shawford_crale1_auto
#### IMPORTS ####
import py12014_ar1201_npc_inst_classes
from bcs import scr_000test_shawford_crale1
from bcs import scr_000test_shawford_crale2
#### END IMPORTS ####
DAEMON_SCRIPT_ID = 12010
DAEMON_MAP_ID = module_consts.MAP_ID_AR1201
DAEMON_GID = "G_5F057E54_EA65_4343_A14D_1BE06C37B75B"

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, DAEMON_MAP_ID, CtrlAR1201)

def san_first_heartbeat(attachee, triggerer):
	#print(attachee.id)
	#debug.breakp("")
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, DAEMON_MAP_ID, CtrlAR1201)

def san_heartbeat(attachee, triggerer): return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, DAEMON_MAP_ID, cs())

def san_dying(attachee, triggerer): return ctrl_daemon2.do_san_dying(attachee, triggerer, DAEMON_MAP_ID, cs())

def san_use(attachee, triggerer): return ctrl_daemon2.do_san_use(attachee, triggerer, DAEMON_MAP_ID, cs())

def cs():
	o = utils_storage.obj_storage_by_id(DAEMON_GID)
	if (not o): return None
	result = o.data.get(CtrlAR1201.get_name())
	assert isinstance(result, CtrlAR1201)
	return result

class CtrlAR1201(ctrl_daemon_ie.CtrlDaemonIE):
	def created(self, npc):
		self.init_daemon2_fields(DAEMON_MAP_ID, DAEMON_SCRIPT_ID, "daemon_ar1201")
		super(CtrlAR1201, self).created(npc)
		return
	
	def place_encounters_initial(self):
		super(CtrlAR1201, self).place_encounters_initial()
		#scr_000test_shawford_crale1_auto.Script_000TEST_Shawford_Crale1_Auto.do_execute(self, continuous=True)
		scr_000test_shawford_crale2.Script_000TEST_Shawford_Crale2.do_execute(self, continuous=True)
		return
	
	def place_npcs_auto(self):
		# Shawford_Crale: 12SHAWFO (477.5, 478.8) const_toee.ROT06 ctrl: py12014_ar1201_npc_inst_classes.Ctrl_12SHAWFO_AR1201_Shawford_Crale 
		ctrl_class, loc = py12014_ar1201_npc_inst_classes.Ctrl_12SHAWFO_AR1201_Shawford_Crale,  utils_obj.sec2loc(477, 478)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Shawford_Crale", 0, 1)
		
		return
	
	def place_bcs_auto(self):
		self.vars["script_area"] = scr_000test_shawford_crale2.Script_000TEST_Shawford_Crale2
		return

	def setup_ambients_auto(self):
		ctrl_class, loc = ctrl_ambients.CtrlAmbient, utils_obj.sec2loc(480, 475)
		npc, ctrl = self.create_cabbage(loc, ctrl_class, None)
		ctrl.setup(name="Fireplace", flags="Enabled, Looping", frequency=0, frequency_variation=0, radius=500, x=480, y=475, schedule="ALL")
		ctrl.setup_sound(sound_id=4275, durationf=7.583356, volume=65, title="AR1201\Fireplace AM1201A")
		ctrl.run(npc)
		
		return
