from asyncore import write
from importlib.resources import path
import json
import os

class InfinityExportedDir:
    def __init__(self, dir: str) -> None:
        self.dir = dir
        self.folders = dict()
        self.folders["act"] = dict()
        self.folders["cre"] = dict()
        self.folders["dlg"] = dict()

        self.elements = dict()

        self.lines_script = list()
        self.lines_dialog = list()
        self.copy_speaches = list()
        self.current_crename = ""
        self.cre = dict()

        self.setup_elements()
        self.journal = None
        return

    @staticmethod
    def read_file(file_name: str):
        with open(file_name, 'r') as f:
            file_ = json.load(f)
        return file_

    def setup_elements(self):
        self.elements["base_class"] = "NPCBase"
        return

    def read_cre(self, name: str):
        file_name = os.path.join(self.dir, "Creatures", name + '.json')
        value = self.folders["cre"].get(name)
        if not value:
            value = self.read_file(file_name)
            self.folders["cre"][name] = value
        self.cre = value
        return value

    @staticmethod
    def cre_strref_to_string(strref):
        if strref:
            eText = strref.get("Text")
            return eText
        return None

    def load_toee_class_specs(self, dir: str):
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

        self.elements["toee_class_specs"] = d
        return

    def toee_class_spec_has_prof(self, class_name: str, feat: str):
        n = class_name.split("_")
        name = n[len(n)-1]
        class_spec = self.elements["toee_class_specs"].get(name)
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

    def load_cre_dialog(self, dialog_name):
        fn = os.path.join(self.dir, 'Dialogs', dialog_name + '.json')
        result = self.read_file(fn)
        return result