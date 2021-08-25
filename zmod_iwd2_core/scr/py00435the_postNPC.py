import toee, rttoee_consts

def san_dialog(attachee, triggerer):
	if (attachee.map == 5001):
		triggerer.begin_dialog(attachee, 1)
	return toee.SKIP_DEFAULT

def goto(x, y):
	toee.game.fade_and_teleport(0, 0, 0, rttoee_consts.MAP_ID_HOMMLET, x, y)
	toee.game.timevent_add(post_scroll_to_leader, (), 1, 1)
	return

def post_scroll_to_leader():
	toee.game.scroll_to(toee.game.leader)
	return