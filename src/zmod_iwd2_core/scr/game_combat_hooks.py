import toee, debug, ctrl_daemon

def combat_start(initiator):
	assert isinstance(initiator, toee.PyObjHandle)
	#print("game_combat::combat_start initiator: {}".format(initiator))
	#debug.breakp("game_combat::combat_start")

	daemon = ctrl_daemon.CtrlDaemon.get_current_daemon()
	print("game_combat::combat_start daemon: {}".format(daemon))
	if (daemon and "combat_start" in dir(daemon)):
		daemon.combat_start(initiator)
	return


def combat_end():
	#print("game_combat::combat_end")
	#debug.breakp("game_combat::combat_end")

	daemon = ctrl_daemon.CtrlDaemon.get_current_daemon()
	print("game_combat::combat_end daemon: {}".format(daemon))
	if (daemon and "combat_end" in dir(daemon)):
		daemon.combat_end()
	return
