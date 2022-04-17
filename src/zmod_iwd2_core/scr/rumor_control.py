import toee

def find_rumor(pc, npc):
	""" this function returns the message line (0, 10, 20, etc) of a
		rumor to be told to the PC in question, or -1 if no rumor is
		available
	"""
	assert isinstance(pc, toee.PyObjHandle)
	assert isinstance(npc, toee.PyObjHandle)
	print("find_rumor({}, {})".format(pc, npc))
	return -1

def rumor_valid(rumor, pc, npc):
	assert isinstance(rumor, int)
	assert isinstance(pc, toee.PyObjHandle)
	assert isinstance(npc, toee.PyObjHandle)
	print("rumor_valid({}, {}, {})".format(rumor, pc, npc))
	return 1

def rumor_given_out(rumor):
	assert isinstance(rumor, int)
	flag_num = rumor_id_to_global_flag(rumor // 10)
	checked = toee.game.global_flags[flag_num]
	print("rumor_given_out({}), toee.game.global_flags[{}] is {}".format(rumor, flag_num, checked))
	if (not checked):
		toee.game.global_flags[flag_num] = 1
	return

def rumor_id_to_global_flag(rumor_id):
	assert isinstance(rumor_id, int)
	rumor = rumor_id * 10
	offset = (toee.game.story_state) * 200
	sk_lookup = ( (rumor - offset)/10 )
	flag_num = 209 + sk_lookup
	#print("rumor: {}, offset: {}, sk_lookup: {}, flag_num: {}".format(rumor, offset, sk_lookup, flag_num))
	return flag_num
	
def is_rumor_given(rumor_id):
	flag_num = rumor_id_to_global_flag(rumor_id)
	checked = toee.game.global_flags[flag_num]
	return checked

def rumor_give(rumor_id):
	flag_num = rumor_id_to_global_flag(rumor_id)
	checked = toee.game.global_flags[flag_num]
	print("rumor_give({}), toee.game.global_flags[{}] is {}".format(rumor_id, flag_num, checked))
	if (not checked):
		toee.game.leader.rumor_log_add(rumor_id)
		return 1
	return 0