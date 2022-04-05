import toee, utils_item, const_proto_list_items, const_proto_list_potions

def san_dialog(attachee, triggerer):
	triggerer.begin_dialog(attachee, 1500)
	return toee.SKIP_DEFAULT