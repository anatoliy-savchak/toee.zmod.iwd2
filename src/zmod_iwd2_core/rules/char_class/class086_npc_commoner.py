from toee import *
import char_class_utils
import char_editor
###################################################

def GetConditionName(): # used by API
	return "NPC Commoner"

def GetCategory():
	return "Core 3.5 Ed Classes"

def GetClassDefinitionFlags():
	return CDF_None

def GetClassHelpTopic():
	return "TAG_FIGHTERS"

classEnum = 86

###################################################
class_skills = (skill_climb, skill_craft, skill_handle_animal, skill_jump, skill_listen, skill_profession, skill_ride, skill_spot, skill_swim, skill_use_rope)

def IsEnabled():
	return 1

def GetHitDieType():
	return 4
	
def GetSkillPtsPerLevel():
	return 2
	
def GetBabProgression():
	return base_attack_bonus_type_martial
	
def IsFortSaveFavored():
	return 1
	
def IsRefSaveFavored():
	return 0
	
def IsWillSaveFavored():
	return 0

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