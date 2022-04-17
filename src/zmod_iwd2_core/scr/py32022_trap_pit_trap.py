import toee, debug

def san_trap(trap, triggerer):
	assert isinstance(triggerer, toee.PyObjHandle)
	assert isinstance(trap, toee.PyTrap)

	trap_trigger_pit_trap(trap.obj, triggerer, trap.partsys)
	return toee.SKIP_DEFAULT

def trap_trigger_pit_trap(attachee, triggerer, partsys):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)

	if (partsys):
		toee.game.particles(partsys, attachee)
	#toee.game.sound(4029, 1)
	dice = toee.dice_new("1d6")
	dc_reflex = 20
	radius_ft = 7
	for obj in toee.game.obj_list_range(attachee.location, radius_ft, toee.OLC_CRITTERS):
		f = obj.object_flags_get()
		if ((f & toee.OF_OFF) or (f & toee.OF_DESTROYED) or (f & toee.OF_DONTDRAW)): continue
		if (not obj.reflex_save_and_damage(attachee, dc_reflex, toee.D20_Save_Reduction_Half, toee.D20STD_F_TRAP, dice, toee.D20DT_SUBDUAL, toee.D20DAP_NORMAL, toee.D20A_NONE, 0)):
			obj.fall_down()
	return