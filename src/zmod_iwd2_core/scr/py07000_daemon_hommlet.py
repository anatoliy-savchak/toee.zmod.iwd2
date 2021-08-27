import toee, debug, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee, ctrl_daemon
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import startup_zmod, utils_sneak, monster_info, copy, rttoee_consts, const_animate, const_sceneries, const_proto_cloth, const_proto_items

HOMMLET = "hommlet"
HOMMLET_DAEMON_SCRIPT = 7000
HOMMLET_DAEMON_ID = "G_227925DC_74BE_4461_BA6D_1DA88F0C6AD0"
HOMMLET_DAEMON_DIALOG = 7000

def cs():
	return ctrl_daemon2.ccs(HOMMLET_DAEMON_ID, CtrlHommlet)

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, rttoee_consts.MAP_ID_HOMMLET, CtrlHommlet)

def san_first_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_HOMMLET, CtrlHommlet)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_HOMMLET, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, rttoee_consts.MAP_ID_HOMMLET, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, rttoee_consts.MAP_ID_HOMMLET, cs())

class CtrlHommlet(ctrl_daemon2.CtrlDaemon2):
	def __init__(self):
		super(CtrlHommlet, self).__init__()
		self.init_daemon2_fields(rttoee_consts.MAP_ID_HOMMLET, HOMMLET_DAEMON_SCRIPT, HOMMLET)
		return

	def place_encounters_initial(self):
		self.place_post()
		self.disable_portals()
		self.place_animals()
		self.place_smithy()
		return

	def place_staff(self):
		obj = toee.game.obj_create(14016, utils_obj.sec2loc(488, 478), 9.89949607849, 9.89949607849) # Ostler Gundigoot
		if (obj):
			obj.rotation = 0.785398185253
			item = utils_item.item_create_in_inventory(const_proto_items.PROTO_ARMOR_NECKLACE_JADE, obj)
			if (item): item.obj_set_int(toee.obj_f_item_quantity, 2)
			item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CLOTH_ARMOR, obj)
			item = utils_item.item_create_in_inventory(const_proto_rings.PROTO_RING_PLATINUM, obj)
			if (item): item.obj_set_int(toee.obj_f_item_quantity, 2)
			item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_PADDED_TAN, obj)
			item = utils_item.item_create_in_inventory(const_proto_items.PROTO_MONEY_COPPER, obj)
			item = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, obj)
		return

	def get_animals_at(self, loc, animals):
		for npc in toee.game.obj_list_range(loc, 200, toee.OLC_NPC):
			if (not npc in animals and npc.get_category_type() == toee.mc_type_animal):
				animals.append(npc)
		return

	def place_post(self):
		loc = utils_obj.sec2loc(614, 418)
		npc = toee.game.obj_create(14799, loc, 4.242642, -1.41421306)
		npc.move(loc)
		return

	def place_animals(self):
		obj = toee.game.obj_create(14363, utils_obj.sec2loc(720, 459), -8.48528194427, 2.8284277916) # Chicken
		obj.rotation = 4.01425743103
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(715, 461), 0.0, 0.0) # Chicken
		obj.rotation = 4.81710863113
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(714, 462), -9.89949512482, 9.89949607849) # Chicken
		obj.rotation = 1.51843643188
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(717, 459), -9.89949512482, -4.24264097214) # Chicken
		obj.rotation = 0.802851438522
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14364, utils_obj.sec2loc(719, 462), -14.1421356201, -14.1421356201) # Rooster
		obj.rotation = 0.890117883682
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(713, 460), -4.24264097214, 9.89949607849) # Chicken
		obj.rotation = 3.7699110508
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(721, 462), 0.0, 0.0) # Chicken
		obj.rotation = 3.43829870224
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(718, 463), -14.1421356201, 0.0) # Chicken
		obj.rotation = 5.82939958572
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(722, 464), -7.07106781006, -1.41421306133) # Chicken
		obj.rotation = 6.23082542419
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14362, utils_obj.sec2loc(737, 394), 0.0, 0.0) # Chicken
		obj.rotation = 4.88692188263
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14362, utils_obj.sec2loc(713, 364), 0.0, 0.0) # Chicken
		obj.rotation = 1.90240883827
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14362, utils_obj.sec2loc(737, 377), 0.0, 0.0) # Chicken
		obj.rotation = 1.95476877689
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14362, utils_obj.sec2loc(724, 389), 0.0, 0.0) # Chicken
		obj.rotation = 1.67551612854
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(774, 409), 0.0, 0.0) # Chicken
		obj.rotation = 1.95476877689
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(776, 393), 0.0, 0.0) # Chicken
		obj.rotation = 2.46091413498
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14362, utils_obj.sec2loc(767, 433), 0.0, 0.0) # Chicken
		obj.rotation = 2.72271370888
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(783, 396), 0.0, 0.0) # Chicken
		obj.rotation = 4.398229599
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14362, utils_obj.sec2loc(772, 395), 0.0, 0.0) # Chicken
		obj.rotation = 4.15388345718
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(773, 431), 0.0, 0.0) # Chicken
		obj.rotation = 3.75245785713
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(775, 402), 0.0, 0.0) # Chicken
		obj.rotation = 3.49065852165
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(767, 397), 0.0, 0.0) # Chicken
		obj.rotation = 5.30580091476
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14363, utils_obj.sec2loc(774, 391), 0.0, 0.0) # Chicken
		obj.rotation = 3.85717773438
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14365, utils_obj.sec2loc(564, 233), 0.0, 0.0) # Sheep
		obj.rotation = 2.53072738647
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14366, utils_obj.sec2loc(573, 229), 0.0, 0.0) # Sheep
		obj.rotation = 6.26573181152
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14365, utils_obj.sec2loc(569, 214), 0.0, 0.0) # Sheep
		obj.rotation = 3.8920841217
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14048, utils_obj.sec2loc(547, 244), 0.0, 0.0) # Farm Dog
		obj.rotation = 3.75245785713
		waypoints = list()
		waypoints.append(utils_npc.Waypoint(547, 244, 3.86085752891e-41, 1308260, 0, 149, 192, 0, 0, 56, 128, 224, 50, 0.0, 0.0))
		waypoints.append(utils_npc.Waypoint(558, 249, 15471.4960938, 1181859324, 0, 31, 31, 31, 31, 0, 0, 0, 0, 0.0, 0.0))
		obj.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
		obj.npc_flag_set(toee.ONF_WAYPOINTS_NIGHT)
		obj.npc_waypoints_set(waypoints, 1)

		obj = toee.game.obj_create(14365, utils_obj.sec2loc(562, 217), 0.0, 0.0) # Sheep
		obj.rotation = 3.42084527016
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14366, utils_obj.sec2loc(565, 241), 0.0, 0.0) # Sheep
		obj.rotation = 5.13126802444
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14365, utils_obj.sec2loc(572, 238), 0.0, 0.0) # Sheep
		obj.rotation = 2.49582076073
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14048, utils_obj.sec2loc(560, 239), 0.0, 0.0) # Farm Dog
		obj.rotation = 1.39626336098
		waypoints = list()
		waypoints.append(utils_npc.Waypoint(560, 239, 3.86085752891e-41, 1308260, 0, 149, 192, 0, 0, 56, 128, 224, 50, 0.0, 0.0))
		waypoints.append(utils_npc.Waypoint(558, 230, 15839.1914062, 1182235844, 0, 231, 231, 231, 231, 0, 0, 0, 0, 0.0, 0.0))
		obj.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
		obj.npc_flag_set(toee.ONF_WAYPOINTS_NIGHT)
		obj.npc_waypoints_set(waypoints, 1)

		obj = toee.game.obj_create(14365, utils_obj.sec2loc(582, 223), 0.0, 0.0) # Sheep
		obj.rotation = 0.959931075573
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14365, utils_obj.sec2loc(571, 498), 0.0, 0.0) # Sheep
		obj.rotation = 6.24827861786
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14365, utils_obj.sec2loc(564, 511), 0.0, 0.0) # Sheep
		obj.rotation = 4.03171062469
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14366, utils_obj.sec2loc(568, 507), 0.0, 0.0) # Sheep
		obj.rotation = 4.88692188263
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14365, utils_obj.sec2loc(564, 497), 0.0, 0.0) # Sheep
		obj.rotation = 2.00712871552
		obj.npc_flag_set(toee.ONF_WANDERS)

		obj = toee.game.obj_create(14365, utils_obj.sec2loc(567, 492), 0.0, 0.0) # Sheep
		obj.rotation = 5.7246799469
		waypoints = list()
		waypoints.append(utils_npc.Waypoint(448, 555, 3.61535003796e-43, 32, 0, 64, 1, 192, 135, 224, 192, 0, 0, 0.0, 0.0))
		waypoints.append(utils_npc.Waypoint(448, 555, 3.61535003796e-43, 32, 0, 64, 1, 192, 135, 224, 192, 0, 0, 0.0, 0.0))
		obj.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
		obj.npc_flag_set(toee.ONF_WAYPOINTS_NIGHT)
		obj.npc_waypoints_set(waypoints, 1)

		obj = toee.game.obj_create(14365, utils_obj.sec2loc(570, 513), 0.0, 0.0) # Sheep
		obj.rotation = 0.174532920122
		obj.npc_flag_set(toee.ONF_WANDERS)
		return

	def produce_animals(self):
		#npc = toee.game.obj_create(14799, utils_obj.sec2loc(614, 418), 4.242642, -1.41421306)
		animals = list()
		self.get_animals_at(utils_obj.sec2loc(707, 521), animals)
		self.get_animals_at(utils_obj.sec2loc(710, 445), animals)
		self.get_animals_at(utils_obj.sec2loc(748, 406), animals)
		self.get_animals_at(utils_obj.sec2loc(559, 232), animals)
		self.get_animals_at(utils_obj.sec2loc(560, 484), animals)

		lines = list()
		for npc in animals:
			assert isinstance(npc, toee.PyObjHandle)
			standpoint = npc.standpoint_get()
			locx, locy= utils_obj.loc2sec(npc.location)
			off_x, off_y = npc.off_x, npc.off_y
			if (standpoint):
				locx, locy, off_x, off_y = standpoint["loc_x"], standpoint["loc_y"], standpoint["off_x"], standpoint["off_y"]
			line = "obj = toee.game.obj_create({}, utils_obj.sec2loc({}, {}), {}, {}) # {}".format(npc.proto, locx, locy, off_x, off_y, npc.description)
			lines.append(line)
			lines.append("obj.rotation = {}".format(npc.rotation))
			if (npc.npc_flags_get() & toee.ONF_WANDERS):
				lines.append("obj.npc_flag_set(toee.ONF_WANDERS)")
			
			waypoints = npc.npc_waypoints_get()
			if (waypoints):
				wplines = utils_npc.Waypoint.produce_code_from_list(waypoints)
				if (wplines):
					lines.append("waypoints = list()")
					lines.extend(wplines)
					if (npc.npc_flags_get() & toee.ONF_WAYPOINTS_DAY):
						lines.append("obj.npc_flag_set(toee.ONF_WAYPOINTS_DAY)")
					if (npc.npc_flags_get() & toee.ONF_WAYPOINTS_NIGHT):
						lines.append("obj.npc_flag_set(toee.ONF_WAYPOINTS_NIGHT)")
					lines.append("obj.npc_waypoints_set(waypoints, 1)")
					
			lines.append("")

		txt = "\n".join(lines)
		f = open("D:\Temp\lines.txt", "w")
		f.write(txt)
		f.close()
		return

	def get_portals_at(self, loc, portals):
		for obj in toee.game.obj_list_range(loc, 200, toee.OLC_SCENERY):
			if (not obj.proto in const_sceneries.PROTOS_SCENERY_ICONS): continue
			if (not obj in portals):
				portals.append(obj)
		return

	def disable_portals(self):
		portals = list()
		#260, 170=> 800, 720
		x, y = 250, 150
		while (x <= 800):
			y = 150
			while (y <= 750):
				self.get_portals_at(utils_obj.sec2loc(x, y), portals)
				y += 50
			x += 50

		allowed_portal_names = (rttoee_consts.PORTAL_HOMMLET_INN, rttoee_consts.PORTAL_HOMMLET_OLD_TRADING_POST, rttoee_consts.PORTAL_HOMMLET_VILLAGE_ELDER)
		for portal in portals:
			assert isinstance(portal, toee.PyObjHandle)
			if (portal.name in allowed_portal_names): continue
			portal.object_flag_set(toee.OF_OFF)
			portal.object_flag_set(toee.OF_DONTDRAW)
		return

	def scan_all(self):
		npcs = list()
		#260, 170=> 800, 720
		x, y = 250, 150
		while (x <= 800):
			y = 150
			while (y <= 750):
				utils_npc.get_npcs_range(utils_obj.sec2loc(x, y), lst = npcs)
				y += 50
			x += 50
		utils_npc.build_npcs(npcs, {"save_to": r"D:\Temp\npcs.py"})
		return

	def place_smithy(self):
		loc = utils_obj.sec2loc(571, 434)
		obj = toee.game.obj_create(14010, loc, 0.0, 0.0) # Brother Smith
		if (obj):
			obj.move(loc)
			obj.rotation = 3.05432605743
			waypoints = list()
			waypoints.append(utils_npc.Waypoint(571, 434, 2.51112684807e-41, 1449216, 0, 152, 148, 224, 0, 136, 136, 136, 136, 0.0, 0.0))
			waypoints.append(utils_npc.Waypoint(571, 434, 4.20389539297e-44, 4, 4, 1, 1, 1, 1, 1, 0, 0, 0, 0.0, 0.0))
			obj.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
			obj.npc_waypoints_set(waypoints, 1)
			item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_LEATHER_BROWN, obj)
			item = utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, obj)
			item = utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BROWN, obj)
			item = utils_item.item_create_in_inventory(const_proto_items.PROTO_MONEY_COPPER, obj)
			item = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_WARHAMMER, obj)
			obj.item_wield_best_all()
		return