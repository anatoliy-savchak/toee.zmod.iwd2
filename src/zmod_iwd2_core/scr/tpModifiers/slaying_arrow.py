import toee, templeplus.pymod, traceback, sys, debug, const_toee

###################################################

def GetConditionName():
	return "Slaying_Arrow"

print("Registering " + GetConditionName())
###################################################

def Slaying_Arrow_OnDealingDamage(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjDamage)
	try:
		tgt = evt_obj.attack_packet.target
		assert isinstance(tgt, toee.PyObjHandle)

		print("Slaying_Arrow_OnDealingDamage target: {}, event_key: {}".format(tgt, evt_obj.attack_packet.event_key))

		hit = evt_obj.attack_packet.get_flags() & toee.D20CAF_HIT
		print("hit: {}, flags: {}".format(hit, evt_obj.attack_packet.get_flags()))
		if not (hit and tgt):
			return 0

		category = args.get_arg(0)
		if category:
			target_category = tgt.get_category_type()
			if category != target_category:
				print("Wrong category! category: {}, target_category: {}".format(category, target_category))
				return 0

		category_subtype = args.get_arg(1)
		if category_subtype and not tgt.is_category_subtype(category_subtype):
			print("Wrong category_subtype! category_subtype: {}".format(category_subtype))
			return 0

		fort_dc = args.get_arg(3)
		if not fort_dc: fort_dc = 23
		if fort_dc:
			#saved = tgt.saving_throw_spell(fort_dc, toee.D20_Save_Fortitude, const_toee.D20STD_SPELL_SCHOOL_NECROMANCY & const_toee.D20STD_SPELL_DESCRIPTOR_DEATH, attachee, 0, 0)
			saved = tgt.saving_throw(fort_dc, toee.D20_Save_Fortitude, const_toee.D20STD_SPELL_SCHOOL_NECROMANCY & const_toee.D20STD_SPELL_DESCRIPTOR_DEATH, attachee, toee.D20A_ACTIVATE_DEVICE_SPELL)
			if saved:
				tgt.float_mesfile_line('mes\\spell.mes', 30001)
				return 0
			else:
				tgt.float_mesfile_line('mes\\spell.mes', 30002)

		toee.game.particles('sp-Vampiric Touch', tgt)
		tgt.critter_kill_by_effect(attachee)
	except Exception, e:
		print "Slaying_Arrow_OnDealingDamage error:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("error")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 6) # 0 - monster type, 1 - monster subtype, 2 - item_inv, 3 - Fort DC
modObj.AddHook(toee.ET_OnDealingDamage, toee.EK_NONE, Slaying_Arrow_OnDealingDamage, ())
