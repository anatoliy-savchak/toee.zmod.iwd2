"""
MANUAL
"""
import produce_icon
import produce_proto
import common
from proto_file import *
import re
import os
import copy

def process(producer_app):
    ProtoBuilderItem(producer_app).cfp(12036).ufi("00Gem02").sp(12710).save()
    ProtoBuilderItem(producer_app).cfp(9000).ufi("10Vellum").sp(12711).sf(idx_obj_f_item_flags, "OIF_IS_MAGICAL OIF_NO_DECAY").save()
    ProtoBuilderItem(producer_app).cfp(9000).ufi("10GenCrW").sp(12712, 12711).sf(idx_int32_two_fields, "12083").save()
    return

class ProtoBuilder(object):
    def __init__(self, app, obj: dict = None):
        self.app = app
        self.tabbed = dict()
        self.proto = -1
        self.obj = obj
        self.obj_name = None
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
            self.object_type_str = self.tabbed[idx_obj_type]
            self.tabbed[idx_obj_f_name] = ""
        return self

    def cfp(self, src_proto: int):
        return self.copy_from_proto(src_proto)

    def _update_file_names(self):
        return

    def set_field(self, field_idx: int, value: str):
        self.tabbed[field_idx] = value
        return self

    def sf(self, field_idx: int, value: str):
        return self.set_field(field_idx, value)

    def get_field(self, field_idx: int):
        return self.tabbed[field_idx]

    def gf(self, field_idx: int):
        return self.get_field(field_idx)

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
        self.tabbed[idx_obj_f_item_description_unknown] = str(self.item_udescription_id) if self.item_udescription else ""

        self.tabbed[idx_obj_f_description] = str(proto_override) if self.item_udescription else ""
        return

    def update_from_item(self, item_name: str, elicit_icon: bool = True):
        self.obj = self.app.get_itm(item_name)
        self.obj_name = item_name
        icon_name = self.obj["InventoryIcon"]
        if elicit_icon:
            self.icon_id = self.app.icons.find_icon_id(icon_name)
            if not self.icon_id:
                self.icon_id = self.app.icons.produce_icon(icon_name)
            if self.icon_id > 0:
                self.tabbed[idx_obj_f_item_inv_aid] = str(self.icon_id)

        self.item_description = common.text_of_strrefs(self.obj, "IdentifiedName", "UnidentifiedName")

        self.item_udescription = common.text_of_strrefs(self.obj, "UnidentifiedName")

        self.item_long_description = common.text_of_strrefs(self.obj, "IdentifiedDescription", "UnidentifiedDescription")
        self.item_long_udescription = common.text_of_strrefs(self.obj, "UnidentifiedDescription")
        self._update_file_names()
        return self

    def ufi(self, item_name: str, elicit_icon: bool = True):
        return self.update_from_item(item_name, elicit_icon)

    def set_proto(self, new_proto: int, obj_type_range_start_proto: int = None):
        if new_proto is None or new_proto <= 0:
            if obj_type_range_start_proto is None:
                raise Exception("obj_type_range_start_proto must be provided if proto: -1!")
            new_proto = self.app.protos.find_unused_proto(obj_type_range_start_proto)
            self._update_file_names(new_proto)
            self.print_const(new_proto)
            raise Exception("Write this and call again with correct proto!")
        self.proto = new_proto
        self.tabbed[0] = str(self.proto)
        self._update_file_names()
        return self

    def sp(self, new_proto: int, obj_type_range_start_proto: int = None):
        return self.set_proto(new_proto, obj_type_range_start_proto)

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

    def print_const(self, proto: int = None):
        if not proto: proto = self.proto
        const_line = f'PROTO_{self.object_type_str.replace("obj_t_", "").upper()}_{self.proto_code_name.upper()} = {proto} # Cost: {self.gf(idx_obj_f_item_worth)} gp; {self.obj_name}'
        print(f"proto: {proto}")
        print(const_line)
        return