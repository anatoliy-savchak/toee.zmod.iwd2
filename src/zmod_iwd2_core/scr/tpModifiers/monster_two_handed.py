import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def GetConditionName():
	return "Monster_Two_Handed"

print("Registering " + GetConditionName())
###################################################

def Monster_Two_Handed_OnDealingDamage(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjDamage)
	try:
		str_mod = (attachee.stat_level_get(toee.stat_strength) - 10) >> 1
		if (str_mod > 1):
			evt_obj.damage_packet.add_damage_bonus(str_mod // 2, 0, 103) # damage.mes {103}{Strength}
	except Exception, e:
		print "Monster_Two_Handed_OnDealingDamage:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("error")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # 
modObj.AddHook(toee.ET_OnDealingDamage, toee.EK_NONE, Monster_Two_Handed_OnDealingDamage, ())