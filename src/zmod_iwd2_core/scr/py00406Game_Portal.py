import toee, debug, const_toee, utils_storage, startup_zmod, utils_obj, const_proto_containers
import debug, utils_pc, module_consts, const_proto_weapon, const_proto_list_cloth, const_proto_cloth, utils_item

def san_dialog(attachee, triggerer):
	triggerer.begin_dialog( attachee, 1 )
	return toee.SKIP_DEFAULT

def san_first_heartbeat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	#attachee.critter_flag_set(toee.OCF_NO_FLEE)
	if not attachee.critter_flags_get(toee.OCF_NO_FLEE):
		zmod_startup()
		place_chests()
		reset_money()
		outfit_pcs()
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
	#place_chest(14575, 492, 474, 2.82842779, 2.82842779, 2.3561945)

	# Weapons Chest
	#place_chest(14755, 481, 474, -9.899495, 12.7279215, 2.3561945)

	# Clothing Chest
	place_chest(14757, 465, 475, -9.899495, -12.7279215, 2.3561945)

	# Scrolls Chest
	#place_chest(14754, 485, 475, 5.65685368, -14.1421356, 3.92699075)

	# Armor Chest
	#place_chest(14756, 471, 488, 7.071068, 4.242642, 5.497787)

	# Supplies Chest
	place_chest(14753, 485, 483, 12.7279215, 9.899496, 3.926991)
	return

def reset_money():
	pc = toee.game.party[0]
	if (pc):
		pc.money_adj(130 * const_toee.gp - pc.money_get())
	return

def outfit_pcs():
	garbs1 = const_proto_list_cloth.PROTO_CLOTH_GARBS_FARMER[:]
	garbs2 = const_proto_list_cloth.PROTO_CLOTH_GARBS_VILLAGER[:]
	garbs3 = const_proto_list_cloth.PROTO_CLOTH_GARBS_NOBLE[:]
	garbs3.append(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT)
	garbs3.append(const_proto_cloth.PROTO_CLOTH_GARB_MYSTIC_ORANGE)

	def garb_in_collections(garb):
		if garb in garbs1:
			return garb
		if garb in garbs2:
			return garb
		if garb in garbs3:
			return garb
		return

	def garb_remove_from_collections(garb):
		if garb in garbs1:
			garbs1.remove(garb)
		if garb in garbs2:
			garbs2.remove(garb)
		if garb in garbs3:
			garbs3.remove(garb)
		return


	garb_proto = None
	for pc in toee.game.party:
		pc_class = pc.char_classes[0]
		pc_gender = pc.obj_get_int(toee.obj_f_critter_gender)
		if pc_class == toee.stat_level_fighter:
			garb_proto = garb_in_collections(const_proto_cloth.PROTO_CLOTH_GARB_NOBLE_RED)
		elif pc_class == toee.stat_level_cleric:
			garb_proto = garb_in_collections(const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_BLUE)
		elif pc_class == toee.stat_level_sorcerer:
			if pc_gender:
				garb_proto = garb_in_collections(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT)
			else:
				garb_proto = garb_in_collections(const_proto_cloth.PROTO_CLOTH_GARB_MYSTIC_ORANGE)
			
		if not garb_proto:
			if garbs1:
				garb_proto = garbs1[toee.game.random_range(0, len(garbs1)-1)]
			if garbs2:
				garb_proto = garbs2[toee.game.random_range(0, len(garbs2)-1)]

		if garb_proto:
			garb_remove_from_collections(garb_proto)
			utils_item.item_create_in_inventory2(garb_proto, pc, 0, toee.item_wear_armor)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, pc, 0, toee.item_wear_boots)
		utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_QUARTERSTAFF, pc, 0, toee.item_wear_weapon_primary)

	return