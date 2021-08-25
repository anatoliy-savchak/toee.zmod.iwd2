import toee, ctrl_daemon, utils_toee, const_toee, debug

def san_new_map(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	#debug.breakp("pc san_new_map")
	daemon = ctrl_daemon.CtrlDaemon.get_current_daemon()
	print("san_new_map daemon: {}".format(daemon))
	if (daemon):
		daemon_obj = utils_toee.get_obj_by_id(daemon.id)
		print("san_new_map daemon_obj: {}".format(daemon_obj))
		if (daemon_obj):
			daemon_obj.object_script_execute(attachee, const_toee.sn_new_map)
		
	return toee.RUN_DEFAULT

def san_enter_combat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	debug.breakp("pc san_enter_combat {}".format(attachee))
	daemon = ctrl_daemon.CtrlDaemon.get_current_daemon()
	print("san_new_map daemon: {}".format(daemon))
	if (daemon and "pc_san_enter_combat" in dir(daemon)):
		daemon.pc_san_enter_combat(attachee, triggerer)
	return toee.RUN_DEFAULT
