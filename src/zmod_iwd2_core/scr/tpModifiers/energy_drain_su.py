import toee, templeplus.pymod, tpdp

###################################################

def GetConditionName():
	return "Energy_Drain_Su"

print("Registering " + GetConditionName())
###################################################

def Energy_Drain_Su_DamageBonus(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjDamage)
	print("Energy_Drain_Su_DamageBonus adding negative level")

	attacks_with_drain = args.get_arg(0)
	num_nat_attack = evt_obj.attack_packet.event_key - 1000
	print("evt_obj.attack_packet.event_key: {}, mode: {}".format(evt_obj.attack_packet.event_key, attacks_with_drain))

	if (attacks_with_drain != 0): # 0 for all
		flag = 1
		if (num_nat_attack > 0):
			flag = (1 << (num_nat_attack))
		print("attacks_with_drain: {}, flag: {}".format(attacks_with_drain, flag))
		if (not (attacks_with_drain & flag)): 
			print("NOT THIS NATURAL ATTACK")
			return 0

	target = evt_obj.attack_packet.target
	target.condition_add("Temp Negative Level")
	target.float_text_line("Nagative Level!", toee.tf_red)
	toee.game.create_history_from_pattern(60, attachee, target) # {60}{[ACTOR] strikes with ~energy drain~[TAG_ENERGY_DRAINED] on [TARGET]!}

	heal_hp = args.get_arg(1)
	attachee.condition_add_with_args("Temporary_Hit_Points", 0, 14400, heal_hp)
	toee.game.create_history_from_pattern(61, attachee, toee.OBJ_HANDLE_NULL) # {61}{[ACTOR] recieves 5 ~temporary hit points~[TAG_TEMPORARY_HIT_POINTS].}
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2) # 0- attacks_with_drain, 1 - heal hp
modObj.AddHook(toee.ET_OnDealingDamage, toee.EK_NONE, Energy_Drain_Su_DamageBonus, ())

