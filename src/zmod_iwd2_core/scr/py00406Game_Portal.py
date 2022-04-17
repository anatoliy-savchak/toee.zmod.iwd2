import toee, utils_storage, startup_zmod, utils_obj, const_proto_containers, debug, utils_pc, module_consts

def san_dialog(attachee, triggerer):
	triggerer.begin_dialog( attachee, 1 )
	return toee.SKIP_DEFAULT

def san_first_heartbeat(attachee, triggerer):
	zmod_startup()
	place_chests()
	return toee.RUN_DEFAULT

def zmod_startup():
	utils_storage.Storage.reset()
	startup_zmod.zmod_conditions_apply_pc()
	return

def place_chests():
	def place_chest(proto, locx, locy, offset_x, offset_y, rot):
		loc = utils_obj.sec2loc(locx, locy)
		obj = toee.game.obj_create(proto, loc, offset_x, offset_y)
		if (obj):
			obj.rotation = rot
			obj.move(loc, offset_x, offset_y)
			box = toee.game.obj_create(const_proto_containers.PROTO_CONTAINER_CHEST_GENERIC, obj.location)
			box.object_flag_set(toee.OF_DONTDRAW)
			box.obj_set_int(toee.obj_f_container_inventory_source, 0)
			obj.substitute_inventory = box
		return

	#debug.breakp("")
	# Standard Equipment Chest
	place_chest(14575, 492, 474, 2.82842779, 2.82842779, 2.3561945)

	# Weapons Chest
	place_chest(14755, 481, 474, -9.899495, 12.7279215, 2.3561945)

	# Clothing Chest
	place_chest(14757, 465, 475, -9.899495, -12.7279215, 2.3561945)

	# Scrolls Chest
	place_chest(14754, 485, 475, 5.65685368, -14.1421356, 3.92699075)

	# Armor Chest
	place_chest(14756, 471, 488, 7.071068, 4.242642, 5.497787)

	# Supplies Chest
	place_chest(14753, 485, 483, 12.7279215, 9.899496, 3.926991)

	# reset money
	pc = toee.game.party[0]
	if (pc):
		currentcp = pc.money_get()
		print("{}: {}".format(pc, currentcp))
		pc.money_adj(-currentcp)
		utils_pc.pc_party_set_starting_gold_as_raw(0)

	return