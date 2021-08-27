import toee, debug, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee, ctrl_daemon
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import startup_zmod, utils_sneak, monster_info, copy, rttoee_consts, const_animate, const_sceneries
import const_proto_items, const_proto_cloth, const_proto_rings

ELDER_DAEMON_SCRIPT = 7002
ELDER_DAEMON_ID = "G_D9CB20A9_868D_471E_BE93_F44E63C41E80"
ELDER_DAEMON_DIALOG = 7002

def cs():
	return ctrl_daemon2.ccs(ELDER_DAEMON_ID, CtrlElder)

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_TOWER, CtrlTempleTower)

def san_first_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_TOWER, CtrlTempleTower)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_TOWER, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_TOWER, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_TOWER, cs())

class CtrlElder(ctrl_daemon2.CtrlDaemon2):
	def __init__(self):
		super(CtrlElder, self).__init__()
		self.init_daemon2_fields(rttoee_consts.MAP_ID_ELDER, ELDER_DAEMON_SCRIPT, "elder")
		return

	def place_encounters_initial(self):
		return
