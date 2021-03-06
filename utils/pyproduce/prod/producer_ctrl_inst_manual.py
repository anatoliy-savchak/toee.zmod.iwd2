import os
import producer_base
import common

class ProducerOfCtrlInstManual(producer_base.ProducerOfFile):
    def __init__(self, doc
        , cre_name: str
        , are_name: str
        , script_id: int
        , make_new: bool
        , base_class: tuple
        , actor_name: str
    ):
        template_path = doc.get_path_template_npcs_class_inst_manual_file()
        out_path = doc.get_path_out_npcs_class_inst_manual_file(are_name, script_id)
        src_path = doc.get_path_cre(cre_name)
        super().__init__(doc, out_path=out_path, template_path=template_path, make_new=make_new, src_path=src_path)

        self.cre_name = cre_name
        self.are_name = are_name
        self.script_id = script_id
        self.base_class = base_class
        self.actor_name = actor_name
        self.ctrl_name = f'Ctrl_{self.cre_name}_{self.are_name}_{common.str_to_name(self.actor_name)}'
        return

    def produce(self):
        line1 = f'class {self.ctrl_name}('
        if next((line for line in self.lines if line1 in line), None):
            return
            
        self.add_import(self.base_class["file_name"])
        line2 = f'{self.base_class["file_name"]}.{self.base_class["class_name"]}): # {self.cre_name} ' # leave trailing whitespace here
        self.writeline(line1 + line2)
        self.indent()
        self.writeline('pass')
        self.indent(False)
        self.writeline('')
        self.produce_imports()
        return

    def get_ctrl_tuple(self): return (self.ctrl_name, os.path.basename(self.out_path).replace('.py', ''))
