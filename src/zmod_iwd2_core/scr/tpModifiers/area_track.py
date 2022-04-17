import toee, templeplus.pymod, debug, sys, tpdp, traceback

###################################################

def GetConditionName():
	return "AreaTrack"

print("Registering " + GetConditionName())
###################################################

def AreaTrack_OnConditionAdd(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)

	radius_ft = args.get_arg(1)
	evt_id = attachee.object_event_append(toee.OLC_PC, radius_ft)
	args.set_arg(0, evt_id)
	#print("AreaTrack_OnConditionAdd ({}, {}) radius_ft: {}, evt_id: {}, attachee: {}".format(attachee.location_full.loc_xy.x, attachee.location_full.loc_xy.y, radius_ft, evt_id, attachee))
	return

def AreaTrack_OnObjectEventEnter(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjObjectEvent)
	try:
		evt_id = args.get_arg(0)
		if (evt_id != evt_obj.evt_id):
			return 0

		enter_script = args.get_arg(2)
		if (enter_script):
			result = attachee.object_script_execute(evt_obj.target, enter_script)
			if (result):
				leave_script = args.get_arg(3)
				evt_obj.target.condition_add_with_args("AreaTrack Aura", evt_id, leave_script)
		#print("AreaTrack_OnObjectEventEnter ({}, {}):: target: {}".format(attachee.location_full.loc_xy.x, attachee.location_full.loc_xy.y, evt_obj.target))
	except Exception, e:
		print "AreaTrack_OnObjectEventEnter:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 10) # 0 - evt_id, 1 - radius_ft, 2 - enter_script, 3 - leave_script
modObj.AddHook(toee.ET_OnConditionAdd, toee.EK_NONE, AreaTrack_OnConditionAdd, ())
modObj.AddHook(toee.ET_OnObjectEvent, toee.EK_OnEnterAoE, AreaTrack_OnObjectEventEnter, ())

###################################################

def GetConditionName():
	return "AreaTrack Aura"

print("Registering " + GetConditionName())
###################################################


def AreaTrack_OnObjectEventLeave(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjObjectEvent)
	try:
		evt_id = args.get_arg(0)
		if (evt_id != evt_obj.evt_id):
			return 0

		#print("AreaTrack_OnObjectEventLeave ({}, {}) :: sleep_status_update post call".format(attachee.location_full.loc_xy.x, attachee.location_full.loc_xy.y))
		leave_script = args.get_arg(1)
		if (leave_script):
			evt_obj.aoe_obj.object_script_execute(attachee, leave_script)
		args.condition_remove()
	except Exception, e:
		print "AreaTrack_OnObjectEventLeave:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return

def AreaTrack_Teleport_Prepare(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Signal)
	try:
		leave_script = args.get_arg(1)
		#TODO!!!
		#if (leave_script):
			#evt_obj.aoe_obj.object_script_execute(attachee, leave_script)
		args.condition_remove()
	except Exception, e:
		print "AreaTrack_Teleport_Prepare:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return

modObj2 = templeplus.pymod.PythonModifier(GetConditionName(), 2) # 0 - evt_id, 1 - leave_script
modObj2.AddHook(toee.ET_OnObjectEvent, toee.EK_OnLeaveAoE, AreaTrack_OnObjectEventLeave, ())
modObj2.AddHook(toee.ET_OnD20Signal, toee.EK_S_Teleport_Prepare, AreaTrack_Teleport_Prepare, ())