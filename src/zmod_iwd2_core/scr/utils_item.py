import toee, debugg, const_proto_items

def item_create_in_inventory(item_proto_num, npc, quantity = 1, is_loot = 1):
	assert isinstance(item_proto_num, int)
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(is_loot, int)
	item = toee.game.obj_create(item_proto_num, npc.location)
	#item_alter_worth_as_raw(item, is_loot)
	if (npc.type == toee.obj_t_pc):
		item.item_flag_set(toee.OIF_IDENTIFIED)
	else: item.item_flag_unset(toee.OIF_IDENTIFIED)

	if (item != toee.OBJ_HANDLE_NULL):
		npc.item_get(item)
	if (quantity > 1):
		for i in range(2, quantity):
			item = toee.game.obj_create(item_proto_num, npc.location)
			#item_alter_worth_as_raw(item, is_loot)
			if (item != toee.OBJ_HANDLE_NULL):
				npc.item_get(item)
	return item

def item_create_in_inventory_buy(item_proto_num, npc, price_override = None, worth_mult = None):
	assert isinstance(item_proto_num, int)
	assert isinstance(npc, toee.PyObjHandle)
	item = toee.game.obj_create(item_proto_num, npc.location)
	if (npc.type == toee.obj_t_pc):
		item.item_flag_set(toee.OIF_IDENTIFIED)
	if (item != toee.OBJ_HANDLE_NULL):
		worth = item.obj_get_int(toee.obj_f_item_worth)
		if (worth_mult): worth = int(worth * worth_mult)
		if (price_override): worth = price_override
		left = npc.money_get()
		text = "{}: {} gp | {}".format(item.description, worth // 100, left // 100)
		print(text)
		if (left >= worth):
			npc.money_adj(-worth)
			npc.item_get(item)
		else: 
			print("Lack of money!")
			item.destroy()
			item = None
	return item

def item_create_in_inventory2(item_proto_num, npc, no_loot, wear_on = None):
	assert isinstance(item_proto_num, int)
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(no_loot, int)
	assert isinstance(wear_on, int)

	item = item_create_in_inventory(item_proto_num, npc)
	if (no_loot and item):
		item.item_flag_set(toee.OIF_NO_LOOT)
	if (not wear_on is None and item):
		npc.item_wield(item, wear_on) # toee.item_wear_cloak
	return item

def item_alter_worth_as_raw(item, is_loot):
	# todo - disable when T+ support will be added
	assert isinstance(item, toee.PyObjHandle)
	assert isinstance(is_loot, int)
	if (not is_loot or not item): return None
	if (item.type == toee.obj_t_generic and item.obj_get_int(toee.obj_f_category) == 5): # gems should have full price
		return None
	worth = item.obj_get_int(toee.obj_f_item_worth)
	new_worh = worth // 2
	item.obj_set_int(toee.obj_f_item_worth, new_worh)
	return new_worh

def item_place_into_inventory(item, npc):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(item, toee.PyObjHandle)
	if (item != OBJ_HANDLE_NULL):
		npc.item_get(item)
	return item

def item_create_in_inventory_mass(npc, protos):
	assert isinstance(npc, toee.PyObjHandle)
	for item_proto_num in protos:
		item_create_in_inventory(item_proto_num, npc)
	return

def item_clear_all(npc):
	assert isinstance(npc, toee.PyObjHandle)
	#breakp("inventory clear_all")
	item_unwield_all(npc)
	otype = npc.type
	invenField = 0
	invenNumField = 0
	if ((otype == toee.obj_t_npc) or (otype == toee.obj_t_pc)):
		invenField = toee.obj_f_critter_inventory_list_idx
		invenNumField = toee.obj_f_critter_inventory_num
	elif ((otype == toee.obj_t_container) or (otype == toee.obj_t_bag)):
		invenField = toee.obj_f_container_inventory_list_idx
		invenNumField = toee.obj_f_container_inventory_num
	else:
		invenField = toee.obj_f_critter_inventory_list_idx
		invenNumField = toee.obj_f_critter_inventory_num

	#print("invenField: {}, invenNumField: {}".format(invenField, invenNumField))
	numItems = npc.obj_get_int(invenNumField)
	#print("Inventory count {} for obj {}".format(numItems, npc))
	if (numItems > 0):
		for i in range(0, 199):
			#itemProto = npc.obj_get_idx_obj(invenField, i)
			#item = npc.item_find(4077)
			item = npc.inventory_item(i)
			#print("Item at {}: {}".format(i, item))
			if (item != toee.OBJ_HANDLE_NULL):
				numItems = numItems - 1
				item.destroy()
			if (numItems <=0): break

	return numItems

def item_clear_by_proto(npc, proto_id):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(proto_id, int)
	#breakp("inventory clear_all")
	item_unwield_by_proto(npc, proto_id)
	otype = npc.type
	invenField = 0
	invenNumField = 0
	if ((otype == toee.obj_t_npc) or (otype == toee.obj_t_pc)):
		invenField = toee.obj_f_critter_inventory_list_idx
		invenNumField = toee.obj_f_critter_inventory_num
	elif ((otype == toee.obj_t_container) or (otype == toee.obj_t_bag)):
		invenField = toee.obj_f_container_inventory_list_idx
		invenNumField = toee.obj_f_container_inventory_num
	else:
		invenField = toee.obj_f_critter_inventory_list_idx
		invenNumField = toee.obj_f_critter_inventory_num

	#print("invenField: {}, invenNumField: {}".format(invenField, invenNumField))
	numItems = npc.obj_get_int(invenNumField)
	#print("Inventory count {} for obj {}".format(numItems, npc))
	if (numItems > 0):
		for i in range(0, 199):
			#itemProto = npc.obj_get_idx_obj(invenField, i)
			#item = npc.item_find(4077)
			item = npc.inventory_item(i)
			#print("Item at {}: {}".format(i, item))
			if (item != toee.OBJ_HANDLE_NULL):
				numItems = numItems - 1
				if (item.proto == proto_id): 
					item.destroy()
			if (numItems <=0): break

	return numItems

def item_unwield_all(npc):
	assert isinstance(npc, toee.PyObjHandle)
	if (not npc): return
	if (npc.type == toee.obj_t_npc or npc.type == toee.obj_t_pc):
		for i in range(toee.item_wear_helmet, toee.item_wear_lockpicks):
			npc.item_worn_unwield(i, 0)
	return

def item_unwield_by_proto(npc, proto_id):
	assert isinstance(npc, toee.PyObjHandle)
	for i in range(toee.item_wear_helmet, toee.item_wear_lockpicks):
		item = npc.item_worn_at(i)
		if (item and item.proto == proto_id):
			npc.item_worn_unwield(i, 0)
	return

def item_do_use_getset(attachee, new_used = None):
	assert isinstance(attachee, toee.PyObjHandle)
	result = attachee.object_flags_get() & toee.OF_UNUSED_40000 != 0
	if (new_used is None): return result
	if (new_used):
		attachee.object_flag_set(toee.OF_UNUSED_40000)
	else:
		attachee.object_flag_unset(toee.OF_UNUSED_40000)
	return result

def item_get_marker(attachee):
	assert isinstance(attachee, toee.PyObjHandle)
	return attachee.obj_get_int(toee.obj_f_hp_pts)

def item_get_dialog_hint_id(attachee):
	assert isinstance(attachee, toee.PyObjHandle)
	return attachee.obj_get_int(toee.obj_f_hp_damage)

def item_money_create_in_inventory(obj, platinum, gold = None, silver = None, copper = None):
	assert isinstance(obj, toee.PyObjHandle)
	if (platinum):
		item = item_create_in_inventory(const_proto_items.PROTO_MONEY_PLATINUM, obj)
		item.obj_set_int(toee.obj_f_money_quantity, platinum)
	if (gold):
		item = item_create_in_inventory(const_proto_items.PROTO_MONEY_GOLD, obj)
		item.obj_set_int(toee.obj_f_money_quantity, gold)
	if (silver):
		item = item_create_in_inventory(const_proto_items.PROTO_MONEY_SILVER, obj)
		item.obj_set_int(toee.obj_f_money_quantity, silver)
	if (copper):
		item = item_create_in_inventory(const_proto_items.PROTO_MONEY_COPPER, obj)
		item.obj_set_int(toee.obj_f_money_quantity, copper)
	return

def items_get(npc, unwield_all = 1):
	assert isinstance(npc, toee.PyObjHandle)
	otype = npc.type
	invenField = 0
	invenNumField = 0
	if ((otype == toee.obj_t_npc) or (otype == toee.obj_t_pc)):
		invenField = toee.obj_f_critter_inventory_list_idx
		invenNumField = toee.obj_f_critter_inventory_num
	elif ((otype == toee.obj_t_container) or (otype == toee.obj_t_bag)):
		invenField = toee.obj_f_container_inventory_list_idx
		invenNumField = toee.obj_f_container_inventory_num
	else:
		invenField = toee.obj_f_critter_inventory_list_idx
		invenNumField = toee.obj_f_critter_inventory_num
	numItems = npc.obj_get_int(invenNumField)
	result = list()
	print("numItems: {}".format(numItems))
	if (numItems > 0):
		#debugg.breakp("numItems")
		if (unwield_all):
			for i in range(toee.item_wear_helmet, toee.item_wear_lockpicks):
				npc.item_worn_unwield(i, 0)
		else:
			for i in range(toee.item_wear_helmet, toee.item_wear_lockpicks):
				item = npc.item_worn_at(i)
				if (item and not item in result):
					result.append(item)

		for i in range(0, 199):
			item = npc.inventory_item(i)
			if (item and not item in result):
				print(item)
				result.append(item)
				numItems -= 1
			if (numItems <=0): break
	print(result)
	return result

def item_has(npc, itemproto): # find
	assert isinstance(npc, toee.PyObjHandle)
	otype = npc.type
	invenField = 0
	invenNumField = 0
	if ((otype == toee.obj_t_npc) or (otype == toee.obj_t_pc)):
		invenField = toee.obj_f_critter_inventory_list_idx
		invenNumField = toee.obj_f_critter_inventory_num
	elif ((otype == toee.obj_t_container) or (otype == toee.obj_t_bag)):
		invenField = toee.obj_f_container_inventory_list_idx
		invenNumField = toee.obj_f_container_inventory_num
	else:
		invenField = toee.obj_f_critter_inventory_list_idx
		invenNumField = toee.obj_f_critter_inventory_num
	numItems = npc.obj_get_int(invenNumField)
	result = list()
	#print("numItems: {}".format(numItems))
	if (numItems > 0):
		#debugg.breakp("numItems")
		for i in range(toee.item_wear_helmet, toee.item_wear_lockpicks):
			item = npc.item_worn_at(i)
			if (item and item.proto == itemproto):
				return item

		for i in range(0, 199):
			item = npc.inventory_item(i)
			if (item and item.proto == itemproto):
				return item
	return toee.OBJ_HANDLE_NULL

def acquire_sell_modifier_once():
	highest_appraise = -999
	highest_obj = None
	for obj in toee.game.party:
		appr = obj.skill_level_get(toee.skill_appraise)
		if appr > highest_appraise:
			highest_appraise = appr
			highest_obj = obj

	result = 0.0
	if highest_appraise > 19:
		result = 0.97
	elif highest_appraise < -13:
		result = 0
	else:
		result = 0.4 + float(highest_appraise)*0.03
	print("sell_modifier = {}, highest_appraise: {}, highest_obj: {}".format(result, highest_appraise, highest_obj))
	return result

def autosell(sell_modifier, items):
	assert isinstance(sell_modifier, float)
	assert isinstance(items, list)
	
	#items = items_get(bag, 0)
	num = 0
	total_lb = 0
	total_gp = 0
	total_sell = 0.0
	for item in items:
		assert isinstance(item, toee.PyObjHandle)
		num +=1
		text = item.description
		worth0 = item.obj_get_int(toee.obj_f_item_worth)
		worth_gp = worth0 // 100
		total_gp += worth_gp
		total_sell += worth0 * sell_modifier
		worth_gp_sell = worth_gp * sell_modifier
		x2 = ""
		x = item.obj_get_int(toee.obj_f_item_quantity)
		if (x > 1): x2 = " x{}".format(x)
		text = "{:02d}. {}{}.\n {} gp\n".format(num, text, x2, int(worth_gp_sell))
		toee.game.create_history_freeform(text)

	if (num):
		toee.game.create_history_freeform("---------\n")
		text = "Total sold: {} gp\n".format(int(total_sell / 100))
		toee.game.create_history_freeform(text)
	toee.game.create_history_freeform("\n")

	for item in items:
		item.destroy()

	total_sell_adj = int(total_sell)
	toee.game.leader.money_adj(total_sell_adj)
	print("attachee.money_adj: {}".format(total_sell_adj))
	return

def barter_sell(npc):
	assert isinstance(npc, toee.PyObjHandle)
	item_clear_all(npc.substitute_inventory)
	return

def barter_list(npc, protos):
	assert isinstance(npc, toee.PyObjHandle)
	subs = npc.substitute_inventory
	item_clear_all(subs)
	items = dict()
	j = 0
	for i in protos:
		j += 1
		item = toee.game.obj_create(i, subs.location)
		item.item_flag_set(toee.OIF_IDENTIFIED)
		#items["{}_{}_{}".format(item.description, i, j)] = i
		items["{}_{}_{}".format(item.description, i, j)] = item
		#item.destroy()

	for key in sorted(items):
		print(key)
		#item = toee.game.obj_create(items[key], subs.location)
		#item.item_flag_set(toee.OIF_IDENTIFIED)
		item = items[key]
		subs.item_get(item)
	return

items_const = None

def items_const_init_module(module_name, module_items):
	assert isinstance(module_name, str)
	assert isinstance(module_items, dict)
	for item_name in module_items:
		assert isinstance(item_name, str)
		if (not item_name.lower().startswith("proto")): continue
		item_full_name = "{}.{}".format(module_name, item_name)
		ev = "__import__('{}').{}".format(module_name, item_name)
		print("eval(\"{}\")".format(ev))
		item_value = eval(ev, {}, {})
		if (not type(item_value) is int): continue
		items_const[item_value] = item_full_name
	return

def items_const_init():
	global items_const
	if (not items_const):
		items_const = dict()
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
	return items_const

def item_get_const(proto):
	assert isinstance(proto, toee.PyObjHandle)
	items_const_ = items_const_init()
	if (proto in items_const_): return items_const_[proto]
	return

def npc_build_items(npc, lines, prefix = ""):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(lines, list)
	items = items_get(npc, 0)
	for item in items:
		assert isinstance(item, toee.PyObjHandle)
		item_name = item_get_const(item.proto)
		desc = ""
		if (not item_name): 
			item_name = str(item.proto)
			desc = " # " + item.description
		lines.append("{}item = utils_item.item_create_in_inventory({}, obj){}".format(prefix, item_name, desc))
		item_quantity = item.obj_get_int(toee.obj_f_item_quantity)
		if (item_quantity > 1):
			lines.append("{}if (item): item.obj_set_int(toee.obj_f_item_quantity, {})".format(prefix, item_quantity))

	return