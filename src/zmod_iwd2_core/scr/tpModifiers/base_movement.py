import toee, templeplus.pymod, debug, tpdp

###################################################

def GetConditionName():
	return "Base_Movement"

print("Registering " + GetConditionName())
###################################################

def Base_Movement_OnGetBaseMoveSpeed(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjMoveSpeed)

	alter_speed = args.get_arg(0)
	if (alter_speed):
		mesline = args.get_arg(2)
		if (not mesline): mesline = 139
		evt_obj.bonus_list.add(alter_speed, 1, mesline)

	factor = args.get_arg(1)
	if (factor):
		evt_obj.factor = factor / 100.0
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 10) # 0 - alter_speed in feet, 1 - factor100 (total*factor100/100.0), 2 - mesline
modObj.AddHook(toee.ET_OnGetMoveSpeedBase, toee.EK_NONE, Base_Movement_OnGetBaseMoveSpeed, ())