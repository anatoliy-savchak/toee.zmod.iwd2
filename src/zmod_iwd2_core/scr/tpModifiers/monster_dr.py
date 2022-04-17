import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def GetConditionName():
	return "Monster_DR"

print("Registering " + GetConditionName())
###################################################

def OnTakingDamage(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjDamage)
	try:
		amount = args.get_arg(0)
		if amount > 0:
			bypass = args.get_arg(1)# toee.D20DAP_SILVER
			if bypass:
				evt_obj.damage_packet.add_physical_damage_res(amount, bypass, 126)# damage.mes {126}{~Damage Reduction~[TAG_SPECIAL_ABILITIES_DAMAGE_REDUCTION]}
	except Exception, e:
		print("{} OnDealingDamage:".format(GetConditionName()))
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("error")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 6) # 0 - amount, 1 - bypass power
modObj.AddHook(toee.ET_OnTakingDamage, toee.EK_NONE, OnTakingDamage, ())