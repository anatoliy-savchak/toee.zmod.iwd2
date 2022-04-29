import json
import os
from types import SimpleNamespace
import subprocess
import common

class ProduceSound:
    def __init__(self, file_path_index: str, file_path_sound_scheme: str, file_path_sound_index: str, dir_wav: str, dir_sound: str, producer_app):
        self.producer_app = producer_app
        self.file_path_index = file_path_index
        self.file_path_sound_scheme = file_path_sound_scheme
        self.file_path_sound_index = file_path_sound_index
        self.dir_wav = dir_wav
        self.dir_sound = dir_sound
        self.are_dict = dict()

        self.lines_sound_scheme = self._preload_file(self.file_path_sound_scheme, "{0}{dummy - none}")
        self.lines_sound_index = self._preload_file(self.file_path_sound_index, "{0}{<<NONE>>}")
        self.dict_index = dict()
        self.last_sound_index = 0
        self.music_files = dict() # source name = dest path
        self.main_are_music = dict()

        return

    def _preload_file(self, fp: str, cutoff_line: str):
        with open(fp, 'r') as fi:
            lines =  fi.readlines()
        if cutoff_line:
            cutoff_line_id = next((i for i, line in enumerate(lines) if cutoff_line in line), None)
            if cutoff_line_id:
                del lines[cutoff_line_id+1:]
        return lines

    def _preload_json_file(self, fp: str):
        if not os.path.exists(fp):
            return dict()
        with open(fp, 'r') as fi:
            return json.load(fi)

    def process_are(self, are_name: str):
        are_path = os.path.join(self.producer_app.exp_dir, "Areas", are_name, are_name + "_sec.json")
        if not os.path.exists(are_path):
            are_path = os.path.join(self.producer_app.exp_dir, "Areas", are_name, are_name + ".json")
            if not os.path.exists(are_path):
                raise Exception("{are_path} does not exists!")

        with open(are_path, 'r') as fi:
            self.are_dict = json.load(fi)

        are_main_music = None
        recs = list()
        for ambient_dict in self.are_dict["ambients"]:
            flags_str = ambient_dict["Flags"]
            if not "Enabled" in flags_str: continue
            name = ambient_dict["Name"]
            #add_count = ambient_dict["ResRefCount"]
            music_names = list()
            is_looping = "Looping" in flags_str
            sloop = " /loop" if is_looping else ""
            volume = int(ambient_dict["Volume"])
            for i in range(1, 11):
                s = f"Resref{i}"
                s = ambient_dict.get(s)
                music_names.append(s)
            entries = list()
            for index, sound_name in enumerate(music_names):
                if not sound_name: continue
                self.last_sound_index += 1
                scheme_index = self.last_sound_index * 100
                suffix = f" - {index}" if index > 0 else ""
                self.lines_sound_index.append(f'{{{self.last_sound_index}}}{{{are_name} - {name}{suffix} #{scheme_index}}}')
                self.lines_sound_scheme.append('')
                self.lines_sound_scheme.append(f'§§§ {are_name} - {name}{suffix} §§§')
                self.lines_sound_scheme.append('')
                if not are_main_music and is_looping:
                    are_main_music = self.last_sound_index

                mrec = self.ensure_sound_name(sound_name)

                self.lines_sound_scheme.append(f'{{{scheme_index}}}{{{mrec["sound_path"]}.mp3 /VOL:{volume}{sloop}}}')
                if are_main_music and are_main_music == self.last_sound_index:
                    self.lines_sound_scheme.append('{101}{music\\hommlet_combat_Rev1_loop.mp3 /VOL:50 /combatmusic}')

                entry = common.tDict(sound_name = sound_name, sound_index = self.last_sound_index, index = index, durationf = mrec["durationf"])
                entries.append(entry)
            rec = common.tDict(name = name, is_looping = is_looping, volume = volume, entries = entries)
            recs.append(rec)
        self.dict_index[are_name] = common.tDict(are_main_music = are_main_music, recs = recs)

        if are_main_music:
            self.main_are_music[are_name] = common.tDict(are_main_music = are_main_music)

        return

    def ensure_sound_name(self, sound_name: str):
        if not (mrec := self.music_files.get(sound_name)):
            sound_path = f"ambient\\{sound_name}"
            src_file_path = os.path.join(self.producer_app.wav_dir, sound_name + ".wav")
            durationf = self.get_music_duration(src_file_path)
            mrec = common.tDict(sound_path = sound_path, sound_name = sound_name, durationf = durationf, src_file_path = src_file_path)
            self.music_files[sound_name] = mrec
        return mrec

    def save_schemes(self):
        with open(self.file_path_sound_scheme, 'w') as f:
            for line in self.lines_sound_scheme:
                f.write(line + ("\n" if not "\n" in line else ""))
        with open(self.file_path_sound_index, 'w') as f:
            for line in self.lines_sound_index:
                f.write(line + ("\n" if not "\n" in line else ""))
        return

    def save_map_info_file(self, are_name: str):
        return # debug!
        rec = self.main_are_music.get(are_name)
        if rec:
            fp = self.producer_app.get_path_out_map_info(are_name)
            if fp:
                with open(fp, 'w') as f:
                    theme_index = rec["are_main_music"]
                    ambient_index = theme_index
                    f.write(f'SoundScheme: {theme_index},{ambient_index}\n')
        return

    def save_file_index(self):
        fp = self.file_path_index
        if fp:
            with open(fp, 'w') as f:
                json.dump(self.dict_index, f, indent=4)
        return

    def load_file_index(self):
        if os.path.exists(self.file_path_index):
            self.dict_index = self._preload_json_file(self.file_path_index)
            return True
        return False

    def is_are_loaded(self, are_name: str):
        if self.dict_index.get(are_name):
            return True
        return False

    @staticmethod
    def get_music_duration(file_path: str):
        #ffprobe -i D:\IE\Resources\IWD2\WAV\2BFF002.wav -show_entries format=duration -v quiet -of csv="p=0"
        line = fr'venv\Library\bin\ffprobe.exe -i {file_path} -show_entries format=duration -v quiet -of csv="p=0"'
        #val = subprocess.check_output(line)
        val = subprocess.run(line, capture_output=True, text=True).stdout
        val = val.removesuffix("\n")
        return float(val)

    def save_music_files(self, overwrite: bool = False):
        ffmpeg_path = "venv\\Library\\bin\\ffmpeg.exe"
        path_sound = os.path.abspath(self.producer_app.get_path_sound())
        for sound_name, mrec in self.music_files.items():
            src_file_path = os.path.normpath(mrec["src_file_path"])
            sound_path = mrec["sound_path"]
            tf = os.path.normpath(os.path.join(path_sound, sound_path + ".mp3"))
            if not overwrite and os.path.exists(tf):
                continue
            command = f'{ffmpeg_path} -i "{src_file_path}" -acodec libmp3lame "{tf}" -y'
            os.system(command)
        return
