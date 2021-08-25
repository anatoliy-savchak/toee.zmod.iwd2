import toee

def pc_party_set_starting_gold_as_raw(roll = None):
	totalgp = 0
	for pc in toee.game.party:
		class_num = pc.char_classes[0]
		pcgp = 200
		if (class_num == toee.stat_level_barbarian):
			if (roll): pcgp = toee.dice_new("4d4").roll()*10
			else: pcgp = 160
		elif (class_num == toee.stat_level_bard):
			if (roll): pcgp = toee.dice_new("4d4").roll()*10
			else: pcgp = 160
		elif (class_num == toee.stat_level_cleric):
			if (roll): pcgp = toee.dice_new("5d4").roll()*10
			else: pcgp = 200
		elif (class_num == toee.stat_level_druid):
			if (roll): pcgp = toee.dice_new("2d4").roll()*10
			else: pcgp = 80
		elif (class_num == toee.stat_level_fighter):
			if (roll): pcgp = toee.dice_new("6d4").roll()*10
			else: pcgp = 240
		elif (class_num == toee.stat_level_monk):
			if (roll): pcgp = toee.dice_new("5d4").roll()*10
			else: pcgp = 200
		elif (class_num == toee.stat_level_paladin):
			if (roll): pcgp = toee.dice_new("6d4").roll()*10
			else: pcgp = 240
		elif (class_num == toee.stat_level_ranger):
			if (roll): pcgp = toee.dice_new("6d4").roll()*10
			else: pcgp = 240
		elif (class_num == toee.stat_level_rogue):
			if (roll): pcgp = toee.dice_new("5d4").roll()*10
			else: pcgp = 200
		elif (class_num == toee.stat_level_sorcerer):
			if (roll): pcgp = toee.dice_new("3d4").roll()*10
			else: pcgp = 120
		elif (class_num == toee.stat_level_wizard):
			if (roll): pcgp = toee.dice_new("3d4").roll()*10
			else: pcgp = 120
		totalgp += pcgp
	total = totalgp * 100
	currentcp = toee.game.party[0].money_get()
	diff = total - currentcp
	print("Supposed totalgp: {}, current: {}, diff: {}".format(totalgp, currentcp // 100, diff))
	if (diff > 0):
		 toee.game.party[0].money_adj(diff)
	return diff
