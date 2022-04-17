import toee, debug, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee, ctrl_daemon
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import startup_zmod, utils_sneak, monster_info, copy, kots_consts, const_animate

# import py06500_daemon_barovia
# py06500_daemon_barovia.cs()
# game.fade_and_teleport(0, 0, 0, 5125, 429, 478)
# game.fade_and_teleport(0, 0, 0, 5125, 467, 478)

JZADIRUN = "keep"
JZADIRUN_DAEMON_SCRIPT = 6605
JZADIRUN_DAEMON_ID = "G_A8B07BB3_A25F_4BA7_8407_B3AAA51D9526"
JZADIRUN_DAEMON_DIALOG = 6725

def san_new_map(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	#print(attachee.id)
	#debug.breakp("san_new_map")
	startup_zmod.zmod_templeplus_config_apply()
	if (attachee.map != kots_consts.MAP_ID_CORINTH): toee.RUN_DEFAULT
	ctrl = CtrlJzadirun.ensure(attachee)
	ctrl.place_encounters(1)
	return toee.RUN_DEFAULT

def san_first_heartbeat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	#print(attachee.id)
	#debug.breakp("san_first_heartbeat")
	startup_zmod.zmod_templeplus_config_apply()
	if (attachee.map != kots_consts.MAP_ID_CORINTH): toee.RUN_DEFAULT
	ctrl = CtrlJzadirun.ensure(attachee)
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
	o = utils_storage.obj_storage_by_id(JZADIRUN_DAEMON_ID)
	#print("utils_storage.obj_storage(): {}".format(o))
	if (not o): return None
	if (CtrlJzadirun.get_name() in o.data):
		result = o.data[CtrlJzadirun.get_name()]
	else: return None
	#print("data: {}".format(result))
	#debugg.breakp("csl")
	return result

class CtrlJzadirun(ctrl_daemon.CtrlDaemon):
	def __init__(self):
		super(CtrlJzadirun, self).__init__()
		self.last_heartbeat_time_sec = toee.game.time.time_game_in_seconds(toee.game.time)
		self.last_heartbeat_time_hr = toee.game.time.time_game_in_hours2(toee.game.time)
		return

	def created(self, npc):
		super(CtrlJzadirun, self).created(npc)
		npc.scripts[const_toee.sn_dialog] = JZADIRUN_DAEMON_SCRIPT
		return

	@staticmethod
	def get_name():
		return "CtrlJzadirun"

	@classmethod
	def get_alias(self):
		return "jzadirun" # utils_storage.ca("jzadirun")

	def get_map_default(self):
		return 5145

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
			# 473, 464
			pass

		self.encounters_placed += 1
		self.factions_existance_refresh()
		self.check_sleep_status_update(1)

		utils_obj.scroll_to_leader()
		return

	def heartbeat(self, deamon_npc):
		assert isinstance(deamon_npc, toee.PyObjHandle)

		for obj in toee.game.obj_list_range(deamon_npc.location, 100, toee.OLC_PORTAL):
			secretdoor_flags = obj.obj_get_int(toee.obj_f_secretdoor_flags)
			if (not secretdoor_flags & const_toee.OSDF_SECRET_DOOR): continue
			if (secretdoor_flags & const_toee.OSDF_SECRET_DOOR_FOUND):
				if (obj.object_flags_get() & toee.OF_DONTDRAW):
					obj.object_flag_unset(toee.OF_DONTDRAW)
					print("Unset OF_DONTDRAW due to revealed for {}".format(obj))
					#debug.breakp("")
		return