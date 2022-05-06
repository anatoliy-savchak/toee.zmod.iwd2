import os

class ProduceBCSManager(object):
    def __init__(self, app):
        self.app = app
        self.dict_index = dict()
        return

    def ensure_bcs(self, bcs_name: str, file_path_out: str):
        result = self.get_bc(bcs_name)
        if not result:
            pass
        return

    def get_bc(self, bcs_name: str):
        return self.dict_index.get(bcs_name)

    def produce_bcs(self, bcs_name: str, file_path_out: str):
        fn = bcs_name + '.BAF'
        fn = os.path.join(self.app.baf_dir, fn)
        with open(fn, 'r') as f:
            script_lines = f.readlines()

        fn = self.app.get_bcs_template_path()
        if os.path.exists(file_path_out):
            fn = file_path_out
        with open(fn, 'r') as f:
            lines = f.readlines()

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

        for i, line in enumerate(script_lines):
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

            if lline.startswith("\tresponse"):
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

        print(blocks)

        return