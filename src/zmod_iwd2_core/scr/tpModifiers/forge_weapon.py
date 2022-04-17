import toee, templeplus.pymod, sys, tpdp, math, traceback, debug, debugg
import const_proto_weapon, const_proto_list_weapons, const_proto_list_weapons_masterwork, const_toee, const_proto_map_weapons, const_proto_map_armor, utils_pc, utils_obj
import json

###################################################

def GetConditionName():
	return "Forge_Weapon"

print("Registering " + GetConditionName())
###################################################

PA_FORGE = 3021
def Forge_Weapon_OnBuildRadialMenuEntry(attachee, args, evt_obj):
	try:
		def do_group3(name, parent_id, protos_map):
			assert isinstance(protos_map, dict)
			group = tpdp.RadialMenuEntryParent(name)
			group_id = group.add_as_child(attachee, parent_id)
			for proto in protos_map:
				map = protos_map.get(proto) # PROTO_WEAPON_DAGGER_MAP = {"proto": const_proto_weapon.PROTO_WEAPON_DAGGER, "xp": 0, "mwproto": const_proto_weapon.PROTO_WEAPON_DAGGER_MASTERWORK, "wmxp": 0, "q": 1}
				item = toee.game.getproto(proto)
				item_group = tpdp.RadialMenuEntryParent(item.description)
				item_group_id = item_group.add_as_child(attachee, group_id)

				quantity = map.get("q")
				if (not quantity): quantity = 1
				quantity_str = " (x{})".format(quantity) if (quantity > 1) else ""
				materials_cost = item.obj_get_int(toee.obj_f_item_worth) * quantity // 2 
				xp_cost = map["xp"]
				xp_cost_str = ", {} xp".format(xp_cost) if (xp_cost) else ""
				text = "Normal {}{}{}".format(utils_obj.money_to_str(materials_cost), xp_cost_str, quantity_str)
				raf = tpdp.RadialMenuEntryPythonAction(text, toee.D20A_PYTHON_ACTION, PA_FORGE, proto*10, "TAG_INTERFACE_HELP")
				raf.add_as_child(attachee, item_group_id)

				wm_proto = map.get("mwp")
				if (wm_proto):
					mw_item = toee.game.getproto(wm_proto)
					materials_cost = mw_item.obj_get_int(toee.obj_f_item_worth) * quantity // 2 
					xp_cost = map["mwxp"]
					xp_cost_str = ", {} xp".format(xp_cost) if (xp_cost) else ""
					text = "Masterwork {}{}".format(utils_obj.money_to_str(materials_cost), xp_cost_str, quantity_str)
					wm_raf = tpdp.RadialMenuEntryPythonAction(text, toee.D20A_PYTHON_ACTION, PA_FORGE, proto*10 + 1, "TAG_INTERFACE_HELP")
					wm_raf.add_as_child(attachee, item_group_id)

				# mithril
				wm_proto = map.get("mip")
				if (wm_proto):
					mw_item = toee.game.getproto(wm_proto)
					materials_cost = mw_item.obj_get_int(toee.obj_f_item_worth) * quantity // 2 
					xp_cost = map["mixp"]
					xp_cost_str = ", {} xp".format(xp_cost) if (xp_cost) else ""
					text = "Mithril {}{}".format(utils_obj.money_to_str(materials_cost), xp_cost_str, quantity_str)
					wm_raf = tpdp.RadialMenuEntryPythonAction(text, toee.D20A_PYTHON_ACTION, PA_FORGE, proto*10 + 2, "TAG_INTERFACE_HELP")
					wm_raf.add_as_child(attachee, item_group_id)
			return group_id

		raf_weapon = tpdp.RadialMenuEntryParent("Forge Weapon")
		raf_weapon_id = raf_weapon.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Skills)
		
		do_group3("Simple", raf_weapon_id, const_proto_map_weapons.PROTOS_WEAPON_SIMPLE_MAP)
		do_group3("Martial", raf_weapon_id, const_proto_map_weapons.PROTOS_WEAPON_MARTIAL_MAP)
		do_group3("Exotic", raf_weapon_id, const_proto_map_weapons.PROTOS_WEAPON_EXOTIC_MAP)

		raf_armor = tpdp.RadialMenuEntryParent("Forge Armor")
		raf_armor_id = raf_armor.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Skills)
		do_group3("Light", raf_armor_id, const_proto_map_armor.PROTOS_ARMOR_LIGHT_MAP)
		do_group3("Medium", raf_armor_id, const_proto_map_armor.PROTOS_ARMOR_MEDIUM_MAP)
		do_group3("Heavy", raf_armor_id, const_proto_map_armor.PROTOS_ARMOR_HEAVY_MAP)

	except Exception, e:
		print "Forge_Weapon_OnBuildRadialMenuEntry:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return 0

