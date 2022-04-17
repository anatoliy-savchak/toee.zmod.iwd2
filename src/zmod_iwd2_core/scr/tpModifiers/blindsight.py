import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def GetConditionName():
	return "Blindsignt"

print("Registering " + GetConditionName())
###################################################

def Blindsignt_OnD20PythonQuery_BlindsightRange(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Signal)
	
	evt_obj.return_val = args.get_arg(0)
	return 0

def OnQueryReturnTrue(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Query)

	evt_obj.return_val = 1
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # 0 = range, reserved
modObj.AddHook(toee.ET_OnD20PythonQuery, "Blindsight Range", Blindsignt_OnD20PythonQuery_BlindsightRange, ())
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_Critter_Has_True_Seeing, OnQueryReturnTrue, ())