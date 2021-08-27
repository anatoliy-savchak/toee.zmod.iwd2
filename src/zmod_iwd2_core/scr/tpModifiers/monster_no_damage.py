import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def GetConditionName():
	return "Monster_No_Damage" # will not work due to minimum damage, see DamageCritter / Dispatch21TakingDamageFinal / EnsureMinimumDamage1

print("Registering " + GetConditionName())
###################################################

def Monster_No_Damage_OnDealingDamage2(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjDamage)
	try:
		evt_obj.damage_packet.add_damage_bonus(-evt_obj.damage_packet.final_damage, 0, 0)
		evt_obj.damage_packet.final_damage = 0
	except Exception, e:
		print "Monster_No_Damage_OnDealingDamage2:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("error")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # natural_attack_num_pattern, 
modObj.AddHook(toee.ET_OnDealingDamage2, toee.EK_NONE, Monster_No_Damage_OnDealingDamage2, ())