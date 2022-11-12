import os
import producer_base
import common
import produce_dialog
import json

class ProducerOfCtrlInstAuto(producer_base.ProducerOfFile):
    def __init__(self, doc
        , cre_name: str
        , are_name: str
        , script_id: int
        , make_new: bool
        , base_class: str
        , actor_name: str
        , actor_dict: dict
        , dialog_file: object
    ):
        template_path = doc.get_path_template_npcs_class_inst_auto_file()
        out_path = doc.get_path_out_npcs_class_inst_auto_file(are_name, script_id)
        src_path = doc.get_path_cre(cre_name)
        super().__init__(doc, out_path=out_path, template_path=template_path, make_new=make_new, src_path=src_path)

        self.cre_name = cre_name
        self.are_name = are_name
        self.script_id = script_id
        self.base_class = base_class
        self.actor_name = actor_name
        self.actor_dict = actor_dict
        self.dialog_file = dialog_file
        self.cre = None

        self.ctrl_name = f'Ctrl_{self.cre_name}_{self.are_name}_{common.str_to_name(self.actor_name)}_Auto'
        self.produce_imports(clear=make_new)
        self.skip_script_general = False
        self.skip_script_class = False
        self.skip_script_race = False
        self.skip_script_default = False
        self.skip_script_specific = False
        self.skip_script_special1 = False

        self.team_number = None
        return

    def produce(self):
        line1 = f'class {self.ctrl_name}('
        if next((line for line in self.lines if line1 in line), None):
            return

        self.add_import(self.base_class["file_name"])

        line2 = f'{self.base_class["file_name"]}.{self.base_class["class_name"]}): # {self.cre_name} ' # leave trailing whitespace here
        self.writeline(line1 + line2)
        self.indent()

        self.writeline('@classmethod')
        self.writeline('def get_difficulty_mask(cls):')
        self.indent()
        self.writeline(f'return {self.actor_dict["AreaDifficultyMask"]}')
        self.indent(False)
        self.writeline()

        team_script_name = self.actor_dict["ScriptSpecific"]
        self.writeline('@classmethod')
        self.writeline('def get_team_number(cls):')
        self.indent()
        self.team_number, comment = self.extract_team_number(team_script_name)
        self.writeline(f'return {self.team_number} # {comment}')
        self.indent(False)
        self.writeline()

        self.writeline('def setup_bcs(self):')

        def write_script(bcs_attribute: str, script_name: str, mode_simple: bool = None):
            bcs_name = self.actor_dict[bcs_attribute]
            if bcs_name:
                ctrl_name, file_name, pkg_name = self.doc.bcsManager.ensure_bcs(
                    bcs_name=bcs_name
                    , hint_are_name=self.are_name
                    , hint_cre_name=self.cre_name
                    , hint_actor_name=self.actor_name
                    , hint_script_code=bcs_attribute
                    , mode_simple=mode_simple
                )
                self.add_import(file_name, pkg_name)

                self.writeline(f'self.vars["{script_name}"] = {file_name}.{ctrl_name}')

            return
        self.indent()
        if not self.skip_script_general:
            write_script("ScriptGeneral", 'bcs_general')
        if not self.skip_script_class:
            write_script("ScriptClass", 'bcs_class')
        if not self.skip_script_race:
            write_script("ScriptRace", 'bcs_combat', True)
        if not self.skip_script_default:
            write_script("ScriptDefault", 'bcs_movement')
        if not self.skip_script_specific:
            write_script("ScriptSpecific", 'bcs_team')
        if not self.skip_script_special1:
            write_script("ScriptSpecial1", 'bcs_special_one')
        self.writeline('return')
        self.indent(False)
        self.indent(False)
        self.writeline('')

        self.produce_dialog()
        self.produce_npc_script_hooks()
        self.produce_imports()

        self.current_line_id = common.lines_after_before_cutoff(self.lines, '#### GVARS ####', '#### GVARS END ####')
        if self.current_line_id and self.current_line_id > 0:
            self.writeline(f'MODULE_SCRIPT_ID = {self.script_id}')
            self.current_line_id = -1

        return

    def get_ctrl_tuple(self): return (self.ctrl_name, os.path.basename(self.out_path).replace('.py', ''))

    @classmethod
    def overwrite_by_template(cls, doc, are_name, script_id):
        template_path = doc.get_path_template_npcs_class_inst_auto_file()
        out_path = doc.get_path_out_npcs_class_inst_auto_file(are_name, script_id)
        with open(template_path, 'r') as fs:
            with open(out_path, 'w') as fo:
                fo.writelines(fs.readlines())
        return

    def extract_team_number(self, script_name):
        if not script_name: return 0, "no team script"
        script_lines = None
        fn = script_name + '.BAF'
        fn = os.path.join(self.doc.baf_dir, fn)
        fn_override = fn.replace('.BAF', '_override.BAF')
        if os.path.exists(fn_override):
            with open(fn_override, 'r') as f:
                script_lines = f.readlines()
        elif os.path.exists(fn):
            with open(fn, 'r') as f:
                script_lines = f.readlines()
        else:
            print(f'Script {fn} does not exists!')
        
        if script_lines: 
            for i in range(21):
                query_line = f'SetTeamBit(TEAM_{i}_BIT,TRUE)'.lower()
                line = next((line for line in script_lines if query_line in line.lower()), None)
                if line: return i, line.strip()

        return 0, f"incorrect script: {script_name}"

    def produce_dialog(self):
        dialog_name = self.actor_dict["Dialog"]
        if not dialog_name or dialog_name == "None":
            return
        fn = os.path.join(self.doc.exp_dir, 'Dialogs', dialog_name + '.json')
        dialog_dict = common.read_file_json(fn)
        self.dialog = produce_dialog.ProduceNPCDialog(dialog_name, self, dialog_dict, self.dialog_file)
        if not self.cre:
            cre_path = self.doc.get_path_cre(self.cre_name)
            if os.path.exists(cre_path):
                with open(cre_path, encoding='utf-8', mode='r') as f:
                    self.cre = json.load(f)

        self.indent(True)
        self.dialog.produce(self.are_name, self.cre_name)
        self.indent(False)
        return

    def produce_npc_script_hooks(self):
        dialog_name = self.actor_dict["Dialog"]
        if not dialog_name or dialog_name == "None":
            return
        self.writeline("def setup_scripts(self, npc):")
        self.indent(True)
        self.writeline(f'super({self.ctrl_name}, self).setup_scripts(npc)')
        self.writeline("npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID")
        self.writeline("self.enable_dialog(npc)")
        self.writeline("return")
        self.indent(False)
        self.writeline("")
        return
