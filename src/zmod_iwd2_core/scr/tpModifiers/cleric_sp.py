from templeplus.pymod import PythonModifier
from toee import *
import tpdp
import char_class_utils

###################################################

def GetConditionName():
	return "Cleric Sp"
	
# def GetSpellCasterConditionName():
	# return "Sorcerer Spellcasting"

# print "Registering " + GetSpellCasterConditionName()

classEnum = 90
classSpecModule = __import__('class090_cleric_sp')
###################################################


#### standard callbacks - BAB and Save values
def OnGetToHitBonusBase(attachee, args, evt_obj):
	classLvl = attachee.stat_level_get(classEnum)
	babvalue = game.get_bab_for_class(classEnum, classLvl)
	evt_obj.bonus_list.add(babvalue, 0, 137) # untyped, description: "Class"
	return 0

def OnGetSaveThrowFort(attachee, args, evt_obj):
	value = char_class_utils.SavingThrowLevel(classEnum, attachee, D20_Save_Fortitude)
	evt_obj.bonus_list.add(value, 0, 137)
	return 0

def OnGetSaveThrowReflex(attachee, args, evt_obj):
	value = char_class_utils.SavingThrowLevel(classEnum, attachee, D20_Save_Reflex)
	evt_obj.bonus_list.add(value, 0, 137)
	return 0

def OnGetSaveThrowWill(attachee, args, evt_obj):
	value = char_class_utils.SavingThrowLevel(classEnum, attachee, D20_Save_Will)
	evt_obj.bonus_list.add(value, 0, 137)
	return 0


classSpecObj = PythonModifier(GetConditionName(), 0)
classSpecObj.AddHook(ET_OnToHitBonusBase, EK_NONE, OnGetToHitBonusBase, ())
classSpecObj.AddHook(ET_OnSaveThrowLevel, EK_SAVE_FORTITUDE, OnGetSaveThrowFort, ())
classSpecObj.AddHook(ET_OnSaveThrowLevel, EK_SAVE_REFLEX, OnGetSaveThrowReflex, ())
classSpecObj.AddHook(ET_OnSaveThrowLevel, EK_SAVE_WILL, OnGetSaveThrowWill, ())


### Spell casting
def OnGetBaseCasterLevel(attachee, args, evt_obj):
	if evt_obj.arg0 != classEnum:
		return 0
	classLvl = attachee.stat_level_get(classEnum)
	evt_obj.bonus_list.add(classLvl, 0, 137)
	return 0

def OnInitLevelupSpellSelection(attachee, args, evt_obj):
	if evt_obj.arg0 != classEnum:
		return 0
	classSpecModule.InitSpellSelection(attachee)
	return 0
	
def OnLevelupSpellsCheckComplete(attachee, args, evt_obj):
	if evt_obj.arg0 != classEnum:
		return 0
	if not classSpecModule.LevelupCheckSpells(attachee):
		evt_obj.bonus_list.add(-1, 0, 137) # denotes incomplete spell selection
	return 1

def OnLevelupSpellsFinalize(attachee, args, evt_obj):
	if evt_obj.arg0 != classEnum:
		return 0
	classSpecModule.LevelupSpellsFinalize(attachee)
	return

classSpecObj.AddHook(ET_OnGetBaseCasterLevel, EK_NONE, OnGetBaseCasterLevel, ())
classSpecObj.AddHook(ET_OnLevelupSystemEvent, EK_LVL_Spells_Activate, OnInitLevelupSpellSelection, ())
classSpecObj.AddHook(ET_OnLevelupSystemEvent, EK_LVL_Spells_Finalize, OnLevelupSpellsFinalize, ())
classSpecObj.AddHook(ET_OnLevelupSystemEvent, EK_LVL_Spells_Check_Complete, OnLevelupSpellsCheckComplete, ())
