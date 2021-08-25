import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def GetConditionName():
	return "Open_Door"

print("Registering " + GetConditionName())
###################################################

def Open_Door_Check(attachee, args, evt_obj):
	return 1

sn_use = 0x1

def Open_Door_Perform(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	try:
		target = evt_obj.d20a.target
		assert isinstance(target, toee.PyObjHandle)
		print(target)
		target_type = 0
		if (target):
			target_type = target.type
		if (not target or target_type != toee.obj_t_portal):
			message = "Please popup Break action on Portal!"
			target.float_text_line(message, toee.tf_red)
			#toee.game.alert_show(message, "Close")
			return 0

		ag_open_door = 0xC
		print("opening the door")
		attachee.anim_goal_use_object(target, 40, target.location, 1)
		attachee.turn_towards(target)
		target.portal_flag_unset(toee.OPF_LOCKED)
		target.portal_toggle_open()
		target.object_script_execute(attachee, sn_use)
		isOpen = None
		isJammed = None
		isLocked = None
		if (target):
			isOpen = target.portal_flags_get() & toee.OPF_OPEN
			isJammed = target.portal_flags_get() & toee.OPF_JAMMED
			isLocked = target.portal_flags_get() & toee.OPF_LOCKED

		print("target: {}, open: {}, jammed: {}, locked: {}".format(target, isOpen, isJammed, isLocked))

	except Exception, e:
		print "Open_Door_Perform:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("error")
	return 0
modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # 
modObj.AddHook(toee.ET_OnD20PythonActionCheck, 3018, Open_Door_Check, ())
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3018, Open_Door_Perform, ())