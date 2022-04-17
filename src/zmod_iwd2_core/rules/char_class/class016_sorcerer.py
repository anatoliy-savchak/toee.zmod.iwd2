from toee import *
import char_class_utils
import char_editor
###################################################

def GetConditionName(): # used by API
	return "Sorcerer"

# def GetSpellCasterConditionName():
	# return "Sorcerer Spellcasting"

def GetCategory():
	return "Core 3.5 Ed Classes"

def GetClassDefinitionFlags():
	return CDF_BaseClass | CDF_CoreClass

def GetClassHelpTopic():
	return "TAG_SORCERERS"

classEnum = stat_level_sorcerer

###################################################

class_feats = {

1: (feat_simple_weapon_proficiency, feat_call_familiar, feat_scribe_scroll)
}

bonus_feats = [feat_brew_potion, feat_craft_magic_arms_and_armor, feat_craft_rod, feat_craft_staff, feat_craft_wand, feat_craft_wondrous_item, 
feat_empower_spell, feat_enlarge_spell, feat_extend_spell, feat_forge_ring, feat_heighten_spell, feat_maximize_spell, feat_quicken_spell, 
feat_scribe_scroll, feat_silent_spell, feat_still_spell, feat_widen_spell
]

class_skills = (skill_alchemy, skill_bluff, skill_concentration, skill_craft, skill_knowledge_arcana, skill_profession, skill_spellcraft)

spells_per_day = {
1:  (5, 1),
2:  (6, 2),
3:  (6, 2, 1),
4:  (6, 3, 2),
5:  (6, 3, 2, 1),
6:  (6, 3, 3, 2),
7:  (6, 4, 3, 2, 1),
8:  (6, 4, 3, 3, 2),
9:  (6, 4, 4, 3, 2, 1),
10: (6, 4, 4, 3, 3, 2),
11: (6, 4, 4, 4, 3, 2, 1),
12: (6, 4, 4, 4, 3, 3, 2),
13: (6, 4, 4, 4, 4, 3, 2, 1),
14: (6, 4, 4, 4, 4, 3, 3, 2),
15: (6, 4, 4, 4, 4, 4, 3, 2, 1),
16: (6, 4, 4, 4, 4, 4, 3, 3, 2),
17: (6, 4, 4, 4, 4, 4, 4, 3, 2, 1),
18: (6, 4, 4, 4, 4, 4, 4, 3, 3, 2),
19: (6, 4, 4, 4, 4, 4, 4, 4, 3, 3),
20: (6, 4, 4, 4, 4, 4, 4, 4, 4, 4)
#lvl 0  1  2  3  4  5  6  7  8  9
}

spells_known = {
1:  (4, 3),
2:  (5, 5),
3:  (6, 5, 2),
4:  (6, 5, 4),
5:  (7, 5, 5, 2),
6:  (7, 5, 5, 4),
7:  (8, 5, 5, 4, 2),
8:  (8, 5, 4, 5, 4),
9:  (9, 5, 4, 5, 4, 2),
10: (9, 5, 5, 5, 5, 4),
11: (9, 5, 5, 5, 5, 4, 2),
12: (9, 5, 5, 5, 5, 5, 4),
13: (9, 5, 5, 5, 5, 5, 4, 2),
14: (9, 5, 5, 5, 5, 5, 5, 4),
15: (9, 5, 5, 5, 5, 5, 5, 4, 2),
16: (9, 5, 5, 5, 5, 5, 5, 5, 4),
17: (9, 5, 5, 5, 5, 5, 5, 5, 4, 2),
18: (9, 5, 5, 5, 5, 5, 5, 5, 5, 4),
19: (9, 5, 5, 5, 5, 5, 5, 5, 5, 5),
20: (9, 5, 5, 5, 5, 5, 5, 5, 5, 5)
#lvl 0  1  2  3  4  5  6  7  8  9
}

def IsEnabled():
	return 1

def GetHitDieType():
	return 4
	
def GetSkillPtsPerLevel():
	return 2
	
def GetBabProgression():
	return base_attack_bonus_type_non_martial
	
def IsFortSaveFavored():
	return 0
	
def IsRefSaveFavored():
	return 0
	
def IsWillSaveFavored():
	return 1

# Spell casting
def GetSpellListType():
	return spell_list_type_arcane

def GetSpellSourceType():
	return spell_source_type_arcane

def GetSpellReadyingType():
	return spell_readying_innate

def GetSpellsPerDay():
	return spells_per_day

caster_levels = range(1, 21)
def GetCasterLevels():
	return caster_levels

def GetSpellDeterminingStat():
	return stat_charisma

def IsClassSkill(skillEnum):
	return char_class_utils.IsClassSkill(class_skills, skillEnum)

def IsClassFeat(featEnum):
	return char_class_utils.IsClassFeat(class_feats, featEnum)

def GetClassFeats():
	return class_feats

def IsAlignmentCompatible( alignment):
	return 1
	
def ObjMeetsPrereqs( obj ):
	abScore = obj.stat_base_get(stat_charisma)
	if abScore > 10:
		return 1
	return 0

## Levelup callbacks

def IsSelectingFeaturesOnLevelup( obj ):
	newLvl = obj.stat_level_get( classEnum ) + 1
	if newLvl == 1:
		return 1
	return 0

def IsSelectingFeatsOnLevelup( obj ):
	newLvl = obj.stat_level_get( classEnum ) + 1
	if newLvl % 5 == 0:
		return 1
	return 0

