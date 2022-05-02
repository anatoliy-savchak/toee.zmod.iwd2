import os
import PIL
from PIL import Image
import common

class ProduceIcons(object):
    def __init__(self, app):
        self.app = app
        self.invenory_index = list()
        # {00666} {sigil.tga}
        self.icon_id_last = 666
        return

    @staticmethod
    def png_to_tga(src_path: str, dest_path: str):
        with Image.new("RGBA", (64, 64)) as oim:
            with Image.open(src_path) as im:
                alpha = im.split()[-1]
                oim.putalpha(1)
                dx = int((oim.size[0] - im.size[0]) / 2)
                dy = int((oim.size[1] - im.size[1]) / 2)
                oim.paste(im, (dx, dy))
            oim.save(dest_path, "TGA")
        #oim.close()
        return

    def produce_icon(self, icon_name: str, append_to_inventory_mes: bool = True, save_index: bool = True):
        dir = os.path.join(self.app.bam_dir, icon_name)

        prevsize = -1
        best_fn = None
        for fn in os.listdir(dir):
            if not fn.lower().endswith(".png"): continue
            fnp = os.path.join(dir, fn)
            size = os.path.getsize(fnp)
            if size > prevsize:
                best_fn = fnp
                prevsize = size
        dest_name = icon_name + ".tga"
        # D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\src\zmod_iwd2_core\art\interface\Inventory 
        dest_path = os.path.normpath(os.path.join(self.app.core_dir, "art", "interface", "Inventory", dest_name))
        self.png_to_tga(best_fn, dest_path)
        self.icon_id_last += 1
        rec = {"icon_name": icon_name, "icon_id": self.icon_id_last, "icon_file_name": dest_name, "icon_orig_name": os.path.basename(best_fn)}
        self.invenory_index.append(rec)

        if append_to_inventory_mes:
            inc_path = os.path.normpath(os.path.join(self.app.core_dir, "art", "interface", "Inventory", "inventory.mes"))
            with open(inc_path, 'a') as f:
                f.write(f'{{{self.icon_id_last:05d}}} {{{dest_name}}}\n')
        if save_index:
            self.save_index()
        return

    def load_index(self):
        fp = os.path.join(self.app.exp_dir, "Icons", "icons.json")
        if os.path.exists(fp):
            self.invenory_index = common.read_file_json(fp)
            self.icon_id_last = int(self.invenory_index[-1]["icon_id"])
        return

    def find_icon(self, icon_name: str):
        return next((rec for rec in self.invenory_index if rec["icon_name"] == icon_name), None)
    
    def save_index(self):
        fp = os.path.join(self.app.exp_dir, "Icons", "icons.json")
        common.write_json(fp, self.invenory_index)
        return