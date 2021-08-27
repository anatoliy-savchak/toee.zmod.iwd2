import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def GetConditionName():
	return "Monster_Touch_Attack"

print("Registering " + GetConditionName())
###################################################

def Monster_Touch_Attack_OnToHitBonus2(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjAttack)
	try:
		evt_obj.attack_packet.set_flags(toee.D20CAF_TOUCH_ATTACK)
	except Exception, e:
		print "Monster_Touch_Attack_OnToHitBonus2:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("error")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # natural_attack_num_pattern, 
modObj.AddHook(toee.ET_OnToHitBonus2, toee.EK_NONE, Monster_Touch_Attack_OnToHitBonus2, ())