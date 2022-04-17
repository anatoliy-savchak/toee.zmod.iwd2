
items_const = None
items_const_names = None

def items_const_init_module(module_name, module_items):
	assert isinstance(module_name, str)
	#print(type(module_items))
	assert isinstance(module_items, list)
	for item_name in module_items:
		assert isinstance(item_name, str)
		if (not item_name.lower().startswith("proto")): continue
		item_full_name = "{}.{}".format(module_name, item_name)
		ev = "__import__('{}').{}".format(module_name, item_name)
		#print("eval(\"{}\")".format(ev))
		item_value = eval(ev, {}, {})
		if (type(item_value) is int): 
			items_const[item_value] = item_full_name
		items_const_names[item_full_name] = item_value
	return

def items_const_init():
	global items_const
	global items_const_names
	if (not items_const):
		items_const = dict()
		items_const_names = dict()
		import const_proto_armor
		items_const_init_module("const_proto_armor", dir(const_proto_armor))
		import const_proto_cloth
		items_const_init_module("const_proto_cloth", dir(const_proto_cloth))
		import const_proto_containers
		items_const_init_module("const_proto_containers", dir(const_proto_containers))
		import const_proto_food
		items_const_init_module("const_proto_food", dir(const_proto_food))
		import const_proto_items
		items_const_init_module("const_proto_items", dir(const_proto_items))
		import const_proto_potions
		items_const_init_module("const_proto_potions", dir(const_proto_potions))
		import const_proto_rings
		items_const_init_module("const_proto_rings", dir(const_proto_rings))
		import const_proto_scrolls
		items_const_init_module("const_proto_scrolls", dir(const_proto_scrolls))
		import const_proto_wands
		items_const_init_module("const_proto_wands", dir(const_proto_wands))
		import const_proto_weapon
		items_const_init_module("const_proto_weapon", dir(const_proto_weapon))
		import const_proto_wondrous
		items_const_init_module("const_proto_wondrous", dir(const_proto_wondrous))

		import const_proto_list_armor
		items_const_init_module("const_proto_list_armor", dir(const_proto_list_armor))
		import const_proto_list_cloth
		items_const_init_module("const_proto_list_cloth", dir(const_proto_list_cloth))
		import const_proto_list_scrolls
		items_const_init_module("const_proto_list_scrolls", dir(const_proto_list_scrolls))
		import const_proto_list_wands
		items_const_init_module("const_proto_list_wands", dir(const_proto_list_wands))
		import const_proto_list_weapons
		items_const_init_module("const_proto_list_weapons", dir(const_proto_list_weapons))
		import const_proto_list_weapons_magic
		items_const_init_module("const_proto_list_weapons_magic", dir(const_proto_list_weapons_magic))
		import const_proto_list_weapons_masterwork
		items_const_init_module("const_proto_list_weapons_masterwork", dir(const_proto_list_weapons_masterwork))
	return items_const, items_const_names

def item_get_const(proto):
	assert isinstance(proto, int)
	items_const_, items_const_names_ = items_const_init()
	return items_const_.get(proto)

def item_get_byname(name):
	assert isinstance(name, str)
	items_const_, items_const_names_ = items_const_init()
	return items_const_names_.get(name)

def item_map_build(list_module_name, names, file_path = None):
	assert isinstance(list_module_name, str)
	assert isinstance(names, list)
	assert isinstance(file_path, str)
	items_const_, items_const_names_ = items_const_init()
	#for full_name in items_const_names_:
	#	if (not full_name.startswith(list_module_name)): continue
	#	print(full_name)

	f = open(file_path, "w") if (file_path) else None

	def doline(text):
		print(text)
		if (f):
			f.write(text + "\n")
		return

	doline("import const_proto_armor, utils_const")
	doline("")
	for name in names:
		assert isinstance(name, str)
		if (name.startswith("=")):
			doline("")
			doline(name[1:])
			doline("")
			continue
		fname = list_module_name + "." + name
		v = item_get_byname(fname)
		if not v: continue
		if (not type(v) is list): continue

		for proto in v:
			proto_name = item_get_const(proto)
			proto_name_masterwork = "{}_MASTERWORK".format(proto_name)
			proto_name_masterwork_val = item_get_byname(proto_name_masterwork)
			if (not proto_name_masterwork_val): proto_name_masterwork = 0
			quantity = 1
			if ("QUIVER" in proto_name or "POUCH" in proto_name): quantity = 10
			quantity_str = ', "q": {}'.format(quantity) if (quantity > 1) else ""
			#doline('{}_MAP = {{"proto": {}, "xp": 0, "mwproto": {}, "mwxp": 0, "svxp": 0, "mixp": 0, "adxp": 0, "svp": 0, "mip": 0}}'.format(proto_name.split('.')[1], proto_name, proto_name_masterwork))
			doline('{}_MAP = {{"proto": {}{}, "xp": 0 \\'.format(proto_name.split('.')[1], proto_name, quantity_str))
			doline('\t, "mwp": {}, "mwxp": 0 \\'.format(proto_name_masterwork))
			doline('\t, "svp": 0, "svxp": 0 \\')
			doline('\t, "cip": 0, "cixp": 0 \\')
			doline('\t, "mip": 0, "mixp": 0 \\')
			doline('\t, "adp": 0, "adxp": 0 \\')
			doline('\t}')

		doline("")
		doline("{}_MAP = {{\\".format(name))
		first = True
		for proto in v:
			proto_name = item_get_const(proto)
			prefix = "" if (first) else ", "
			first = False
			doline("\t{}{} : {}_MAP \\".format(prefix, proto_name, proto_name.split('.')[1]))
		doline("\t}")
		doline("")
	if (f):
		f.close()
	return

