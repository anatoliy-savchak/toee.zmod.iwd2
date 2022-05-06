import os


class TempleClassSpecs(object):
    def __init__(self
        , temple_src_path: str
    ):
        self.temple_src_path = temple_src_path
        self.registry = self.load_toee_class_specs(self.temple_src_path)
        return
        
    def load_toee_class_specs(self
        , temple_src_path: str # '../../../TemplePlus'
        ):
        dir = os.path.join(temple_src_path, 'tpdatasrc/tpgamefiles/rules/char_class')
        d = dict()
        for fn in os.listdir(dir):
            if not fn.endswith(".py") or not fn.startswith("class"): continue
            with open(os.path.join(dir, fn), 'r') as f:
                name = fn.removesuffix(".py")
                # class011_fighter
                n = name.split("_")
                name = n[len(n)-1]
                # fighter
                d[name] = f.readlines()

        return d

    def toee_class_spec_has_prof(self, class_name: str, feat: str):
        n = class_name.split("_")
        name = n[len(n)-1]
        class_spec = self.registry.get(name)
        if not class_spec: return

        def has(prof: str):
            nonlocal class_spec
            line = next((line for line in class_spec if prof in line), None)
            return line

        feat = feat.removeprefix("toee.")
        if has(feat): 
            return name

        if feat.startswith("feat_martial_weapon_proficiency"):
            if has("feat_martial_weapon_proficiency_all"): 
                return name
        elif feat.startswith("feat_simple_weapon_proficiency"):
            if has("feat_simple_weapon_proficiency"): 
                return name

        return
