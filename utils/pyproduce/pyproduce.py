from asyncore import write
from importlib.resources import path
import json
import os
from posixpath import basename
import inf_commands
import produce_npc
from types import SimpleNamespace
import produce_dialog
import common
import produce_ar
import produce_sound

class ProducerApp:
    def __init__(self, exp_dir:str, core_dir: str, wav_dir: str, src_dir: str, module_dir: str, baf_dir: str, bam_dir: str) -> None:
        self.exp_dir = exp_dir
        self.core_dir = core_dir
        self.wav_dir = wav_dir
        self.src_dir = src_dir
        self.module_dir = module_dir
        self.baf_dir = baf_dir
        self.bam_dir = bam_dir

        self.copy_speaches = list()
        self.cres = dict()
        self.elements = dict()
        self.current_are_name = ""
        self.current_dialog_file = None
        self.bafs = dict()

        self.journal = None
        self.commands = inf_commands.InfCommands()
        self.produceSound = produce_sound.ProduceSound(self.get_path_sounds_index()
            , file_path_sound_scheme = self.get_path_sound_scheme()
            , file_path_sound_index = self.get_path_sound_index()
            , dir_wav = self.wav_dir
            , dir_sound = self.get_path_sound()
            , producer_app = self
        )

        return

    @staticmethod
    def read_file_json(file_name: str):
        with open(file_name, 'r') as f:
            file_ = json.load(f)
        return file_

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
        fn = os.path.join(self.exp_dir, 'Dialogs', dialog_name + '.json')
        result = self.read_file_json(fn)
        return result

    def get_cre_path(self, cre_name: str):
        return os.path.join(self.exp_dir, 'Creatures', cre_name + ".json")

    def get_path_sounds_index(self):
        return os.path.join(self.exp_dir, "Sounds/sounds.json")

    def get_path_sound_scheme(self):
        return os.path.join(self.core_dir, "sound/schemelist.mes")

    def get_path_sound_index(self):
        return os.path.join(self.core_dir, "sound/schemeindex.mes")        

    def get_path_sounds_file(self):
        return os.path.join(self.core_dir, "sound/snd_misc.mes")

    def get_path_sound(self):
        return os.path.join(self.core_dir, "sound")                

    def get_path_actions(self):
        return os.path.join(self.src_dir, "IDS/ACTION.IDS")

    def get_path_triggers(self):
        return os.path.join(self.src_dir, "IDS/TRIGGER.IDS")

    def get_path_out_rumors_file(self):
        return os.path.join(self.core_dir, "mes/game_rd_npc_m2m.mes")

    def get_path_template_rumors_file(self):
        return os.path.join(self.core_dir, "mes/game_rd_npc_f2m.mes")

    def get_path_map_rumors_file(self):
        return os.path.join(self.exp_dir, "journal/journal_map.json")

    def get_path_out_npcs_file(self, are_name: str, script_id: int = None):
        if script_id is None:
            script_id = self.are_name_to_script_id(are_name) + 1
        name = f"py{script_id:05d}_{are_name.lower()}_npcs.py"
        return os.path.join(self.core_dir, "scr", name)

    def get_path_out_npcs_dialog_file(self, are_name: str, script_id: int = None):
        if script_id is None:
            script_id = self.are_name_to_script_id(are_name) + 1
        name = f"{script_id:05d}_{are_name.lower()}_npcs.dlg"
        return os.path.join(self.core_dir, "dlg", name)

    def get_path_out_daemon_file(self, are_name: str, script_id: int = None):
        if script_id is None:
            script_id = self.are_name_to_script_id(are_name)
        name = f"py{script_id:05d}_{are_name.lower()}_daemon.py"
        return os.path.join(self.core_dir, "scr", name)

    def get_path_template_npcs_file(self, are_name):
        return 'data/py06616_template.py'

    def get_path_template_daemon_file(self, are_name):
        return 'data/daemon_template.py'

    def get_path_out_map_info(self, are_name):
        return os.path.join(self.module_dir, "maps", are_name, "mapinfo.txt")

    def produce_are_start(self, are_name: str, force_process_ambients: bool = False):
        self.current_are_name = are_name

        self.current_dialog_file = produce_dialog.DialogFile(self.get_path_out_npcs_dialog_file(are_name))
        script_id = self.are_name_to_script_id(are_name) + 1
        dfn = self.get_path_out_npcs_file(are_name, script_id)
        #sfn = self.get_path_template_npcs_file(are_name)
        with open(dfn, 'r') as fi:
            lines = fi.readlines()
        common.lines_after_cutoff(lines, common.marked_line("NPCS"))
        lines.append(f"MODULE_SCRIPT_ID = {script_id}\n")
        lines.append(" ")
        with open(dfn, 'w') as f:
            f.writelines(lines)
        return

    def produce_are_end(self):
        script_id = self.are_name_to_script_id(self.current_are_name) + 1
        dest_speech_path = os.path.join(self.get_path_sound(), "speech", f"{script_id:05d}")
        self.current_dialog_file.copy_sound_files(self.wav_dir, dest_speech_path)
        self.current_are_name = None
        self.current_dialog_file = None
        return

    def produce_are_npc(self, cre_name: str, are_name: str = None):
        are_name = are_name if are_name else self.current_are_name
        if rec := self.cres.get(cre_name):
            rec.are_names.append(are_name)
            return

        script_id = self.are_name_to_script_id(are_name) + 1
        out_npcs_file = self.get_path_out_npcs_file(are_name, script_id)
        prod = produce_npc.ProduceNPC(self
            , out_npcs_file
            , self.current_dialog_file
        ).produce_npc(cre_name)
        prod.save()

        are_names = list()
        are_names.append(are_name)
        rec = SimpleNamespace(are_names = are_names, cre_name = cre_name, ctrl_name= prod.ctrl_name, out_npcs_file = out_npcs_file)
        self.cres[cre_name] = rec
        return

    @staticmethod
    def are_name_to_script_id(are_name: str):
        return int(are_name.lower().replace("ar", ""))*10

    def produce_are(self, are_name: str):
        daemon = produce_ar.ProduceDaemon(self, are_name)
        fn = self.get_path_out_daemon_file(are_name)
        fnt = self.get_path_template_npcs_file
        daemon.load_template(fn)
        daemon.produce_npcs("place_npcs")
        #daemon.produce_ambients("setup_ambients")
        daemon.save(fn)
        return

    def find_npc_class(self, cre_name: str) -> tuple: # ctrl_name, module_name
        #next((for are_name, rec in self.cres.items() if rec.), None)
        rec = self.cres.get(cre_name)
        if rec:
            module_name = os.path.basename(rec.out_npcs_file).replace(".py", "")
            return (rec.ctrl_name, module_name)
        return (None, None)

    def find_first_in_bafs(self, lines: list):
        for fn in os.listdir(self.baf_dir):
            if not fn.lower().endswith(".baf"): continue
            baf_path = os.path.join(self.baf_dir, fn)
            src = self.bafs.get(fn)
            if src is None:
                with open(baf_path, 'r') as f:
                    src = f.readlines()
                    self.bafs[fn] = src
            
            result = self.find_first_in_baf_lines(src, lines, baf_path)
            if result:
                return result
        return None

    @staticmethod
    def find_first_in_baf(baf_path: str, lines: list):
        lowerlines = list()
        for l in lines: lowerlines.append(l.lower())
        with open(baf_path,'r') as src:
            found= None
            for line in src:
                if len(line) == 0: break #happens at end of file, then stop loop
                for i, l in enumerate(lines):
                    if l in line or lowerlines[i] in line.lower():
                        return (baf_path, line)
        return

    @staticmethod
    def find_first_in_baf_lines(src: list, lines: list, baf_path: str):
        lowerlines = list()
        for l in lines: lowerlines.append(l.lower())
        found= None
        for line in src:
            if len(line) == 0: break #happens at end of file, then stop loop
            for i, l in enumerate(lines):
                if l in line or lowerlines[i] in line.lower():
                    return (baf_path, line)
        return

    def list_ares(self):
        dir = os.path.join(self.exp_dir, "Areas")
        for are_name in os.listdir(dir):
            aredir = os.path.join(dir, are_name)
            fn = os.path.join(aredir, are_name + "_sec.json")
            if not os.path.exists(fn):
                fn = os.path.join(aredir, are_name + ".json")
            yield fn
        return

    def list_ares_with_sec(self):
        dir = os.path.join(self.exp_dir, "Areas")
        for are_name in os.listdir(dir):
            aredir = os.path.join(dir, are_name)
            fnsec = os.path.join(aredir, are_name + "_sec.json")
            if not os.path.exists(fnsec):
                fnsec = None
            fn = os.path.join(aredir, are_name + ".json")
            yield fn, fnsec
        return
