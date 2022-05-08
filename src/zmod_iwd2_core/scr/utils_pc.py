import toee, debug, const_toee

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

def pc_party_receive_money_and_print(value, float = True):
	#prev_wealth_copper = toee.game.leader.money_get()
	toee.game.leader.money_adj(value)
	new_wealth_copper = toee.game.leader.money_get()
	value_gp = value // const_toee.gp
	net_gp = new_wealth_copper // const_toee.gp
	text_fly = "Party received money: {} gp".format(value_gp)
	text = "\n{} (net: {} gp).\n".format(text_fly, net_gp)
	print(text)
	toee.game.create_history_freeform(text)
	if float:
		toee.game.leader.float_text_line(text_fly, toee.tf_yellow)
	return

def pc_receive_item_print(pc, item, float):
	assert isinstance(pc, toee.PyObjHandle)
	assert isinstance(item, toee.PyObjHandle)

	text_fly = "{} received : {}!".format(pc.description, item.description)
	text = "\n{}\n".format(text_fly)
	print(text_fly)
	toee.game.create_history_freeform(text)
	if float:
		pc.float_text_line(text_fly, toee.tf_green)
	return

def pc_award_experience_each(xp_awarded_each, do_print = 0):
	print("pc_award_experience_each xp_awarded_party: {}, do_print: {}".format(xp_awarded_each, do_print))
	# XXX gains 123 experience points.
	template = "{} " + "{} {} {}".format(toee.game.get_mesline("mes\combat.mes", 145), xp_awarded_each, toee.game.get_mesline("mes\combat.mes", 146)) + "\n"if (do_print) else None 
	print("template: {}".format(template))
	for pc in toee.game.party:
		pc.award_experience(xp_awarded_each)
		if (do_print and template):
			toee.game.create_history_freeform(template.format(pc.description))
	return

def pc_award_experience_party(xp_awarded_party, do_print = 0):
	print("pc_award_experience_party xp_awarded_party: {}, do_print: {}".format(xp_awarded_party, do_print))
	count = len(toee.game.party)
	xp_awarded_each = xp_awarded_party // count
	pc_award_experience_each(xp_awarded_each, do_print)
	return

def pc_turn_all(rotation):
	for pc in toee.game.party:
		pc.rotation = rotation
	return

def pc_xp_require_for_level(level):
	assert isinstance(level, int)
	if (level >=3):
		return 1000* (level - 1) * level // 2
	elif (level == 2): 
		return 1000
	return 0

def pc_xp_surplus(pc):
	assert isinstance(pc, toee.PyObjHandle)
	lvl = pc.stat_level_get(toee.stat_level)
	#if (lvl > 1): lvl = pc.GetEffectiveLevel(toee.stat_level) TODO
	xp_req = pc_xp_require_for_level(lvl)
	return pc.obj_get_int(toee.obj_f_critter_experience) - xp_req

def pc_move_party(x, y):
	# potentially also try to move pcs
	toee.game.fade_and_teleport(0, 0, 0, toee.game.leader.map, x, y)
	return