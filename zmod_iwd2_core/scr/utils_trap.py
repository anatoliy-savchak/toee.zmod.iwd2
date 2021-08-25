import toee, const_toee

def setup_trap(obj, trap_id, trap_impl_script_id):
	assert isinstance(obj, toee.PyObjHandle)
	assert isinstance(trap_id, int)
	assert isinstance(trap_impl_script_id, int)

	obj.scripts[const_toee.sn_trap] = trap_impl_script_id
	if ("counter_set" in dir(obj.scripts)):
		obj.scripts.counter_set(const_toee.sn_trap, 0, trap_id)
	return
