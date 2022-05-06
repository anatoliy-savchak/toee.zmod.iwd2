import json
import os
from types import SimpleNamespace
import subprocess
import producer_base
import common

class ProducerSound(producer_base.Producer):
    def __init__(self, file_path_index: str, file_path_sound_scheme: str, file_path_sound_index: str, dir_wav: str, dir_sound: str, doc):
        super().__init__(doc, file_path_index, dict())
        self.doc = doc
        self.file_path_index = file_path_index
        self.file_path_sound_scheme = file_path_sound_scheme
        self.file_path_sound_index = file_path_sound_index
        self.dir_wav = dir_wav
        self.dir_sound = dir_sound
        self.are_dict = dict()

        self.lines_sound_scheme = list()
        self.lines_sound_index = list()

        self.music_files = dict() # source name = dest path
        self.main_are_music = dict()
        self.last_sound_id = 4108

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
        are_path = os.path.join(self.doc.exp_dir, "Areas", are_name, are_name + "_sec.json")
        if not os.path.exists(are_path):
            are_path = os.path.join(self.doc.exp_dir, "Areas", are_name, are_name + ".json")
            if not os.path.exists(are_path):
                raise Exception("{are_path} does not exists!")

        with open(are_path, 'r') as fi:
            self.are_dict = json.load(fi)
        return

    def ensure_sound_name2(self, sound_name: str, music_files: dict, volume: int, name, should_be_sound: bool):
        folder = "ambients" if should_be_sound else "music"
        nv = (name, volume)
        if not (mrec := music_files.get(sound_name)):
            sound_path = f"{folder}\\{sound_name}"
            src_file_path = os.path.join(self.doc.wav_dir, sound_name + ".wav")
            durationf = self.get_music_duration(src_file_path)
            sound_id = -1
            if should_be_sound:
                self.last_sound_id += 1
                sound_id = self.last_sound_id
            mrec = common.tDict(sound_path = sound_path, sound_name = sound_name
                , durationf = durationf, volume = volume, src_file_path = src_file_path
                , sound_id = sound_id
                , names = [nv, ])
            music_files[sound_name] = mrec
        else:
            #if int(mrec["volume"]) != volume: print("")
            names = mrec["names"]
            sound_id = mrec["sound_id"]
            if sound_id < 0 and should_be_sound:
                self.last_sound_id += 1
                sound_id = self.last_sound_id
                sound_path = f"{folder}\\{sound_name}"
                mrec["sound_id"] = sound_id
                mrec["sound_path"] = sound_path

            already = next((n for n, vol in names if n == name and vol == volume), None)
            if not already:
                names.append(nv)
            mrec["names"] = names
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
        rec = self.main_are_music.get(are_name)
        fp = self.doc.get_path_out_map_info(are_name)
        music_theme_index = 0
        ambients_theme_index = 0
        if rec:
            music_theme_index = rec["music_theme_index"]
            if music_theme_index is None: music_theme_index = 0
            ambients_theme_index = rec["ambients_theme_index"]
            if ambients_theme_index is None: ambients_theme_index = 0
        with open(fp, 'w') as f:
            f.write(f'SoundScheme: {music_theme_index},{ambients_theme_index}\n')
        return

    def save_file_index(self):
        fp = self.file_path_index
        if fp:
            with open(fp, 'w') as f:
                json.dump(self.src, f, indent=4)
        return

    def load_file_index(self):
        if os.path.exists(self.file_path_index):
            self.src = self._preload_json_file(self.file_path_index)
            return True
        return False

    def is_are_loaded(self, are_name: str):
        if self.src.get(are_name):
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
        path_sound = os.path.abspath(self.doc.get_path_sound())
        for mrec in self.src["Files"].values():
            src_file_path = os.path.normpath(mrec["src_file_path"])
            sound_path = mrec["sound_path"]
            tf = os.path.normpath(os.path.join(path_sound, sound_path + ".mp3"))
            if not overwrite and os.path.exists(tf):
                continue
            command = f'{ffmpeg_path} -i "{src_file_path}" -acodec libmp3lame "{tf}" -y'
            os.system(command)
            if not os.path.exists(tf):
                pass
        return

    def build_index(self):
        """ The purpose of index is for:
            * List of all sound files to convert and copy;
            * Info for snd_*.mes files;
            * Info for schemeindex.mes and schemelist.mes music files;
            * Info for daemons to create sound cabbages;
            Files : orig_name = (dest_file_path, sound_id, ambient_name_first, volume)
            Are: are_name = (
                 categories = (
                      music_theme, music_ambient, ambients
                  )
            SoundRec:
                ...
            )

        """
        lastSoundID = 4108
        Files = {}
        Ares = {}
        for are_path, are_sec_path in self.doc.list_ares_with_sec():
            are_src = common.read_file_json(are_path)
            are_src_sec = common.read_file_json(are_sec_path) if are_sec_path else None
            are_name = os.path.basename(os.path.dirname(are_path))
            music_themes = {}
            music_ambients = {}
            ambient_sounds = {}
            ambients = are_src["ambients"]
            print(f"are: {are_name}")
            if ambients:
                def describe(d: dict):
                    return d["Name"] + ("" if "IgnoreRadius" in d.get("Flags")  else f'({d["Radius"]})')

                def transcribe(d: dict, dsec: dict, should_be_sound = True) -> dict:
                    name = d["Name"]
                    volume = int(d["Volume"])
                    sounds = []
                    for i in range(1, 11):
                        s = f"Resref{i}"
                        s = d.get(s)
                        if s:
                            rec = self.ensure_sound_name2(s, Files, volume, rf'{are_name}\{name}', should_be_sound)
                            sounds.append(rec)

                    r = {
                        "Name" : name,
                        "Flags" : d["Flags"],
                        "XCoordinateSec" : dsec.get("XCoordinateSec") if dsec else -1,
                        "YCoordinateSec" : dsec.get("YCoordinateSec") if dsec else -1,
                        "Radius" : d["Radius"],
                        "Volume" : volume,
                        "FrequencyBase" : d["FrequencyBase"],
                        "FrequencyVariation" : d["FrequencyVariation"],
                        "AmbientAppearenceSchedule" : d["AmbientAppearenceSchedule"],
                        "AmbientAppearenceScheduleStr" : d["AmbientAppearenceScheduleStr"],
                        "Sounds": sounds
                    }
                    if baf := d.get("baf"):
                        r["baf"] = baf

                    return r

                def check_for_baf(l):
                    for amb in l:
                        name = amb["Name"]
                        activate_str = f'Activate("{name}")'
                        deactivate_str = f'Deactivate("{name}")'
                        found = self.doc.find_first_in_bafs([activate_str, deactivate_str])
                        if found:
                            amb["baf"] = found
                    return

                def get_amb_sec(name: str):
                    nonlocal are_src_sec
                    if not are_src_sec: return None
                    return next((amb for amb in are_src_sec["ambients"] if amb["Name"] == name), None)

                theme_music_ambs = [amb for amb in ambients 
                    if ("Enabled" in amb.get("Flags") 
                        and "IgnoreRadius" in amb.get("Flags") 
                        and "Looping" in amb.get("Flags") 
                        )
                ]
                theme_ambient_ambs0 = [amb for amb in ambients 
                    if ("Enabled" in amb.get("Flags") 
                        and "IgnoreRadius" in amb.get("Flags") 
                        and not amb in theme_music_ambs
                        )
                ]
                theme_music_amb_names = [describe(amb) for amb in theme_music_ambs]

                theme_ambient_ambs = list()
                environment_ambient_ambs = list()
                for amb in theme_ambient_ambs0:
                    name = amb["Name"]
                    activate_str = f'Activate("{name}")'
                    deactivate_str = f'Deactivate("{name}")'
                    found = self.doc.find_first_in_bafs([activate_str, deactivate_str])
                    if False: # disabled for now
                        theme_ambient_ambs.append(amb)
                    else:
                        if found:
                            amb["baf"] = found
                        environment_ambient_ambs.append(amb)

                theme_ambient_ambs_names = [describe(amb) for amb in theme_ambient_ambs]
                environment_ambient_names = [describe(amb) for amb in environment_ambient_ambs]

                effects_ambs = [amb for amb in ambients 
                    if ("Enabled" in amb.get("Flags") 
                        and not "IgnoreRadius" in amb.get("Flags") 
                        )
                ]
                effects_ambs_names = [describe(amb) for amb in effects_ambs]
                check_for_baf(effects_ambs)

                print(f"theme music: {theme_music_amb_names}")
                print(f"theme ambient: {theme_ambient_ambs_names}")
                print(f"sounds map: {environment_ambient_names}")
                print(f"sounds local: {effects_ambs_names}")
                for amb in theme_music_ambs: music_themes[amb["Name"]] = transcribe(amb, get_amb_sec(amb["Name"]), False)
                for amb in theme_ambient_ambs: music_ambients[amb["Name"]] = transcribe(amb, get_amb_sec(amb["Name"]), False)
                for amb in environment_ambient_ambs: ambient_sounds[amb["Name"]] = transcribe(amb, get_amb_sec(amb["Name"]))
                for amb in effects_ambs: ambient_sounds[amb["Name"]] = transcribe(amb, get_amb_sec(amb["Name"]))

            are_dest = {"music_themes": music_themes, "music_ambients": music_ambients, "ambient_sounds": ambient_sounds}
            Ares[are_name] = are_dest


        self.src = {"Ares": Ares, "Files": Files}
        self.save_file_index()
        return

    def build_and_save_sounds_file(self):
        fn = self.doc.get_path_sounds_file()
        with open(fn, 'r') as f:
            lines = f.readlines()
        common.lines_after_cutoff(lines, "{4108}{speech\slide\CE_2.mp3}", 1)
        items = sorted(self.src["Files"].values(), key=lambda item: int(item["sound_id"]))
        for mrec in items:
            sound_id = mrec["sound_id"]
            if sound_id < 0: continue
            sound_path = mrec["sound_path"]
            if not ".mp3" in sound_path.lower():
                sound_path += ".mp3"
            line = f'{{{sound_id}}}{{{sound_path}}}'
            lines.append(line)

        with open(fn, 'w') as f:
            for line in lines:
                f.write(line + ("\n" if not "\n" in line else ""))
        return

    def build_and_save_schemes(self):
        self.lines_sound_scheme = self._preload_file(self.file_path_sound_scheme, "{0}{dummy - none}")
        self.lines_sound_index = self._preload_file(self.file_path_sound_index, "{0}{<<NONE>>}")

        last_index = 0
        last_scheme_index = 0
        for are_name, arrec in self.src["Ares"].items():
            music_theme_index = None
            ambients_theme_index = None
            music_themes = arrec["music_themes"]
            if music_themes:
                last_index += 1
                music_theme_index = last_index
                last_scheme_index = last_index * 100
                self.lines_sound_index.append(f'{{{last_index}}}{{{are_name} - music #{last_scheme_index}}}')

                self.lines_sound_scheme.append('')
                self.lines_sound_scheme.append(f'§§§ {are_name} - music §§§')
                self.lines_sound_scheme.append('')
                last_scheme_index += -1
                for name, rec in music_themes.items():
                    ambientAppearenceScheduleStr = rec["AmbientAppearenceScheduleStr"]
                    ambientAppearenceSchedule = rec["AmbientAppearenceSchedule"]
                    is_all = str(ambientAppearenceSchedule) == "ALL"
                    is_day = ("From_0530_to_0629" in ambientAppearenceScheduleStr) and ("From_1630_to_1729" in ambientAppearenceScheduleStr)
                    is_night = ("From_0030_to_0129" in ambientAppearenceScheduleStr) and ("From_2330_to_0029" in ambientAppearenceScheduleStr)
                    if not is_all and not is_day and not is_night:
                        raise Exception("Not supported")
                    if not is_all and is_day and is_night:
                        raise Exception("Not supported")

                    last_scheme_index += 1
                    mrec = rec["Sounds"][0]# always 1 for music
                    sound_file_name = mrec["sound_path"]
                    volume = int(mrec["volume"])
                    content_no_time = f'{sound_file_name}.mp3 /VOL:{volume} /loop'

                    if is_all:
                        self.lines_sound_scheme.append(f'{{{last_scheme_index}}}{{{content_no_time}}}')
                    elif is_night:
                        self.lines_sound_scheme.append(f'{{{last_scheme_index}}}{{{content_no_time} /time:18-23}}')
                        self.lines_sound_scheme.append(f'{{{last_scheme_index}}}{{{content_no_time} /time:0-5}}')
                    elif is_day:
                        self.lines_sound_scheme.append(f'{{{last_scheme_index}}}{{{content_no_time} /time:6-17}}')

                # comabat music
                last_scheme_index += 1
                self.lines_sound_scheme.append(f'{{{last_scheme_index}}}{{music\hommlet_combat_Rev1_loop.mp3 /VOL:50 /combatmusic}}')

            music_ambients = arrec["music_ambients"]
            if music_ambients:
                last_index += 1
                ambients_theme_index = last_index
                last_scheme_index = last_index * 100
                self.lines_sound_index.append(f'{{{last_index}}}{{{are_name} - ambients #{last_scheme_index}}}')

                self.lines_sound_scheme.append('')
                self.lines_sound_scheme.append(f'§§§ {are_name} - ambients §§§')
                self.lines_sound_scheme.append('')
                last_scheme_index += -1
                for name, rec in music_ambients.items():
                    ambientAppearenceScheduleStr = rec["AmbientAppearenceScheduleStr"]
                    ambientAppearenceSchedule = rec["AmbientAppearenceSchedule"]
                    is_all = str(ambientAppearenceSchedule) == "ALL"
                    is_day = ("From_0530_to_0629" in ambientAppearenceScheduleStr) and ("From_1630_to_1729" in ambientAppearenceScheduleStr)
                    is_night = ("From_0030_to_0129" in ambientAppearenceScheduleStr) and ("From_2330_to_0029" in ambientAppearenceScheduleStr)
                    if not is_all and not is_day and not is_night:
                        raise Exception("Not supported")
                    if not is_all and is_day and is_night:
                        raise Exception("Not supported")

                    sounds_count = len(rec["Sounds"])
                    is_loop = "LOOP" in rec["Flags"]
                    for mrec in rec["Sounds"]:
                        last_scheme_index += 1
                        sound_file_name = mrec["sound_path"]
                        volume = int(mrec["volume"])
                        sloop = "" if not is_loop else " /loop"
                        scatter_val = 50 - sounds_count
                        frequencyBase = rec["FrequencyBase"]
                        freq_val = 50 - frequencyBase
                        s_scatter = ""
                        s_freq = ""
                        if sounds_count > 1:
                            s_scatter = f" /scatter:{scatter_val}"
                            s_freq = f" /freq:{freq_val}"
                            if is_loop:
                                raise Exception("Not supported")

                        content_no_time = f'{sound_file_name}.mp3 /VOL:{volume}{sloop}{s_scatter}{s_freq}'
                        if is_all:
                            self.lines_sound_scheme.append(f'{{{last_scheme_index}}}{{{content_no_time}}}')
                        elif is_night:
                            self.lines_sound_scheme.append(f'{{{last_scheme_index}}}{{{content_no_time} /time:18-23}}')
                            self.lines_sound_scheme.append(f'{{{last_scheme_index}}}{{{content_no_time} /time:0-5}}')
                        elif is_day:
                            self.lines_sound_scheme.append(f'{{{last_scheme_index}}}{{{content_no_time} /time:6-17}}')
            self.main_are_music[are_name] = {"music_theme_index": music_theme_index, "ambients_theme_index": ambients_theme_index}
            self.save_map_info_file(are_name)

        self.save_schemes()
        return