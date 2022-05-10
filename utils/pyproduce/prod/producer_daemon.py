import producer_base
import common
import produce_bcs_manager

class ProducerOfDaemon(producer_base.ProducerOfFile):
    def __init__(self, doc
        , are_name: str
        , script_id: int
        , make_new: bool
        , src: dict
        , src_sec: dict
    ):
        template_path = doc.get_path_template_daemon_file()
        out_path = doc.get_path_out_daemon_file(are_name, script_id)
        super().__init__(doc, out_path=out_path, template_path=template_path, make_new=make_new, src=src)

        self.are_name = are_name
        self.script_id = script_id
        self.src_sec = src_sec
        return

    def get_eligible_actor_recs(self):
        for rec in self.src['actors']:
            if not rec['DefaultHiddenCalc']:
                yield rec
        return

    def produce(self, skip_bcs: bool = False):
        self.produce_npcs('place_npcs')
        if not skip_bcs:
            self.produce_bcs('place_bcs')
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
            if not hidden:
                if ctrl_class:
                    self.writeline(f'ctrl_class, loc = {class_file}.{ctrl_class},  utils_obj.sec2loc({int(x)}, {int(y)})')
                    self.writeline(f'self.create_npc_at(loc, ctrl_class, {direction}, "{name}", 0, 1)')
            self.writeline()
        #self.writeline()
        self.indent(False)
        if not self.current_line_id:
            self.writeline(f"return")
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

    def produce_bcs(self, def_name: str):
        subline = f"def {def_name}("
        self.current_line_id = common.lines_after_before_cutoff(self.lines, subline, '\t\treturn')
        self.indent()
        if not self.current_line_id:
            self.writeline(f"def {def_name}(self):")
        self.indent()

        file_name = None

        area_script = self.src["AreaScript"]
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