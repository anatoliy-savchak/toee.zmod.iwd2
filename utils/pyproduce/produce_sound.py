import json
import os

class ProduceSound:
    def __init__(self, file_path_index: str, file_path_sound_scheme: str, file_path_sound_index: str, dir_wav: str, dir_sound: str):
        self.file_path_index = file_path_index
        self.file_path_sound_scheme = file_path_sound_scheme
        self.file_path_sound_index = file_path_sound_index
        self.dir_wav = dir_wav
        self.dir_sound = dir_sound
        self.are_dict = dict()

        self.lines_sound_scheme = self._preload_file(self.file_path_sound_scheme)
        self.lines_path_sound_index = self._preload_file(self.file_path_sound_index)
        self.dict_index = self._preload_json_file(self.file_path_sound_index)
        self.last_sound_index = 0

        return

    def _preload_file(self, fp: str):
        with open(fp, 'r') as fi:
            return fi.readlines()

    def _preload_json_file(self, fp: str):
        if not os.path.exists(fp):
            return dict()
        with open(fp, 'r') as fi:
            return json.load(fi)

    def process_are(self, are_file_path: str):
        with open(are_file_path, 'r') as fi:
            self.are_dict = json.load(fi)

        for ambient_dict in self.are_dict["ambients"]:


        return
