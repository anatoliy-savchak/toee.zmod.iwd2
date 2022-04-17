import toee, utils_toee
import debugg

def spell_name(spell_id):
	#debugg.breakp("spell_name {}".format(spell_id))
	#line = utils_toee.readMesLine("data\\mes\\spell.mes", spell_id)
	line = toee.game.get_spell_mesline(spell_id)
	#print(line)
	#debugg.breakp("spell_name {} = ".format(spell_id, line))
	return line

def spell_name_safe(spell_id):
	line = spell_name(spell_id).replace("'", "")
	return line

def get_spell_class(class_enum):
	return 0x80 | class_enum

def get_class_enum(spell_class):
	return spell_class & 0x7F