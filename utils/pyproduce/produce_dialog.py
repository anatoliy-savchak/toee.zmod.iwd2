import os
import re
import produce_scripts

def text_strip_directions(text: str):
    return re.sub("[\[].*?[\]]", "", text)

class DialogFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.line_tups = list()
        self.last_num = 0
        self.last_num_phrase = 0
        self.phrases = dict() # phrase_id : line_id
        return

    def add_phrase(self, phrase_id: int, text: str, speech_id: int = None, effect_code: str = None):
        # {line_id}{text}{text female}{min IQ}{test field|speech_id}{answer key}{effect python}
        line_id = ((self.last_num // 10) + 1)*10
        
        speech_id_str = str(speech_id) if not speech_id is None else ""
        line = f"{{{line_id}}}{{{text}}}{{{text}}}{{}}{{{speech_id_str}}}{{}}{{{str(effect_code or '')}}}"
        if self.last_num:
            self.line_tups.append((None, ""))
        self.line_tups.append((line_id, line))

        self.last_num = line_id
        self.last_num_phrase = line_id
        self.phrases[phrase_id] = line_id
        return line_id

    def add_response(self, text: str, test_field: str = None, answer_id: int = None, effect_code: str = None):
        # {line_id}{text}{text female}{min IQ}{test field|speech_id}{answer key}{effect python}
        line_id = self.last_num + 1
        
        answer_id_str = str(answer_id) if not answer_id is None else ""
        if answer_id == 0:
            answer_id_str = 0
        line = f"{{{line_id}}}{{{text}}}{{}}{{1}}{{{str(test_field or '')}}}{{{answer_id_str}}}{{{str(effect_code or '')}}}"
        self.line_tups.append((line_id, line))

        self.last_num = line_id
        return line_id

    def update_response(self, line_id: int, text: str, test_field: str = None, answer_id: int = None, effect_code: str = None):
        # {line_id}{text}{text female}{min IQ}{test field|speech_id}{answer key}{effect python}
        index = next((i for i, tup in enumerate(self.line_tups) if tup[0] == line_id), None)
        if index is None:
            #print(f'update_response line_id: {line_id} not found!')
            raise Exception(f'update_response line_id: {line_id} not found!')
        
        answer_id_str = str(answer_id) if not answer_id is None else ""
        line = f"{{{line_id}}}{{{text}}}{{}}{{1}}{{{str(test_field or '')}}}{{{answer_id_str}}}{{{str(effect_code or '')}}}"
        self.line_tups[index] = ((line_id, line))

        return line_id

    def find_phrase(self, phrase_id: int):
        line_id = self.phrases.get(phrase_id)
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

        self.trigger_cache = dict()
        self.response_triggers = dict()
        return

    def _add_line(self, line):
        self.parent._add_line(line)
        return

    def produce(self):
        phrases, responses, triggersPhrase, triggersResponse = self.dialog.get("Phrases"), self.dialog.get("Responses"), self.dialog.get("TriggersPhrase"), self.dialog.get("TriggersResponse")
        if not phrases: return


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

            trigger_lines, out_lines = self.calc_trigger(triggersPhrase[triggerIndex])
            for trigger_line in trigger_lines:
                self._add_line(f"# {trigger_line}")
            for l in out_lines:
                self._add_line(l)
                
            line_id, phrase_text = self.process_phrase_dialog(phrase, False)

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

        self._add_line("def dialog_test_do(self, npc, pc, index):")
        self.parent._indent(True)
        #self._add_line(f"# {self.dialog_name}")
        #self._add_line(f'print("dialog_test_do {self.dialog_name}")')
        self._add_line("assert isinstance(npc, toee.PyObjHandle)")
        self._add_line("assert isinstance(pc, toee.PyObjHandle)")
        self._add_line("assert isinstance(index, int)")
        self._add_line("")

        _iff = "if"
        for triggerIndex in sorted(self.response_triggers.keys()):
            self._add_line(f'{_iff} index == {triggerIndex}:')
            _iff = "elif"
            self.parent._indent(True)
            
            trigger_lines, out_lines = self.calc_trigger(triggersResponse[triggerIndex])
            for trigger_line in trigger_lines:
                self._add_line(f"# {trigger_line}")

            for l in out_lines:
                self._add_line(l)

            self.parent._indent(True)
            response_text, resp_line_id = self.response_triggers[triggerIndex]
            self._add_line(f'return True # {resp_line_id}: {response_text}')
            self.parent._indent(False)
            self._add_line("")
            self.parent._indent(False)
        
        self._add_line("return False # dialog_test_do")
        self.parent._indent(False)
        self._add_line("")

        return

    def calc_trigger(self, trigger: dict):
        trigger_lines = produce_scripts.condition_split(trigger)
        out_lines = produce_scripts.transate_trigger_lines(trigger_lines)
        return trigger_lines, out_lines

    def process_phrase_dialog(self, phrase: dict, check_trigger: bool):
        phrase_id = phrase["Index"]
        line_id = self.dialog_file.find_phrase(phrase_id)
        if not line_id is None:
            return line_id, None

        #phrases, responses, triggersPhrase, triggersResponse = self.dialog.get("Phrases"), self.dialog.get("Responses"), self.dialog.get("TriggersPhrase"), self.dialog.get("TriggersResponse")

        if check_trigger:
            triggerIndex = int(phrase["TriggerIndex"])
            if triggerIndex != -1: 
                raise Exception("Phrase should not have triggers!!")

        phrase_text = phrase["Text"]["Text"]
        phrase_text = text_strip_directions(phrase_text)
        phrase_text = self.translate_dialog_const(phrase_text)

        line_id = self.dialog_file.add_phrase(phrase_id, phrase_text)

        self.process_phrase_responses(phrase)
        return line_id, phrase_text

    def process_phrase_responses(self, phrase: dict):
        phrases, responses, triggersPhrase, triggersResponse = self.dialog.get("Phrases"), self.dialog.get("Responses"), self.dialog.get("TriggersPhrase"), self.dialog.get("TriggersResponse")
        responsesIndexFirst = int(phrase["ResponsesIndexFirst"])
        responsesCount = int(phrase["ResponsesCount"])
        for i, response in enumerate(responses):
            if i < responsesIndexFirst: continue
            response_flags = response["Flags"]
            
            response_text = response["Text"]["Text"]
            if response_text is None: response_text = "Continue"
            response_text = text_strip_directions(response_text)
            response_text = self.translate_dialog_const(response_text)

            phrase_line_id = 0
            test_field = ""
            if "HasTrigger" in response_flags:
                triggerIndex = response["TriggerIndex"]
                test_field = f"ctrl(npc).dialog_test(npc, pc, {triggerIndex})"
                self.response_triggers[triggerIndex] = (response_text, -1)

            resp_line_id = self.dialog_file.add_response(response_text, answer_id=phrase_line_id, test_field=test_field)

            if "HasTrigger" in response_flags:
                self.response_triggers[triggerIndex] = (response_text, resp_line_id)

            nextPhraseIndex = response["NextPhraseIndex"]
            if not "HasNextDialog" in response_flags and nextPhraseIndex >=0:
                phrase_next = phrases[nextPhraseIndex]
                phrase_line_id, phrase_text = self.process_phrase_dialog(phrase_next, True)
                self.dialog_file.update_response(resp_line_id, response_text, answer_id=phrase_line_id)
            
            responsesCount += -1
            if responsesCount == 0:
                break
        return

    def save(self):
        self.dialog_file.save()
        return

    def translate_dialog_const(self, line: str):
        line = line.replace("<CHARNAME>", "@pcname@ ")
        return line