import toee, templeplus.pymod, tpdp, traceback, sys

###################################################

def GetConditionName():
	return "Monster Displacement"

print("Registering " + GetConditionName())
###################################################


def Monster_Displacement_OnGetDefenderConcealmentMissChance(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Signal)

	if (not evt_obj.attack_packet.attacker.d20_query(toee.Q_Critter_Has_True_Seeing)):
		evt_obj.bonus_list.add(50, 19, 185) #{185}{~Displacement~[TAG_SPELLS_DISPLACEMENT]}
	return 0

def Monster_Displacement_OnGetEffectTooltip(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjEffectTooltip)
	evt_obj.append(27, toee.spell_displacement, "")
	return 0

def Monster_Displacement_OnGetTooltip(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjTooltip)
	evt_obj.append("Displacement (Su)")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 6) # 0 
modObj.AddHook(toee.ET_OnGetDefenderConcealmentMissChance, toee.EK_NONE, Monster_Displacement_OnGetDefenderConcealmentMissChance, ())
modObj.AddHook(toee.ET_OnGetEffectTooltip, toee.EK_NONE, Monster_Displacement_OnGetEffectTooltip, ())
#modObj.AddHook(toee.ET_OnGetTooltip, toee.EK_NONE, Monster_Displacement_OnGetTooltip, ())