import toee, templeplus.pymod, tpdp, debug, sys

###################################################

def GetConditionName():
	return "Bonus_AC"

print("Registering " + GetConditionName())
###################################################

def Bonus_AC_OnGetBonusAttacks(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	
	if (evt_obj.bonus_list and args.get_arg(0)):
		evt_obj.bonus_list.add(args.get_arg(0), 9, "Custom")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2) # 0 - number of AC bonus
modObj.AddHook(toee.ET_OnGetAC, toee.EK_NONE, Bonus_AC_OnGetBonusAttacks, ())

