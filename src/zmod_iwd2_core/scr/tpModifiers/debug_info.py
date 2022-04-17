import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def Debug_Location_GetConditionName():
	return "Debug_Location"

print("Registering " + Debug_Location_GetConditionName())
###################################################

def Debug_Location_OnGetTooltip(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjTooltip)

	loc = attachee.location_full
	evt_obj.append(str(loc) + "=> " + str(loc.get_overall_offset()))
	return 0

oDebug_Location = templeplus.pymod.PythonModifier(Debug_Location_GetConditionName(), 3) # reserved
oDebug_Location.AddHook(toee.ET_OnGetTooltip, toee.EK_NONE, Debug_Location_OnGetTooltip, ())

###################################################
def Debug_Rotation_GetConditionName():
	return "Debug_Rotation"

print("Registering " + Debug_Rotation_GetConditionName())
###################################################

def Debug_Rotation_OnGetTooltip(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjTooltip)

	rot = attachee.rotation
	rot_degr = math.degrees(rot)
	evt_obj.append("Rot: {:.1f} ({:.3f})".format(rot_degr, rot))
	return 0

oDebug_Rotation = templeplus.pymod.PythonModifier(Debug_Rotation_GetConditionName(), 3) # reserved
oDebug_Rotation.AddHook(toee.ET_OnGetTooltip, toee.EK_NONE, Debug_Rotation_OnGetTooltip, ())

###################################################

def GetConditionName():
	return "TurnWatcher"

print("Registering " + GetConditionName())
###################################################

def TurnWatcher_OnTurnBasedStatusInit(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjTurnBasedStatus)

	print("OnTurnBasedStatusInit is_combat_active: {}, is_combatant: {}, NPC: {}".format(toee.game.combat_is_active(), attachee.is_active_combatant(), attachee))
	return 0

def TurnWatcher_OnBeginRound(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Signal)

	print("OnBeginRound is_combat_active: {}, is_combatant: {}, NPC: {}".format(toee.game.combat_is_active(), attachee.is_active_combatant(), attachee))
	return 0

def TurnWatcher_OnD20Signal_S_BeginTurn(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Signal)

	print("OnD20Signal_S_BeginTurn is_combat_active: {}, is_combatant: {}, NPC: {}".format(toee.game.combat_is_active(), attachee.is_active_combatant(), attachee))
	return 0

def TurnWatcher_OnD20Signal_S_EndTurn(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Signal)

	print("OnD20Signal_S_EndTurn {}".format(attachee))
	return 0

def TurnWatcher_OnInitiative(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	# evt_obj is None

	print("OnInitiative is_combat_active: {}, is_combatant: {}, NPC: {}".format(toee.game.combat_is_active(), attachee.is_active_combatant(), attachee))
	return 0

turn_watcher_modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2, 1) #
turn_watcher_modObj.AddHook(toee.ET_OnInitiative, toee.EK_NONE, TurnWatcher_OnInitiative, ())
turn_watcher_modObj.AddHook(toee.ET_OnBeginRound, toee.EK_NONE, TurnWatcher_OnBeginRound, ())
turn_watcher_modObj.AddHook(toee.ET_OnTurnBasedStatusInit, toee.EK_NONE, TurnWatcher_OnTurnBasedStatusInit, ())
turn_watcher_modObj.AddHook(toee.ET_OnD20Signal, toee.EK_S_BeginTurn, TurnWatcher_OnD20Signal_S_BeginTurn, ())
turn_watcher_modObj.AddHook(toee.ET_OnD20Signal, toee.EK_S_EndTurn, TurnWatcher_OnD20Signal_S_EndTurn, ())
