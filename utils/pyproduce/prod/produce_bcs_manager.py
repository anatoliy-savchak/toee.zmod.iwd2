import os
import producer_base
import produce_scripts


class ProduceBCSManager(producer_base.Producer):
    def __init__(self, doc):
        super().__init__(doc)
        return

    def get_bc(self, bcs_name: str):
        return self.index_file.get(bcs_name)

    def set_bc(self, bcs_name: str, file_name: str, class_name: str):
        rec = (file_name, class_name)
        self.index_file[bcs_name] = rec
        return

class ProduceBCSFile(producer_base.ProducerOfFile):
    def __init__(self, doc
        , bcs_name: str
        , are_name: str
        , script_id: int
        , make_new: bool
    ):
        template_path = doc.get_path_template_are_bcs_file()
        out_path = doc.get_path_out_are_bcs_file(are_name, script_id)
        super().__init__(doc, out_path, template_path, make_new)

        self.bcs_name = bcs_name
        self.ctrl_name = f'Script_{self.bcs_name}'

        fn = bcs_name + '.BAF'
        fn = os.path.join(self.doc.baf_dir, fn)
        with open(fn, 'r') as f:
            self.script_lines = f.readlines()
        return

    def produce(self, def_name: str):
        blocks = self._parse_blocks()
        self.writeline(f'class {self.ctrl_name}(object):')
        self.indent()
        self.writeline()
        self.writeline(f'def {def_name}(self, npc):')
        self.indent()

        self.writeline('while True:')
        self.indent()
        for block in blocks:
            if_lines = self.script_lines[block["if"]["start_index"]:int(block["if"]["last_index"])+1]
            if_lines_translated = produce_scripts.transate_trigger_lines(if_lines, self.doc)
            for line in if_lines:
                self.writeline(f'# {line.strip()}')

            for line in if_lines_translated:
                self.writeline(f'{line}')
            self.indent()

            resp_lines = self.script_lines[block["then"][0]["start_index"]:int(block["then"][0]["end_index"])+1]
            is_continue = False
            resp_lines_stripped = list()
            for line in resp_lines:
                if 'continue' in line.strip().lower():
                    is_continue = True
                    continue
                resp_lines_stripped.append(line)
            resp_lines_translated = produce_scripts.transate_action_lines(resp_lines_stripped, self.doc)

            for line in resp_lines:
                self.writeline(f'# {line.strip()}')

            for line in resp_lines_translated:
                self.writeline(f'{line}')

            if not is_continue:
                self.writeline('break')
            else:
                self.writeline('pass # continue() - let it pass below')
            self.indent(False)
            self.writeline('')
        self.writeline('break # while')
        self.indent(False)
        self.writeline('return')
        self.writeline('')
        return

    def _parse_blocks(self):
        # block(if_index, end_index, if_body(start_index, last_index), then(sub(start_index, end_index, has_continue), ...))
        blocks = list()
        block_started = False
        if_started = False
        then_started = False
        resp_started = False
        block = dict()
        if_dict = dict()
        then_list = list()
        resp_dict = dict()

        for i, line in enumerate(self.script_lines):
            lline = line.lower().strip()

            if lline == "if":
                block_started = True
                if_started = True
                block = dict()
                block["if_index"] = i
                if_dict = dict()
                if_dict["start_index"] = i + 1
                continue
            
            if lline == "then":
                if_started = False
                then_started = True
                if_dict["last_index"] = i - 1
                then_list = list()
                continue

            if lline == "end":
                block_started = False
                if resp_started:
                    resp_started = False
                    resp_dict["end_index"] = i-1
                    then_list.append(resp_dict)
                then_started = False
                block["end_index"] = i
                block["if"] = if_dict
                block["then"] = then_list
                blocks.append(block)
                block = None
                continue

            if lline.startswith("response"):
                #00MONKS5
                if resp_started:
                    resp_started = False
                    resp_dict["end_index"] = i-1
                    then_list.append(resp_dict)
                resp_started = True
                resp_dict = dict()
                resp_started = True
                resp_dict["start_index"] = i + 1
                resp_dict["resp_index"] = i
                continue

            if resp_started and 'continue' in lline:
                resp_dict["continue_index"] = i
        return blocks

    def get_ctrl_tuple(self): return (self.ctrl_name, os.path.basename(self.out_path).replace('.py', ''))
