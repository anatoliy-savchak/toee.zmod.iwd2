import toee, utils_item, const_proto_list_weapons, const_proto_list_weapons_masterwork, const_proto_list_weapons_magic

def san_dialog(attachee, triggerer):
	triggerer.begin_dialog(attachee, 1000)
	return toee.SKIP_DEFAULT