def LevelupGetBonusFeats( obj ):
	bonFeatInfo = []
	for ft in bonus_feats:
		bonFeatInfo.append(char_editor.FeatInfo(ft))
	char_editor.set_bonus_feats(bonFeatInfo)
	return

def IsSelectingSpellsOnLevelup( obj ):
	return 1
	
def InitSpellSelection( obj, classLvlNew = -1, classLvlIncrement = 1):
	assert isinstance(obj, PyObjHandle)
	classLvl = obj.stat_level_get(classEnum)
	if classLvlNew <= 0:
		classLvlNew = classLvl + 1
	maxSpellLvl = char_editor.get_max_spell_level( obj, classEnum, classLvlNew ) # this regards spell list extension by stuff like Mystic Theurge
	
	# Available Spells (spells you can choose, on the left side)
	spAvail = char_editor.get_learnable_spells(obj, classEnum, maxSpellLvl)
	# add spell level labels
	for p in range(0,maxSpellLvl+1):
		spAvail.append(char_editor.KnownSpellInfo(spell_label_level_0 + p, 0, classEnum))
	spAvail.sort()
	char_editor.append_available_spells(spAvail)
	
	# Create Known Spells list (right side) spEnums
	# Case 1 - newly taken class
	if classLvlNew == 1:
		spEnums = []
		spEnums.append(char_editor.KnownSpellInfo(spell_label_level_0, 0, classEnum)) # add "Level 0" label
		for p in range(0,4): # 4 cantrips
			spEnums.append(char_editor.KnownSpellInfo(spell_new_slot_lvl_0, 3, classEnum))
		spEnums.append(char_editor.KnownSpellInfo(spell_label_level_1, 0, classEnum)) # add "Level 1" label
		# KOTC: At @LEVEL@ 1, a wizard knows a number of spells equal to 3 + his @INTELLIGENCE@ modifier. At every level after the first, wizards learn ЈtwoЈ new spells.
		bonus_spells_known_first = max(0, (obj.stat_level_get(GetSpellDeterminingStat()) - 10) // 2)
		maxfirst = 2 + bonus_spells_known_first
		for p in range(0, maxfirst): 
			spEnums.append(char_editor.KnownSpellInfo(spell_new_slot_lvl_1, 3, classEnum))
		char_editor.append_spell_enums(spEnums)
		return 0
	
	# Case 2 - Incrementing class level
	spellListLvl = obj.stat_level_get(stat_spell_list_level, classEnum) + classLvlIncrement # the effective level for getting the number of spells known
	if spellListLvl <= 20:
		spEnums = char_editor.get_known_class_spells(obj, classEnum) # get all spells known by this character for this class
		for spellLvl in range(0, maxSpellLvl+1):
			spEnums.append(char_editor.KnownSpellInfo(spell_label_level_0 + spellLvl, 0, classEnum))  # add label
			# add spells
			newSpellsKnownCount = char_class_utils.GetSpellsKnownAddedCount( spells_known , spellListLvl, spellLvl)
			# print("new num spells for spell level " + str(spellLvl) + ": " + str(newSpellsKnownCount))
			for q in range(0, newSpellsKnownCount):
				spEnums.append(char_editor.KnownSpellInfo(spell_new_slot_lvl_0 + spellLvl, 3, classEnum))
	else: # Epic Level sorcerer - add a single spell of any level (kind of like a freebie Spell knowledge feat, since there isn't one yet)
		spEnums = []
		vacant_slot = char_editor.KnownSpellInfo(spell_vacant, 3, classEnum) # sets it to spell level -1
		spEnums.append(vacant_slot)
		char_editor.append_spell_enums(spEnums)
		return 0
	
	# Handle spell replacement on even levels
	isReplacing = 0
	if spellListLvl >= 4 and (spellListLvl % 2) == 0: # spell replacement
		isReplacing = 1
	if char_editor.get_class_code() !=  classEnum: #grant this benefit only for strict levelup (also to prevent some headache...)
		isReplacing = 0
	
	if isReplacing == 0:
		spEnums.sort()
		char_editor.append_spell_enums(spEnums)
		return 0
	
	# mark as replaceable
	for p in range(0,len(spEnums)):
		spEnum = spEnums[p].spell_enum
		if spell_vacant <= spEnum <= spell_label_level_9:
			continue
		if spell_new_slot_lvl_0 <= spEnum <= spell_new_slot_lvl_9:
			continue
		if char_editor.get_spell_level(spEnum, classEnum) <= maxSpellLvl-2:
			spEnums[p].spell_status = 1 # marked as replaceable
	
	# Finally, return spEnums list to the engine
	spEnums.sort()
	char_editor.append_spell_enums(spEnums)
	return 0

def LevelupCheckSpells( obj ):
	classLvl = obj.stat_level_get(classEnum)
	classLvlNew = classLvl + 1
	maxSpellLvl = char_editor.get_max_spell_level( obj, classEnum, classLvlNew )
	
	spell_enums = char_editor.get_spell_enums()
	for spInfo in spell_enums:
		if spInfo.spell_enum == spell_vacant:
			if maxSpellLvl >= 4 and spInfo.spell_level == 0: # in case the cantrips are causing problems
				continue
			return 0
	return 1

def LevelupSpellsFinalize( obj, classLvlNew = -1 ):
	spEnums = char_editor.get_spell_enums()
	char_editor.spell_known_add(spEnums) # internally takes care of duplicates and the labels/vacant slots
	return