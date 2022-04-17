import toee, debug, const_toee, utils_toee

def sec2loc( x, y ):
	# initialize loc to be a LONG integer
	loc = 0L + y
	loc = ( loc << 32 ) + x
	return loc

def loc2sec(loc):
	assert isinstance(loc, long)
	y = loc >> 32
	x = loc & 4294967295
	return ( x, y )

def obj_scripts_clear(obj):
	assert isinstance(obj, toee.PyObjHandle)
	mob_scripts = obj.scripts
	mob_scripts[const_toee.sn_examine] = 0
	mob_scripts[const_toee.sn_use] = 0
	mob_scripts[const_toee.sn_destroy] = 0
	mob_scripts[const_toee.sn_unlock] = 0
	mob_scripts[const_toee.sn_get] = 0
	mob_scripts[const_toee.sn_drop] = 0
	mob_scripts[const_toee.sn_throw] = 0
	mob_scripts[const_toee.sn_hit] = 0
	mob_scripts[const_toee.sn_miss] = 0
	mob_scripts[const_toee.sn_dialog] = 0
	mob_scripts[const_toee.sn_first_heartbeat] = 0
	mob_scripts[const_toee.sn_catching_thief_pc] = 0
	mob_scripts[const_toee.sn_dying] = 0
	mob_scripts[const_toee.sn_enter_combat] = 0
	mob_scripts[const_toee.sn_exit_combat] = 0
	mob_scripts[const_toee.sn_start_combat] = 0
	mob_scripts[const_toee.sn_end_combat] = 0
	mob_scripts[const_toee.sn_buy_object] = 0
	mob_scripts[const_toee.sn_resurrect] = 0
	mob_scripts[const_toee.sn_heartbeat] = 0
	mob_scripts[const_toee.sn_leader_killing] = 0
	mob_scripts[const_toee.sn_insert_item] = 0
	mob_scripts[const_toee.sn_will_kos] = 0
	mob_scripts[const_toee.sn_taking_damage] = 0
	mob_scripts[const_toee.sn_wield_on] = 0
	mob_scripts[const_toee.sn_wield_off] = 0
	mob_scripts[const_toee.sn_critter_hits] = 0
	mob_scripts[const_toee.sn_new_sector] = 0
	mob_scripts[const_toee.sn_remove_item] = 0
	mob_scripts[const_toee.sn_leader_sleeping] = 0
	mob_scripts[const_toee.sn_bust] = 0
	mob_scripts[const_toee.sn_dialog_override] = 0
	mob_scripts[const_toee.sn_transfer] = 0
	mob_scripts[const_toee.sn_caught_thief] = 0
	mob_scripts[const_toee.sn_critical_hit] = 0
	mob_scripts[const_toee.sn_critical_miss] = 0
	mob_scripts[const_toee.sn_join] = 0
	mob_scripts[const_toee.sn_disband] = 0
	mob_scripts[const_toee.sn_new_map] = 0
	mob_scripts[const_toee.sn_trap] = 0
	mob_scripts[const_toee.sn_true_seeing] = 0
	mob_scripts[const_toee.sn_spell_cast] = 0
	mob_scripts[const_toee.sn_unlock_attempt] = 0
	return

def obj_timed_destroy(obj, time, is_realtime = 0):
	assert isinstance(obj, toee.PyObjHandle)
	toee.game.timevent_add( _destroy_on_timeevent, ( obj ), time, is_realtime) # 1000 = 1 second
	return

def _destroy_on_timeevent(obj):
	assert isinstance(obj, toee.PyObjHandle)
	if (obj):
		obj.destroy()
	return 1

def obj_timed_off(obj, time):
	assert isinstance(obj, toee.PyObjHandle)
	toee.game.timevent_add( _off_on_timeevent, ( obj ), time) # 1000 = 1 second
	return

def _off_on_timeevent(obj):
	obj.object_flag_set(toee.OF_OFF)
	return 1

def obj_timed_receive(obj, item, time = 1000, is_realtime = 0):
	assert isinstance(obj, toee.PyObjHandle)
	assert isinstance(item, toee.PyObjHandle)
	toee.game.timevent_add(_receive_on_timeevent, ( obj, item ), time, is_realtime) # 1000 = 1 second
	return

def _receive_on_timeevent(obj, item):
	assert isinstance(obj, toee.PyObjHandle)
	assert isinstance(item, toee.PyObjHandle)
	if (obj and item):
		obj.item_get(item)
	return 1


def scroll_to_leader(time = 100):
	toee.game.timevent_add(_scroll_to_leader_on_timeevent, (), time, 1) # 1000 = 1 second
	return

def _scroll_to_leader_on_timeevent():
	toee.game.scroll_to(toee.game.leader)
	return 1

def pop_up_box(message_id):
	# generates popup box ala tutorial (without messing with the tutorial entries...)
	a = toee.game.obj_create(11001, toee.game.leader.location)
	a.obj_set_int(toee.obj_f_written_text_start_line,message_id)
	toee.game.written_ui_show(a)
	a.destroy()
	return


