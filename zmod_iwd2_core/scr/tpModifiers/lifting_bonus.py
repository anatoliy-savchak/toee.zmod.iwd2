import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def GetConditionName():
	return "Lifting_Bonus"

print("Registering " + GetConditionName())
###################################################

def Lifting_Bonus_OnAbilityScoreLevel_STR(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjBonusList)
	
	# new flag 0x8 = Encumbrance Str Score
	if (evt_obj.flags & 0x8):
		str_bonus = args.get_arg(0)
		if (str_bonus != 0):
			evt_obj.bonus_list.add(str_bonus, toee.stat_strength, "Lifting Bonus") 
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # 1: Str bonus for Encumbrance
modObj.AddHook(toee.ET_OnAbilityScoreLevel, toee.EK_STAT_STRENGTH, Lifting_Bonus_OnAbilityScoreLevel_STR, ())