import toee, startup_zmod

def pc_start(pc):
	assert isinstance(pc, toee.PyObjHandle)
	startup_zmod.zmod_templeplus_config_apply()
	startup_zmod.zmod_conditions_apply_pc()
	return
