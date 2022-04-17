import toee, templeplus.pymod, tpdp, debug

###################################################

def GetConditionName():
	return "Rest_Full"

print("Registering " + GetConditionName())
###################################################

def Rest_Full_OnNewDay(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)

	max_hp = attachee.stat_level_get(toee.stat_hp_max)
	hp_current = attachee.stat_level_get(toee.stat_hp_current)

	delta = max_hp - hp_current
	if (delta > 0):
		print('Rest_Full_OnNewDay, heal: {} on {}'.format(delta, attachee))
		attachee.heal(attachee, toee.dice_new('0d0+{}'.format(delta)), toee.D20A_NONE, 0)

	return 0

def Rest_Full_MaxHPTest(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)

	debug.breakp('Rest_Full_MaxHPTest')

	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 4) # reserved
modObj.AddHook(toee.ET_OnNewDay, toee.EK_NEWDAY_REST, Rest_Full_OnNewDay, ())
#modObj.AddHook(toee.ET_OnGetMaxHP, toee.EK_NONE, Rest_Full_MaxHPTest, ())


