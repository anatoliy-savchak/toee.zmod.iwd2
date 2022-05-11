from asyncore import write
import os
import producer_base
import produce_scripts
import common

class ProduceBCSManager(producer_base.Producer):
    def __init__(self, doc):
        super().__init__(doc)
        return

    def get_bc(self, bcs_name: str):
        return self.index_file.get(bcs_name)

    def set_bc(self, bcs_name: str, class_name: str, file_name: str, pkg: str):
        rec = (class_name, file_name, pkg)
        self.index_file[bcs_name] = rec
        return rec

    def ensure_bcs(self, bcs_name: str
        , hint_are_name: str = None
        , hint_cre_name: str = None
        , hint_actor_name: str = None
        , hint_script_code: str = None
    ):
        tup = self.get_bc(bcs_name)
        if tup:
            return tup

        prod_auto = ProduceBCSFileAuto(doc=self.doc, bcs_name = bcs_name, are_name = hint_are_name, make_new=True)
        prod_auto.produce(cre_name=hint_cre_name, actor_name=hint_actor_name, script_code=hint_script_code)
        prod_auto.save()
        ctrl_name_auto, file_name_auto, pkg_name_auto = prod_auto.get_ctrl_tuple()
        self.set_bc(bcs_name, ctrl_name_auto, file_name_auto, pkg_name_auto)
        
        prod_manual = ProduceBCSFileManual(doc=self.doc, bcs_name = bcs_name, are_name = hint_are_name, base_file_name=file_name_auto, base_name=ctrl_name_auto, make_new=False)
        prod_manual.produce(cre_name=hint_cre_name, actor_name=hint_actor_name, script_code=hint_script_code)
        prod_manual.save()
        ctrl_name, file_name, pkg_name = prod_manual.get_ctrl_tuple()
        return self.set_bc(bcs_name, ctrl_name, file_name, pkg_name)

class ProduceBCSFileBase(producer_base.ProducerOfFile):
    def get_ctrl_tuple(self): return (
        self.ctrl_name
        , os.path.basename(self.out_path).replace('.py', '')
        , os.path.basename(os.path.dirname(self.out_path))
    )

class ProduceBCSFileAuto(ProduceBCSFileBase):
    def __init__(self, doc
        , bcs_name: str
        , are_name: str
        , make_new: bool
        , ancestor_class: str = None
    ):
        template_path = doc.get_path_template_are_bcs_auto_file()
        out_path = self.calc_ctrl_file_name(doc, bcs_name, True)
        super().__init__(doc, out_path, template_path, make_new)

        self.bcs_name = bcs_name
        self.are_name = are_name
        self.ctrl_name = self.calc_ctrl_name(self.bcs_name)
        if not ancestor_class: ancestor_class = 'inf_scripting.ScriptBase'
        self.ancestor_class = ancestor_class

        fn = bcs_name + '.BAF'
        fn = os.path.join(self.doc.baf_dir, fn)
        if os.path.exists(fn):
            with open(fn, 'r') as f:
                self.script_lines = f.readlines()
        else:
            print(f'Script {fn} does not exists!')
            self.script_lines = list()
        return

    @classmethod
    def calc_ctrl_name(cls, bcs_name: str):
        return f'Script_{bcs_name}_Auto'

    @classmethod
    def calc_ctrl_file_name(cls, doc, bcs_name: str, full: bool):
        out_path = doc.get_path_out_are_bcs_auto_file(bcs_name)
        if full: return out_path
        return os.path.basename(out_path).replace('.py', '')

    def produce(self, cre_name: str = None, actor_name: str = None, script_code: str = None, parent_producer = None):
        blocks = self._parse_blocks()
        self.writeline(f'class {self.ctrl_name}({self.ancestor_class}): # {self.bcs_name}')
        self.indent()
        self.writeline(f'# {self.are_name}{str((" "+cre_name) if cre_name else "")}{str((" "+actor_name) if actor_name else "")}{str((" "+script_code) if script_code else "")}')
        self.writeline()
        self.writeline('@classmethod')
        self.writeline('def do_execute(cls, self, continuous):')
        self.indent()
        self.writeline('assert isinstance(self, inf_scripting.InfScriptSupport)')

        self.writeline('while True:')
        self.indent()
        for index, block in enumerate(blocks):
            if block.get("unreachable"):
                print("unreachable")
                continue

            block_index = index + 1
            block["index"] = block_index
            if_lines = self.script_lines[block["if"]["start_index"]:int(block["if"]["last_index"])+1]
            block["if_lines"] = if_lines
            if_lines_translated = self.doc.producerOfScripts.transate_trigger_lines(if_lines, are_name = self.are_name, cre_name = cre_name, actor_name = actor_name)
            block["if_lines_translated"] = if_lines_translated
            resp_lines = self.script_lines[block["then"][0]["start_index"]:int(block["then"][0]["end_index"])+1]
            block["resp_lines"] = resp_lines
            is_continue = False
            resp_lines_stripped = list()
            for line in resp_lines:
                if 'continue' in line.strip().lower():
                    is_continue = True
                    continue
                resp_lines_stripped.append(line)
            block["resp_lines_stripped"] = resp_lines_stripped
            block["is_continue"] = is_continue

            resp_lines_translated = self.doc.producerOfScripts.transate_action_lines_complex(resp_lines_stripped
                , cre_name=cre_name, actor_name=actor_name, script_code=script_code, bcs_name=self.bcs_name, are_name=self.are_name, file_producer = self)
            block["resp_lines_translated"] = resp_lines_translated
            block_name = f'do_execute_block_{block_index:02d}'
            block["block_name"] = block_name

            self.writeline(f'break_ = cls.{block_name}()')
            self.writeline('if break_ and not continuous: break')
            self.writeline()
            # self.writeline('')
        self.writeline('break # while')
        self.indent(False)
        self.writeline('return')
        self.writeline('')
        self.indent(False)

        for index, block in enumerate(blocks):
            block_index = block.get("index")
            if not block_index:
                continue
            block_name = block["block_name"]
            if_lines = block["if_lines"]
            resp_lines = block["resp_lines"]
            resp_lines_stripped = block["resp_lines_stripped"]
            resp_lines_translated = block["resp_lines_translated"]
            is_continue = block["is_continue"]

            self.writeline('@classmethod')
            self.writeline(f'def {block_name}(cls, self):')
            self.indent()
            self.writeline('assert isinstance(self, inf_scripting.InfScriptSupport)')
            for line in if_lines:
                self.writeline(f'# {line.strip()}')

            for line in if_lines_translated:
                self.writeline(f'{line}')
            self.indent()

            for line in resp_lines:
                self.writeline(f'# {line.strip()}')

            for line in resp_lines_translated:
                self.writeline(f'{line}')

            if not is_continue:
                self.writeline('return True # break further blocks')
            else:
                self.writeline('return False # continue() - pass further blocks')
            self.indent(False)

            self.writeline('return False')
            self.writeline('')
            self.indent(False)

        self.produce_imports()

        return

    def scan(self, cre_name: str = None, actor_name: str = None):
        blocks = self._parse_blocks()
        for block in blocks:
            if block.get("unreachable"): 
                continue
            if_lines = self.script_lines[block["if"]["start_index"]:int(block["if"]["last_index"])+1]
            if_lines_translated = self.doc.producerOfScripts.transate_trigger_lines(if_lines, are_name = self.are_name, cre_name = cre_name, actor_name = actor_name)
            resp_lines = self.script_lines[block["then"][0]["start_index"]:int(block["then"][0]["end_index"])+1]
            is_continue = False
            resp_lines_stripped = list()
            for line in resp_lines:
                if 'continue' in line.strip().lower():
                    is_continue = True
                    continue
                resp_lines_stripped.append(line)
            resp_lines_translated = self.doc.producerOfScripts.transate_action_lines(resp_lines_stripped, are_name = self.are_name, cre_name = cre_name, bcs_name = self.bcs_name)
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

        subsequent_blocks_are_unreachable = False
        for block in blocks:
            if subsequent_blocks_are_unreachable:
                block["unreachable"] = True
            if (block["if"]["start_index"] == block["if"]["last_index"]
                and self.script_lines[block["if"]["start_index"]].lower() == 'true()'):
                subsequent_blocks_are_unreachable = True

        return blocks

