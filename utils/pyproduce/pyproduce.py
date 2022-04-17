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

    def load_template(self, file_name):
        with open(file_name, 'r') as f:
            self.lines_script = f.readlines()
        return

    def save(self, file_name):
        content = '\n'.join(self.lines_script)
        with open(file_name, 'w') as f:
            f.write(content)
        return
    
    def produce_npc(self, cre_name):
        self.read_cre(cre_name)
        self.current_crename = cre_name

        self.lines_script.append(f"class Ctrl{self.current_crename}: {self.elements['base_class']}:")
        self.lines_script.append("")

        self.produce_npc_baseproto()
        return

    def produce_npc_baseproto(self):
        proto = "const_proto_npc.PROTO_NPC_MAN"

        race_name = self.cre["RaceName"].lower()
        race = self.cre["Race"]
        gander = self.cre["Gender"]
        if not race_name or race_name == "human":
            if gander:
                proto = "const_proto_npc.PROTO_NPC_MAN"
            else:
                proto = "const_proto_npc.PROTO_NPC_WOMAN"
        else:
            raise Exception(f"Unknown race: {race_name}({race})")

        self.lines_script.append("\t\t@classmethod")
        self.lines_script.append(f"\t\tdef get_proto_id(cls): return {proto}")
        self.lines_script.append("")
        return

    def produce_npc_appearance(self):
        return