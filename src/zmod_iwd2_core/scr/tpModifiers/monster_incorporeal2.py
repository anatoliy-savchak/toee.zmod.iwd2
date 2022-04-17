import toee, templeplus.pymod, sys, tpdp, math, traceback, debug
import roll_history

###################################################
def GetConditionName():
	return "Monster_Incorporeal2"

print("Registering " + GetConditionName())
###################################################

def roll_miss_chance():
    concealmentDice = toee.dice_new("1d100")
    concealmentDiceRoll = concealmentDice.roll()
    if concealmentDiceRoll > 50:
        return True, concealmentDiceRoll
    return False, concealmentDiceRoll

def debug_print_damage(damage_packet, type, type_name):
	assert isinstance(damage_packet, tpdp.DamagePacket)
	assert isinstance(type, int)
	dam = damage_packet.get_overall_damage_by_type(type)
	print('{}: {}'.format(type_name, dam))
	return

def debug_print_damages(damage_packet):
	assert isinstance(damage_packet, tpdp.DamagePacket)
	debug_print_damage(damage_packet, toee.D20DT_UNSPECIFIED, 'D20DT_UNSPECIFIED')
	debug_print_damage(damage_packet, toee.D20DT_BLUDGEONING, 'D20DT_BLUDGEONING')
	debug_print_damage(damage_packet, toee.D20DT_PIERCING, 'D20DT_PIERCING')
	debug_print_damage(damage_packet, toee.D20DT_SLASHING, 'D20DT_SLASHING')
	debug_print_damage(damage_packet, toee.D20DT_BLUDGEONING_AND_PIERCING, 'D20DT_BLUDGEONING_AND_PIERCING')
	debug_print_damage(damage_packet, toee.D20DT_PIERCING_AND_SLASHING, 'D20DT_PIERCING_AND_SLASHING')
	debug_print_damage(damage_packet, toee.D20DT_SLASHING_AND_BLUDGEONING, 'D20DT_SLASHING_AND_BLUDGEONING')
	debug_print_damage(damage_packet, toee.D20DT_SLASHING_AND_BLUDGEONING_AND_PIERCING, 'D20DT_SLASHING_AND_BLUDGEONING_AND_PIERCING')
	debug_print_damage(damage_packet, toee.D20DT_ACID, 'D20DT_ACID')
	debug_print_damage(damage_packet, toee.D20DT_COLD, 'D20DT_COLD')
	debug_print_damage(damage_packet, toee.D20DT_ELECTRICITY, 'D20DT_ELECTRICITY')
	debug_print_damage(damage_packet, toee.D20DT_FIRE, 'D20DT_FIRE')
	debug_print_damage(damage_packet, toee.D20DT_SONIC, 'D20DT_SONIC')
	debug_print_damage(damage_packet, toee.D20DT_NEGATIVE_ENERGY, 'D20DT_NEGATIVE_ENERGY')
	debug_print_damage(damage_packet, toee.D20DT_SUBDUAL, 'D20DT_SUBDUAL')
	debug_print_damage(damage_packet, toee.D20DT_POISON, 'D20DT_POISON')
	debug_print_damage(damage_packet, toee.D20DT_POSITIVE_ENERGY, 'D20DT_POSITIVE_ENERGY')
	debug_print_damage(damage_packet, toee.D20DT_FORCE, 'D20DT_FORCE')
	debug_print_damage(damage_packet, toee.D20DT_BLOOD_LOSS, 'D20DT_BLOOD_LOSS')
	debug_print_damage(damage_packet, toee.D20DT_MAGIC, 'D20DT_MAGIC')
	return

def get_immune_damage(except_types, damage_packet, type, type_name):
	if (type in except_types):
		#print('{}: bypass'.format(type_name))
		return None

	dam = damage_packet.get_overall_damage_by_type(type)
	#print('immune? {}: {}'.format(type_name, dam))
	if (dam > 0):
		return (type, dam)
	return None

def get_immune_damages(damage_packet, except_types):
	result = list()
	#tup = get_immune_damage(damage_packet, except_types, toee.D20DT_UNSPECIFIED, 'D20DT_UNSPECIFIED')
	#if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_BLUDGEONING, 'D20DT_BLUDGEONING')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_PIERCING, 'D20DT_PIERCING')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_SLASHING, 'D20DT_SLASHING')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_BLUDGEONING_AND_PIERCING, 'D20DT_BLUDGEONING_AND_PIERCING')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_PIERCING_AND_SLASHING, 'D20DT_PIERCING_AND_SLASHING')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_SLASHING_AND_BLUDGEONING, 'D20DT_SLASHING_AND_BLUDGEONING')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_SLASHING_AND_BLUDGEONING_AND_PIERCING, 'D20DT_SLASHING_AND_BLUDGEONING_AND_PIERCING')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_ACID, 'D20DT_ACID')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_COLD, 'D20DT_COLD')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_ELECTRICITY, 'D20DT_ELECTRICITY')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_FIRE, 'D20DT_FIRE')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_SONIC, 'D20DT_SONIC')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_NEGATIVE_ENERGY, 'D20DT_NEGATIVE_ENERGY')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_SUBDUAL, 'D20DT_SUBDUAL')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_POISON, 'D20DT_POISON')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_POSITIVE_ENERGY, 'D20DT_POSITIVE_ENERGY')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_FORCE, 'D20DT_FORCE')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_BLOOD_LOSS, 'D20DT_BLOOD_LOSS')
	if (tup): result.append(tup)
	tup = get_immune_damage(except_types, damage_packet, toee.D20DT_MAGIC, 'D20DT_MAGIC')
	if (tup): result.append(tup)
	return result

def OnTakingDamage(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjDamage)
	try:
		bypassed = toee.D20DAP_HOLY | toee.D20DAP_UNHOLY | toee.D20DAP_MAGIC
		evt_obj.damage_packet.add_physical_damage_res(100, bypassed, 131) # not sure about this
		overall = evt_obj.damage_packet.get_overall_damage()
		if (overall > 0):
			got_list = get_immune_damages(evt_obj.damage_packet, [toee.D20DT_FORCE, toee.D20DT_NEGATIVE_ENERGY, toee.D20DT_POSITIVE_ENERGY])
			#print("got_list: ".format(got_list))

			if (got_list):
				is_success, miss_chance_roll = roll_miss_chance()
				roll_id = 0
				if (is_success):
					roll_id = roll_history.add_percent_chance_roll(attachee, evt_obj.attack_packet.target, 50, 60, miss_chance_roll, 194, 193)
				else:
					roll_id = roll_history.add_percent_chance_roll(attachee, evt_obj.attack_packet.target, 50, 60, miss_chance_roll, 195, 193)
				toee.game.create_history_from_id(roll_id)

				if (is_success):
					for tup in got_list:
						type = tup[0]
						dam = tup[1]
						evt_obj.damage_packet.add_mod_factor(0, type, 131)
	except Exception, e:
		print("{} OnDealingDamage:".format(GetConditionName()))
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("error")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # 
modObj.AddHook(toee.ET_OnTakingDamage, toee.EK_NONE, OnTakingDamage, ())