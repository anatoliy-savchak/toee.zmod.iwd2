import toee, tpactions, tpdp, debug

def GetActionName():
	return "Knowstone Learn"

def GetActionDefinitionFlags():
	return toee.D20ADF_None
	
def GetTargetingClassification():
	return toee.D20TC_Target0

def GetActionCostType():
	return toee.D20ACT_Standard_Action

def AddToSequence(d20action, action_seq, tb_status):
	assert isinstance(d20action, tpdp.D20Action)
	action_seq.add_action(d20action)
	return toee.AEC_OK
