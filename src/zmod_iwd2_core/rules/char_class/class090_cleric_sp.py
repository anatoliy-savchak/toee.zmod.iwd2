from toee import *
import char_class_utils
import char_editor
###################################################

def GetConditionName(): # used by API
	return "Cleric Sp"

# def GetSpellCasterConditionName():
	# return "Cleric Spellcasting"

def GetCategory():
	return "Unearthed Arcana"

def GetClassDefinitionFlags():
	return CDF_BaseClass

def GetClassHelpTopic():
	return "TAG_FAVORED_SOULS"
	
classEnum = 90

###################################################

class_feats = {
1: (feat_armor_proficiency_light, feat_armor_proficiency_medium, feat_armor_proficiency_heavy, feat_shield_proficiency, feat_simple_weapon_proficiency, feat_domain_power)
}

class_skills = (skill_alchemy, skill_concentration, skill_craft, skill_diplomacy, skill_heal, skill_knowledge_arcana, skill_knowledge_religion, skill_profession, skill_spellcraft)

# not including domain spells
spells_per_day = {
1:  (3, 1),
2:  (4, 2),
3:  (4, 2, 1),
4:  (4, 3, 2),
5:  (4, 3, 2, 1),
6:  (4, 3, 3, 2),
7:  (4, 4, 3, 2, 1),
8:  (4, 4, 3, 3, 2),
9:  (4, 4, 4, 3, 2, 1),
10: (4, 4, 4, 3, 3, 2),
11: (4, 4, 4, 4, 3, 2, 1),
12: (4, 4, 4, 4, 3, 3, 2),
13: (4, 4, 4, 4, 4, 3, 2, 1),
14: (4, 4, 4, 4, 4, 3, 3, 2),
15: (4, 4, 4, 4, 4, 4, 3, 2, 1),
16: (4, 4, 4, 4, 4, 4, 3, 3, 2),
17: (4, 4, 4, 4, 4, 4, 4, 3, 2, 1),
18: (4, 4, 4, 4, 4, 4, 4, 3, 3, 2),
19: (4, 4, 4, 4, 4, 4, 4, 4, 3, 3),
20: (4, 4, 4, 4, 4, 4, 4, 4, 4, 4)
#lvl 0  1  2  3  4  5  6  7  8  9
}


spells_known = {
1:  (4, 3),
2:  (5, 5),
3:  (5, 5),
4:  (6, 5, 2),
5:  (6, 5, 4),
6:  (7, 5, 4, 2),
7:  (7, 5, 4, 4),
8:  (8, 5, 4, 4, 2),
9:  (8, 5, 4, 4, 4),
10: (9, 5, 4, 4, 4, 2),
11: (9, 5, 4, 4, 4, 4),
12: (9, 5, 4, 4, 4, 4, 2),
13: (9, 5, 4, 4, 4, 4, 4),
14: (9, 5, 4, 4, 4, 4, 4, 2),
15: (9, 5, 4, 4, 4, 4, 4, 4),
16: (9, 5, 4, 4, 4, 4, 4, 4, 2),
17: (9, 5, 4, 4, 4, 4, 4, 4, 4),
18: (9, 5, 4, 4, 4, 4, 4, 4, 4, 2),
19: (9, 5, 4, 4, 4, 4, 4, 4, 4, 4),
20: (9, 5, 4, 4, 4, 4, 4, 4, 4, 6)
#lvl 0  1  2  3  4  5  6  7  8  9
}

def IsEnabled():
	return 1

def GetHitDieType():
	return 8
	
def GetSkillPtsPerLevel():
	return 2
	
def GetBabProgression():
	return base_attack_bonus_type_semi_martial
	
def IsFortSaveFavored():
	return 1
	
def IsRefSaveFavored():
	return 1
	
def IsWillSaveFavored():
	return 1

# Spell casting
def GetSpellListType():
	return spell_list_type_clerical

def GetSpellSourceType():
	return spell_source_type_divine

def GetSpellReadyingType():
	return spell_readying_innate

def GetSpellsPerDay():
	return spells_per_day

caster_levels = range(1, 21)
def GetCasterLevels():
	return caster_levels

def GetSpellDeterminingStat():
	return stat_wisdom

def GetSpellDcStat():
	return stat_wisdom

def IsClassSkill(skillEnum):
	return char_class_utils.IsClassSkill(class_skills, skillEnum)

def IsClassFeat(featEnum):
	return char_class_utils.IsClassFeat(class_feats, featEnum)

def GetClassFeats():
	return class_feats

def IsAlignmentCompatible( alignment):
	return 1

def ObjMeetsPrereqs( obj ):
	abScore = obj.stat_base_get(stat_wisdom)
	if abScore > 10:
		return 1
	return 0

def GetDeityClass():
	return stat_level_cleric

## Levelup


