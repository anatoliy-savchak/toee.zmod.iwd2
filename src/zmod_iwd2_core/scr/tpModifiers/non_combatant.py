import toee, templeplus.pymod, tpdp, debug

###################################################

def GetConditionName():
	return "Non_Combatant"

print("Registering " + GetConditionName())
###################################################

def OnQueryReturnTrue(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Query)
	
	evt_obj.return_val = 1
	return 0

def OnQueryReturnFalse(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Query)
	
	evt_obj.return_val = 0
	return 0

def OnQueryReturnFalseAndHide(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Query)
	
	evt_obj.return_val = 0
	attachee.object_flag_set(toee.OF_DONTDRAW)
	return 0

def Reveal(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	#assert isinstance(evt_obj, tpdp.EventObjD20Query)
	
	attachee.object_flag_unset(toee.OF_DONTDRAW)
	return 0

def OnTurnBasedStatusInit(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjTurnBasedStatus)

	attachee.critter_flag_set(toee.ONF_NO_ATTACK)
	if (attachee.is_active_combatant()):
		attachee.ai_stop_attacking()
		Reveal(attachee, args, evt_obj)
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2) #
modObj.AddHook(toee.ET_OnTurnBasedStatusInit, toee.EK_NONE, OnTurnBasedStatusInit, ())
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_CanBeAffected_PerformAction, OnQueryReturnFalse, ())
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_CanBeAffected_ActionFrame, OnQueryReturnFalse, ())
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_EnterCombat, OnQueryReturnFalseAndHide, ())
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_Autoend_Turn, OnQueryReturnTrue, ())
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_ExperienceExempt, OnQueryReturnTrue, ())
modObj.AddHook(toee.ET_OnD20Signal, toee.EK_S_Combat_End, Reveal, ())
