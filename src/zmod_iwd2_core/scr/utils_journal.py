import rumor_control

def journal_add(strref, rumors):
	for rumor_id in rumors:
		rumor_control.rumor_give(rumor_id)
	return
