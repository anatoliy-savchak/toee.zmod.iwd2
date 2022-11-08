import json

class JournalFile:
    def __init__(self):
        self.data = dict();
        self.text_max_len = 113
        self.lines = dict()
        self.last_line_id = -1
        return

    def _add_line(self, text: str, strref: int):
        self.last_line_id += 1
        self.lines[self.last_line_id] = (text, strref)

        return self.last_line_id

    def load_iwd_journal(self, file_path: str):
        with open(file_path, 'r') as f:
            j = json.load(f)

        self.data = j["Entries"]
        for entry in self.data:
            strref = int(entry["Strref"])
            text = str(entry["Text"])
            if text:
                if len(text) > self.text_max_len:
                    words = text.split(' ')
                    text = ""
                    for word in words:
                        if len(text + (" " if text else "") + word) > self.text_max_len:
                            self._add_line(text, strref)
                            text = "..."

                        text = text + (" " if text else "") + word
                self._add_line(text, strref)
        return

    def produce_rumors(self, out_file_path: str, template_file_path: str):
        with open(template_file_path, 'r') as fi:
            lines = fi.readlines()

        for rumor_id, rec in self.lines.items():
            text = rec[0]
            lines.append(f'{{{rumor_id*10}}} {{{text}}}')
            lines.append(f'{{{rumor_id*10+1}}} {{{text}}}')
            lines.append('')

        with open(out_file_path, 'w') as f:
            for line in lines:
                f.write(line + ("\n" if not "\n" in line else ""))

        return

    def get_rumors_by_strref(self, strref: int):
        q = [str(rumor_id) for rumor_id, rec in self.lines.items() if rec[1] == strref]
        if len(q) == 0: 
            return None
        result = "(" + ", ".join(q) + ", )"
        return result

    def save_map(self, file_path: str):
        with open(file_path, 'w') as f:
            json.dump(self.lines, f, indent=4)
        return

    def load_map(self, file_path: str):
        with open(file_path, 'r') as f:
            self.lines = json.load(f)
        return