from tkinter.tix import Tree
import common
import os
import re

"""
How to create a gem:
Given: gem_name, gem_icon_name, gem_value, gem_desc
1. Produce inventory icon (gem_inventory_id) in toee from gem_icon_name:
    a. Look for gem_bam (png) file from gem_icon_name. There are many for some reason, pick largest by file size.
    b. Convert gem_bam into gem_tga.
    c. Copy into core\art\interface\Inventory 
    d. open inventory.mes and decide new gem_inventory_id
    e. save result into inventory.json for further lookups and produce of inventory.mes
2. Look for available proto_id => gem_proto_id
3. Take gem template, replace proto fields and store into protos.json
4. Store proto_id as const into the lookup. Also save producer class for that one.
"""
class ProduceProtos(object):
    def __init__(self, app):
        self.app = app
        self.protos_index = dict()
        return

    def build_index(self):
        for fp in self.app.list_protos_filesy():
            self.parse_proto_for_index(fp)
        return

    def parse_proto_for_index(self, file_path: str):
        with open(file_path, 'r') as f:
            for line in f:
                if not line: continue
                values = line.split('\t', 24)
                if len(values) < 24: 
                    continue
                proto = int(values[0])
                proto_type = values[1]
                proto_desc_id = values[23]
                self.protos_index[proto] = common.tDict(proto = proto, proto_type = proto_type, proto_desc_id = proto_desc_id, file_path = file_path, content = line)
        return

    def find_unused_proto(self, obj_type_range_start_proto: int):
        for i in range(obj_type_range_start_proto + 1, obj_type_range_start_proto + 1000):
            proto_rec = self.protos_index.get(i)
            if not proto_rec:
                return i
        return

    def create_proto_item(self, proto: int, icon_id: int, price_gp: int, base_proto: int):
        
        tabbed = self.protos_index[base_proto]["content"].split('\t')
        tabbed[0] = str(proto)
        tabbed[52] = str(price_gp*100) # obj_f_item_worth
        tabbed[22] = str(proto) #obj_f_name
        tabbed[23] = str(proto) #obj_f_description
        tabbed[53] = str(icon_id) #obj_f_item_inv_aid
        tabbed[55] = ""
        return tabbed

    def save_proto_files(self, proto: int, tabbed: list, title: str, utitle: str, name: str, long_description: str, proto_type: str = "", save: bool = True):
        prefix_ = "" if not proto_type else proto_type + "_"
        title_ = re.sub('\W|^(?=\d)','_', title)
        proto_stem = f'{prefix_}{proto}_{title_}_iwd2_{name.lower()}'
        proto_fn = proto_stem + '.tab'
        proto_path = os.path.join(self.app.core_dir, "rules","protos", proto_fn)
        result = {"proto": proto, "title": title, "title_name": title_, "proto_stem": proto_stem, "proto_fn": proto_fn, "proto_path": proto_path}

        uproto = None
        if title:
            if utitle:
                uproto = proto + 20000
                tabbed[55] = str(uproto) #obj_f_item_description_unknown
            desc_fn = proto_stem + '.mes'
            desc_path = os.path.join(self.app.core_dir, "mes","description", desc_fn)
            if save:
                with open(desc_path, 'w') as f:
                    f.write(f'{{{proto}}}{{{title}}}')
                    if utitle:
                        f.write(f'\n{{{uproto}}}{{{utitle}}}')
            result["desc_fn"] = desc_fn
            result["desc_path"] = desc_path

        if long_description:
            desc_fn = proto_stem + '.mes'
            desc_path = os.path.join(self.app.core_dir, "mes","long_descr", desc_fn)
            if save:
                with open(desc_path, 'w') as f:
                    f.write(f'{{{proto}}}{{{long_description}}}')
            result["long_desc_fn"] = desc_fn
            result["long_desc_path"] = desc_path

        if save:
            with open(proto_path, 'w') as f:
                f.write('\t'.join(tabbed))

        self.protos_index[proto] = common.tDict(proto = proto, proto_type = proto_type, proto_desc_id = proto, file_path = proto_path, uproto = uproto)
        return result