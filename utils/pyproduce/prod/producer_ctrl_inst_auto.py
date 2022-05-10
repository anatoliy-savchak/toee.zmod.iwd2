import os
import producer_base
import common

class ProducerOfCtrlInstAuto(producer_base.ProducerOfFile):
    def __init__(self, doc
        , cre_name: str
        , are_name: str
        , script_id: int
        , make_new: bool
        , base_class: str
        , actor_name: str
        , actor_dict: dict
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
        self.ctrl_name = f'Ctrl_{self.cre_name}_{self.are_name}_{self.actor_name}_Auto'
        self.produce_imports(clear=make_new)
        return

    def produce(self):
        line1 = f'class {self.ctrl_name}('
        if next((line for line in self.lines if line1 in line), None):
            return

        self.add_import(self.base_class["file_name"])

        line2 = f'{self.base_class["file_name"]}.{self.base_class["class_name"]}): # {self.cre_name} ' # leave trailing whitespace here
        self.writeline(line1 + line2)
        self.indent()
        self.writeline('def setup_bcs(self):')

        def write_script(bcs_attribute: str, script_name: str):
            bcs_name = self.actor_dict[bcs_attribute]
            if bcs_name:
                ctrl_name, file_name, pkg_name = self.doc.bcsManager.ensure_bcs(
                    bcs_name=bcs_name
                    , hint_are_name=self.are_name
                    , hint_cre_name=self.cre_name
                    , hint_actor_name=self.actor_name
                    , hint_script_code=bcs_attribute
                )
                self.add_import(file_name, pkg_name)

                self.writeline(f'self.vars["{script_name}"] = {file_name}.{ctrl_name}')

            return
        self.indent()
        write_script("ScriptGeneral", 'bcs_general')
        write_script("ScriptClass", 'bcs_class')
        write_script("ScriptRace", 'bcs_combat')
        write_script("ScriptDefault", 'bcs_movement')
        write_script("ScriptSpecific", 'bcs_team')
        write_script("ScriptSpecial1", 'bcs_special_one')
        self.writeline('return')
        self.indent(False)
        self.indent(False)
        self.writeline('')

        self.produce_imports()
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
