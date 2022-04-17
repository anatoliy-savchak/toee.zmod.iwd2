import toee, templeplus.pymod, tpdp, debug

###################################################
#draft
def GetConditionName():
	return "Vulnurability_Energy"

print("Registering " + GetConditionName())
###################################################

def OnTakingDamage2(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjDamage)
	if (args.get_arg(1) or not (evt_obj.attack_packet.flags & toee.D20CAF_SAVE_SUCCESSFUL)):
		evt_obj.damage_packet.add_mod_factor(2.0, args.get_arg(0), 129) # {129}{Doubled Damage}
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2) # 0 - Damage Type D20DT_UNSPECIFIED, 1 - skip save
modObj.AddHook(toee.ET_OnTakingDamage2, toee.EK_NONE, OnTakingDamage2, ())

