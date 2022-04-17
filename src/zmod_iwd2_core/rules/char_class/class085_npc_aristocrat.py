from toee import *
import char_class_utils
import char_editor
###################################################

def GetConditionName(): # used by API
	return "NPC Aristocrat"

def GetCategory():
	return "Core 3.5 Ed Classes"

def GetClassDefinitionFlags():
	return CDF_None

def GetClassHelpTopic():
	return "TAG_NPC_CLASSES"

classEnum = 85

###################################################

class_skills = (skill_appraise, skill_bluff, skill_diplomacy, skill_disguise, skill_forgery, skill_gather_information, skill_handle_animal \
	, skill_intimidate, skill_knowledge_arcana, skill_knowledge_religion, skill_knowledge_nature, skill_knowledge_all, skill_listen, skill_perform \
	, skill_ride, skill_sense_motive, skill_spot, skill_swim, skill_wilderness_lore)

def IsEnabled():
	return 1

def GetHitDieType():
	return 8
	
def GetSkillPtsPerLevel():
	return 4
	
def GetBabProgression():
	return base_attack_bonus_type_semi_martial
	
def IsFortSaveFavored():
	return 0
	
def IsRefSaveFavored():
	return 0
	
def IsWillSaveFavored():
	return 1

def GetSpellListType():
	return spell_list_type_none

def IsClassSkill(skillEnum):
	return char_class_utils.IsClassSkill(class_skills, skillEnum)

def IsClassFeat(featEnum):
	return 0

def GetClassFeats():
	return None

def IsAlignmentCompatible( alignment):
	return 1

def ObjMeetsPrereqs( obj ):
	return 1

# Levelup

def IsSelectingFeatsOnLevelup( obj ):
	newLvl = obj.stat_level_get( classEnum ) + 1
	if newLvl % 2 == 0 or newLvl == 1:
		return 1
	return 0

def LevelupGetBonusFeats( obj ):
	return 