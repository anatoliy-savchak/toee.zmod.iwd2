import toee, templeplus.pymod, tpdp, traceback, sys, debug

###################################################

def GetConditionName():
	return "Monster Melee Paralysis Ex"

print("Registering " + GetConditionName())
###################################################

def Monster_Melee_Paralysis_Ex_OnDealingDamage2(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjDamage)
	try:
		print("Monster_Melee_Paralysis_Ex_OnDealingDamage2")
		attacks_with_paralysis = args.get_arg(3)
		num_nat_attack = evt_obj.attack_packet.event_key - 1000 # attacks start from 0, always increase, even if double strike
		print("evt_obj.attack_packet.event_key: {}, attacks_with_paralysis: {}".format(evt_obj.attack_packet.event_key, attacks_with_paralysis))

		if (attacks_with_paralysis != 0): # 0 for all
			flag = 1
			if (num_nat_attack > 0):
				flag = (1 << (num_nat_attack))
			print("attacks_with_paralysis: {}, flag: {}".format(attacks_with_paralysis, flag))
			if (not (attacks_with_paralysis & flag)): 
				print("NOT THIS NATURAL ATTACK")
				return 0

		target = evt_obj.attack_packet.target
		toee.game.create_history_from_pattern(69, attachee, target) # {69}{[ACTOR] strikes with ~paralysis~[TAG_PARALYZED] on [TARGET]!}

		dc = args.get_arg(0)
		if (dc):
			save = args.get_arg(1)
			saved = target.saving_throw(dc, save, toee.D20STD_F_NONE, attachee)
			if (saved): 
				print("saved!")
				return 0

		dice_packed = int(args.get_arg(2)) #!! long will fail

		dice = toee.dice_new("1d1")
		#print("setting dice_packed: {}".format(dice_packed))
		#debug.breakp("dice_packed")
		dice.packed = dice_packed

		amount = dice.roll()
		print("target.condition_add_with_args(Paralyzed, {} rounds) {}".format(amount, target))
		target.condition_add_with_args("Paralyzed", amount)
		target.float_text_line("Paralyzed!", toee.tf_red)
	except Exception, e:
		print "Monster_Melee_Paralysis_Ex_OnDealingDamage2 error:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("error")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 6) # 0 dc, 1 save, 2 dice, 3 attacks_with_paralysis
modObj.AddHook(toee.ET_OnDealingDamage2, toee.EK_NONE, Monster_Melee_Paralysis_Ex_OnDealingDamage2, ())

