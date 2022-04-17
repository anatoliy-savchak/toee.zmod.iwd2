import toee, templeplus.pymod, tpdp, debug, sys, traceback

###################################################

def GetConditionName():
	return "Bag_Of_Holding"

print("Registering " + GetConditionName())
###################################################

PROTO_CONTAINER_BAG_OF_HOLDING = 1400

def get_item(attachee, args):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	inv_idx = args.get_arg(2)
	item = attachee.inventory_item(inv_idx)
	if (not item):
		print("not item for attachee: {}, inv_idx: {}".format(attachee, inv_idx))
		debug.breakp("not item")
	return item

def items_get(npc):
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
		if ((otype == toee.obj_t_npc) or (otype == toee.obj_t_pc)):
			for i in range(toee.item_wear_helmet, toee.item_wear_lockpicks):
				item = npc.item_worn_at(i)
				assert isinstance(item, toee.PyObjHandle)
				if (item and not item in result and not (item.item_flags_get() & toee.OIF_NO_LOOT)):
					result.append(item)

		for i in range(0, 199):
			item = npc.inventory_item(i)
			if (item and not item in result and not (item.item_flags_get() & toee.OIF_NO_LOOT)):
				print(item)
				result.append(item)
				numItems -= 1
			if (numItems <=0): break
	#print(result)
	return result

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

def make_chest(attachee, args):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	inv_idx = args.get_arg(2)
	item = get_item(attachee, args)
	prev_chest = FindChest()
	if (prev_chest): prev_chest.destroy()
	chest = toee.game.obj_create(PROTO_CONTAINER_BAG_OF_HOLDING, attachee.location)
	chest.obj_set_int(toee.obj_f_container_pad_i_1, inv_idx)
	if (args.get_param(0)):
		chest.container_flag_set(toee.OPF_NEVER_LOCKED)
	
	if (item):
		desc_id = item.obj_get_int(25) #obj_f_description_correct
		if (desc_id):
			chest.obj_set_int(25, desc_id)

		icon_id = item.obj_get_int(toee.obj_f_item_inv_aid)
		if (icon_id):
			chest.obj_set_int(toee.obj_f_aid, icon_id)
	chest.object_flag_set(toee.OF_DONTDRAW)
	chest.move(attachee.location)
	#chest.obj_set_obj(toee.obj_f_container_notify_npc, attachee)
	return chest

Bag_Of_Holding_Support = "Bag_Of_Holding_Support"

def Bag_Of_Holding_OnBuildRadialMenuEntry(attachee, args, evt_obj):
	assert isinstance(args, tpdp.EventArgs)
	try:
		item = get_item(attachee, args)
		#print("Bag_Of_Holding_OnBuildRadialMenuEntry item: {}".format(item))
		inv_idx = args.get_arg(2)
		item_name = "Bag of Holding"
		if (item): item_name = item.description

		radial_parent = tpdp.RadialMenuEntryParent(item_name)
		radial_parent_id = radial_parent.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)

		radial_action = tpdp.RadialMenuEntryPythonAction("Inventory", toee.D20A_PYTHON_ACTION, 3006, inv_idx, "TAG_INTERFACE_HELP")
		#assert isinstance(radial_action, tpdp.RadialMenuEntryParent)
		radial_action.add_as_child(attachee, radial_parent_id)
		#radial_action.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)

		radial_action = tpdp.RadialMenuEntryPythonAction("Examine bodies", toee.D20A_PYTHON_ACTION, 3007, inv_idx, "TAG_INTERFACE_HELP")
		#assert isinstance(radial_action, tpdp.RadialMenuEntryParent)
		#radial_action.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)
		radial_action.add_as_child(attachee, radial_parent_id)

		radial_action = tpdp.RadialMenuEntryPythonAction("Transfer from bodies", toee.D20A_PYTHON_ACTION, 3008, inv_idx, "TAG_INTERFACE_HELP")
		#assert isinstance(radial_action, tpdp.RadialMenuEntryParent)
		#radial_action.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)
		radial_action.add_as_child(attachee, radial_parent_id)

		radial_action = tpdp.RadialMenuEntryPythonAction("List contents", toee.D20A_PYTHON_ACTION, 3009, inv_idx, "TAG_INTERFACE_HELP")
		#assert isinstance(radial_action, tpdp.RadialMenuEntryParent)
		#radial_action.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)
		radial_action.add_as_child(attachee, radial_parent_id)

		radial_action = tpdp.RadialMenuEntrySlider("Min worth", "Min worth x50 when transfering - {}".format(item_name), 0, 20, "TAG_INTERFACE_HELP")
		radial_action.link_to_args(args, 1)
		#assert isinstance(radial_action, tpdp.RadialMenuEntryParent)
		#radial_action.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)
		radial_action.add_as_child(attachee, radial_parent_id)

		if (0):
			radial_action = tpdp.RadialMenuEntryPythonAction("Autosell", toee.D20A_PYTHON_ACTION, 3013, inv_idx, "TAG_INTERFACE_HELP")
			#assert isinstance(radial_action, tpdp.RadialMenuEntryParent)
			#radial_action.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)
			radial_action.add_as_child(attachee, radial_parent_id)
	except Exception, e:
		print "Bag_Of_Holding_OnBuildRadialMenuEntry:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return 0

