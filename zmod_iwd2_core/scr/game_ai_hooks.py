import toee, debug, ctrl_daemon

def consider_target_not_too_far(attacker, target, distance_direct_ft):
	assert isinstance(attacker, toee.PyObjHandle)
	assert isinstance(target, toee.PyObjHandle)
	assert isinstance(distance_direct_ft, float)

	daemon = ctrl_daemon.CtrlDaemon.get_current_daemon()
	#print("game_combat::consider_target_is_too_far daemon: {}".format(daemon))
	if (daemon and "consider_target_not_too_far" in dir(daemon)):
		return daemon.consider_target_not_too_far(attacker, target, distance_direct_ft)

	# None means default
	return None
