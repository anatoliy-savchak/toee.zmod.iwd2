import toee, templeplus.pymod, debug, sys, tpdp

###################################################

def GetConditionName():
	return "ExperienceExempt"

print("Registering " + GetConditionName())
###################################################

def ExperienceExempt_OnD20Query_Q_Unconscious(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Query)
	evt_obj.return_val = 1
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2)
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_ExperienceExempt, ExperienceExempt_OnD20Query_Q_Unconscious, ())
