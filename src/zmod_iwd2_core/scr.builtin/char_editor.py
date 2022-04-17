import toee

def get_max_spell_level(handle, classEnum, characterLvl):
	assert isinstance(handle, toee.PyObjHandle)
	assert isinstance(classEnum, int)
	assert isinstance(characterLvl, int)

	return 1

def get_learnable_spells(obj_handle, class_enum, max_spell_level, is_domain_spell_class):
	assert isinstance(obj_handle, toee.PyObjHandle)
	assert isinstance(class_enum, int)
	assert isinstance(max_spell_level, int)
	assert isinstance(is_domain_spell_class, int)

	result = list()
	result.append(KnownSpellInfo())
	return result

def get_known_class_spells(handle, classEnum):
	assert isinstance(handle, toee.PyObjHandle)
	assert isinstance(classEnum, int)

	result = list()
	result.append(KnownSpellInfo())
	return result

def get_spell_level(spEnum, classEnum):
	assert isinstance(spEnum, int)
	assert isinstance(classEnum, int)

	return 1

def spell_known_add(ksi):
	assert isinstance(ksi, list)
	return

class KnownSpellInfo(object):
	def __init__(self, spell_enum, spell_status, spell_class, is_domain_spell):
		assert isinstance(spell_enum, int)
		assert isinstance(spell_status, int) # 1 - denotes as replaceable spell (e.g. sorcerers), 2 - ??, 3 - new spell slot; use 0 for the spell level labels
		assert isinstance(spell_class, int) # Note: this is not the same as the casting class enum (use set_casting_class instead)
		assert isinstance(is_domain_spell, int)

		self.spell_enum = spell_enum
		self.spell_status = spell_status
		self.spell_class = spell_class
		self.spell_level = 0 # Spell level; is calculated automatically on init according to the spell class
		return

	def __init__(self, spell_enum, spell_status):
		self.__init__(spell_enum, spell_status, 0, 0)
		return

	def __init__(self):
		self.__init__(0, 0, 0, 0)
		return

	def get_casting_class(self):
		return 0 

	def set_casting_class(self, class_enum):
		return