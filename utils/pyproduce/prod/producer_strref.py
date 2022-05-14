import os
import producer_base
import common

class ProducerOfFloats(producer_base.ProducerOfFile):
    def __init__(self, doc, make_new: bool):
        out_path = os.path.join(doc.core_dir, 'mes', 'floats.mes')
        template_path = 'data/empty.mes'
        src_path = os.path.join(doc.exp_dir, 'Text', 'strrefs_all.json')
        super().__init__(doc, out_path, template_path, make_new, src_path)

        self.strrefs = common.parse_mes_lines(self.lines, True)
        return

    def ensure_str_ref(self, strref: int):
        if strref in self.strrefs.keys():
            return
        text_rec = self.get_str_ref_rec(strref)
        if text_rec:
            text = text_rec["Text"]
            if text:
                text = common.strip_quotes(text)
            if (sound := text_rec["Sound"]) and sound.strip():
                print(sound)
                pass
            self.strrefs[strref] = text
            self.save()
        #self.writeline(f'{{{strref}}}{{{text}}}')
        return

    def get_str_ref_rec(self, strref: int):
        return next((rec for rec in self.src["Strings"] if rec["Strref"] == strref), None)

    def get_str_ref(self, strref: int):
        text_rec = self.get_str_ref_rec(strref)
        if text_rec:
            text = text_rec["Text"]
            if text:
                text = common.strip_quotes(text)
            if (sound := text_rec["Sound"]) and sound.strip():
                print(sound)
                pass
            return text
        return

    def save(self):
        self.lines.clear()
        for key, text in sorted(self.strrefs.items()):
            self.writeline(f'{{{key}}}{{{text}}}')
        return super().save()