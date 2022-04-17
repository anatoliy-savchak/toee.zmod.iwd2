import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def GetConditionName():
	return "Improved_Natural_Armor"

print("Registering " + GetConditionName())
###################################################

def Improved_Natural_Armor_OnGetAC(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjAttack)

	evt_obj.bonus_list.add(args.get_arg(0), 9, 400)

	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # 0 - amount
modObj.AddHook(toee.ET_OnGetAC, toee.EK_NONE, Improved_Natural_Armor_OnGetAC, ())