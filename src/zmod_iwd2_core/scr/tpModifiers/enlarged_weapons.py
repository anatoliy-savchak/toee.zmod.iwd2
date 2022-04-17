import toee, templeplus.pymod, tpdp, debug, sys

###################################################

def GetConditionName():
	return "Enlarged_Weapons"

print("Registering " + GetConditionName())
###################################################

def Enlarged_Weapons_OnGetAttackDice(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjGetAttackDice)
	
	if (evt_obj.weapon):
		dice = toee.dice_new("0d0")
		dice.packed = evt_obj.dice_packed
		sides = dice.size
		count = dice.number
		new_sides = sides
		new_count = count
		if (sides == 2):
			new_sides = 3
		elif (sides == 3):
			new_sides = 4
		elif (sides == 4):
			new_sides = 6
		elif (sides == 6):
			if (count == 1):
				new_sides = 8
			elif (count <= 3):
				new_count = count + 1
			else:
				new_count = count + 2
		elif (sides == 8):
			if (count == 1):
				new_count = 2
				new_sides = 6
			elif (count <= 3):
				new_count = count + 1
			elif (count <= 6):
				new_count = count + 2
			else:
				new_count = count + 4
		elif (sides == 10):
			new_count = count * 2
			new_sides = 8
		elif (sides == 12):
			new_count = 3
			new_sides = 6

		dice2 = toee.dice_new("{}d{}+{}".format(new_count, new_sides, dice.bonus))
		evt_obj.dice_packed = dice2.packed
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 4) # 0 - how much sizes to change
modObj.AddHook(toee.ET_OnGetAttackDice, toee.EK_NONE, Enlarged_Weapons_OnGetAttackDice, ())

