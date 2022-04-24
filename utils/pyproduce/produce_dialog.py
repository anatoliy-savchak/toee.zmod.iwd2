import os
import re

class DialogFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.line_tups = list()
        self.last_num = 0
        return

    def add_phrase(self, text: str, speech_id: int = None, effect_code: str = None):
        # {line_id}{text}{text female}{min IQ}{test field|speech_id}{answer key}{effect python}
        line_id = self.last_num + 10
        
        speech_id_str = str(speech_id) if not speech_id is None else ""
        line = f"{{{line_id}}}{{{text}}}{{{text}}}{{}}{{{speech_id_str}}}{{}}{{{str(effect_code or '')}}}"
        if self.last_num:
            self.line_tups.append((None, ""))
        self.line_tups.append((line_id, line))

        self.last_num = line_id
        return line_id

    def save(self):
        with open(self.file_name, 'w') as f:
            for num, line in self.line_tups:
                #aline = line
                f.write(line + ("\n" if not "\n" in line else ""))
        return

class ProduceNPCDialog:
    def __init__(self, dialog_name, parent, dialog: dict, dialog_file: DialogFile):
        self.dialog_name = dialog_name
        self.parent = parent

        self.dialog = dialog
        self.dialog_file = dialog_file
        self.cre = parent.cre
        return

    def _add_line(self, line):
        self.parent._add_line(line)
        return

    def produce(self):
        phrases, responses, triggersPhrase, triggersResponse = self.dialog.get("Phrases"), self.dialog.get("Responses"), self.dialog.get("TriggersPhrase"), self.dialog.get("TriggersResponse")
        if not phrases: return

        def text_strip_directions(text: str):
            return re.sub("[\[].*?[\]]", "", text)

        #self.parent.current_indent = "\t"
        self.parent._indent(False)
        self._add_line("def dialog(self, attachee, triggerer):")
        self.parent._indent(True)
        self._add_line("assert isinstance(attachee, toee.PyObjHandle)")
        self._add_line("assert isinstance(triggerer, toee.PyObjHandle)")

        self._add_line("")
        self._add_line("attachee.turn_towards(triggerer)")
        self._add_line("")
        self._add_line('line_id = -1')

        for phrase in phrases:
            triggerIndex = int(phrase["TriggerIndex"])
            if triggerIndex == -1: continue

            trigger = triggersPhrase[triggerIndex]
            trigger_lines = str(trigger).splitlines(False)
            for trigger_line in trigger_lines:
                self._add_line(f"# {trigger_line}")


            for index, trigger_line in enumerate(trigger_lines):
                is_last_line = index + 1 == len(trigger_lines)
                line = ""
                tline = trigger_line
                if tline == "NumTimesTalkedTo(0)": 
                    tline = "not attachee.has_met(triggerer)"
                elif tline == "NumTimesTalkedToGT(0)": 
                    tline = "attachee.has_met(triggerer)"
                else:
                    tline = "ies." + tline
                if index == 0:
                    line = "if "
                else:
                    line = "\tand "
                line = line + tline + (" \\" if not is_last_line else ":")
                
                self._add_line(line)
                
            phrase_text = phrase["Text"]["Text"]
            phrase_text = text_strip_directions(phrase_text)
            line_id = self.dialog_file.add_phrase(phrase_text)

            self.parent._indent(True)
            #self._add_line(f'triggerer.begin_dialog(attachee, {line_id}) # {phrase_text}')
            self._add_line(f'line_id = {line_id} # {phrase_text}')
            self.parent._indent(False)
            self._add_line("")

        self._add_line('if line_id >= 0:')
        self._add_line(f'\ttriggerer.begin_dialog(attachee, line_id)')
        self._add_line("return toee.SKIP_DEFAULT")
        self.parent._indent(False)
        self._add_line("")
        return

    def save(self):
        self.dialog_file.save()
        return