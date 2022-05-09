import json
import os
import re
import produce_scripts
import common
#import pydub does not work

def text_strip_directions(text: str):
    return re.sub("[\[].*?[\]]", "", text)

class DialogFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.line_tups = list()
        self.last_num = 0
        self.last_num_phrase = 0
        self.current_cre_name = ""
        self.sound_map = dict()
        return

    def add_phrase(self, phrase_id: int, text: str, speech_id: int = None, effect_code: str = None):
        # {line_id}{text}{text female}{min IQ}{test field|speech_id}{answer key}{effect python}
        line_id = ((self.last_num // 10) + 1)*10
        
        speech_id_str = str(speech_id) if not speech_id is None else ""
        line = f"{{{line_id}}}{{{text}}}{{{text}}}{{}}{{{speech_id_str}}}{{}}{{{str(effect_code or '')}}} # phrase: {self.current_cre_name} {phrase_id}"
        if self.last_num:
            self.line_tups.append((None, "", None))
        self.line_tups.append((line_id, line, None))

        self.last_num = line_id
        self.last_num_phrase = line_id
        return line_id

    def add_response(self, resp_id: int, text: str, test_field: str = None, answer_id: int = None, effect_code: str = None):
        # {line_id}{text}{text female}{min IQ}{test field|speech_id}{answer key}{effect python}
        line_id = self.last_num + 1
        
        answer_id_str = str(answer_id) if not answer_id is None else ""
        if answer_id == 0:
            answer_id_str = 0
        line = f"{{{line_id}}}{{{text}}}{{}}{{1}}{{{str(test_field or '')}}}{{{answer_id_str}}}{{{str(effect_code or '')}}} # resp: {self.current_cre_name} {resp_id}"
        self.line_tups.append((line_id, line, common.tDict(resp_id=resp_id, text=text, test_field=test_field, answer_id=answer_id, effect_code=effect_code)))

        self.last_num = line_id
        return line_id

    def update_response(self, line_id: int, resp_id: int, text: str, test_field: str = None, answer_id: int = None, effect_code: str = None):
        # {line_id}{text}{text female}{min IQ}{test field|speech_id}{answer key}{effect python}
        index = next((i for i, tup in enumerate(self.line_tups) if tup[0] == line_id), None)
        if index is None:
            #print(f'update_response line_id: {line_id} not found!')
            raise Exception(f'update_response line_id: {line_id} not found!')
        
        answer_id_str = str(answer_id) if not answer_id is None else ""
        line = f"{{{line_id}}}{{{text}}}{{}}{{1}}{{{str(test_field or '')}}}{{{answer_id_str}}}{{{str(effect_code or '')}}} # resp: {self.current_cre_name} {resp_id}"
        self.line_tups[index] = ((line_id, line, common.tDict(resp_id=resp_id, text=text, test_field=test_field, answer_id=answer_id, effect_code=effect_code, answer_id_str=answer_id_str)))

        return line_id

    def update_response_test_field_append(self, line_id: int, add_test_field_part: str):
        index = next((i for i, tup in enumerate(self.line_tups) if tup[0] == line_id), None)
        if index is None:
            raise Exception(f'update_response line_id: {line_id} not found!')
        tup = self.line_tups[index]
        d = tup[2]
        if not d['test_field']:
            d['test_field'] = f'True {add_test_field_part}'
        else: d['test_field'] = f"{d['test_field']}{add_test_field_part}"
        line = f"{{{line_id}}}{{{d['text']}}}{{}}{{1}}{{{str(d['test_field'] or '')}}}{{{d['answer_id_str']}}}{{{str(d['effect_code'] or '')}}} # resp: {self.current_cre_name} {d['resp_id']}"
        self.line_tups[index] = ((tup[0], line, d))
        return

    def save(self):
        with open(self.file_name, 'w') as f:
            for num, line, d in self.line_tups:
                #aline = line
                f.write(line + ("\n" if not "\n" in line else ""))
        self.save_sound_map()
        return

    def save_sound_map(self, fn = None):
        if not fn:
            fn = self.file_name.replace(".dlg", "_sound.json")
        with open(fn, 'w') as f:
            json.dump(self.sound_map, f, indent=4)
        return

    def copy_sound_files(self, source_dir: str, dest_dir: str, overwrite: bool = False):
        source_dir = os.path.normpath(source_dir)
        dest_dir = os.path.normpath(dest_dir)
        if not os.path.exists(dest_dir) and os.path.exists(os.path.dirname(dest_dir)):
            os.mkdir(dest_dir)
        else:
            if overwrite:
                os.system(f'del "{dest_dir}\\*.mp3" /Q')
        ffmpeg_path = "venv\\Library\\bin\\ffmpeg.exe"
        for line_id, sound_file_name in self.sound_map.items():
            sf = os.path.join(source_dir, sound_file_name + ".WAV")
            tf = os.path.join(dest_dir, f"v{line_id}_m.mp3")
            if not overwrite and os.path.exists(tf):
                continue
            #os.system(f'copy "{sf}" "{tf}"')
            command = f'{ffmpeg_path} -i "{sf}" -acodec libmp3lame "{tf}" -y'
            print(command)
            os.system(command)
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
        self.response_actions = dict()
        self.phrases = dict()
        self.responses = dict()

        self.current_are_name = None
        self.current_cre_name = None
        self.trigger_index_skills = dict()
        self.trigger_max_index = 0
        return

    def _add_line(self, line):
        return self.parent.writeline(line)

    def produce(self, are_name: str, cre_name: str):
        self.current_are_name = are_name
        self.current_cre_name = cre_name

        phrases, responses, triggersPhrase, triggersResponse = self.dialog.get("Phrases"), self.dialog.get("Responses"), self.dialog.get("TriggersPhrase"), self.dialog.get("TriggersResponse")
        actions = self.dialog.get("Actions")
        if not phrases: return

        self.dialog_file.current_cre_name = self.dialog_name


        if self.dialog_name == "10JORUN": # debug!
            print("")

        #self.parent.current_indent = "\t"
        # self.parent.indent(False)
        # self._add_line("def dialog(self, attachee, triggerer):")
        # self.parent.indent(True)
        # self._add_line("assert isinstance(attachee, toee.PyObjHandle)")
        # self._add_line("assert isinstance(triggerer, toee.PyObjHandle)")
        # self._add_line("")
        # self._add_line("try:")
        # self.parent.indent(True)
        # self._add_line('self.vars["attachee"] = attachee')
        # self._add_line('self.vars["triggerer"] = triggerer')
        # self._add_line("")
        # self._add_line("self.script_dialog(attachee, triggerer)")
        # self.parent.indent(False)
        # self._add_line("finally:")
        # self.parent.indent(True)
        # self._add_line('self.vars["attachee"] = None')
        # self._add_line('self.vars["triggerer"] = None')
        # self.parent.indent(False)
        # self._add_line("")
        # self._add_line("return toee.SKIP_DEFAULT")
        # self._add_line("")

        self._add_line("def script_dialog(self, attachee, triggerer):")
        self.parent.indent(True)
        #self._add_line(f"# {self.dialog_name}")
        self._add_line(f'print("script_dialog {self.dialog_name}")')
        self._add_line("assert isinstance(attachee, toee.PyObjHandle)")
        self._add_line("assert isinstance(triggerer, toee.PyObjHandle)")
        self._add_line("")
        self._add_line("attachee.turn_towards(triggerer)")
        self._add_line("")
        self._add_line('line_id = -1')
        self._add_line("while True:")
        self.parent.indent(True)

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

            self.parent.indent(True)
            #self._add_line(f'triggerer.begin_dialog(attachee, {line_id}) # {phrase_text}')
            self._add_line(f'line_id = {line_id} # {phrase_text}')
            self._add_line(f'print("STATE {phase_index}: line_id = {line_id}")')
            self._add_line('break')
            self.parent.indent(False)
            self._add_line("")

        self._add_line("break # while")
        self._add_line("")
        self.parent.indent(False)
        self._add_line('print("script_dialog line_id: {}".format(line_id))')
        self._add_line('if line_id >= 0:')
        self._add_line(f'\ttriggerer.begin_dialog(attachee, line_id)')
        self._add_line("")
        self._add_line("return line_id # script_dialog")
        self.parent.indent(False)
        self._add_line("")

        self._add_line("def dialog_test_do(self, npc, pc, index):")
        self.parent.indent(True)
        #self._add_line(f'print("dialog_test_do {self.dialog_name}")')
        self._add_line("assert isinstance(npc, toee.PyObjHandle)")
        self._add_line("assert isinstance(pc, toee.PyObjHandle)")
        self._add_line("assert isinstance(index, int)")
        self._add_line(f"# {self.dialog_name}")
        self._add_line("")

        _iff = "if"
        for triggerIndex in sorted(self.response_triggers.keys()):
            self._add_line(f'{_iff} index == {triggerIndex}:')
            if self.trigger_max_index < (triggerIndex ):
                self.trigger_max_index = triggerIndex
            _iff = "elif"
            self.parent.indent(True)
            
            trigger_lines, out_lines = self.calc_trigger(triggersResponse[triggerIndex])
            for trigger_line in trigger_lines:
                self._add_line(f"# {trigger_line}")

            for l in out_lines:
                self._add_line(l)

            self.parent.indent(True)
            response_text, resp_line_id = self.response_triggers[triggerIndex]
            self._add_line(f'return True # {resp_line_id}: {response_text}')
            skill_name = self.scan_for_skills(out_lines, triggerIndex)
            if skill_name:
                self.dialog_file.update_response_test_field_append(resp_line_id, f'# {skill_name}')
            self.parent.indent(False)
            self._add_line("")
            self.parent.indent(False)
        
        self._add_line("return False # dialog_test_do")
        self.parent.indent(False)
        self._add_line("")

        self._add_line("def dialog_action_do(self, npc, pc, index):")
        self.parent.indent(True)
        #self._add_line(f"# {self.dialog_name}")
        #self._add_line(f'print("dialog_test_do {self.dialog_name}")')
        self._add_line("assert isinstance(npc, toee.PyObjHandle)")
        self._add_line("assert isinstance(pc, toee.PyObjHandle)")
        self._add_line("assert isinstance(index, int)")
        self._add_line("")

        _iff = "if"
        for actionIndex in sorted(self.response_actions.keys()):
            self._add_line(f'{_iff} index == {actionIndex}:')
            _iff = "elif"
            self.parent.indent(True)
            
            trigger_lines, out_lines = self.calc_actions(actions[actionIndex])
            #for trigger_line in trigger_lines:
            #    self._add_line(f"# {trigger_line}")

            for i, l in enumerate(out_lines):
                #self._add_line(f'print("{l}") # {trigger_lines[i]}')
                #self._add_line(f"print('{l}')")
                self._add_line(f'# {trigger_lines[i]}')
                self._add_line(l)

            response_text, resp_line_id = self.response_actions[actionIndex]
            self._add_line(f'# {resp_line_id}: {response_text}')
            self._add_line("")
            self.parent.indent(False)
        
        self._add_line("return # dialog_action_do")
        self._add_line("")

        self.parent.indent(False)
        self._add_line(f"def get_dialog_trigger_max_index(self): return {self.trigger_max_index}")
        self._add_line("")
        self.parent.indent(True)
        return

    def calc_trigger(self, trigger: str):
        trigger_lines = produce_scripts.condition_split(trigger)
        out_lines = self.parent.doc.producerOfScripts.transate_trigger_lines(trigger_lines, are_name=self.current_are_name, cre_name=self.current_cre_name)
        return trigger_lines, out_lines

    def calc_actions(self, action: str):
        action_lines = produce_scripts.condition_split(action)
        out_lines = self.parent.doc.producerOfScripts.transate_action_lines(action_lines)
        return action_lines, out_lines

    def process_phrase_dialog(self, phrase: dict, check_trigger: bool):
        phrase_id = phrase["Index"]

        line_id = self.phrases.get(phrase_id)
        if not line_id is None:
            return line_id, None

        #phrases, responses, triggersPhrase, triggersResponse = self.dialog.get("Phrases"), self.dialog.get("Responses"), self.dialog.get("TriggersPhrase"), self.dialog.get("TriggersResponse")

        if check_trigger:
            triggerIndex = int(phrase["TriggerIndex"])
            #if triggerIndex != -1: 
            #    self.save()
            #    raise Exception("Phrase should not have triggers!!")

        phrase_text = phrase["Text"]["Text"]
        phrase_text = text_strip_directions(phrase_text)
        phrase_text = self.translate_dialog_const(phrase_text)

        line_id = self.dialog_file.add_phrase(phrase_id, phrase_text)
        self.phrases[phrase_id] = line_id
        phrase_sound_file = phrase["Text"]["Sound"]
        if phrase_sound_file:
            self.dialog_file.sound_map[line_id] = phrase_sound_file

        self.process_phrase_responses(phrase)
        return line_id, phrase_text

    def process_phrase_responses(self, phrase: dict):
        phrases, responses, triggersPhrase, triggersResponse = self.dialog.get("Phrases"), self.dialog.get("Responses"), self.dialog.get("TriggersPhrase"), self.dialog.get("TriggersResponse")
        responsesIndexFirst = int(phrase["ResponsesIndexFirst"])
        if responsesIndexFirst == 40:
            print("")
        responsesCount = int(phrase["ResponsesCount"])
        next_steps = list() # (phrase_id, from_response_line_id, resp_id)
        for i, response in enumerate(responses):
            if i < responsesIndexFirst: continue
            response_flags = response["Flags"]
            response_index = response["Index"]
            if i != response_index:
                raise Exception("i != response_index")
            
            response_text = response["Text"]["Text"]
            if response_text is None: response_text = "Continue"
            response_text = text_strip_directions(response_text)
            response_text = self.translate_dialog_const(response_text)

            phrase_line_id = 0
            test_field = ""
            effect_code = ""
            if "HasTrigger" in response_flags:
                triggerIndex = response["TriggerIndex"]
                test_field = f"ctrl(npc).dialog_test(npc, pc, {triggerIndex})"
                self.response_triggers[triggerIndex] = (response_text, -1)

            if "HasAction" in response_flags:
                actionIndex = response["ActionIndex"]
                effect_code = f"ctrl(npc).dialog_action(npc, pc, {actionIndex})"
                self.response_actions[actionIndex] = (response_text, -1)

            if "HasJournal" in response_flags:
                journalIndex = response["JournalIndex"]
                rums = self.parent.doc.journalFile.get_rumors_by_strref(journalIndex)
                if effect_code:
                    effect_code = effect_code.strip()
                effect_code = (effect_code + "; " if effect_code else "") + f'uj.journal_add({journalIndex}, {rums})'

            resp_line_id = self.dialog_file.add_response(response_index, response_text, answer_id=phrase_line_id, test_field=test_field, effect_code=effect_code)

            if "HasTrigger" in response_flags:
                self.response_triggers[triggerIndex] = (response_text, resp_line_id)
            if "HasAction" in response_flags:
                self.response_actions[actionIndex] = (response_text, resp_line_id)

            nextPhraseIndex = response["NextPhraseIndex"]
            if not "HasNextDialog" in response_flags and nextPhraseIndex >=0:
                #phrase_next = phrases[nextPhraseIndex]
                next_steps.append((nextPhraseIndex, resp_line_id, response_index, response_text, phrase_line_id, test_field, effect_code))
                #phrase_line_id, phrase_text = self.process_phrase_dialog(phrase_next, True)
                #self.dialog_file.update_response(resp_line_id, response_text, answer_id=phrase_line_id)
            
            responsesCount += -1
            if responsesCount == 0:
                break

        for nextPhraseIndex, resp_line_id, response_index, response_text, phrase_line_id, test_field, effect_code in next_steps:
            phrase_line_id = self.phrases.get(nextPhraseIndex)
            if phrase_line_id is None:
                phrase_next = phrases[nextPhraseIndex]
                phrase_line_id, phrase_text = self.process_phrase_dialog(phrase_next, True)
            self.dialog_file.update_response(resp_line_id, response_index, response_text, answer_id=phrase_line_id, test_field=test_field, effect_code=effect_code)

        return

    def save(self):
        self.dialog_file.save()
        return

    def translate_dialog_const(self, line: str):
        line = line.replace("<CHARNAME>", "@pcname@ ")
        return line

    @classmethod
    def scan(cls, doc, dialog: dict, are_name: str, cre_name: str):
        phrases, responses, triggersPhrase, triggersResponse = dialog.get("Phrases"), dialog.get("Responses"), dialog.get("TriggersPhrase"), dialog.get("TriggersResponse")
        for trigger in triggersPhrase:
            trigger_lines = produce_scripts.condition_split(trigger)
            out_lines = doc.producerOfScripts.transate_trigger_lines(trigger_lines, are_name=are_name, cre_name=cre_name)

        for action in dialog.get("Actions"):
            action_lines = produce_scripts.condition_split(action)
            doc.producerOfScripts.transate_action_lines(action_lines, are_name=are_name, cre_name=cre_name)
        return

    def scan_for_skills(self, out_lines: list, trigger_index: int):
        def get_val(line: str, arg_index: int):
            funct_name, func_args = produce_scripts.ScriptTran._parse_func(line, None)
            if func_args and len(func_args) > arg_index + 1:
                val = func_args[arg_index].value
                return val
            return
        skill_name = None
        for line in out_lines:
            lline = line.lower()
            if 'icheckstatgt(' in lline:
                if '"chr"' in lline:
                    if get_val(line.replace('self.', '').replace('if', '').replace('\\', '').strip(), 1) >= 15:
                        skill_name = 'skill_diplomacy'
                        break
            if 'checkskillgt(' in lline:
                if 'diplomacy' in lline:
                        skill_name = 'skill_diplomacy'
                        break
                if 'bluff' in lline:
                        skill_name = 'skill_bluff'
                        break

        if not skill_name is None:
            self.trigger_index_skills[trigger_index] = skill_name
            return skill_name
        return