def Forge_Weapon_OnD20PythonActionCheck(attachee, args, evt_obj):
	return 1

def Forge_Weapon_OnD20PythonActionPerform(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	print("Forge_Weapon_OnD20PythonActionPerform start")
	try:
		def do_error_message(text):
			attachee.float_text_line(text, toee.tf_red)
			print(text)
			return

		def do_fail_message(text):
			attachee.float_text_line(text, toee.tf_red)
			toee.game.create_history_freeform("\n" + text + "\n")
			print(text)
			return

		def do_message(text):
			attachee.float_text_line(text, toee.tf_yellow)
			toee.game.create_history_freeform("\n" + text + "\n")
			print(text)
			return

		proto_code = evt_obj.d20a.data1
		proto = proto_code // 10
		proto_subtype = proto_code - proto * 10
		map = const_proto_map_weapons.PROTOS_WEAPONS_MAP.get(proto)
		if (not map): 
			map = const_proto_map_armor.PROTOS_ARMOR_MAP.get(proto)
		print("{} {} {} = {}".format(proto_code, proto, proto_subtype, map))
		if (not map):
			do_error_message("Unknown item proto_code: {}".format(proto_code))
			return

		xp_cost = map["xp"]
		if (proto_subtype == 1):
			proto = map["mwp"]
			xp_cost = map["mwxp"]
		elif (proto_subtype == 2):
			proto = map["mip"]
			xp_cost = map["mixp"]

		quantity = map.get("q")
		if (not quantity): quantity = 1
		quantity_str = " (x{})".format(quantity) if (quantity > 1) else ""

		if (not proto):
			do_error_message("Unknown item proto_code: {}".format(proto_code))
			return

		item_proto = toee.game.getproto(proto)
		if (not item_proto):
			do_error_message("Unknown item proto: {}".format(proto))
			return 1

		if (xp_cost > 0):
			xp_surplus = utils_pc.pc_xp_surplus(attachee)
			if (xp_cost > xp_surplus):
				do_fail_message("Insufficient XP ({:,}) to create item ({:,} xp): {}!".format(xp_surplus, xp_cost, item_proto.description))
				return

		cost_cp = item_proto.obj_get_int(toee.obj_f_item_worth) // 2
		wealth = attachee.money_get()
		if (cost_cp > wealth):
			do_fail_message("Insufficient funds ({}) to create item ({}): {}!".format(utils_obj.money_to_str(wealth), utils_obj.money_to_str(cost_cp), item_proto.description))
			return 1

		item = toee.game.obj_create(proto, attachee.location)
		item.item_flag_set(toee.OIF_IDENTIFIED)
		attachee.item_get(item)

		if (cost_cp):
			attachee.money_adj(-cost_cp)
		if (xp_cost):
			attachee.obj_set_int(toee.obj_f_critter_experience, attachee.obj_get_int(toee.obj_f_critter_experience) - xp_cost)

		do_message("Spent {}, {:,} xp to forge: {}{}.".format(utils_obj.money_to_str(cost_cp), xp_cost, item.description, quantity_str))
	except Exception, e:
		print "Forge_Weapon_OnD20PythonActionPerform:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		#print "Inspect_OnD20PythonActionPerform error:", sys.exc_info()[0]
		#print(str(e))
		#debug.breakp("Lodged_Quills_OnD20PythonActionPerform error")
	return 1


modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # 
modObj.MapToFeat("Forge Weapon and Armor")
modObj.AddHook(toee.ET_OnBuildRadialMenuEntry, toee.EK_NONE, Forge_Weapon_OnBuildRadialMenuEntry, ())
modObj.AddHook(toee.ET_OnD20PythonActionCheck, PA_FORGE, Forge_Weapon_OnD20PythonActionCheck, ())
modObj.AddHook(toee.ET_OnD20PythonActionPerform, PA_FORGE, Forge_Weapon_OnD20PythonActionPerform, ())
