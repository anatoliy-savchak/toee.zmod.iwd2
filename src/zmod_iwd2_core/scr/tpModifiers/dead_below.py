import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def GetConditionName():
	return "Dead_Below"

print("Registering " + GetConditionName())
###################################################

def Kill(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	try:
		hp = attachee.stat_level_get(toee.stat_hp_current)
		if (hp < 0 or (hp == 0 and args.get_arg(0))):
			last = attachee.obj_get_obj(toee.obj_f_npc_who_hit_me_last)
			attachee.critter_kill_by_effect(last)
	except Exception, e:
		print "Kill:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("error")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # 0 - when 1 then 0 HP means dead
modObj.AddHook(toee.ET_OnObjectEvent, toee.EK_S_HP_Changed, Kill, ())
