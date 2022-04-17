import toee, debug, utils_obj, const_toee, const_proto_items

LOCK_DC_VERY_SIMPLE = 20
LOCK_DC_AVERAGE = 25
LOCK_DC_GOOD = 30
LOCK_DC_AMAZING = 40

BREAK_DC_CHEST_SMALL = 17
BREAK_DC_CHEST_TREASURE = 23

BREAK_DC_DOOR_WOODEN_SIMPLE = 13
BREAK_DC_DOOR_WOODEN_GOOD = 18
BREAK_DC_DOOR_WOODEN_STRONG = 23
BREAK_DC_DOOR_IRON = 28

HARDNESS_DOOR_WOODEN_SIMPLE = 5
HARDNESS_DOOR_WOODEN_GOOD = 5
HARDNESS_DOOR_WOODEN_STRONG = 5
HARDNESS_DOOR_IRON = 10
HARDNESS_CHEST_SMALL = 5
HARDNESS_CHEST_TREASURE = 5

HP_DOOR_WOODEN_SIMPLE = 10
HP_DOOR_WOODEN_GOOD = 15
HP_DOOR_WOODEN_STRONG = 20
HP_DOOR_IRON = 60
HP_CHEST_SMALL = 1
HP_CHEST_TREASURE = 15

def container_setup_dc(obj, locked_dc, key_id, hp, hardeness, break_dc):
	assert isinstance(obj, toee.PyObjHandle)
	if (obj.type != toee.obj_t_container):
		print("container_setup_dc :: obj is not obj_t_container! {}".format(obj))
		debug.breakp("container_setup_dc")
		return
	
	#obj.obj_set_int(toee.obj_f_secretdoor_dc, break_dc)
	obj.obj_set_int(toee.obj_f_portal_pad_i_1, break_dc)
	

	if (locked_dc):
		obj.container_flag_set(toee.OCOF_LOCKED)
		if (locked_dc < 0):
			obj.container_flag_set(toee.OCOF_JAMMED)
		else:
			obj.obj_set_int(toee.obj_f_container_lock_dc, locked_dc)
			
		if (key_id):
			obj.obj_set_int(toee.obj_f_container_key_id, key_id)

	if (hp):
		obj.obj_set_int(toee.obj_f_hp_pts, hp)

	if (hardeness):
		obj.obj_set_int(toee.obj_f_hp_adj, hardeness)
	return obj

def portal_setup_dc(obj, locked_dc, key_id, hp, hardeness, break_dc):
	assert isinstance(obj, toee.PyObjHandle)
	if (obj.type != toee.obj_t_portal):
		print("portal_setup_dc :: obj is not obj_t_portal! {}".format(obj))
		debug.breakp("portal_setup_dc")
		return
	
	obj.obj_set_int(toee.obj_f_portal_pad_i_1, break_dc)

	if (locked_dc):
		obj.portal_flag_set(toee.OPF_LOCKED)
		if (locked_dc < 0):
			obj.portal_flag_set(toee.OPF_JAMMED)
		else:
			obj.obj_set_int(toee.obj_f_portal_lock_dc, locked_dc)
			
		if (key_id):
			obj.obj_set_int(toee.obj_f_portal_key_id, key_id)

	if (hp):
		obj.obj_set_int(toee.obj_f_hp_pts, hp)

	if (hardeness):
		obj.obj_set_int(toee.obj_f_hp_adj, hardeness)
	return obj

def portal_hook_autodestroy(x, y, radius_ft = 10, script_id = 6214):
	result = list()
	for obj in toee.game.obj_list_range(utils_obj.sec2loc(x, y), radius_ft, toee.OLC_PORTAL):
		assert isinstance(obj, toee.PyObjHandle)
		obj.scripts[const_toee.sn_use] = script_id #py06214_doors_autodestroy
		result.append(obj)
	return result

def key_create(loc, key_id, key_proto = None):
	assert isinstance(loc, int)
	assert isinstance(key_id, int)
	assert isinstance(key_proto, int)
	if not key_proto:
		key_proto = const_proto_items.PROTO_KEY_IRON_RUSTY
	key = toee.game.obj_create(key_proto, loc)
	key.obj_set_int(toee.obj_f_key_key_id, key_id)
	return key

def key_create_npc(npc, key_id, key_proto = None):
	assert isinstance(npc, toee.PyObjHandle)
	key = key_create(npc.location, key_id, key_proto)
	if key:
		npc.item_get(key)
	return key