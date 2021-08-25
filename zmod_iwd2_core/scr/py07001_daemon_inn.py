import toee, debug, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee, ctrl_daemon
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import startup_zmod, utils_sneak, monster_info, copy, rttoee_consts, const_animate, const_sceneries
import const_proto_items, const_proto_cloth, const_proto_rings

INN = "inn"
INN_DAEMON_SCRIPT = 7001
INN_DAEMON_ID = "G_B068EF18_1DF2_4EC0_9416_754227FBD7CC"
INN_DAEMON_DIALOG = 7001


def cs():
	return ctrl_daemon2.ccs(INN_DAEMON_ID, CtrlInn)

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, rttoee_consts.MAP_ID_INN, CtrlInn)

def san_first_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_INN, CtrlInn)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_INN, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, rttoee_consts.MAP_ID_INN, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, rttoee_consts.MAP_ID_INN, cs())

class CtrlInn(ctrl_daemon2.CtrlDaemon2):
	def __init__(self):
		super(CtrlInn, self).__init__()
		self.init_daemon2_fields(rttoee_consts.MAP_ID_INN, INN_DAEMON_SCRIPT, INN)
		return

	def place_encounters_initial(self):
		self.place_staff()
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
