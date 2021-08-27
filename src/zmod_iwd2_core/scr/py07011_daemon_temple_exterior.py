import toee, debug, ctrl_daemon, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import startup_zmod, utils_sneak, monster_info, copy, rttoee_consts, const_animate, const_sceneries
import const_proto_items, const_proto_cloth, const_proto_rings, py07023_npc_temple_tower, const_proto_containers, const_proto_potions, utils_locks

TEMPLE_EXTERIOR = 7011
TEMPLE_EXTERIOR_DAEMON_ID = "G_E81B6873_F53D_4375_9C72_8C87C1571AB4"
TEMPLE_EXTERIOR_DAEMON_DIALOG = 7011

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_EXTERIOR, CtrlTempleExterior)

def san_first_heartbeat(attachee, triggerer):
	#print(attachee.id)
	#debug.breakp("")
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_EXTERIOR, CtrlTempleExterior)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_EXTERIOR, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_EXTERIOR, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_EXTERIOR, cs())

def cs():
	o = utils_storage.obj_storage_by_id(TEMPLE_EXTERIOR_DAEMON_ID)
	if (not o): return None
	if (CtrlTempleExterior.get_name() in o.data):
		result = o.data[CtrlTempleExterior.get_name()]
	else: return None
	assert isinstance(result, CtrlTempleExterior)
	return result

class CtrlTempleExterior(ctrl_daemon2.CtrlDaemon2):
	def __init__(self):
		super(CtrlTempleExterior, self).__init__()
		self.init_daemon2_fields(rttoee_consts.MAP_ID_TEMPLE_EXTERIOR, TEMPLE_EXTERIOR, "temple_exterior")
		return

	def place_encounters_initial(self):
		self.place_monsters()
		return

	def place_monsters(self):
		self.create_npc_at(utils_obj.sec2loc(507, 480), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_01", "01", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(502, 478), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_01", "02", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(483, 477), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_01", "03", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(505, 473), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_01", "04", None, 0, 0)

		self.create_npc_at(utils_obj.sec2loc(496, 457), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_02", "01", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(494, 457), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_02", "02", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(492, 457), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_02", "03", None, 0, 0)
		self.create_npc_at(utils_obj.sec2loc(494, 461), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_02", "04", None, 0, 0)
		return

	def critter_entered_combat(self, ctrl, npc):
		print("critter_entered_combat")
		#debug.breakp("critter_entered_combat")
		for name, baddy in self.get_alive_monster_npcs("temple_").items():
			if (not "temple_01" in name and not "temple_02" in name): continue
			assert isinstance(baddy, toee.PyObjHandle)
			if (baddy == npc): continue
			if (baddy.is_active_combatant()): continue
			print("adding to combat: {}".format(baddy))
			baddy.add_to_initiative()
		return
