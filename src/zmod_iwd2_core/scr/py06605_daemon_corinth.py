import toee, debug, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee, ctrl_daemon
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import startup_zmod, utils_sneak, monster_info, copy, kots_consts, const_animate
import py06606_corinth_encounters

# import py06500_daemon_barovia
# py06500_daemon_barovia.cs()
# game.fade_and_teleport(0, 0, 0, 5125, 429, 478)
# game.fade_and_teleport(0, 0, 0, 5125, 467, 478)

CORINTH = "keep"
CORINTH_DAEMON_SCRIPT = 6605
CORINTH_DAEMON_ID = "G_EF572FEE_9607_4C4C_8C26_16C3A7C028D4"
CORINTH_DAEMON_DIALOG = 6605

def san_new_map(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	#print(attachee.id)
	#debug.breakp("san_new_map")
	startup_zmod.zmod_templeplus_config_apply()
	if (attachee.map != kots_consts.MAP_ID_CORINTH): toee.RUN_DEFAULT
	ctrl = CtrlCorinth.ensure(attachee)
	ctrl.place_encounters(1)
	return toee.RUN_DEFAULT

def san_first_heartbeat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	#print(attachee.id)
	#debug.breakp("san_first_heartbeat")
	startup_zmod.zmod_templeplus_config_apply()
	if (attachee.map != kots_consts.MAP_ID_CORINTH): toee.RUN_DEFAULT
	ctrl = CtrlCorinth.ensure(attachee)
	ctrl.place_encounters(0)
	return toee.RUN_DEFAULT

def san_heartbeat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	#debug.breakp("san_heartbeat")
	if (attachee.map != kots_consts.MAP_ID_CORINTH): toee.RUN_DEFAULT
	ctrl = cs()
	if ("heartbeat" in dir(ctrl)):
		ctrl.heartbeat(attachee)
	return toee.RUN_DEFAULT

def san_dying(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	c = cs()
	if (c):
		c.critter_dying(attachee, triggerer)
	storage = utils_storage.obj_storage_by_id(attachee.id)
	if (storage):
		cb = storage.get_data(ctrl_behaviour.CtrlBehaviour.get_name())
		if ("dying" in dir(cb)):
			cb.dying(attachee, triggerer)
	return toee.RUN_DEFAULT

def san_use(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	print("san_use id: {}, nameid: {}".format(attachee.id, attachee.name))
	if (attachee.name == coe_consts.PORTAL_KASSEN_2_ROAD_2_EVERFLAME):
		toee.game.fade_and_teleport(0, 0, 0, coe_consts.MAP_ID_ROAD2COE, 484, 458)
		return toee.SKIP_DEFAULT
	return toee.RUN_DEFAULT

def cs():
	#print("CtrlShatteredLab.get_name(): {}".format(CtrlShatteredLab.get_name()))
	o = utils_storage.obj_storage_by_id(CORINTH_DAEMON_ID)
	#print("utils_storage.obj_storage(): {}".format(o))
	if (not o): return None
	if (CtrlCorinth.get_name() in o.data):
		result = o.data[CtrlCorinth.get_name()]
	else: return None
	#print("data: {}".format(result))
	#debugg.breakp("csl")
	return result

class CtrlCorinth(ctrl_daemon.CtrlDaemon):
	def __init__(self):
		super(CtrlCorinth, self).__init__()
		self.last_heartbeat_time_sec = toee.game.time.time_game_in_seconds(toee.game.time)
		self.last_heartbeat_time_hr = toee.game.time.time_game_in_hours2(toee.game.time)
		return

	def created(self, npc):
		super(CtrlCorinth, self).created(npc)
		npc.scripts[const_toee.sn_dialog] = CORINTH_DAEMON_SCRIPT
		return

	@staticmethod
	def get_name():
		return "CtrlCorinth"

	@classmethod
	def get_alias(self):
		return "corinth" # utils_storage.ca("corinth")

	def get_map_default(self):
		return kots_consts.MAP_ID_CORINTH

	def place_encounters(self, new_map):
		print("new_map: {}".format(new_map))
		print("place_encounters.encounters_placed == {}".format(self.encounters_placed))
		startup_zmod.zmod_templeplus_config_apply()
		startup_zmod.zmod_conditions_apply_pc()

		if (self.encounters_placed and new_map == 0): return

		this_entrance_time = toee.game.time.time_game_in_hours2(toee.game.time)
		print("this_entrance_time == {}".format(this_entrance_time))
		if (not self.encounters_placed):
			self.first_entered_shrs = this_entrance_time
		self.last_entered_shrs = this_entrance_time
		if (not self.last_leave_shrs):
			self.last_leave_shrs = this_entrance_time

		if (not self.encounters_placed and 1):
			# entry 541, 429
			self.place_encounter_thugs()
			pass

		self.encounters_placed += 1
		self.factions_existance_refresh()
		self.check_sleep_status_update(1)

		utils_obj.scroll_to_leader()
		return

	def monster_setup(self, npc, encounter_name, monster_code_name, monster_name, no_draw = 1, no_kos = 1, faction = None):
		super(CtrlCorinth, self).monster_setup(npc, encounter_name, monster_code_name, monster_name, no_draw, no_kos, faction)
		npc.scripts[const_toee.sn_dying] = CORINTH_DAEMON_SCRIPT
		return

	def get_dialogid_default(self):
		return CORINTH_DAEMON_DIALOG

	def get_monster_faction_default(self, npc):
		return factions_zmod.FACTION_NEUTRAL_NPC

	def get_monster_prefix_default(self):
		return "corinth"

	def time_hour_passed(self, prev_heartbeat_time_hr, prev_heartbeat_time_sec):
		assert isinstance(prev_heartbeat_time_hr, int)
		assert isinstance(prev_heartbeat_time_sec, int)

		self.validate_minfo()
		for minfo in self.monsters.itervalues():
			assert isinstance(minfo, monster_info.MonsterInfo)
			#print("minfo.name: {}, minfo.id: {}".format(minfo.name, minfo.id))
			ctrl = ctrl_behaviour.get_ctrl(minfo.id)
			if ("time_hour_passed" in dir(ctrl)):
				npc = toee.game.get_obj_by_id(minfo.id)
				ctrl.time_hour_passed(npc)
		return

	def place_encounter_thugs(self):
		self.create_promter_at(utils_obj.sec2loc(538, 430), self.get_dialogid_default(), 10, 20, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, "Thugs", const_toee.rotation_0800_oclock)
		return

	def place_monsters_thugs(self):
		self.create_npc_at(utils_obj.sec2loc(540, 433), py06606_corinth_encounters.CtrlThugLeader, const_toee.rotation_0700_oclock, "thugs", "thug_1_leader")
		self.create_npc_at(utils_obj.sec2loc(544, 432), py06606_corinth_encounters.CtrlThug2, const_toee.rotation_0700_oclock, "thugs", "thug_2")
		self.create_npc_at(utils_obj.sec2loc(546, 429), py06606_corinth_encounters.CtrlThug3, const_toee.rotation_0700_oclock, "thugs", "thug_3")
		self.create_npc_at(utils_obj.sec2loc(542, 425), py06606_corinth_encounters.CtrlThug4, const_toee.rotation_0700_oclock, "thugs", "thug_4")
		self.create_npc_at(utils_obj.sec2loc(537, 426), py06606_corinth_encounters.CtrlThug5, const_toee.rotation_0700_oclock, "thugs", "thug_5")
		return

	def display_encounter_thugs(self):
		self.place_monsters_thugs()

		npcs = list() #npc, info
		npcs.append(self.reveal_monster("thugs", "thug_1_leader"))
		npcs.append(self.reveal_monster("thugs", "thug_2"))
		npcs.append(self.reveal_monster("thugs", "thug_3"))
		npcs.append(self.reveal_monster("thugs", "thug_4"))
		npcs.append(self.reveal_monster("thugs", "thug_5"))

		leader = toee.game.leader
		for i in npcs:
			i[0].turn_towards(leader)
		return

	def activate_encounter_thugs(self):
		self.activate_monster("thugs", "thug_1_leader")
		self.activate_monster("thugs", "thug_2")
		self.activate_monster("thugs", "thug_3")
		self.activate_monster("thugs", "thug_4")
		self.activate_monster("thugs", "thug_5")
		return
