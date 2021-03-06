import os
import producer_base
import common

class ProducerOfCtrlManual(producer_base.ProducerOfFile):
    def __init__(self, doc
        , cre_name: str
        , are_name: str
        , script_id: int
        , make_new: bool
        , base_class: str
    ):
        template_path = doc.get_path_template_npcs_class_manual_file()
        out_path = doc.get_path_out_npcs_class_manual_file(are_name, script_id)
        src_path = doc.get_path_cre(cre_name)
        super().__init__(doc, out_path=out_path, template_path=template_path, make_new=make_new, src_path=src_path)

        self.cre_name = cre_name
        self.are_name = are_name
        self.script_id = script_id
        self.base_class = base_class
        self.ctrl_name = f'Ctrl_{self.cre_name}'
        return

    @classmethod
    def overwrite_by_template(cls, doc, are_name, script_id):
        template_path = doc.get_path_template_npcs_class_manual_file()
        out_path = doc.get_path_out_npcs_class_manual_file(are_name, script_id)
        with open(template_path, 'r') as fs:
            with open(out_path, 'w') as fo:
                fo.writelines(fs.readlines())
        return

    def produce(self):
        line1 = f'class {self.ctrl_name}('
        if next((line for line in self.lines if line1 in line), None):
            return

        line2 = f'{self.base_class["file_name"]}.{self.base_class["class_name"]}): # {self.cre_name} ' # leave trailing whitespace here
        self.writeline(line1 + line2)
        self.indent()
        self.writeline('pass')
        self.indent(False)
        self.writeline('')
        self.add_import(self.base_class["file_name"])
        self.produce_imports()
        return

    def get_ctrl_tuple(self): return (self.ctrl_name, os.path.basename(self.out_path).replace('.py', ''))
