
import toee, debug, ctrl_daemon, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import module_consts

DROSKAR = 6810
DROSKAR_DAEMON_ID = "G_2714882F_81EF_4AE1_B9B3_A4F8D1CA239A"

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, module_consts.MAP_ID_ZMOD_GMD0_DROSKAR_CRUCIBLE, CtrlDroskar)

def san_first_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, module_consts.MAP_ID_ZMOD_GMD0_DROSKAR_CRUCIBLE, CtrlDroskar)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, module_consts.MAP_ID_ZMOD_GMD0_DROSKAR_CRUCIBLE, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, module_consts.MAP_ID_ZMOD_GMD0_DROSKAR_CRUCIBLE, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, module_consts.MAP_ID_ZMOD_GMD0_DROSKAR_CRUCIBLE, cs())

def cs():
	o = utils_storage.obj_storage_by_id(DROSKAR_DAEMON_ID)
	if (not o): return None
	if (CtrlDroskar.get_name() in o.data):
		result = o.data[CtrlDroskar.get_name()]
	else: return None
	assert isinstance(result, CtrlDroskar)
	return result

class CtrlDroskar(ctrl_daemon2.CtrlDaemon2):
	def __init__(self):
		super(CtrlDroskar, self).__init__()
		self.init_daemon2_fields(module_consts.MAP_ID_ZMOD_GMD0_DROSKAR_CRUCIBLE, DROSKAR, "droskar")
		return

	def place_encounters_initial(self):
		self.place_encounter_DR01()
		return

	def place_encounter_DR01(self):
		PROMTER_DR01_SET = {
			"loc": utils_obj.sec2loc(491, 487),
			"title": "Approaching the Ruins",
			"rot": const_toee.rotation_0700_oclock
		}
		self.create_promter_at(PROMTER_DR01_SET["loc"], self.get_dialogid_default(), 0011, 10 \
			, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, PROMTER_DR01_SET["title"], PROMTER_DR01_SET["rot"] \
		)

		return