def check_approp_bag(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)

	menu_idx_inv = evt_obj.d20a.data1
	inv_idx = args.get_arg(2)
	if (inv_idx != menu_idx_inv):
		print("Bag_Of_Holding_OnD20PythonActionPerform_... wrong item menu_idx_inv: {}, inv_idx: {}".format(menu_idx_inv, inv_idx))
		return False

	for pc in toee.game.party:
		pc.condition_add(Bag_Of_Holding_Support)
	return True

def Bag_Of_Holding_OnD20PythonActionPerform_inventory(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	#debug.breakp("Lodged_Quills_OnD20PythonActionPerform start")
	try:
		if not check_approp_bag(attachee, args, evt_obj):
			return 0

		chest = make_chest(attachee, args)
		print("Bag_Of_Holding_OnD20PythonActionPerform_inventory chest: {}, critter: {}".format(chest, attachee))
		attachee.anim_goal_use_object(chest)
	except Exception, e:
		print "Bag_Of_Holding_OnD20PythonActionPerform_inventory:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return 1

def Bag_Of_Holding_OnD20PythonActionPerform_examine_bodies(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	#debug.breakp("Lodged_Quills_OnD20PythonActionPerform start")
	try:
		if not check_approp_bag(attachee, args, evt_obj):
			return 0

		print("Bag_Of_Holding_OnD20PythonActionPerform_3007")
		for body in toee.game.obj_list_range(attachee.location, 20, toee.OLC_NPC):
			hp = body.stat_level_get(toee.stat_hp_current)
			print("{} hp in {}".format(hp, body))
			if (hp >= 0): continue
			if (not attachee.can_see(body)): 
				attachee.turn_towards(body)
				if (not attachee.can_see(body)):
					if (attachee.distance_to(body) > 15):
						continue
			items = items_get(body)
			#items = body.inventory_items()
			skip_item = 0
			skip_item_price = args.get_arg(1) * 50
			print("skip_item_price: {}".format(skip_item_price))
			#print("items: {}".format(len(items)))
			if (items):
				for item in items:
					assert isinstance(item, toee.PyObjHandle)
					text = item.description
					#print("{}: {}".format(text, body))
					color = toee.tf_yellow
					tpe = item.type
					is_idenified = item.item_flags_get() & toee.OIF_IDENTIFIED
					skip_item = 0
					if ((tpe >= toee.obj_t_weapon) and (tpe <= toee.obj_t_armor)):
						if (item.item_flags_get() & toee.OIF_IS_MAGICAL): 
							color = toee.tf_blue
							if (not is_idenified):
								if (tpe == toee.obj_t_weapon): text = "Magic Weapon"
								elif (tpe == toee.obj_t_armor): text = "Magic Armor"
								else: text = "Magic Item"
						skip_item = 0
						if skip_item_price > 0:
							mult = 1
							if tpe == toee.obj_t_ammo: mult = item.obj_get_int(toee.obj_f_ammo_quantity)
							else: mult = item.obj_get_int(toee.obj_f_item_quantity)
							worth = int(mult  * item.obj_get_int(toee.obj_f_item_worth) // 100)
							if worth < skip_item_price:
								skip_item = 1
							print("{} {} ? {} = SKIP: {}".format(text, worth, skip_item_price, skip_item))
					elif ((tpe == toee.obj_t_food) or (tpe == toee.obj_t_scroll) or (tpe == toee.obj_t_generic)):
						color = toee.tf_green
						if (not is_idenified):
							if (tpe == toee.obj_t_scroll): text = "Magic Scroll"
							elif (tpe == toee.obj_t_food and item.obj_get_int(toee.obj_f_category) == 4): text = "Magic Potion"
					elif ((tpe == toee.obj_t_key) or (tpe == toee.obj_t_written) or (tpe == toee.obj_t_money)):
						color = toee.tf_light_blue

					skip_item_text = "" if not skip_item else ". SKIPPED!"
					body.float_text_line(text+skip_item_text, color)

					weight = item.obj_get_int(toee.obj_f_item_weight)
					text = "*. {}. {} lb{}\n".format(text, weight, skip_item_text)
					toee.game.create_history_freeform(text)
	except Exception, e:
		print "Bag_Of_Holding_OnD20PythonActionPerform_3007:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return 1

def Bag_Of_Holding_OnD20PythonActionPerform_transfer_from_bodies(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	#debug.breakp("Lodged_Quills_OnD20PythonActionPerform start")
	try:
		if not check_approp_bag(attachee, args, evt_obj):
			return 0
		#debug.breakp("Bag_Of_Holding_OnD20PythonActionPerform")
		chest = make_chest(attachee, args)
		# force load
		chest.object_script_execute(attachee, 0x01) #sn_use
		modified = 0
		for body in toee.game.obj_list_range(attachee.location, 20, toee.OLC_NPC):
			hp = body.stat_level_get(toee.stat_hp_current)
			print("{} hp in {}".format(hp, body))
			if (hp >= 0): continue
			if (not attachee.can_see(body)): 
				attachee.turn_towards(body)
				if (not attachee.can_see(body)):
					if (attachee.distance_to(body) > 15):
						continue
			items = items_get(body)
			#items = body.inventory_items()
			transfer_to_self = 0
			skip_item = 0
			skip_item_price = args.get_arg(1) * 50
			print("skip_item_price: {}".format(skip_item_price))
			#print("items: {}".format(len(items)))
			if (items):
				for item in items:
					assert isinstance(item, toee.PyObjHandle)
					transfer_to_self = 0
					text = item.description
					print("{}: {}".format(text, body))
					color = toee.tf_yellow
					tpe = item.type
					is_idenified = item.item_flags_get() & toee.OIF_IDENTIFIED
					if ((tpe >= toee.obj_t_weapon) and (tpe <= toee.obj_t_armor)):
						if (item.item_flags_get() & toee.OIF_IS_MAGICAL): 
							color = toee.tf_blue
							if (not is_idenified):
								if (tpe == toee.obj_t_weapon): text = "Magic Weapon"
								elif (tpe == toee.obj_t_armor): text = "Magic Armor"
								else: text = "Magic Item"
						skip_item = 0
						if skip_item_price > 0:
							mult = 1
							if tpe == toee.obj_t_ammo: mult = item.obj_get_int(toee.obj_f_ammo_quantity)
							else: mult = item.obj_get_int(toee.obj_f_item_quantity)
							worth = int(mult  * item.obj_get_int(toee.obj_f_item_worth) // 100)
							skip_item = worth < skip_item_price
					elif ((tpe == toee.obj_t_food) or (tpe == toee.obj_t_scroll) or (tpe == toee.obj_t_generic)):
						color = toee.tf_green
						if (not is_idenified):
							if (tpe == toee.obj_t_scroll): text = "Magic Scroll"
							elif (tpe == toee.obj_t_food and item.obj_get_int(toee.obj_f_category) == 4): text = "Magic Potion"
					elif ((tpe == toee.obj_t_key) or (tpe == toee.obj_t_written) or (tpe == toee.obj_t_money)):
						transfer_to_self = 1
						color = toee.tf_light_blue
					if (not modified):
						toee.game.create_history_freeform("Transferred:\n")

					skip_item_text = "" if not skip_item else ". SKIPPED!"
					body.float_text_line(text+skip_item_text, color)

					weight = item.obj_get_int(toee.obj_f_item_weight)
					measure_txt = ". {} lb".format(weight)
					if tpe == toee.obj_t_money:
						measure_txt = " {}".format(item.obj_get_int(toee.obj_f_money_quantity))

					text = "*. {}{}{}\n".format(text, measure_txt, skip_item_text)
					toee.game.create_history_freeform(text)
					if (transfer_to_self):
						attachee.item_get(item)
					elif skip_item_text:
						pass
					else:
						chest.item_get(item)
					modified = 1
		if (modified):
			toee.game.create_history_freeform("\n")
			# force save
			chest.object_script_execute(attachee, 0x20) #sn_transfer
		attachee.anim_goal_use_object(chest)
		#attachee.container_open_ui(bag)
	except Exception, e:
		print "Bag_Of_Holding_OnD20PythonActionPerform_3008:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return 1

def sell_modifier():
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

class ItemInfo:
	def __init__(self, item, worth, weight, text = None, name = None):
		assert isinstance(item, toee.PyObjHandle)
		assert isinstance(worth, int)
		assert isinstance(weight, int)
		assert isinstance(text, str)
		self.item = item
		self.worth = worth
		self.weight = weight
		self.text = text
		self.name = name
		self.ratio = worth
		if (weight):
			self.ratio = worth / weight
		return

def ItemInfo_compare_ratio(m1, m2):
	assert isinstance(m1, ItemInfo)
	assert isinstance(m2, ItemInfo)
	return m2.ratio - m1.ratio

def Bag_Of_Holding_OnD20PythonActionPerform_autosell(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	#debug.breakp("Lodged_Quills_OnD20PythonActionPerform start")
	try:
		if not check_approp_bag(attachee, args, evt_obj):
			return 0
		#debug.breakp("Bag_Of_Holding_OnD20PythonActionPerform")
		chest = make_chest(attachee, args)

		# force load
		chest.object_script_execute(attachee, 0x01) #sn_use
		toee.game.create_history_freeform("Bag of Holding contents:\n")
		items = items_get(chest)
		num = 0
		total_lb = 0
		total_gp = 0
		sm = sell_modifier()
		total_sell = 0.0
		for item in items:
			num +=1
			text = item.description
			worth0 = item.obj_get_int(toee.obj_f_item_worth)
			worth_gp = worth0 // 100
			total_gp += worth_gp
			total_sell += worth0 * sm
			worth_gp_sell = worth_gp * sm
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
		attachee.money_adj(total_sell_adj)
		print("attachee.money_adj: {}".format(total_sell_adj))
		# push fake event to let bag saving
		chest.object_script_execute(attachee, 0x20) #sn_transfer
		attachee.anim_goal_use_object(chest)
		#attachee.container_open_ui(bag)
	except Exception, e:
		print "Bag_Of_Holding_OnD20PythonActionPerform_list_bag:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return 1

def Bag_Of_Holding_OnD20PythonActionPerform_list_bag(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	#debug.breakp("Lodged_Quills_OnD20PythonActionPerform start")
	try:
		if not check_approp_bag(attachee, args, evt_obj):
			return 0
		#debug.breakp("Bag_Of_Holding_OnD20PythonActionPerform")
		chest = make_chest(attachee, args)
		# force load
		chest.object_script_execute(attachee, 0x01) #sn_use
		toee.game.create_history_freeform("Bag of Holding contents:\n")
		items = items_get(chest)
		num = 0
		total_lb = 0
		total_gp = 0
		sm = sell_modifier()
		total_gp_sell = 0.0
		lst = list()
		for item in items:
			num +=1
			weight = item.obj_get_int(toee.obj_f_item_weight)
			total_lb += weight
			text = item.description
			worth0 = item.obj_get_int(toee.obj_f_item_worth)
			worth_gp = worth0 // 100
			total_gp += worth_gp
			total_gp_sell += worth_gp * sm
			worth_gp_sell = worth_gp * sm
			x2 = ""
			x = item.obj_get_int(toee.obj_f_item_quantity)
			if (x > 1): x2 = " x{}".format(x)
			info = ItemInfo(item, worth_gp, weight)
			str_worth_gp_sell = "" if (worth_gp == int(worth_gp_sell)) else " (sell {})".format(int(worth_gp_sell))
			text = "{}.\n   {} lb. {} gp{}\n".format(text, weight, worth_gp, str_worth_gp_sell, int(info.ratio))
			name = "{}{}".format(num, text)
			info.text = text
			info.name = name
			lst.append(info)
			#toee.game.create_history_freeform(text)

		num = 0
		for info in sorted(lst, ItemInfo_compare_ratio):
			num +=1
			text = "{:02d}. {}".format(num, info.text)
			toee.game.create_history_freeform(text)

		if (num):
			toee.game.create_history_freeform("---------\n")
			text = "Total: {} lb, {} gp, sell: {} gp\n".format(total_lb, total_gp, int(total_gp_sell))
			toee.game.create_history_freeform(text)
		toee.game.create_history_freeform("\n")
		attachee.anim_goal_use_object(chest)
		#attachee.container_open_ui(bag)
	except Exception, e:
		print "Bag_Of_Holding_OnD20PythonActionPerform_3009:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return 1

def FindChest():
	for obj in toee.game.obj_list_vicinity(toee.game.leader.location, toee.OLC_CONTAINER):
		if (obj.proto == PROTO_CONTAINER_BAG_OF_HOLDING and not obj.object_flags_get() & toee.OF_DESTROYED):
			return obj
	return None

def Bag_Of_Holding_S_Inventory_Update(attachee, args, evt_obj):
	chest = FindChest()
	print("Bag_Of_Holding_S_Inventory_Update attachee: {}, chest: {}".format(attachee, chest))
	#debug.breakp("Bag_Of_Holding_S_Inventory_Update")
	if (not chest): return 0
	#target = attachee #did not work
	target = toee.game.leader
	#npc = chest.obj_get_obj(toee.obj_f_container_notify_npc)
	#if (npc and (npc.type == toee.obj_t_pc or npc.type == toee.obj_t_npc)):
	#	target = npc
	chest.object_script_execute(target, 0x20) #sn_transfer
	
	# check if Bag_Of_Holding_timed_destroy started running
	if (not chest.object_flags_get() & toee.OF_INVISIBLE):
		chest.object_flag_set(toee.OF_INVISIBLE)
		chest.object_flag_set(toee.OF_DONTDRAW)
		Bag_Of_Holding_timed_destroy(chest, 1000)
	return 0

def Bag_Of_Holding_timed_destroy(chest, time):
	assert isinstance(chest, toee.PyObjHandle)
	toee.game.timevent_add(_Bag_Of_Holding_destroy_on_timeevent, (chest), time) # 1000 = 1 second
	return

def _Bag_Of_Holding_destroy_on_timeevent(chest):
	assert isinstance(chest, toee.PyObjHandle)
	#print("_Bag_Of_Holding_destroy_on_timeevent toee.game.char_ui_display_type: {}".format(toee.game.char_ui_display_type))
	if (not chest.object_flags_get() & toee.OF_DESTROYED):
		is_invetory_screen_opened = 0
		if ("char_ui_display_type" in dir(toee.game)):
			is_invetory_screen_opened = toee.game.char_ui_display_type

		#is_invetory_screen_opened = 0
		if (not is_invetory_screen_opened):
			print("Bag_Of_Holding_S_Inventory_Update destroying bag {}".format(chest))
			chest.destroy()
		else:
			Bag_Of_Holding_timed_destroy(chest, 1000)
	return 1

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # 0 - type, 1 - min value, 2 - invIdx
modObj.AddHook(toee.ET_OnBuildRadialMenuEntry, toee.EK_NONE, Bag_Of_Holding_OnBuildRadialMenuEntry, ())
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3006, Bag_Of_Holding_OnD20PythonActionPerform_inventory, ())
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3007, Bag_Of_Holding_OnD20PythonActionPerform_examine_bodies, ())
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3008, Bag_Of_Holding_OnD20PythonActionPerform_transfer_from_bodies, ())
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3009, Bag_Of_Holding_OnD20PythonActionPerform_list_bag, ())
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3013, Bag_Of_Holding_OnD20PythonActionPerform_autosell, ())
#modObj.AddHook(toee.ET_OnD20Signal, toee.EK_S_Inventory_Update, Bag_Of_Holding_S_Inventory_Update, ())

modObj2 = templeplus.pymod.PythonModifier(Bag_Of_Holding_Support, 2) # 
modObj2.AddHook(toee.ET_OnD20Signal, toee.EK_S_Inventory_Update, Bag_Of_Holding_S_Inventory_Update, ())