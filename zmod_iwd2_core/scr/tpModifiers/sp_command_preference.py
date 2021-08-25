import toee, templeplus.pymod, tpdp, debug

###################################################

def GetConditionName():
	return "sp_command_preference"

print("Registering " + GetConditionName())
###################################################

def SP_Command_Preference_S_EndTurn(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Signal)
	args.condition_remove()
	return 0

def SP_Command_Preference_OnD20PythonQuery(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Signal)
	evt_obj.return_val = args.get_arg(0) + 1
	print("SP_Command_Preference :: evt_obj.return_val = {}".format(evt_obj.return_val))
	#debug.breakp("Contagion_Desease_Preference_OnD20PythonQuery")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2) # 1 - preference
modObj.AddHook(toee.ET_OnD20Signal, toee.EK_S_EndTurn, SP_Command_Preference_S_EndTurn, ())
modObj.AddHook(toee.ET_OnD20PythonQuery, "sp-Command Preference", SP_Command_Preference_OnD20PythonQuery, ())