class ProduceBCSFileManual(ProduceBCSFileBase):
    def __init__(self, doc
        , bcs_name: str
        , are_name: str
        , base_file_name: str
        , base_name: str
        , make_new: bool
    ):
        template_path = doc.get_path_template_are_bcs_manual_file()
        #out_path = doc.get_path_out_are_bcs_manual_file(are_name, script_id)
        out_path = self.calc_ctrl_file_name(doc, bcs_name, True)
        super().__init__(doc, out_path, template_path, make_new)

        self.bcs_name = bcs_name
        self.are_name = are_name
        self.base_file_name = base_file_name
        self.base_name = base_name
        self.ctrl_name = self.calc_ctrl_name(self.bcs_name)
        return

    @classmethod
    def calc_ctrl_name(cls, bcs_name: str):
        return f'Script_{bcs_name}'

    @classmethod
    def calc_ctrl_file_name(cls, doc, bcs_name: str, full: bool):
        out_path = doc.get_path_out_are_bcs_manual_file(bcs_name)
        if full: return out_path
        return os.path.basename(out_path).replace('.py', '')

    def produce(self, cre_name: str = None, actor_name: str = None, script_code: str = None):
        line1 = f'class {self.ctrl_name}('
        if next((line for line in self.lines if line1 in line), None):
            return False

        line2 = f'{self.base_file_name}.{self.base_name}): ' # leave trailing whitespace here
        self.writeline(line1 + line2)
        self.indent()
        self.writeline(f'# {self.are_name}{str((" "+cre_name) if cre_name else "")}{str((" "+actor_name) if actor_name else "")}{str((" "+script_code) if script_code else "")}')
        self.writeline('pass')
        self.indent(False)
        self.writeline()

        import_line = 'import ' + self.base_file_name
        if not next((line for line in self.lines if line == import_line or line == import_line + '\n'), None):
            #line_id = common.lines_after_before_cutoff(self.lines, '#### IMPORT ####', '#### IMPORT END ####')
            line_id = common.lines_find(self.lines, '#### IMPORT ####')
            if line_id:
                self.current_line_id = line_id+1
                self.writeline(import_line)
                self.current_line_id = -1

        return True
