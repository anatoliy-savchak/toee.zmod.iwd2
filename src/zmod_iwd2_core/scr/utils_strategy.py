import toee, tpai

def tactic_exec(npc, name, tac0 = None, data1 = 0, data2 = 0):
	assert isinstance(tac0, tpai.AiTactic)

	tdef = tpai.get_tactic_def(name)
	if (not tdef):
		return (0, None)

	tac = tac0
	if (not tac):
		tac = tpai.AiTactic()
		tac.data1 = data1
		tac.data2 = data2
	tac.performer = npc
	result = tdef.execute(tac)
	return result, tac
