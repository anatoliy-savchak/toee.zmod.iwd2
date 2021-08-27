import toee, templeplus.pymod, debug, sys, tpdp

###################################################

def GetConditionName():
	return "Asleep"

print("Registering " + GetConditionName())
###################################################

def Asleep_OnConditionAdd(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	attachee.fall_down()
	attachee.critter_flag_set(toee.OCF_SLEEPING)
	return

def Asleep_OnD20Query_Q_Unconscious(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Query)
	evt_obj.return_val = 1
	return 0

def Asleep_OnGetTooltip(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjTooltip)
	evt_obj.append("Sleeping")
	return 0

def AsleepRemove(attachee, args):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	args.condition_remove()
	attachee.critter_flag_unset(toee.OCF_SLEEPING)
	#attachee.condition_remove("prone")
	print("AsleepRemove")
	return

def Asleep_Remove(attachee, args, evt_obj):
	AsleepRemove(attachee, args)
	return

def TurnBasedStatusInitNoActions(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjTurnBasedStatus)
	evt_obj.tb_status.hourglass_state = 0
	evt_obj.tb_status.flags |= 2
	return 0

def QuerySetReturnVal1(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Query)
	evt_obj.return_val = 1
	return 0

def QuerySetReturnVal0(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Query)
	evt_obj.return_val = 0
	return 0

def Asleep_OnGetAC(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjAttack)
	if (evt_obj.attack_packet.get_flags() & toee.D20CAF_RANGED):
		evt_obj.bonus_list.add(4, 0, 162) # {162}{~Prone~[TAG_PRONE]}
	else:
		evt_obj.bonus_list.add(-4, 0, 162) # {162}{~Prone~[TAG_PRONE]}
	return 0

def Asleep_OnGetACBonus2(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjAttack)
	if (not (evt_obj.attack_packet.get_flags() & toee.D20CAF_RANGED)):
		evt_obj.bonus_list.add(-4, 0, 162) # {162}{~Prone~[TAG_PRONE]}
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2)
modObj.AddHook(toee.ET_OnConditionAdd, toee.EK_NONE, Asleep_OnConditionAdd, ())
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_Unconscious, Asleep_OnD20Query_Q_Unconscious, ())
modObj.AddHook(toee.ET_OnGetTooltip, toee.EK_NONE, Asleep_OnGetTooltip, ())
modObj.AddHook(toee.ET_OnD20Signal, toee.EK_S_Attack_Made, Asleep_Remove, ()) # gets triggered at the end of the damage calculation
modObj.AddHook(toee.ET_OnD20Signal, toee.EK_S_Killed, Asleep_Remove, ())
modObj.AddHook(toee.ET_OnD20Signal, toee.EK_S_HP_Changed, Asleep_Remove, ())
modObj.AddHook(toee.ET_OnD20Signal, toee.EK_S_AID_ANOTHER_WAKE_UP, Asleep_Remove, ())

# sleeping duplicate
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_SneakAttack, QuerySetReturnVal1, ())
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_Helpless, QuerySetReturnVal1, ())
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_CannotCast, QuerySetReturnVal1, ())
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_AOOPossible, QuerySetReturnVal0, ())
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_CoupDeGrace, QuerySetReturnVal1, ())

# prone duplicate
modObj.AddHook(toee.ET_OnGetAC, toee.EK_NONE, Asleep_OnGetAC, ())
modObj.AddHook(toee.ET_OnGetACBonus2, toee.EK_NONE, Asleep_OnGetACBonus2, ())
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_Prone, QuerySetReturnVal1, ())

modObj.AddHook(toee.ET_OnD20PythonSignal, "wake up", Asleep_Remove, ())