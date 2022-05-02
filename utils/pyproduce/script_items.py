"""
MANUAL
"""
import produce_icon
import produce_proto
import common

def process(producer_app):
    icons = produce_icon.ProduceIcons(producer_app)
    icons.load_index()
    protos = produce_proto.ProduceProtos(producer_app)
    protos.build_index()

    name = "00Gem02"
    proto = 12710
    save = True
    obj_type_range_start_proto = 12709
    #process_item_generic(name, producer_app, icons, protos, obj_type_range_start_proto, proto, save)
    return

def process_item_generic(name, producer_app, icons, protos, obj_type_range_start_proto, proto, save):
    itm = producer_app.get_itm(name)
    icon_name = itm["InventoryIcon"]
    icon_id = icons.find_icon_id(icon_name)
    if not icon_id:
        icon_id = icons.produce_icon("IMISC17")

    if proto < 0:
        new_proto = protos.find_unused_proto(obj_type_range_start_proto)
        proto = new_proto
    if itm and proto > 0:
        title = common.text_of_strrefs(itm, "IdentifiedName", "UnidentifiedName")
        description = common.text_of_strrefs(itm, "IdentifiedDescription")
        price_gp = int(itm["Price"])
        tabbed = protos.create_proto_gem(proto, icon_id, price_gp)
        obj_type_name = "obj_t_generic"
        rec = protos.save_proto_files(proto, tabbed, title, name, description, obj_type_name, save)
        const_line = f'PROTO_{obj_type_name.replace("obj_t_", "").upper()}_{rec["title_name"].upper()} = {proto} # Cost: {price_gp} gp; {name}'
        print(f"proto: {proto}")
        print(const_line)
    return

