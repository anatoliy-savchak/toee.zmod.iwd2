import os
import math
import json
import common

i_def = "\t"
i_code = "\t\t"

class ProduceDaemon:
    def __init__(self, producer_app, name: str) -> None:
        self.producer_app = producer_app
        self.lines_script = list()
        self.name = name
        self.ar = None
        self.ar_sec = None
        self.npc_classes = dict() # name, lines
        self.load_ar()
        return

    def load_template(self, file_name):
        with open(file_name, 'r') as f:
            self.lines_script = f.readlines()
        return

    def load_ar(self):
        fn = os.path.join(self.producer_app.exp_dir, "Areas", self.name, self.name + ".json")
        with open(fn, 'r') as f:
            self.ar = json.load(f)
        fn = os.path.join(self.producer_app.exp_dir, "Areas", self.name, self.name + "_sec.json")
        if os.path.exists(fn):
            with open(fn, 'r') as f:
                self.ar_sec = json.load(f)
        return

    def load_npc_classes(self, file_path: str):
        name = os.path.basename(file_path)
        with open(file_path, 'r') as f:
            self.npc_classes[name] = f.readlines()
        return

    def save(self, file_name):
        with open(file_name, 'w') as f:
            for line in self.lines_script:
                #aline = line
                f.write(line + ("\n" if not "\n" in line else ""))
        return

    def produce_npcs(self, def_name: str):
        subline = f"def {def_name}("
        found_def = len(self.lines_script)
        found_def_return = found_def + 1

        found_defs = [index for index, line in enumerate(self.lines_script) if subline in line ]
        if not found_defs:
            self.lines_script.append(i_def + "def place_npcs(self):")
            self.lines_script.append(i_code+"return")
            self.lines_script.append("")
        else:
            found_def = found_defs[0]
            subline = "\t\treturn"
            found_def_returns = [index for index, line in enumerate(self.lines_script) if index > found_def and str(line).startswith(subline)]
            if found_def_returns:
                found_def_return = found_def_returns[0]

            while found_def_return > found_def +1 and found_def_return < len(self.lines_script):
                found_def_return += -1
                self.lines_script.pop(found_def_return)

        def add_line(line: str):
            nonlocal found_def_return

            self.lines_script.insert(found_def_return, line)
            found_def_return += 1
            return

        #add_line(i_code+'Global = global_injector()')
        actors = self.ar["actors"]
        for actor in actors:
            name = actor["Name"]
            cre_file = actor["CREFile"]
            ori = int(actor["ActorOrientation"])
            direction = self.translate_orientation(ori)
            actor_sec = actor
            if self.ar_sec:
                acts = [act for act in self.ar_sec["actors"] if act["Name"] == name]
                if acts:
                    actor_sec = acts[0]
                
            x = float(actor_sec["CurrentXCoordinateSec"])
            y = float(actor_sec["CurrentYCoordinateSec"])

            hidden = bool(actor["DefaultHiddenCalc"])
            ctrl_class, class_file = self.find_npc_class(cre_file)
            add_line(i_code+f'# {name}: {cre_file} ({x:.1f}, {y:.1f}) {direction} ctrl: {class_file}.{ctrl_class} {"hidden" if hidden else ""}')
            if not hidden:
                if ctrl_class:
                    add_line(i_code+f'ctrl_class, loc = {class_file}.{ctrl_class},  utils_obj.sec2loc({int(x)}, {int(y)})')
                    add_line(i_code+f'self.create_npc_at(loc, ctrl_class, {direction}, "{name}", 0, 1)')
                    #add_line(i_code+f'npc, ctrl = self.create_npc_at(loc, ctrl_class, {direction}, "{name}", 0, 1)')
                    #global_name = f"npc_{name}"
                    #add_line(i_code+f'Global.{global_name} = npc')
                    #add_line(i_code+f'Global["{global_name}"] = npc')
                    #add_line(i_code+f'builtins.{global_name} = npc')
                    #add_line(i_code+f'globals()["{global_name}"] = npc')
                    #add_line(i_code+f'global {global_name}')
                    #add_line(i_code+f'{global_name} = npc')
                    #global_name = f"npc_{name}_ctrl"
                    #add_line(i_code+f'global {global_name}')
                    #add_line(i_code+f'{global_name} = ctrl')
            add_line(i_code)
        return

    def find_npc_class(self, cre_name: str):
        return self.producer_app.find_npc_class(cre_name)

    def translate_orientation(self, ori: int):
        # TODO - modify const_toee to have rotation_0645_oclock
        if ori == 0: return "const_toee.ROT06" # South
        elif ori == 1: return "const_toee.ROT07" # SSW
        elif ori == 2: return "const_toee.ROT08" # SW
        elif ori == 3: return "const_toee.ROT08" # WSW
        elif ori == 4: return "const_toee.ROT09" # West
        elif ori == 5: return "const_toee.ROT10" # WNW
        elif ori == 6: return "const_toee.ROT11" # NW
        elif ori == 7: return "const_toee.ROT11" # NNW
        elif ori == 8: return "const_toee.ROT00" # North
        elif ori == 9: return "const_toee.ROT01" # NNE
        elif ori == 10: return "const_toee.ROT02" # NE
        elif ori == 11: return "const_toee.ROT02" # ENE
        elif ori == 12: return "const_toee.ROT03" # East
        elif ori == 13: return "const_toee.ROT04" # ESE
        elif ori == 14: return "const_toee.ROT05" # SE
        elif ori == 15: return "const_toee.ROT05" # SSE
        return "const_toee.ROT06"

    def produce_ambients(self, def_name: str):
        found_def_return = common.lines_method(self.lines_script, f"\tdef {def_name}(self):")
        def add_codeline(line: str):
            nonlocal found_def_return

            self.lines_script.insert(found_def_return, i_code + line)
            found_def_return += 1
            return

        ambients = self.producer_app.produceSound.dict_index[self.name]
        for ambient_dict in self.ar_sec["ambients"]:
            flags_str = ambient_dict["Flags"]
            if not "Enabled" in flags_str: continue
            name = ambient_dict["Name"]
            if "main" in name.lower(): continue
            is_looping = "Looping" in flags_str
            ignoreRadius = "IgnoreRadius" in flags_str

            sound_indexes = list()
            durations = list()
            rec = next((rec for rec in ambients["recs"] if rec["name"] == name), None)
            for entry in rec["entries"]:
                sound_index = entry["sound_index"]
                durationf = entry["durationf"]
                sound_indexes.append(int(sound_index))
                duration = int(math.ceil(durationf))
                durations.append(duration)
           
            sound_indexes_str = str(sound_indexes)
            durations_str = str(durations)
            add_codeline('')
            add_codeline('handler = ctrl_ambients.AmbientHanlder()')
            add_codeline(f'handler.setup(name="{name}", flags="{flags_str}", frequency={ambient_dict["FrequencyBase"]}, variation={ambient_dict["FrequencyVariation"]}, x={ambient_dict["XCoordinateSec"]}, y={ambient_dict["YCoordinateSec"]}, sound_indexes={sound_indexes_str}, durations={durations_str})')
            add_codeline('self.ambients.append(handler)')

        
        return