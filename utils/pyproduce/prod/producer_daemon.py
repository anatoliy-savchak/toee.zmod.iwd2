from asyncore import write
from re import S
import producer_base
import common
import os
import produce_bcs_manager

class ProducerOfDaemon(producer_base.ProducerOfFile):
    def __init__(self, doc
        , are_name: str
        , script_id: int
        , make_new: bool
        , src: dict
        , src_sec: dict
        , src_path: str
    ):
        template_path = doc.get_path_template_daemon_file()
        out_path = doc.get_path_out_daemon_file(are_name, script_id)
        super().__init__(doc, out_path=out_path, template_path=template_path, make_new=make_new, src=src, src_path=src_path)

        self.are_name = are_name
        self.script_id = script_id
        self.src_sec = src_sec
        self.map_id = script_id // 10
        return

    def get_eligible_actor_recs(self):
        for rec in self.src['actors']:
            # Actually, hidden npcs are used, do not do it
            # if not rec['DefaultHiddenCalc']:
            #     yield rec
            yield rec
        return

    def produce(self, skip_bcs: bool = False, bcs_script_override: str = None):
        if self.make_new:
            self.produce_new()
        self.produce_npcs('place_npcs_auto')
        if not skip_bcs:
            self.produce_bcs('place_bcs_auto', bcs_script_override)
        self.produce_ambients('setup_ambients_auto')
        return

    def produce_npcs(self, def_name: str):
        subline = f"def {def_name}("
        self.current_line_id = common.lines_after_before_cutoff(self.lines, subline, '\t\treturn')
        self.indent()
        if not self.current_line_id:
            self.writeline(f"def {def_name}(self):")
        self.indent()

        for actor in self.get_eligible_actor_recs():
            name = actor["Name"]
            cre_file = actor["CREFile"]
            ori = int(actor["ActorOrientation"])
            direction = self.translate_orientation(ori)
            actor_sec = actor
            if self.src_sec:
                acts = [act for act in self.src_sec["actors"] if act["Name"] == name]
                if acts:
                    actor_sec = acts[0]
                

            x = float(actor_sec["CurrentXCoordinateSec"])
            y = float(actor_sec["CurrentYCoordinateSec"])

            hidden = bool(actor["DefaultHiddenCalc"])
            reg_name = f'{self.are_name}.{cre_file}.{name}'
            d = self.doc.classesRegistry.get_class_tup('class_inst_manual', reg_name)
            if not d:
                continue
            class_file, ctrl_class = d["file_name"], d["class_name"]
            self.add_import(class_file)

            self.writeline(f'# {name}: {cre_file} ({x:.1f}, {y:.1f}) {direction} ctrl: {class_file}.{ctrl_class} {"hidden" if hidden else ""}')
            if ctrl_class:
                self.writeline(f'print("Creating {class_file}.{ctrl_class}...")')
                self.writeline(f'ctrl_class, loc = {class_file}.{ctrl_class},  utils_obj.sec2loc({int(x)}, {int(y)})')
                self.writeline(f'self.create_npc_at(loc, ctrl_class, {direction}, "{name}", 0, 1)')
            self.writeline()
        #self.writeline()
        if not self.current_line_id:
            self.writeline(f"return")
        self.indent(False)
        self.current_line_id = -1
        self.indent(False)

        self.produce_imports()
        return

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

    def produce_bcs(self, def_name: str, bcs_script_override: str = None):
        subline = f"def {def_name}("
        self.current_line_id = common.lines_after_before_cutoff(self.lines, subline, '\t\treturn')
        self.indent()
        if not self.current_line_id:
            self.writeline()
            self.writeline(f"def {def_name}(self):")
        self.indent()

        file_name = None

        area_script = self.src["AreaScript"]
        if bcs_script_override:
            area_script = bcs_script_override
            
        if area_script and area_script != "None":
            ctrl_name, file_name, pkg_name = self.doc.bcsManager.ensure_bcs(
                bcs_name=area_script
                , hint_are_name=self.are_name
                , hint_script_code='script_area'
            )
            self.writeline(f'self.vars["script_area"] = {file_name}.{ctrl_name}')

        if not self.current_line_id:
            self.writeline(f"return")
        self.current_line_id = -1
        self.indent(False)
        self.indent(False)

        if file_name:
            self.add_import(file_name, pkg_name)
            self.produce_imports()
        return

    def produce_new(self):
        daemon_class_name = f'Ctrl{self.are_name}'
        self.writeline(f'DAEMON_SCRIPT_ID = {self.script_id}')
        self.writeline(f'DAEMON_MAP_ID = module_consts.MAP_ID_AR{self.map_id}')
        daemon_gid = self.get_daemon_gid()
        if not daemon_gid:
            daemon_gid = 'TODO!'
        self.writeline(f'DAEMON_GID = "{daemon_gid}"')
        self.writeline()

        self.writeline('def san_new_map(attachee, triggerer):')
        self.indent()
        #self.writeline('#print(attachee.id)')
        #self.writeline('#debug.breakp("")')
        self.writeline(f'return ctrl_daemon2.do_san_new_map(attachee, triggerer, DAEMON_MAP_ID, {daemon_class_name})')
        self.indent(False)
        self.writeline()

        self.writeline('def san_first_heartbeat(attachee, triggerer):')
        self.indent()
        self.writeline('#print(attachee.id)')
        self.writeline('#debug.breakp("")')
        self.writeline(f'return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, DAEMON_MAP_ID, {daemon_class_name})')
        self.indent(False)
        self.writeline()

        self.writeline('def san_heartbeat(attachee, triggerer): return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, DAEMON_MAP_ID, cs())')
        self.writeline()

        self.writeline('def san_dying(attachee, triggerer): return ctrl_daemon2.do_san_dying(attachee, triggerer, DAEMON_MAP_ID, cs())')
        self.writeline()

        self.writeline('def san_use(attachee, triggerer): return ctrl_daemon2.do_san_use(attachee, triggerer, DAEMON_MAP_ID, cs())')
        self.writeline()

        self.writeline('def cs():')
        self.indent()
        self.writeline('o = utils_storage.obj_storage_by_id(DAEMON_GID)')
        self.writeline('if (not o): return None')
        self.writeline(f'result = o.data.get({daemon_class_name}.get_name())')
        self.writeline(f'assert isinstance(result, {daemon_class_name})')
        self.writeline('return result')
        self.indent(False)
        self.writeline()

        self.writeline(f'class {daemon_class_name}(ctrl_daemon_ie.CtrlDaemonIE):')
        self.indent()
        #self.writeline()

        self.writeline('def created(self, npc):')
        self.indent()
        self.writeline(f'self.init_daemon2_fields(DAEMON_MAP_ID, DAEMON_SCRIPT_ID, "daemon_{self.are_name.lower()}")')
        self.writeline(f'super({daemon_class_name}, self).created(npc)')
        self.writeline('return')
        self.indent(False)
        self.writeline()

        self.writeline('def place_encounters_initial(self):')
        self.indent()
        self.writeline(f'super({daemon_class_name}, self).place_encounters_initial()')
        self.writeline('return')
        self.indent(False)
        self.writeline()

        self.indent(False) # class
        return

    def produce_ambients(self, def_name: str):
        found_def_return = common.lines_method(self.lines, f"\tdef {def_name}(self):")
        if found_def_return:
            self.current_line_id = found_def_return

        ambients = self.doc.producerSound.src["Ares"].get(self.are_name)
        if ambients:
            self.indent()
            self.indent()
            handlers_count = 0
            for ambient_dict in ambients["ambient_sounds"].values():
                name = ambient_dict["Name"]
                x, y = int(ambient_dict["XCoordinateSec"]), int(ambient_dict["YCoordinateSec"])
                if x <= 0 or y <= 0:
                    #raise Exception("Incorrect x, y!")
                    if self.src_sec:
                        ambient_dict2 = next((ambient_dict for ambient_dict in self.src_sec["ambients"] if ambient_dict["Name"] == name), None)
                        if ambient_dict2:
                            x, y = int(ambient_dict2["XCoordinateSec"]), int(ambient_dict2["YCoordinateSec"])
                    if x <= 0 or y <= 0:
                        print("Incorrect x, y!")
                        continue

                schedule = ambient_dict["AmbientAppearenceScheduleStr"]
                schedule_all = ambient_dict["AmbientAppearenceSchedule"]
                if str(schedule_all) == "ALL": schedule = schedule_all
                baf = ambient_dict.get('baf')
                alias = f'"{name}"' if baf else 'None'
                is_looping = "Looping" in ambient_dict["Flags"]

                if is_looping:
                    self.writeline(f'ctrl_class, loc = ctrl_ambients.CtrlAmbient, utils_obj.sec2loc({x}, {y})')
                    self.writeline(f'npc, ctrl = self.create_cabbage(loc, ctrl_class, {alias})')
                    self.writeline(f'ctrl.setup(name="{name}", flags="{ambient_dict["Flags"]}", frequency={ambient_dict["FrequencyBase"]}, frequency_variation={ambient_dict["FrequencyVariation"]}, radius={ambient_dict["Radius"]}, x={x}, y={y}, schedule="{schedule}")')
                    for rec in ambient_dict["Sounds"]:
                        sname = rec["sound_name"]
                        stitle = ""
                        if (names := rec.get("names")):
                            stitle = f', title="{names[0][0] + " " + sname}"'
                        self.writeline(f'ctrl.setup_sound(sound_id={rec["sound_id"]}, durationf={rec["durationf"]}, volume={rec["volume"]}{stitle})')
                    self.writeline('ctrl.run(npc)')
                else:
                    self.writeline(f'amb = ctrl_ambients.AmbientHanlder()')
                    self.writeline(f'loc = utils_obj.sec2loc({x}, {y})')
                    self.writeline(f'amb.setup(name="{name}", flags="{ambient_dict["Flags"]}", frequency={ambient_dict["FrequencyBase"]}, frequency_variation={ambient_dict["FrequencyVariation"]}, radius={ambient_dict["Radius"]}, loc=loc, schedule="{schedule}")')
                    for rec in ambient_dict["Sounds"]:
                        sname = rec["sound_name"]
                        stitle = ""
                        if (names := rec.get("names")):
                            stitle = f', title="{names[0][0] + " " + sname}"'
                        self.writeline(f'amb.setup_sound(sound_id={rec["sound_id"]}, durationf={rec["durationf"]}, volume={rec["volume"]}{stitle})')
                    self.writeline('self.ambients.append(amb)')
                    handlers_count += 1
                self.writeline()
            if handlers_count:
                self.writeline()
                self.writeline('self.ambs_timer_start()')
            self.indent(False)
            self.indent(False)
        return

    def get_daemon_gid(self):
        fn = os.path.join(os.path.dirname(self.src_path), 'DAEMON_GID.txt')
        if os.path.exists(fn):
            with open(fn, 'r') as f:
                result = f.readline()
                return result
        return