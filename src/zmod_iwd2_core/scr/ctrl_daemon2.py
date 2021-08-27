import toee, ctrl_daemon
import py06122_cormyr_prompter, utils_toee, const_toee, utils_storage, debug, utils_obj, utils_npc, ctrl_behaviour, monster_info, utils_item, factions_zmod
import startup_zmod

def ccs(guid_str, ctrl_cls):
	assert isinstance(guid_str, str)
	o = utils_storage.obj_storage_by_id(guid_str)
	if (not o): return None
	name = ctrl_cls.get_name()
	if (name in o.data):
		result = o.data[name]
	else: return None
	assert isinstance(result, CtrlDaemon2)
	return result

def do_san_new_map(attachee, triggerer, map_id, cls):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(map_id, int)
	#print(attachee.id)
	#debug.breakp("san_new_map")
	startup_zmod.zmod_templeplus_config_apply()
	if (attachee.map != map_id): toee.RUN_DEFAULT
	ctrl = cls.ensure(attachee)
	ctrl.place_encounters(1)
	return toee.RUN_DEFAULT

def do_san_first_heartbeat(attachee, triggerer, map_id, cls):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(map_id, int)
	#print(attachee.id)
	#debug.breakp("san_first_heartbeat")
	startup_zmod.zmod_templeplus_config_apply()
	if (attachee.map != map_id): toee.RUN_DEFAULT
	ctrl = cls.ensure(attachee)
	ctrl.place_encounters(0)
	return toee.RUN_DEFAULT

def do_san_heartbeat(attachee, triggerer, map_id, ctrl):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(map_id, int)
	assert isinstance(ctrl, CtrlDaemon2)
	#debug.breakp("san_heartbeat")
	if (attachee.map != map_id): toee.RUN_DEFAULT
	if (ctrl):
		ctrl.heartbeat(attachee)
	return toee.RUN_DEFAULT

def do_san_dying(attachee, triggerer, map_id, ctrl):
	assert isinstance(attachee, toee.PyObjHandle)
	if (ctrl):
		ctrl.critter_dying(attachee, triggerer)
	storage = utils_storage.obj_storage_by_id(attachee.id)
	if (storage):
		cb = storage.get_data(ctrl_behaviour.CtrlBehaviour.get_name())
		if ("dying" in dir(cb)):
			cb.dying(attachee, triggerer)
	return toee.RUN_DEFAULT

def do_san_use(attachee, triggerer, ctrl):
	assert isinstance(attachee, toee.PyObjHandle)
	print("san_use id: {}, nameid: {}".format(attachee.id, attachee.name))
	if (attachee.map != map_id): toee.RUN_DEFAULT
	if (ctrl):
		return ctrl.do_san_use(attachee, triggerer)
	return toee.RUN_DEFAULT

class CtrlDaemon2(ctrl_daemon.CtrlDaemon):
	""" More modern than CtrlDaemon(object)"""

	def __init__(self):
		print("CtrlDaemon2 init1")
		super(CtrlDaemon2, self).__init__()
		print("CtrlDaemon2 init2")
		self.last_heartbeat_time_sec = toee.game.time.time_game_in_seconds(toee.game.time)
		self.last_heartbeat_time_hr = toee.game.time.time_game_in_hours2(toee.game.time)
		self.default_map = 0
		self.default_script_id = 0
		self.default_faction = factions_zmod.FACTION_NEUTRAL_NPC
		self.default_monster_prefix = ""
		return

	@classmethod
	def get_name(cls):
		return cls.__name__

	@classmethod
	def get_alias(cls):
		return cls.__name__

	def init_daemon2_fields(self, default_map, default_script_id, default_monster_prefix, default_faction = None):
		print("CtrlDaemon2 init_daemon2_fields")
		self.default_map = default_map
		self.default_script_id = default_script_id
		self.default_faction = default_faction
		return

	def monster_setup(self, npc, encounter_name, monster_code_name, monster_name, no_draw = 1, no_kos = 1, faction = None):
		super(CtrlDaemon2, self).monster_setup(npc, encounter_name, monster_code_name, monster_name, no_draw, no_kos, faction)
		if (self.default_script_id):
			npc.scripts[const_toee.sn_dying] = self.default_script_id
		return

	def get_dialogid_default(self):
		return self.default_script_id

	def get_monster_faction_default(self, npc):
		return  self.default_faction

	def get_map_default(self):
		return self.default_map

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
			self.place_encounters_initial()
			pass

		self.encounters_placed += 1
		self.factions_existance_refresh()
		self.check_sleep_status_update(1)

		utils_obj.scroll_to_leader()
		return

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

	def storage_data_loaded_all(self):
		super(CtrlDaemon2, self).storage_data_loaded_all()
		for minfo in self.monsters.itervalues():
			assert isinstance(minfo, monster_info.MonsterInfo)
			#print("minfo.name: {}, minfo.id: {}".format(minfo.name, minfo.id))
			npc = toee.game.get_obj_by_id(minfo.id)
			if (npc):
				npc.anim_goal_interrupt()
		return

	def place_encounters_initial(self):
		return

	def do_san_use(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		print("san_use id: {}, nameid: {}".format(attachee.id, attachee.name))
		return toee.RUN_DEFAULT

	def heartbeat(self, npc):
		return

	def create_npc_at(self, npc_loc, ctrl_class, rot, encounter, code_name, faction = None, no_draw = 1, no_kos = 1):
		npc, ctrl = super(CtrlDaemon2, self).create_npc_at(npc_loc, ctrl_class, rot, encounter, code_name, faction, no_draw, no_kos)
		if (ctrl):
			ctrl.vars["daemon_name"] = self.get_name()
		return npc, ctrl

	def get_alive_monster_npcs(self, filter = None):
		result = dict()
		for tup in self.monsters.items():
			if (filter and not filter in tup[0] and not filter in tup[0]): continue
			info = tup[1]
			assert isinstance(info, monster_info.MonsterInfo)
			baddy = info.get_npc()
			if (not baddy): continue
			oflags = baddy.object_flags_get()
			if (oflags & toee.OF_DESTROYED or oflags & toee.OF_OFF  or oflags & toee.OF_DONTDRAW): continue
			result[tup[0]] = baddy
		return result