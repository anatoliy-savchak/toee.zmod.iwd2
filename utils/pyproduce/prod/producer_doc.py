import os
import temple_specs
import produce_journal
import inf_commands
import producer_sound
import producer_are
import classes_registry
import produce_bcs_manager

class ProducerDoc(object):
    def __init__(self
        , exp_dir:str
        , core_dir: str
        , wav_dir: str
        , src_dir: str
        , module_dir: str
        , baf_dir: str
        , bam_dir: str
        , protos_paths: str
        , temple_src_path: str
    ):
        self.exp_dir = exp_dir
        self.core_dir = core_dir
        self.wav_dir = wav_dir
        self.src_dir = src_dir
        self.module_dir = module_dir
        self.baf_dir = baf_dir
        self.bam_dir = bam_dir
        self.protos_paths = protos_paths
        self.temple_src_path = temple_src_path

        self.templeClassSpecs = None
        self.journalFile = None
        self.commands = None
        self.producerSound = None
        self.producers_are = dict()
        self.classesRegistry = None
        self.make_new = False
        self.bcsManager = None

        self.copy_speaches = list()
        return

    def init(self, from_scratch: bool = False):
        self.make_new = from_scratch
        self.templeClassSpecs = temple_specs.TempleClassSpecs(self.temple_src_path)

        self.journalFile = produce_journal.JournalFile()
        if self.journalFile:
            self.journalFile.load_map(self.get_path_map_rumors_file())

        self.commands = inf_commands.InfCommands()
        if self.commands:
            self.commands.parse_file_actions(self.get_path_actions())
            self.commands.parse_file_triggers(self.get_path_triggers())
            self.commands.parse_file_triggers(self.get_path_identifiers())

        self.producerSound = producer_sound.ProducerSound(self.get_path_sounds_index()
            , file_path_sound_scheme = self.get_path_sound_scheme()
            , file_path_sound_index = self.get_path_sound_index()
            , dir_wav = self.wav_dir
            , dir_sound = self.get_path_sound()
            , doc = self
        )
        if self.producerSound:
            if not from_scratch:
                self.producerSound.load_file_index()
            else:
                self.producerSound.build_index()
                self.producerSound.build_and_save_sounds_file()
                self.producerSound.save_music_files()
                self.producerSound.build_and_save_schemes()

        self.classesRegistry = classes_registry.ClassesRegistry(self)

        self.bcsManager = produce_bcs_manager.ProduceBCSManager(self)
        return

    def get_path_map_rumors_file(self):
        return os.path.join(self.exp_dir, "journal/journal_map.json")

    def get_path_actions(self):
        return os.path.join(self.src_dir, "IDS/ACTION.IDS")

    def get_path_triggers(self):
        return os.path.join(self.src_dir, "IDS/TRIGGER.IDS")

    def get_path_identifiers(self):
        return os.path.join(self.src_dir, "IDS/OBJECT_FIXED.IDS")

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

    def get_path_registry_dir(self):
        return os.path.join(self.exp_dir, 'Registry')

    def get_path_template_daemon_file(self):
        return 'data/daemon_template.py'

    def get_path_out_daemon_file(self, are_name: str, script_id: int = None):
        if script_id is None:
            script_id = self.are_name_to_script_id(are_name)
        name = f"py{script_id:05d}_{are_name.lower()}_daemon.py"
        return os.path.join(self.core_dir, "scr", name)

    def get_path_cre(self, cre_name: str):
        return os.path.join(self.exp_dir, 'Creatures', cre_name + ".json")

    def get_path_template_npcs_class_auto_file(self):
        return 'data/py06616_template.py'

    def get_path_out_npcs_class_auto_file(self, are_name: str, script_id: int = None):
        if script_id is None:
            script_id = self.are_name_to_script_id(are_name) + 1
        name = f"py{script_id:05d}_{are_name.lower()}_npc_classes_auto.py"
        return os.path.join(self.core_dir, "scr", name)

    def get_path_out_npcs_dialog_file(self, are_name: str, script_id: int = None):
        if script_id is None:
            script_id = self.are_name_to_script_id(are_name) + 1
        name = f"{script_id:05d}_{are_name.lower()}_npc_classes_auto.dlg"
        return os.path.join(self.core_dir, "dlg", name)

    def get_path_template_npcs_class_manual_file(self):
        return 'data/py06616_template.py'

    def get_path_out_npcs_class_manual_file(self, are_name: str, script_id: int = None):
        if script_id is None:
            script_id = self.are_name_to_script_id(are_name) + 2
        name = f"py{script_id:05d}_{are_name.lower()}_npc_classes.py"
        return os.path.join(self.core_dir, "scr", name)

    def get_path_template_are_bcs_file(self):
        return 'data/bcs_template.py'

    def get_path_out_are_bcs_file(self, are_name: str, script_id: int = None):
        if script_id is None:
            script_id = self.are_name_to_script_id(are_name) + 5
        name = f"py{script_id:05d}_{are_name.lower()}_scripts.py"
        return os.path.join(self.core_dir, "scr", name)
        
    @staticmethod
    def are_name_to_script_id(are_name: str):
        return int(are_name.lower().replace("ar", ""))*10

    def acquire_are_producer(self, are_name: str):
        result = self.producers_are.get(are_name)
        if not result:
            result = producer_are.ProducerOfAre(self, are_name, self.are_name_to_script_id(are_name), self.make_new)
        return result