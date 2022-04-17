import toee, templeplus.pymod, tpdp

###################################################

def GetConditionName():
	return "Multiattack"

print("Registering " + GetConditionName())
###################################################
ATTACK_CODE_NATURAL_ATTACK = 1000

def get_natural_attack_index(npc, attack_num):
	assert isinstance(npc, toee.PyObjHandle)

	j = 0
	for i in range(0, 4):
		attacks_count = npc.obj_get_idx_int(toee.obj_f_critter_attacks_idx, i)
		if not attacks_count:
			# there is no monster attacks configured
			break
		j += attacks_count
		if attack_num < j:
			# this is the one
			return i
	return None

def OnToHitBonus2(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjAttack)
	
	if evt_obj.attack_packet.event_key > ATTACK_CODE_NATURAL_ATTACK:
		num_nat_attack = evt_obj.attack_packet.event_key - ATTACK_CODE_NATURAL_ATTACK - 1
		index_nat_attack = num_nat_attack
		if not index_nat_attack is None:
			if index_nat_attack > 0:
				# compensate configured -5 penalty to -2
				evt_obj.bonus_list.add(5-2, 0, "Multiattack")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2) # 
modObj.AddHook(toee.ET_OnToHitBonus2, toee.EK_NONE, OnToHitBonus2, ())
