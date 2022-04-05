import toee, utils_item, const_proto_list_scrolls, const_proto_list_wands, const_proto_scrolls, const_proto_wands

def san_dialog(attachee, triggerer):
	triggerer.begin_dialog(attachee, 1200)
	return toee.SKIP_DEFAULT