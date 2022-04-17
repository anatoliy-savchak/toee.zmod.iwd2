import toee, debug, ctrl_daemon, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import module_consts, const_proto_sceneries, py14714_keep_commander, utils_locks, py06603_keep_encounters, py14710_smith, py14711_smith_wife, utils_toee

KEEP_LV3 = 6602
KEEP_LV3_DAEMON_ID = "G_CD97DDB2_B2A5_456D_84A0_4D3FB4B1BF7B"

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, module_consts.MAP_ID_ZMOD_KEEP_LV3, CtrlKeepLv3)

def san_first_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, module_consts.MAP_ID_ZMOD_KEEP_LV3, CtrlKeepLv3)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, module_consts.MAP_ID_ZMOD_KEEP_LV3, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, module_consts.MAP_ID_ZMOD_KEEP_LV3, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, module_consts.MAP_ID_ZMOD_KEEP_LV3, cs())

def cs():
	o = utils_storage.obj_storage_by_id(KEEP_LV3_DAEMON_ID)
	if (not o): return None
	if (CtrlKeepLv3.get_name() in o.data):
		result = o.data[CtrlKeepLv3.get_name()]
	else: return None
	assert isinstance(result, CtrlKeepLv3)
	return result

class CtrlKeepLv3(ctrl_daemon2.CtrlDaemon2):
	def created(self, npc):
		self.init_daemon2_fields(module_consts.MAP_ID_ZMOD_KEEP_LV3, KEEP_LV3, "keep_lv3")
		super(CtrlKeepLv3, self).created(npc)
		return

	def place_encounters_initial(self):
		#debug.breakp("CtrlKeepLv3 place_encounters_initial")
		self.place_passages()
		self.place_boss()
		self.place_elite_guards()
		self.place_smith()
		return
	
	def place_passages(self):
		# staris down
		loc, ox, oy = utils_obj.sec2loc(477, 484), -12.7279215, -12.7279215
		passage = py06603_keep_encounters.CtrlKeepPortalLv3ToLv2.create_obj(loc)
		passage.move(loc, ox, oy)

		# storage door
		loc, ox, oy = utils_obj.sec2loc(466, 480), -11.3137083, 2.82842779
		passage = toee.game.obj_create(14, loc, ox, oy)
		if (passage):
			passage.move(loc, ox, oy)
			passage.rotation = 0.7853982
			utils_locks.portal_setup_dc(passage, 30, 0, 100, 100, 100)
			#passage.scripts[const_toee.sn_use] = self.default_script_id
			self.vars["storage_door"] = passage.id
			print("storage_door = {}".format(passage.id))
		return

	def do_san_use(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		print("san_use id: {}, nameid: {}".format(attachee.id, attachee.name))

		if (attachee.id == self.vars["passage_down"]):
			toee.game.fade_and_teleport(0, 0, 0, module_consts.MAP_ID_ZMOD_KEEP_LV2, module_consts.ZMOD_KEEP_LV2_ENTRY_COORDS_STAIRS[0], module_consts.ZMOD_KEEP_LV2_ENTRY_COORDS_STAIRS[1])

		return toee.RUN_DEFAULT

	def place_boss(self):
		m = self.get_monsterinfo("keep", "boss")
		if (m): return

		loc = utils_obj.sec2loc(466, 467)
		#print("Creating Commander...")
		npc, ctrl = self.create_npc_at(loc, py14714_keep_commander.CtrlKeepCommander, const_toee.rotation_1100_oclock, "keep", "boss", factions_zmod.FACTION_FIRENDY_NPC, 0, 1)
		#utils_npc.npc_description_set_new(npc, "Commander")
		#print("commander proto: {}, commander: ".format(py14714_keep_commander.CtrlKeepCommander.get_proto_id(), npc))
		#debug.breakp("")

		if (1):
			wpl = list()
			wpl.append(utils_npc.Waypoint(466, 461, const_toee.rotation_1000_oclock, 1000, utils_npc.WaypointFlag.Delay))
			wpl.append(utils_npc.Waypoint(466, 471, const_toee.rotation_0600_oclock, 1000, utils_npc.WaypointFlag.Delay))
			npc.npc_waypoints_set(wpl, 1)
			npc.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
			npc.npc_flag_set(toee.ONF_WAYPOINTS_NIGHT)
		return

	def place_elite_guards(self):
		name_id = utils_toee.make_custom_name("Elite Guard")
		npc, ctrl = self.create_npc_at(utils_obj.sec2loc(475, 465), py06603_keep_encounters.CtrlGuardElite, const_toee.rotation_0700_oclock, "keep", "elite1", factions_zmod.FACTION_FIRENDY_NPC, 0, 1)
		utils_npc.npc_description_set_new(npc, None, name_id)

		npc, ctrl = self.create_npc_at(utils_obj.sec2loc(475, 470), py06603_keep_encounters.CtrlGuardElite, const_toee.rotation_0700_oclock, "keep", "elite2", factions_zmod.FACTION_FIRENDY_NPC, 0, 1)
		utils_npc.npc_description_set_new(npc, None, name_id)

		npc, ctrl = self.create_npc_at(utils_obj.sec2loc(466, 476), py06603_keep_encounters.CtrlGuardElite, const_toee.rotation_0200_oclock, "keep", "elite3", factions_zmod.FACTION_FIRENDY_NPC, 0, 1)
		utils_npc.npc_description_set_new(npc, None, name_id)

		if (1):
			wpl = list()
			wpl.append(utils_npc.Waypoint(466, 476, const_toee.rotation_0200_oclock, 1000, utils_npc.WaypointFlag.Delay))
			wpl.append(utils_npc.Waypoint(487, 476, const_toee.rotation_0700_oclock, 1000, utils_npc.WaypointFlag.Delay))
			npc.npc_waypoints_set(wpl, 1)
			npc.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
			npc.npc_flag_set(toee.ONF_WAYPOINTS_NIGHT)
		return

	def place_smith(self):
		m = self.get_monsterinfo("keep", "smith")
		if (m): return

		loc = utils_obj.sec2loc(484, 463)
		npc, ctrl = self.create_npc_at(loc, py14710_smith.CtrlVillageSmith, const_toee.rotation_0400_oclock, "keep", "smith", factions_zmod.FACTION_FIRENDY_NPC, 0, 1)
		utils_npc.npc_description_set_new(npc, "Smith")

		#loc = utils_obj.sec2loc(491, 468)
		#npc, ctrl = self.create_npc_at(loc, py14711_smith_wife.CtrlVillageSmithWife, const_toee.rotation_0400_oclock, "keep", "smith_wife", factions_zmod.FACTION_FIRENDY_NPC, 0, 1)
		#utils_npc.npc_description_set_new(npc, "Smith Wife")
		return

	# Sleep interface
	def can_sleep(self):
		return toee.SLEEP_PASS_TIME_ONLY
