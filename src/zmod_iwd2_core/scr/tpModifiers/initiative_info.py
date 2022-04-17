import toee, templeplus.pymod, tpdp, sys, debug, traceback
import utils_npc

###################################################

def GetConditionName():
	return "InitiativeInfo"

print("Registering " + GetConditionName())
###################################################

def InitiativeInfo_Print(attachee, args):
	assert isinstance(attachee, toee.PyObjHandle)
	try:
		if not args.get_arg(1) and toee.game.combat_is_active():
			args.set_arg(1, 1)
			npcs = list()
			for npc in toee.game.obj_list_vicinity(attachee.location, toee.OLC_CRITTERS):
				if not utils_npc.npc_could_be_attacked(npc): continue
				tup = (npc, npc.get_initiative())
				npcs.append(tup)

			if npcs:
				npcs = sorted(npcs, key = lambda o: o[1], reverse = True)
				toee.game.create_history_freeform("Initiative Rolls\n\n")
				for tup in npcs:
					line = "+{:02d} {} CR {}\n".format(tup[1], tup[0].description, utils_npc.npc_get_cr(tup[0]))
					toee.game.create_history_freeform(line)
				toee.game.create_history_freeform("\n\n")

	except Exception, e:
		print "InitiativeInfo_Print:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("error")
	return

def InitiativeInfo_OnTurnBasedStatusInit(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjTurnBasedStatus)
	InitiativeInfo_Print(attachee, args)
	return 0

def InitiativeInfo_OnD20Signal_S_Combat_End(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Signal)

	args.set_arg(1, 0)
	return 0

def InitiativeInfo_OnD20PythonSignal_CombatStart(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Signal)

	InitiativeInfo_Print(attachee, args)
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2, 1) # 0 - none, 1 - internal, has printed
modObj.AddHook(toee.ET_OnTurnBasedStatusInit, toee.EK_NONE, InitiativeInfo_OnTurnBasedStatusInit, ())
modObj.AddHook(toee.ET_OnD20Signal, toee.EK_S_Combat_End, InitiativeInfo_OnD20Signal_S_Combat_End, ())
modObj.AddHook(toee.ET_OnD20PythonSignal, "Combat Start", InitiativeInfo_OnD20PythonSignal_CombatStart, ())

###################################################

def GetConditionName():
	return "InitiativeInfoHelper"

print("Registering " + GetConditionName())
###################################################

def InitiativeInfoHelper_OnTurnBasedStatusInit(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjTurnBasedStatus)
	toee.game.party[0].d20_send_signal("Combat Start")
	return 0

def InitiativeInfoHelper_OnD20Signal_S_BeginTurn(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Signal)

	toee.game.party[0].d20_send_signal("Combat Start")
	return 0

modObj2 = templeplus.pymod.PythonModifier(GetConditionName(), 2, 1)
#modObj2.AddHook(toee.ET_OnD20Signal, toee.EK_S_BeginTurn, InitiativeInfoHelper_OnD20Signal_S_BeginTurn, ())
modObj2.AddHook(toee.ET_OnTurnBasedStatusInit, toee.EK_NONE, InitiativeInfoHelper_OnTurnBasedStatusInit, ())