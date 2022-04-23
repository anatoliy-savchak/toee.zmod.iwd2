import os
import json
import pyproduce

i_def = "\t"
i_code = "\t\t"

class ProduceDaemon:
    def __init__(self, exported_dir: pyproduce.InfinityExportedDir, name: str) -> None:
        self.exported_dir = exported_dir
        self.lines_script = list()
        self.name = name
        self.ar = None
        self.npc_classes = dict() # name, lines
        self.load_ar()
        return

    def load_template(self, file_name):
        with open(file_name, 'r') as f:
            self.lines_script = f.readlines()
        return

    def load_ar(self):
        fn = os.path.join(self.exported_dir.dir, "Areas", self.name, self.name + ".json")
        with open(fn, 'r') as f:
            self.ar = json.load(f)
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
            subline = "return"
            found_def_returns = [index for index, line in enumerate(self.lines_script) if subline in line and index > found_def ]
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

        actors = self.ar["actors"]
        for actor in actors:
            name = actor["Name"]
            cre_file = actor["CREFile"]
            ori = int(actor["ActorOrientation"])
            direction = self.translate_orientation(ori)
            x = float(actor["CurrentXCoordinateSec"])
            y = float(actor["CurrentYCoordinateSec"])
            ctrl_class, class_file = self.find_npc_class(cre_file)
            add_line(i_code+f"# {name}: {cre_file} ({x:.1f}, {y:.1f}) {direction} ctrl: {class_file}.{ctrl_class}")
            if ctrl_class:
                add_line(i_code+f'ctrl_class, loc = {class_file}.{ctrl_class},  utils_obj.sec2loc({int(x)}, {int(y)})')
                add_line(i_code+f'self.create_lib_foe(loc, ctrl_class, {direction}, "", "{name}", ctrl_class.get_class_faction(), 0, 1)')
            add_line(i_code)
        return

    def find_npc_class(self, cre_name: str):
        word = f" {cre_name} "
        for npc_file, lines in self.npc_classes.items():
            found_lines = [line for line in lines if word in line]
            if not found_lines: continue
            found_line = str(found_lines[0])
            class_pos = found_line.find("class")
            if class_pos < 0: continue
            class_pos += len("class") + 1
            par_pos = found_line.find("(")
            if par_pos < 0: continue
            value = found_line[class_pos:par_pos]
            return value, npc_file.replace(".py", "")
        return None, None

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