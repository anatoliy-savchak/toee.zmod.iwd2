import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def GetConditionName():
	return "Monster_Sole_Natural"

print("Registering " + GetConditionName())
###################################################

def Monster_Sole_Natural_OnD20Query_Q_WieldedTwoHanded(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Query)
	print("Monster_Sole_Natural_OnD20Query_Q_WieldedTwoHanded = 1")
	evt_obj.return_val = 1
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # 
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_WieldedTwoHanded, Monster_Sole_Natural_OnD20Query_Q_WieldedTwoHanded, ())