# Spells
def IsSelectingSpellsOnLevelup( obj ):
	return 1


def InitSpellSelection(obj, classLvlNew = -1, classLvlIncrement = 1):
	classLvl = obj.stat_level_get(classEnum)
	if classLvlNew <= 0:
		classLvlNew = classLvl + 1
	maxSpellLvl = char_editor.get_max_spell_level(obj, classEnum,
	                                              classLvlNew)  # this regards spell list extension by stuff like Mystic Theurge

	# Available Spells
	spAvail = char_editor.get_learnable_spells(obj, classEnum, maxSpellLvl)
	# add spell level labels
	for p in range(0, maxSpellLvl + 1):
		spAvail.append(char_editor.KnownSpellInfo(spell_label_level_0 + p, 0, classEnum))
	spAvail.sort()
	char_editor.append_available_spells(spAvail)

	# newly taken class
	if classLvlNew == 1:
		spEnums = []
		spEnums.append(char_editor.KnownSpellInfo(spell_label_level_0, 0, classEnum))  # add "Level 0" label
		for p in range(0, 4):  # 4 cantrips
			spEnums.append(char_editor.KnownSpellInfo(spell_new_slot_lvl_0, 3, classEnum))

		spEnums.append(char_editor.KnownSpellInfo(spell_label_level_1, 0, classEnum))  # add "Level 1" label
		# KOTC: At @LEVEL@ 1, a wizard knows a number of spells equal to 3 + his @INTELLIGENCE@ modifier. At every level after the first, wizards learn ЈtwoЈ new spells.
		bonus_spells_known_first = max(0, (obj.stat_level_get(GetSpellDeterminingStat()) - 10) // 2)
		maxfirst = 3 + bonus_spells_known_first
		for p in range(0, maxfirst-1):
			spEnums.append(char_editor.KnownSpellInfo(spell_new_slot_lvl_1, 3, classEnum))
		char_editor.append_spell_enums(spEnums)
		return 0

	# Incrementing class level
	spellListLvl = obj.stat_level_get(stat_spell_list_level,
	                                  classEnum) + classLvlIncrement  # the effective level for getting the number of spells known
	spEnums = char_editor.get_known_class_spells(obj, classEnum)  # get all spells known for this class
	for spellLvl in range(0, maxSpellLvl + 1):
		spEnums.append(char_editor.KnownSpellInfo(spell_label_level_0 + spellLvl, 0, classEnum))  # add label
		# add spells
		newSpellsKnownCount = char_class_utils.GetSpellsKnownAddedCount(spells_known, spellListLvl, spellLvl)
		
		#Do not add more spells than can be selected (otherwise lockup happens)
		spellList = char_editor.get_learnable_spells(obj, classEnum, maxSpellLvl)
		spellAvailableCount = 0
		for spell in spellList:
			if spellLvl == spell.spell_level:
				if not obj.is_spell_known(spell.spell_enum):
					spellAvailableCount = spellAvailableCount + 1
		newSpellsKnownCount = min(newSpellsKnownCount, spellAvailableCount)
		
		print str(newSpellsKnownCount)
		for q in range(0, newSpellsKnownCount):
			spEnums.append(char_editor.KnownSpellInfo(spell_new_slot_lvl_0 + spellLvl, 3, classEnum))

	spEnums.sort()
	char_editor.append_spell_enums(spEnums)
	return 0


def LevelupCheckSpells(obj):
	classLvl = obj.stat_level_get(classEnum)
	classLvlNew = classLvl + 1
	maxSpellLvl = char_editor.get_max_spell_level(obj, classEnum, classLvlNew)

	spell_enums = char_editor.get_spell_enums()
	for spInfo in spell_enums:
		if spInfo.spell_enum == spell_vacant:
			if maxSpellLvl >= 4 and spInfo.spell_level == 0:  # in case the cantrips are causing problems
				continue
			return 0
	return 1

def LevelupSpellsFinalize( obj, classLvlNew = -1 ):
	classLvl = obj.stat_level_get(classEnum)
	if classLvlNew <= 0:
		classLvlNew = classLvl + 1

	maxSpellLvl = char_editor.get_max_spell_level( obj, classEnum, classLvlNew )
	class_spells = char_editor.get_learnable_spells(obj, classEnum, maxSpellLvl)
	char_editor.spell_known_add(class_spells)

	# Domain spells:
	domain_1 = obj.obj_get_int(obj_f_critter_domain_1)
	domain_2 = obj.obj_get_int(obj_f_critter_domain_2)
	domain_1_spells = char_editor.get_learnable_spells(obj, domain_1, maxSpellLvl, 1)
	domain_2_spells = char_editor.get_learnable_spells(obj, domain_2, maxSpellLvl, 1)
	char_editor.spell_known_add(domain_1_spells)
	char_editor.spell_known_add(domain_2_spells)
	return 0

