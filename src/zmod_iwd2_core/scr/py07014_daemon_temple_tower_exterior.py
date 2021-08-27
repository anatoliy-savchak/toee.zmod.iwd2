import toee, debug, ctrl_daemon, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import startup_zmod, utils_sneak, monster_info, copy, rttoee_consts, const_animate, const_sceneries
import const_proto_items, const_proto_cloth, const_proto_rings, py07023_npc_temple_tower, const_proto_containers, const_proto_potions, utils_locks

TEMPLE_TOWER_EXTERIOR = 7014
TEMPLE_TOWER_EXTERIOR_DAEMON_ID = "G_16F37B87_30CD_464B_B609_0E414322CD63"
TEMPLE_TOWER_EXTERIOR_DAEMON_DIALOG = 7014

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_TOWER_EXTERIOR, CtrlTempleTowerExterior)

def san_first_heartbeat(attachee, triggerer):
	#print(attachee.id)
	#debug.breakp("")
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_TOWER_EXTERIOR, CtrlTempleTowerExterior)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_TOWER_EXTERIOR, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_TOWER_EXTERIOR, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_TOWER_EXTERIOR, cs())

def cs():
	o = utils_storage.obj_storage_by_id(TEMPLE_TOWER_EXTERIOR_DAEMON_ID)
	if (not o): return None
	if (CtrlTempleTowerExterior.get_name() in o.data):
		result = o.data[CtrlTempleTowerExterior.get_name()]
	else: return None
	assert isinstance(result, CtrlTempleTowerExterior)
	return result

class CtrlTempleTowerExterior(ctrl_daemon2.CtrlDaemon2):
	def __init__(self):
		super(CtrlTempleTowerExterior, self).__init__()
		self.init_daemon2_fields(rttoee_consts.MAP_ID_TEMPLE_TOWER_EXTERIOR, TEMPLE_TOWER_EXTERIOR, "temple_tower_ext")
		return

	def place_encounters_initial(self):
		self.place_monsters()
		return

	def place_monsters(self):
		self.create_npc_at(utils_obj.sec2loc(483, 494), py07023_npc_temple_tower.CtrlDogAggessive, const_toee.rotation_0500_oclock, "pack", "01", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(481, 492), py07023_npc_temple_tower.CtrlDogAggessive, const_toee.rotation_0500_oclock, "pack", "02", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(476, 492), py07023_npc_temple_tower.CtrlDogAggessive, const_toee.rotation_0500_oclock, "pack", "03", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(475, 495), py07023_npc_temple_tower.CtrlDogAggessive, const_toee.rotation_0700_oclock, "pack", "04", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(492, 493), py07023_npc_temple_tower.CtrlDogAggessive, const_toee.rotation_0500_oclock, "pack", "05", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(495, 493), py07023_npc_temple_tower.CtrlDogAggessive, const_toee.rotation_0500_oclock, "pack", "06", None, 0, 0)
		return