def obj_float_line_dialog(obj, method, lineId, npc):
	assert isinstance(obj, toee.PyObjHandle)
	scriptId = obj.scripts[const_toee.sn_dialog]
	if (scriptId <=0): return 0
	if (method == 0): 
		obj.float_line(lineId, npc)
		return 1
	#print("obj_float_line_dialog({}, {}, {})".format(obj, method, lineId))
	#breakp("obj_float_line_dialog")
	fileName = utils_toee.find_dialog_file_name(scriptId)
	#print(fileName)
	#breakp("obj_float_line_dialog 2")
	if (fileName is None): return 0
	#obj.float_mesfile_line(fileName, lineId, White)
	#if (1==1): return 1
	fileName = "data\\dlg\\" + fileName
	line = utils_toee.readMesLine(fileName, lineId)
	if (line):
		line = line.replace("\\n", "\n")
	print("utils_toee.readMesLine = {}, lineId: {}, dlg: {}".format(line, lineId, scriptId))
	debug.breakp("obj_float_line_dialog 3")


	if (method == 2):
		toee.game.alert_show(line, "Close")
		return 1

	lineshort = ""
	if (method == 3):
		lines = line.split('.')
		lineshort = lines[0]
		if (len(lines) > 1): lineshort = lineshort + ".."
	else: lineshort = line

	if ((line is None) or (line == "")): return 0
	#breakp("obj_float_line_dialog 4")
	obj.float_text_line(lineshort, White)
	line = line + "\n\n"
	toee.game.create_history_freeform(line)
	return 1

def obj_get_id(obj):
	if (not obj): return None
	assert isinstance(obj, toee.PyObjHandle)
	if (hasattr(obj, 'id')):
		return obj.id
	s = obj.__getstate__()
	#print("obj_get_id({}) = {}".format(obj, s))
	#breakp("obj_get_id")
	return s

def isnull(obj, obj_when_null):
	assert isinstance(obj, toee.PyObjHandle)
	assert isinstance(obj_when_null, toee.PyObjHandle)
	if (not obj is None): return obj
	return obj_when_null

def get_sibling_door(door):
	assert isinstance(door, toee.PyObjHandle)
	for sibling in toee.game.obj_list_range(door.location, 15, toee.OLC_PORTAL):
		assert isinstance(sibling, toee.PyObjHandle)
		if (sibling == door): continue
		return sibling
	return

def find_nearest_obj_by_nameid(npc, distance_ft, nameid, flags = None):
	assert isinstance(npc, toee.PyObjHandle)
	if (not flags):
		flags = toee.OLC_ALL
	nearest = None
	nearest_dist = 10000
	for obj in toee.game.obj_list_range(npc.location, distance_ft, flags):
		assert isinstance(obj, toee.PyObjHandle)
		if (not obj.name == nameid): continue
		obj_dist = npc.distance_to(obj)
		if (obj_dist < nearest_dist):
			nearest = obj
			nearest_dist = obj_dist
	return nearest

def find_nearest_obj_by_nameid_loc(loc, distance_ft, nameid, flags = None):
	assert isinstance(npc, toee.PyObjHandle)
	if (not flags):
		flags = toee.OLC_ALL
	nearest = None
	nearest_dist = 10000
	for obj in toee.game.obj_list_range(loc, distance_ft, flags):
		assert isinstance(obj, toee.PyObjHandle)
		if (not obj.name == nameid): continue
		obj_dist = obj.distance_to(loc)
		if (obj_dist < nearest_dist):
			nearest = obj
			nearest_dist = obj_dist
	return nearest

def find_nearest_obj_by_proto_loc(loc, distance_ft, proto, flags = None):
	assert isinstance(npc, toee.PyObjHandle)
	if (not flags):
		flags = toee.OLC_ALL
	nearest = None
	nearest_dist = 10000
	for obj in toee.game.obj_list_range(loc, distance_ft, flags):
		assert isinstance(obj, toee.PyObjHandle)
		if (not obj.proto == proto): continue
		obj_dist = obj.distance_to(loc)
		if (obj_dist < nearest_dist):
			nearest = obj
			nearest_dist = obj_dist
	return nearest

def obj_should_ignore_interaction(npc):
	assert isinstance(npc, toee.PyObjHandle)
	if (not npc): return True
	oflags = npc.object_flags_get()
	if (oflags & toee.OF_DESTROYED or oflags & toee.OF_OFF  or oflags & toee.OF_DONTDRAW): return True
	return False

def obj_setup_secret(obj, secret_door_dc, automatic_detect_allowed_from_ranks = 0):
	assert isinstance(obj, toee.PyObjHandle)
	assert isinstance(secret_door_dc, int)
	assert isinstance(automatic_detect_allowed_from_ranks, int)

	obj.obj_set_int(toee.obj_f_secretdoor_flags, const_toee.OSDF_SECRET_DOOR)

	dc_value = (automatic_detect_allowed_from_ranks << 7) + secret_door_dc
	obj.obj_set_int(toee.obj_f_secretdoor_dc, dc_value)
	return

def money_to_str(value_cp):
	assert isinstance(value_cp, int)
	if (not value_cp):
		return "0 gp"

	gold = int(value_cp // const_toee.gp)
	gold_str = "{:n} gp".format(gold) if (gold) else ""

	reminder = value_cp - gold * const_toee.gp
	if (not reminder):
		if (gold_str == ""): gold_str = "0 gp"
		return gold_str

	silver = int(reminder // 10)
	silver_str = "{:n} sp".format(silver) if (silver) else ""

	reminder = int(reminder - silver * 10)
	if (not reminder):
		return "{} {}".format(gold_str, silver_str).strip()
	return "{} {} {} cp".format(gold_str, silver_str, reminder).strip()