def item_map_build_weapons():
	list_module_name = "const_proto_list_weapons"
	names = ["PROTOS_WEAPON_SIMPLE_MELEE_LIGHT" \
		, "PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED" \
		, "PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED" \
		, "=PROTOS_WEAPON_SIMPLE_MELEE_MAP = utils_const.dmerge(PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_MAP, PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_MAP, PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_MAP)" \
		, "PROTOS_WEAPON_SIMPLE_RANGED" \
		, "=PROTOS_WEAPON_SIMPLE_MAP = utils_const.dmerge(PROTOS_WEAPON_SIMPLE_MELEE_MAP, PROTOS_WEAPON_SIMPLE_RANGED_MAP)" \
		, "PROTOS_WEAPON_MARTIAL_MELEE_LIGHT" \
		, "PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED" \
		, "PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED" \
		, "=PROTOS_WEAPON_MARTIAL_MELEE_MAP = utils_const.dmerge(PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_MAP, PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_MAP, PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_MAP)" \
		, "PROTOS_WEAPON_MARTIAL_RANGED" \
		, "=PROTOS_WEAPON_MARTIAL_MAP = utils_const.dmerge(PROTOS_WEAPON_MARTIAL_MELEE_MAP, PROTOS_WEAPON_MARTIAL_RANGED_MAP)" \
		, "PROTOS_WEAPON_EXOTIC_MELEE_LIGHT" \
		, "PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED" \
		, "PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED" \
		, "=PROTOS_WEAPON_EXOTIC_MELEE_MAP = utils_const.dmerge(PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_MAP, PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_MAP, PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_MAP)" \
		, "PROTOS_WEAPON_EXOTIC_RANGED" \
		, "=PROTOS_WEAPON_EXOTIC_MAP = utils_const.dmerge(PROTOS_WEAPON_EXOTIC_MELEE_MAP, PROTOS_WEAPON_EXOTIC_RANGED_MAP)" \
		, "=PROTOS_WEAPONS_MAP = utils_const.dmerge(PROTOS_WEAPON_SIMPLE_MAP, PROTOS_WEAPON_MARTIAL_MAP, PROTOS_WEAPON_EXOTIC_MAP)" \
		]
	item_map_build(list_module_name, names, r"D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.kots\src\zmod_kots_core\scr\const_proto_map_weapons.py")
	# PROTOS_WEAPON_SIMPLE_MELEE_MAP = PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_MAP + PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_MAP + PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_MAP

	return

def item_map_build_armor():
	list_module_name = "const_proto_list_armor"
	names = ["PROTOS_ARMOR_LIGHT_PADDED" \
		, "PROTOS_ARMOR_LIGHT_LEATHER" \
		, "PROTOS_ARMOR_LIGHT_STUDDED" \
		, "PROTOS_ARMOR_LIGHT_CHAIN_SHIRT" \
		, "=PROTOS_ARMOR_LIGHT_MAP = utils_const.dmerge(PROTOS_ARMOR_LIGHT_PADDED_MAP, PROTOS_ARMOR_LIGHT_LEATHER_MAP, PROTOS_ARMOR_LIGHT_STUDDED_MAP, PROTOS_ARMOR_LIGHT_CHAIN_SHIRT_MAP)" \
		, "PROTOS_ARMOR_MEDIUM_HIDE" \
		, "PROTOS_ARMOR_MEDIUM_SCALE" \
		, "PROTOS_ARMOR_MEDIUM_CHAINMAIL" \
		, "PROTOS_ARMOR_MEDIUM_BREASTPLATE" \
		, "=PROTOS_ARMOR_MEDIUM_MAP = utils_const.dmerge(PROTOS_ARMOR_MEDIUM_HIDE_MAP, PROTOS_ARMOR_MEDIUM_SCALE_MAP, PROTOS_ARMOR_MEDIUM_CHAINMAIL_MAP, PROTOS_ARMOR_MEDIUM_BREASTPLATE_MAP)" \
		, "PROTOS_ARMOR_HEAVY_SPLINT_MAIL" \
		, "PROTOS_ARMOR_HEAVY_BANDED_MAIL" \
		, "PROTOS_ARMOR_HEAVY_HALF_PLATE" \
		, "PROTOS_ARMOR_HEAVY_FULL_PLATE" \
		, "=PROTOS_ARMOR_HEAVY_MAP = utils_const.dmerge(PROTOS_ARMOR_HEAVY_SPLINT_MAIL_MAP, PROTOS_ARMOR_HEAVY_BANDED_MAIL_MAP, PROTOS_ARMOR_HEAVY_HALF_PLATE_MAP, PROTOS_ARMOR_HEAVY_FULL_PLATE_MAP)" \
		, "=PROTOS_ARMOR_MAP = utils_const.dmerge(PROTOS_ARMOR_LIGHT_MAP, PROTOS_ARMOR_MEDIUM_MAP, PROTOS_ARMOR_HEAVY_MAP)" \
		]
	item_map_build(list_module_name, names, r"D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.kots\src\zmod_kots_core\scr\const_proto_map_armor.py")
	# PROTOS_WEAPON_SIMPLE_MELEE_MAP = PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_MAP + PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_MAP + PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_MAP
	return

def dmerge(d1, d2, d3 = None, d4 = None, d5 = None):
	result = d1.copy()
	result.update(d2)
	if (d3): result.update(d3)
	if (d4): result.update(d4)
	if (d5): result.update(d5)
	return result
