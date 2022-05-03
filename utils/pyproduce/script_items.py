"""
MANUAL
"""
import produce_icon
import produce_proto
import common
import proto_file
import re
import os
import copy

def process(producer_app):
    ProtoBuilderItem(producer_app).copy_from_proto(12036).update_from_item("00Gem02").set_proto(12710).save()
    ProtoBuilderItem(producer_app).copy_from_proto(9000).update_from_item("10Vellum").set_proto(12711).set_field(proto_file.idx_obj_f_item_flags, "OIF_IS_MAGICAL OIF_NO_DECAY").save()
    return

def process_item_generic(name, producer_app, icons, protos, obj_type_range_start_proto, proto, base_proto, save = True):
    proto0 = proto
    if proto0 < 0: save = False
    itm = producer_app.get_itm(name)
    icon_name = itm["InventoryIcon"]
    icon_id = icons.find_icon_id(icon_name)
    if not icon_id:
        icon_id = icons.produce_icon(icon_name)

    if proto < 0:
        new_proto = protos.find_unused_proto(obj_type_range_start_proto)
        proto = new_proto

    if itm and proto > 0:
        title = common.text_of_strrefs(itm, "IdentifiedName", "UnidentifiedName")
        utitle = common.text_of_strrefs(itm, "UnidentifiedName")
        description = common.text_of_strrefs(itm, "IdentifiedDescription")
        price_gp = int(itm["Price"])
        tabbed = protos.create_proto_item(proto, icon_id, price_gp, base_proto)
        obj_type_name = "obj_t_generic"
        rec = protos.save_proto_files(proto, tabbed, title, utitle, name, description, obj_type_name, save)
        const_line = f'PROTO_{obj_type_name.replace("obj_t_", "").upper()}_{rec["title_name"].upper()} = {proto} # Cost: {price_gp} gp; {name}'
        print(f"proto: {proto}")
        print(const_line)
        if proto0 < 0:
            raise Exception("Setup proto!")
    return

class ProtoBuilder(object):
    def __init__(self, app, obj: dict = None):
        self.app = app
        self.tabbed = dict()
        self.proto = -1
        self.obj = obj
        self.object_type_str = None
        self.proto_code_name = None
        self.proto_file_stem = None
        self.proto_file_name = None
        self.proto_file_path = None
        return

    def copy_from_proto(self, src_proto: int):
        tabbed = self.app.protos.protos_index[src_proto]["content"].split('\t')
        if tabbed:
            self.tabbed = copy.deepcopy(tabbed)
            self.tabbed[0] = str(self.proto)
            self.object_type_str = self.tabbed[proto_file.idx_obj_type]
            self.tabbed[proto_file.idx_obj_f_name] = ""
        return self

    def _update_file_names(self):
        return

    def set_field(self, field_idx: int, value: str):
        self.tabbed[field_idx] = value
        return self

class ProtoBuilderItem(ProtoBuilder):
    def __init__(self, app, obj: dict = None):
        super().__init__(app, obj)
        self.item_description = None
        self.item_udescription = None
        self.item_udescription_id = None
        self.item_long_description = None
        self.item_long_udescription = None
        self.icon_id = None

        return

    def _update_file_names(self, proto_override: int = None):
        if not proto_override: proto_override = self.proto
        self.proto_code_name = title_ = re.sub('\W|^(?=\d)','_', self.item_description)
        self.proto_file_stem = f'{self.object_type_str}_{proto_override}_{self.proto_code_name}_iwd2_{self.proto_code_name.lower()}'
        self.proto_file_name = self.proto_file_stem + '.tab'
        self.proto_file_path = os.path.join(self.app.core_dir, "rules","protos", self.proto_file_name)

        self.item_udescription_id = proto_override + 20000
        self.tabbed[proto_file.idx_obj_f_item_description_unknown] = str(self.item_udescription_id) if self.item_udescription else ""

        self.tabbed[proto_file.idx_obj_f_description] = str(proto_override) if self.item_udescription else ""
        return

    def update_from_item(self, item_name: str, elicit_icon: bool = True):
        self.obj = self.app.get_itm(item_name)
        icon_name = self.obj["InventoryIcon"]
        if elicit_icon:
            self.icon_id = self.app.icons.find_icon_id(icon_name)
            if not self.icon_id:
                self.icon_id = self.app.icons.produce_icon(icon_name)
            if self.icon_id > 0:
                self.tabbed[proto_file.idx_obj_f_item_inv_aid] = str(self.icon_id)

        self.item_description = common.text_of_strrefs(self.obj, "IdentifiedName", "UnidentifiedName")

        self.item_udescription = common.text_of_strrefs(self.obj, "UnidentifiedName")

        self.item_long_description = common.text_of_strrefs(self.obj, "IdentifiedDescription", "UnidentifiedDescription")
        self.item_long_udescription = common.text_of_strrefs(self.obj, "UnidentifiedDescription")
        self._update_file_names()
        return self

    def set_proto(self, new_proto: int, obj_type_range_start_proto: int = None):
        if new_proto is None or new_proto <= 0:
            if obj_type_range_start_proto is None:
                raise Exception("obj_type_range_start_proto must be provided if proto: -1!")
            new_proto = self.app.protos.find_unused_proto(obj_type_range_start_proto)
            self._update_file_names(new_proto)
            raise Exception("Write this and call again with correct proto!")
        self.proto = new_proto
        self.tabbed[0] = str(self.proto)
        self._update_file_names()
        return self

    def save(self):
        if self.proto is None or self.proto <=0:
            raise Exception("Incorrect proto!")

        if self.item_description:
            desc_fn = self.proto_file_stem + '.mes'
            desc_path = os.path.join(self.app.core_dir, "mes","description", desc_fn)
            with open(desc_path, 'w') as f:
                f.write(f'{{{self.proto}}}{{{self.item_description}}}')
                if self.item_udescription:
                    f.write(f'\n{{{self.item_udescription_id}}}{{{self.item_udescription}}}')

        if self.item_long_description:
            desc_fn = self.proto_file_stem + '.mes'
            desc_path = os.path.join(self.app.core_dir, "mes","long_descr", desc_fn)
            with open(desc_path, 'w') as f:
                f.write(f'{{{self.proto}}}{{{self.item_long_description}}}')

        content = '\t'.join(self.tabbed)
        with open(self.proto_file_path, 'w') as f:
            f.write(content)

        self.app.protos.protos_index[self.proto] = common.tDict(proto = self.proto, proto_type = self.object_type_str
            , proto_desc_id = self.proto, file_path = self.proto_file_path, uproto = self.item_udescription_id
            , content = content)

        return