import toee

def iwd2_classname_to_class_const(classname):
	c = classname.upper()
	if c == "BARBARIAN":
		return "toee.stat_level_barbarian"
	if c == "BARD":
		return "toee.stat_level_bard"
	if c == "CLERIC":
		return "toee.stat_level_cleric"
	if c == "DRUID":
		return "toee.stat_level_druid"
	if c == "FIGHTER":
		return "toee.stat_level_fighter"
	if c == "MONK":
		return "toee.stat_level_monk"
	if c == "PALADIN":
		return "toee.stat_level_paladin"
	if c == "RANGER":
		return "toee.stat_level_ranger"
	if c == "ROGUE":
		return "toee.stat_level_rogue"
	if c == "SORCERER":
		return "toee.stat_level_sorcerer"
	if c == "WIZARD":
		return "toee.stat_level_wizard"
	if c == "MAGE":
		return "toee.stat_level_wizard"
	if c == "THIEF":
		return "toee.stat_level_rogue"
	return

def iwd2_classname_to_class(classname):
	c = classname.upper()
	if c == "BARBARIAN":
		return toee.stat_level_barbarian
	if c == "BARD":
		return toee.stat_level_bard
	if c == "CLERIC":
		return toee.stat_level_cleric
	if c == "DRUID":
		return toee.stat_level_druid
	if c == "FIGHTER":
		return toee.stat_level_fighter
	if c == "MONK":
		return toee.stat_level_monk
	if c == "PALADIN":
		return toee.stat_level_paladin
	if c == "RANGER":
		return toee.stat_level_ranger
	if c == "ROGUE":
		return toee.stat_level_rogue
	if c == "SORCERER":
		return toee.stat_level_sorcerer
	if c == "WIZARD":
		return toee.stat_level_wizard
	if c == "MAGE":
		return toee.stat_level_wizard
	if c == "THIEF":
		return toee.stat_level_rogue
	err = "Unknown iwd2 class: {}".format(classname)
	print(err)
	raise Exception(err)
	return

def iwd2_stat_convert(statname):
	stat = None
	if statname == "CHR":
		stat = toee.stat_charisma
	return (stat, )
