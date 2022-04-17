import toee, debugg, utils_obj, const_toee, utils_toee

def fireplace_create(x, y, radius_feet, ox, oy):
	loc = utils_obj.sec2loc(x, y)
	obj = toee.game.obj_create(toee.OBJECT_SPELL_GENERIC, loc)
	if (obj):
		obj.move(loc, ox, oy)
		obj.d20_status_init() # make sure dispatcher is ready
		enter_script = const_toee.sn_wield_on
		leave_script = const_toee.sn_wield_off
		obj.scripts[enter_script] = 6123
		obj.scripts[leave_script] = 6123
		obj.condition_add_with_args("AreaTrack", 0, radius_feet, enter_script, leave_script)
		obj.obj_set_int(toee.obj_f_generic_usage_bonus, radius_feet)
		fireplace_change_effect(obj, "ef-Fireplace")
	return obj

def fireplace_is_in_area(fireplace, npc):
	dist = fireplace.distance_to(npc)
	radius_feet = fireplace.obj_get_int(toee.obj_f_generic_usage_bonus)
	if (dist <= radius_feet): return 1
	return 0

def san_wield_on(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	print("san_wield_on {}, {}".format(attachee, triggerer))

	_sleep_status_update()
	toee.game.timevent_add(_sleep_status_update, (), 1000, 1) # 1000 = 1 second

	return toee.RUN_DEFAULT

def san_wield_off(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	#print("san_wield_off {}, {}".format(attachee, triggerer))

	_sleep_status_update()

	toee.game.timevent_add(_sleep_status_update, (), 1000, 1) # 1000 = 1 second
	toee.game.timevent_add(_sleep_status_update, (), 5000, 1) # 1000 = 1 second

	return toee.RUN_DEFAULT

def _sleep_status_update():
	toee.game.sleep_status_update()
	return

def fireplace_change_effect(fireplace, part_name):
	oldpartid = fireplace.obj_get_int(toee.obj_f_generic_usage_count_remaining)
	if (oldpartid):
		toee.game.particles_kill(oldpartid)
	partid = toee.game.particles(part_name, fireplace)
	fireplace.obj_set_int(toee.obj_f_generic_usage_count_remaining, partid)
	return partid