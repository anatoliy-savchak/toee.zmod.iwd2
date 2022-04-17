import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def GetConditionName():
	return "Fast_Healing"

print("Registering " + GetConditionName())
###################################################

def OnBeginRound(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjDamage)
	try:
		hp_current = attachee.stat_level_get(toee.stat_hp_current)
		if hp_current > 0: # zero does not allow healing
			hp_max = attachee.stat_level_get(toee.stat_hp_max)
			damaged = hp_max - hp_current
			if damaged > 0: 
				amount = args.get_arg(0)
				if amount > 0:
					dice = toee.dice_new("0d0+{}".format(amount))
					attachee.heal(attachee, dice, toee.D20A_CLASS_ABILITY_SA, 0)
					toee.game.create_history_from_pattern(57, attachee, attachee) # {57}{[ACTOR] ~uses fast healing~[TAG_SPECIAL_ABILITIES_FAST_HEALING]!}
	except Exception, e:
		print("{} OnBeginRound:".format(GetConditionName()))
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("error")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 6) # 0 - amount
modObj.AddHook(toee.ET_OnBeginRound, toee.EK_NONE, OnBeginRound, ())