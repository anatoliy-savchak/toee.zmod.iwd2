import toee, debug, ctrl_daemon, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import startup_zmod, utils_sneak, monster_info, copy, rttoee_consts, const_animate, const_sceneries
import const_proto_items, const_proto_cloth, const_proto_rings, py07023_npc_temple_tower, const_proto_containers, const_proto_potions, utils_locks

TEMPLE_TOWER = 7013
TEMPLE_TOWER_DAEMON_ID = "G_05B39EBA_F2BD_4A0E_9623_2B2129D9FD99"
TEMPLE_TOWER_DAEMON_DIALOG = 7013

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

def cs():
	o = utils_storage.obj_storage_by_id(TEMPLE_TOWER_DAEMON_ID)
	if (not o): return None
	if (CtrlTempleTower.get_name() in o.data):
		result = o.data[CtrlTempleTower.get_name()]
	else: return None
	assert isinstance(result, CtrlTempleTower)
	return result

class CtrlTempleTower(ctrl_daemon2.CtrlDaemon2):
	def __init__(self):
		super(CtrlTempleTower, self).__init__()
		self.init_daemon2_fields(rttoee_consts.MAP_ID_TEMPLE_TOWER, TEMPLE_TOWER, "temple_tower")
		return

	def place_encounters_initial(self):
		self.place_chest()
		self.place_monsters()
		return

	def place_monsters(self):
		self.create_npc_at(utils_obj.sec2loc(494, 487), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "hob", "01", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(492, 487), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "hob", "02", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(486, 492), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "hob", "03", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(480, 496), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0700_oclock, "hob", "04", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(485, 487), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "hob", "05", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(494, 495), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "hob", "06", None, 0, 0)

		self.create_npc_at(utils_obj.sec2loc(493, 485), py07023_npc_temple_tower.CtrlGoblinNaked, const_toee.rotation_0500_oclock, "gob", "01", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(488, 484), py07023_npc_temple_tower.CtrlGoblinNaked, const_toee.rotation_0500_oclock, "gob", "02", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(481, 489), py07023_npc_temple_tower.CtrlGoblinNaked, const_toee.rotation_0500_oclock, "gob", "03", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(492, 480), py07023_npc_temple_tower.CtrlGoblinNaked, const_toee.rotation_0500_oclock, "gob", "04", None, 0, 0)
		return

	def place_chest(self):
		loc = utils_obj.sec2loc(474, 476)
		chest = toee.game.obj_create(const_proto_containers.PROTO_CONTAINER_CHEST_GENERIC, loc)
		chest.move(loc)
		if (chest):
			utils_item.item_money_create_in_inventory(chest, 0, 800, 200)
			item = utils_item.item_create_in_inventory(const_proto_potions.PROTO_POTION_OF_CURE_SERIOUS_WOUNDS, chest)
			if (item):
				item.obj_set_int(toee.obj_f_item_quantity, 2)
			utils_locks.container_setup_dc(chest, utils_locks.LOCK_DC_VERY_SIMPLE, 0, utils_locks.HP_CHEST_TREASURE \
				, utils_locks.HARDNESS_CHEST_TREASURE, utils_locks.BREAK_DC_CHEST_TREASURE)
		return