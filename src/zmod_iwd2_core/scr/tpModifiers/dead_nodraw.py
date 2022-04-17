import toee, templeplus.pymod, sys, tpdp, math, traceback, debug

###################################################
def GetConditionName():
	return "Dead_NoDraw"

print("Registering " + GetConditionName())
###################################################

obj_f_transparency = toee.obj_f_overlay_back #7
def CheckDraw(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	try:
		is_dead = attachee.stat_level_get(toee.stat_hp_current) < 0
		if (is_dead):
			is_nodraw = attachee.object_flags_get() & toee.OF_DONTDRAW
			#print("CheckDraw dead nodraw: {}, combat: {} for {}".format(is_nodraw, toee.game.combat_is_active(), attachee))
			#debug.breakp("CheckDraw")
			if (is_nodraw and not toee.game.combat_is_active()):
				#print("UnSetting no draw")
				attachee.object_flag_unset(toee.OF_DONTDRAW)
				attachee.obj_set_int(obj_f_transparency, 256)
			elif (not is_nodraw and toee.game.combat_is_active()):
				#print("Setting no draw")
				attachee.object_flag_set(toee.OF_DONTDRAW)
				attachee.obj_set_int(obj_f_transparency, 128)
	except Exception, e:
		print "CheckDraw:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("error")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3)
modObj.AddHook(toee.ET_OnBeginRound, toee.EK_NONE, CheckDraw, ())
modObj.AddHook(toee.ET_OnObjectEvent, toee.EK_S_Killed, CheckDraw, ())
modObj.AddHook(toee.ET_OnObjectEvent, toee.EK_S_HP_Changed, CheckDraw, ())
