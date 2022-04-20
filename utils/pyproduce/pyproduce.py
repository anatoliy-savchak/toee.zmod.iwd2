from asyncore import write
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
