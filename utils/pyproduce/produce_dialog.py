import os
import re
import produce_scripts

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

        if self.dialog_name == "10JORUN": # debug!
            print("")

        #self.parent.current_indent = "\t"
        # self.parent._indent(False)
        # self._add_line("def dialog(self, attachee, triggerer):")
        # self.parent._indent(True)
        # self._add_line("assert isinstance(attachee, toee.PyObjHandle)")
        # self._add_line("assert isinstance(triggerer, toee.PyObjHandle)")
        # self._add_line("")
        # self._add_line("try:")
        # self.parent._indent(True)
        # self._add_line('self.vars["attachee"] = attachee')
        # self._add_line('self.vars["triggerer"] = triggerer')
        # self._add_line("")
        # self._add_line("self.script_dialog(attachee, triggerer)")
        # self.parent._indent(False)
        # self._add_line("finally:")
        # self.parent._indent(True)
        # self._add_line('self.vars["attachee"] = None')
        # self._add_line('self.vars["triggerer"] = None')
        # self.parent._indent(False)
        # self._add_line("")
        # self._add_line("return toee.SKIP_DEFAULT")
        # self._add_line("")

        self.parent._indent(False)
        self._add_line("def script_dialog(self, attachee, triggerer):")
        self.parent._indent(True)
        #self._add_line(f"# {self.dialog_name}")
        self._add_line(f'print("script_dialog {self.dialog_name}")')
        self._add_line("assert isinstance(attachee, toee.PyObjHandle)")
        self._add_line("assert isinstance(triggerer, toee.PyObjHandle)")
        self._add_line("")
        self._add_line("attachee.turn_towards(triggerer)")
        self._add_line("")
        self._add_line('line_id = -1')
        self._add_line("while True:")
        self.parent._indent(True)

        for phrase in phrases:
            triggerIndex = int(phrase["TriggerIndex"])
            if triggerIndex == -1: continue

            phase_index = phrase["Index"]
            self._add_line(f'print("STATE {phase_index}")')
            #self._add_line(f'# STATE {phase_index}')

            trigger = triggersPhrase[triggerIndex]
            trigger_lines = produce_scripts.condition_split(trigger)
            for trigger_line in trigger_lines:
                self._add_line(f"# {trigger_line}")

            out_lines = produce_scripts.transate_trigger_lines(trigger_lines)
            for l in out_lines:
                self._add_line(l)
                
            phrase_text = phrase["Text"]["Text"]
            phrase_text = text_strip_directions(phrase_text)
            line_id = self.dialog_file.add_phrase(phrase_text)

            self.parent._indent(True)
            #self._add_line(f'triggerer.begin_dialog(attachee, {line_id}) # {phrase_text}')
            self._add_line(f'line_id = {line_id} # {phrase_text}')
            self._add_line(f'print("STATE {phase_index}: line_id = {line_id}")')
            self._add_line('break')
            self.parent._indent(False)
            self._add_line("")

        self._add_line("break # while")
        self._add_line("")
        self.parent._indent(False)
        self._add_line('print("script_dialog line_id: {}".format(line_id))')
        self._add_line('if line_id >= 0:')
        self._add_line(f'\ttriggerer.begin_dialog(attachee, line_id)')
        self._add_line("")
        self._add_line("return # script_dialog")
        self.parent._indent(False)
        self._add_line("")
        return

    def save(self):
        self.dialog_file.save()
        return

    def translate_trigger(self, trigger: str):
        # should produce if (conditions):
        return

    def translate_trigger_line(self, trigger_line: str):
        # should produce condition:
        return