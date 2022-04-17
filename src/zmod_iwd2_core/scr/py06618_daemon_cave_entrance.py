import toee, debug, utils_toee, utils_storage, utils_obj, utils_item, const_toee, ctrl_daemon, ctrl_daemon2
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, utils_npc, utils_locks, const_proto_items, const_proto_scrolls, const_proto_rings
import monster_info, module_quests, module_consts, module_globals
import py06619_cave_encounters, py06123_event_object_fireplace, module_world_travel, module_cheats

DAEMON_SCRIPT_ID = 6618
DAEMON_GID = "G_E2A27A98_A4EF_4FCD_B69A_D6F8348298BB"

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, module_consts.MAP_ID_ZMOD_CAVE_ENTRANCE, CtrlCaveEntrance)

def san_first_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, module_consts.MAP_ID_ZMOD_CAVE_ENTRANCE, CtrlCaveEntrance)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, module_consts.MAP_ID_ZMOD_CAVE_ENTRANCE, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, module_consts.MAP_ID_ZMOD_CAVE_ENTRANCE, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, module_consts.MAP_ID_ZMOD_CAVE_ENTRANCE, cs())

def san_bust(attachee, triggerer):
	return ctrl_daemon2.do_san_bust(attachee, triggerer, module_consts.MAP_ID_ZMOD_CAVE_ENTRANCE, cs())

def cs():
	o = utils_storage.obj_storage_by_id(DAEMON_GID)
	if (not o): 
		return None
	result = o.data.get(CtrlCaveEntrance.get_name())
	assert isinstance(result, CtrlCaveEntrance)
	return result

class CtrlCaveEntrance(ctrl_daemon2.CtrlDaemon2):
	def created(self, npc):
		self.init_daemon2_fields(module_consts.MAP_ID_ZMOD_CAVE_ENTRANCE, DAEMON_SCRIPT_ID, "cave_entrance")
		super(CtrlCaveEntrance, self).created(npc)
		self.vars["foe_ids"] = list()
		return

	def place_encounters_initial(self):
		self.place_portals()
		self.place_fireplace()
		self.place_monsters_e01()
		return

	def place_encounters_next(self):
		return

	# Sleep interface
	def can_sleep(self):
		can_create = True if self.vars.get("can_camp") else False
		fireplace = self.ensure_fireplace(False)
		if (fireplace):
			for pc in toee.game.party:
				if (py06123_event_object_fireplace.fireplace_is_in_area(fireplace, pc)):
					return toee.SLEEP_SAFE
		return toee.SLEEP_IMPOSSIBLE

	def ensure_fireplace(self, can_create):
		fireplace = self.get_fireplace()
		#print("ensure_fireplace: {}".format(fireplace))
		if (not fireplace and can_create):
			#print("ensure_fireplace recreating...")
			fireplace = self.place_fireplace()

		return fireplace

	def place_fireplace(self):
		fireplace = self.get_fireplace()
		if (fireplace):
			fireplace.destroy()
			self.vars["fireplace_id"] = 0

		if (toee.game.leader.map != self.get_map_default()): return
		radius_feet_int = 10
		fireplace = py06123_event_object_fireplace.fireplace_create(458, 448, radius_feet_int, 5, 5)
		self.vars["fireplace_id"] = fireplace.id
		return fireplace

	def get_fireplace(self):
		fireplace_id = self.get_var("fireplace_id")
		if (fireplace_id):
			fireplace = toee.game.get_obj_by_id(fireplace_id)
			if (fireplace and fireplace.object_flags_get() & toee.OF_DESTROYED):
				print("no fireplace!")
				return
			return fireplace
		return

	def create_lib_foe(self, npc_loc, ctrl_class, rot, encounter, code_name, faction = None, no_draw = 1, no_kos = 1, no_move = 0):
		result = self.create_npc_at(npc_loc, ctrl_class, rot, encounter, code_name, faction, no_draw, no_kos, no_move)
		self.vars["foe_ids"].append(result[0].id)
		if (module_cheats.CHEAT_GLOBAL_DEBUG_NAMES):
			utils_npc.npc_description_set_new(result[0], code_name)
		return result

	def place_portals(self):
		module_world_travel.CtrlWorldPortalCaveEntrance.create_obj_at_loc(utils_obj.sec2loc(475, 490))
		py06619_cave_encounters.CtrlCavesPortalGroundToLevel1.create_obj_at_loc(utils_obj.sec2loc(498, 438))
		return

	def place_monsters_e01(self):
		npc_leader = self.create_lib_foe(utils_obj.sec2loc(460, 442), py06619_cave_encounters.CtrlBrownBearLeader, const_toee.ROT07, "e01", "bear_leader", factions_zmod.FACTION_WILDERNESS_INDIFFERENT, 0, 1)[0]
		npc = self.create_lib_foe(utils_obj.sec2loc(460, 450), py06619_cave_encounters.CtrlBrownBear, const_toee.ROT10, "e01", "bear_2", factions_zmod.FACTION_WILDERNESS_INDIFFERENT, 0, 1)[0]
		npc.obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		return

	def dialog_enable_camping(self):
		self.vars["can_camp"] = 1
		self.ensure_fireplace(True)
		return