import toee, debug, ctrl_daemon, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import startup_zmod, utils_sneak, monster_info, copy, rttoee_consts, const_animate, const_sceneries
import const_proto_items, const_proto_cloth, const_proto_rings, py07023_npc_temple_tower, const_proto_containers, const_proto_potions, utils_locks

TEMPLE_HOUSE = 7015
TEMPLE_HOUSE_DAEMON_ID = "G_48025A16_F71D_4D0F_A378_F586A1F28282"
TEMPLE_HOUSE_DAEMON_DIALOG = 7015

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_HOUSE, CtrlTempleHouse)

def san_first_heartbeat(attachee, triggerer):
	#print(attachee.id)
	#debug.breakp("")
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_HOUSE, CtrlTempleHouse)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_HOUSE, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_HOUSE, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_HOUSE, cs())

def cs():
	o = utils_storage.obj_storage_by_id(TEMPLE_HOUSE_DAEMON_ID)
	if (not o): return None
	if (CtrlTempleHouse.get_name() in o.data):
		result = o.data[CtrlTempleHouse.get_name()]
	else: return None
	assert isinstance(result, CtrlTempleHouse)
	return result

class CtrlTempleHouse(ctrl_daemon2.CtrlDaemon2):
	def __init__(self):
		super(CtrlTempleHouse, self).__init__()
		self.init_daemon2_fields(rttoee_consts.MAP_ID_TEMPLE_HOUSE, TEMPLE_HOUSE, "temple_house")
		return

	def place_encounters_initial(self):
		self.place_monsters()
		return

	def place_monsters(self):
		self.create_npc_at(utils_obj.sec2loc(471, 495), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "pack", "01", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(476, 498), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0300_oclock, "pack", "02", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(475, 492), py07023_npc_temple_tower.CtrlHobgoblinAlubya, const_toee.rotation_0500_oclock, "pack", "03", None, 0, 0)
		return
