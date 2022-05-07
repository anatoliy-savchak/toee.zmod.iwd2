import os
import json
import producer_doc

class Producer(object):
    def __init__(self
        , doc
        , src_path: str = None
        , src: dict = None
        , index_path: str = None
    ):
        self.doc = doc
        self.src_path = src_path
        self.src = src
        self.index_path = index_path
        self.index_file = dict()

        self._load_src()
        self._load_index_file()
        return

    def _load_src(self):
        if not self.src:
            if not self.src_path is None and os.path.exists(self.src_path):
                with open(self.src_path, encoding='utf-8', mode='r') as f:
                    self.src = json.load(f)
            else:
                self.src = dict()
        return

    def _load_index_file(self):
        if self.index_path and os.path.exists(self.index_path):
            with open(self.index_path, encoding='utf-8', mode='r') as f:
                self.index_file = json.load(f)
        else:
            self.index_file = dict()
        return

    def _save_index(self):
        if self.index_path and self.index_file:
            with open(self.index_path, 'w') as f:
                json.dump(self.index_file, f, indent=4)
                return

class ProducerOfFile(Producer):
    def __init__(self
        , doc
        , out_path: str
        , template_path: str
        , make_new: bool
        , src_path: str = None
        , src: dict = None
    ):
        super().__init__(doc, src_path, src)

        self.out_path = out_path
        self.template_path = template_path
        self.make_new = make_new

        self.current_line_id = -1
        self.current_indent = ''

        self.lines = list()
        self._preload_lines()
        return

    def _preload_lines(self):
        fn = self.out_path
        if self.make_new or not os.path.exists(self.out_path):
            fn = self.template_path
        with open(fn, 'r') as f:
            self.lines = f.readlines()
        return

    def save(self):
        with open(self.out_path, 'w') as f:
            for line in self.lines:
                f.write(line + ("\n" if not "\n" in line else ""))
        return

    def writeline(self, line: str = ''):
        if self.current_line_id is None or self.current_line_id < 0:
            self.lines.append(self.current_indent + line)
        else:
            self.lines.insert(self.current_line_id, self.current_indent + line)
            self.current_line_id += 1
        return

    def indent(self, forward: bool = True):
        if not forward:
            self.current_indent = self.current_indent[:-1]
        else:
            self.current_indent += "\t"
        return
