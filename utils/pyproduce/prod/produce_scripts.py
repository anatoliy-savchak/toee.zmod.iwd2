from cmath import e
from email import message
import os
import sys
import inspect
import ast
import produce_items
import producer_base
import json
import common
import copy
#import pyproduce

class ProducerOfScripts(producer_base.Producer):
    def __init__(self, doc, path_inf_scripting: str):
        index_path = os.path.join(doc.exp_dir, 'Scripts', 'scripts_index.json')
        super().__init__(doc, index_path = index_path)

        self.path_inf_scripting = path_inf_scripting
        self.inf_scripting_lines = list()
        if self.path_inf_scripting:
            with open(self.path_inf_scripting, 'r') as f:
                self.inf_scripting_lines = f.readlines()

        if self.index_file.get("statistics") is None:
            self.index_file["statistics"] = dict()
        if self.index_file["statistics"].get("funcs") is None:
            self.index_file["statistics"]["funcs"] = dict()
        if self.index_file["statistics"].get("funcs_log") is None:
            self.index_file["statistics"]["funcs_log"] = list()

        self.error_messages = list()
        self.log_usage = False
        self.log_strrefs = True
        self.log_statistics = False
        return

    def transate_trigger_lines(self, trigger_lines: list, are_name: str, cre_name: str, actor_name: str = None):
        context={"producer": self, "are_name": are_name, "cre_name": cre_name, "actor_name": actor_name, "bcs_name": None, "script_code": None, "file_producer": None}

        trigger_lines2 = list()
        for i, action_line in enumerate(trigger_lines):
            action_linea = self.remove_comment(action_line)
            sub = None
            if action_linea: 
                for line in condition_split(action_linea):
                    sub = [i, action_line, line]
                    trigger_lines2.append(sub)
            else:
                sub = [i, action_line, action_linea]
                trigger_lines2.append(sub)

        lines = list()
        or_left = 0
        or_count_max = 0
        for i, trigger_line_sub in enumerate(trigger_lines2):
            #line = transate_trigger_line(trigger_line)
            trigger_line = trigger_line_sub[2]
            trigger_linea = trigger_line.strip()
            if not trigger_linea: continue
            #print(f'Translating {trigger_linea}')
            if str(trigger_linea).lower().startswith('or('):
                or_left = int(trigger_linea.split('(', 2)[1].split(')', 2)[0].strip())
                or_count_max = or_left
                line = '('
                if i == 0:
                    line = "if " + line + ' False'
                else:
                    line = "\t and " + line + ' False'
            else:
                line = ScriptTran.translate_script_line(trigger_linea, context)
                if line is None:
                    line = ''
                    continue

                if i == 0:
                    line = "if " + line
                elif or_left:
                    if or_left == or_count_max:
                        line = "\t\tor " + line
                    elif or_left == 1:
                        line = "\t\tor " + line + ' )'
                    else:
                        line = "\t\tor " + line
                    or_left += -1
                    if not or_left: 
                        or_count_max = 0
                else:
                    line = "\t and " + line

            if i == len(trigger_lines2) - 1: # last
                line = line + ":"
            else:
                line = line + " \\"
            lines.append(line)

        return lines

    def transate_action_lines(self, action_lines: list, are_name: str = None, cre_name: str = None, bcs_name: str = None, script_code: str = None, actor_name: str = None, file_producer = None):
        context={"producer": self, "are_name": are_name, "cre_name": cre_name, "actor_name": actor_name, "bcs_name": bcs_name, "script_code": script_code, "file_producer": file_producer}

        lines = list()
        action_lines2 = list()
        for i, action_line in enumerate(action_lines):
            action_linea = self.remove_comment(action_line)
            if not action_linea: continue
            action_lines2.extend(condition_split(action_linea))
        
        self.current_action_lines = action_lines2
        self.current_action_line_index = None

        for i, action_line in enumerate(action_lines2):
            action_linea = action_line.strip()
            if not action_linea: continue

            self.current_action_line_index = i
            scripted_lines = ScriptTran.translate_script_line_ex(action_linea, context)
            line = None
            if isinstance(scripted_lines, str):
                line = scripted_lines
            if line is None:
                line = 'pass'
            lines.append(line)

        self.current_action_lines = None
        self.current_action_line_index = None

        return lines

    def transate_action_lines_complex(self, action_lines: list, context: dict):
        context["producer"] = self
        context["is_complex"] = True
        #context={"producer": self, "are_name": are_name, "cre_name": cre_name, "actor_name": actor_name, "bcs_name": bcs_name, "script_code": script_code, "file_producer": file_producer, "is_complex": True}

        lines = list()
        action_lines2 = list()
        for i, action_line in enumerate(action_lines):
            action_linea = self.remove_comment(action_line)
            if action_linea: 
                for line in condition_split(action_linea):
                    sub = [i, action_line, line]
                    action_lines2.append(sub)
            else:
                sub = [i, action_line, action_linea]
                action_lines2.append(sub)

        
        self.current_action_lines = action_lines2
        self.current_action_line_index = None

        for i, action_line_sub in enumerate(action_lines2):
            action_line = action_line_sub[2]
            action_linea = action_line.strip()
            if action_linea:
                self.current_action_line_index = i
                con = dict()
                for key, value in context.items():
                    con[key] = value
                con["line_index"] = i
                scripted_lines = ScriptTran.translate_script_line_ex(action_linea, con)
                if "CutSceneId" in con.keys():
                    context["CutSceneId"] = con.get("CutSceneId")
                line = scripted_lines
                if not isinstance(scripted_lines, dict):
                    line = {"instructions": [{"line": line}], "context": con, "breaks_after": 0}
                line["orig"] = action_line_sub[1]

                lines.append(line)

        self.current_action_lines = None
        self.current_action_line_index = None

        return lines

    def remove_comment(self, line):
        if '//' in line:
            pos = line.index('//')
            if pos > 0:
                line = line[:pos]
                line = line.strip()
            elif(pos == 0):
                return ''
        return line

    def check_func_implemented(self, func_name: str):
        if not self.inf_scripting_lines:
            return False
        func_name = "def "+ func_name + '('
        result = not next((line for line in self.inf_scripting_lines if func_name in line), None) is None
        return result

    def log_func(self, line: str, func_name: str, args_src: list, args: list, func_info: dict):
        if self.log_statistics:
            if not line is None:
                if not next((rec for rec in self.index_file["statistics"]["funcs_log"] if line.lower() == rec["line"].lower()), None):
                    log_rec = {
                        "line": line,
                        "func_name": func_name,
                        "args": args,
                    }
                    self.index_file["statistics"]["funcs_log"].append(log_rec)

            func_name_correct = func_info["func_name"]
            usage_rec = self.index_file["statistics"]["funcs"].get(func_name_correct)
            if usage_rec is None:
                usage_rec = {"func_name": func_name_correct, "kind": func_info["kind"], "args": list(), "func_name_spellings": [func_name]}
            else:
                if not func_name in usage_rec["func_name_spellings"]:
                    usage_rec["func_name_spellings"].append(func_name)


            for index, arg_value in enumerate(args):
                arg_rec = dict()
                arg_value_src = args_src[index]
                if len(usage_rec["args"]) > index:
                    arg_rec = usage_rec["args"][index]
                else:
                    arg_info = func_info["args"][index]
                    arg_rec["def"] = arg_info
                    arg_rec["values"] = list()
                    usage_rec["args"].append(arg_rec)

                value_rec = next((rec for rec in arg_rec["values"] if arg_value_src.lower() == rec["src"].lower()), None)
                if value_rec is None:
                    value_rec = {"src": arg_value_src
                        , "used_count": 1
                        , "value": arg_value
                        , "first_occurence": f'{self.current_are_name}.{self.current_cre_name}.{self.current_actor_name}'
                    }
                    arg_rec["values"].append(value_rec)
                else:
                    if self.log_usage:
                        value_rec["used_count"] += 1

            self.index_file["statistics"]["funcs"][func_name_correct] = usage_rec

        if self.log_strrefs and self.doc.producerOfFloats:
            func_name_lo = func_name.lower()
            if func_name_lo == 'floatmessage':
                self.doc.producerOfFloats.ensure_str_ref(int(args_src[1]))
            elif func_name_lo == 'addxpvar':
                self.doc.producerOfFloats.ensure_str_ref(int(args_src[1]))
            elif func_name_lo == 'savegame':
                self.doc.producerOfFloats.ensure_str_ref(int(args_src[0]))
        return

    def log_error(self, error_message: str):
        self.error_messages.append(error_message)
        return

    def _save_index(self):
        if self.index_path and self.index_file:
            d = self.index_file["statistics"]["funcs"]
            for func, func_body in d.items():
                fn = os.path.join(os.path.dirname(self.index_path), func + '.json')
                with open(fn, 'w') as f:
                    json.dump(func_body, f, indent=4)
                    
            with open(self.index_path, 'w') as f:
                json.dump(self.index_file, f, indent=4)
        return

    def produce_func_defs(self, out_file_path: str = None, merge_from_path: str = None):
        if not out_file_path:
            out_file_path = os.path.join(self.doc.core_dir, "scr/inf_scripting_auto.py")
        template_path = 'data/inf_scripting_auto.py'
        merge_from_lines = None
        if merge_from_path:
            with open(merge_from_path, 'r') as f:
                merge_from_lines = f.readlines()

        prod = producer_base.ProducerOfFile(self.doc, out_file_path, template_path, True)
        prod.indent()

        def produce_funcs(commands, label: str):
            nonlocal prod
            prod.writeline(f'########## {label} ##########')
            for rec in commands:
                func_name = rec["func_name"]
                func_merged = False
                if merge_from_lines:
                    func_name_lo = func_name.lower()
                    func_def_find = f'i{func_name_lo}('
                    func_line_id = common.lines_find_lower(merge_from_lines, func_def_find)
                    if func_line_id:
                        func_line_id += -1
                        func_merged = True
                        while func_line_id < len(merge_from_lines):
                            line = merge_from_lines[func_line_id]
                            if line[:8] == '\t\treturn':
                                prod.lines.append(line)
                                prod.lines.append('')
                                break
                            prod.lines.append(line)
                            func_line_id += 1
                        #continue

                args = rec["args"]
                args_orig_defs = list()
                args_defs = list()
                args_defs.append('self')
                for arg in args:
                    arg_line = arg["def"]["arg_line"]
                    args_orig_defs.append(arg_line)
                    arg_name = arg["def"]["arg_name"]
                    param_name = arg_name.lower().replace(' ', '_')
                    if param_name == 'object': param_name = 'obj'
                    if param_name == 'class': param_name = 'class_'
                    if param_name == 'with': param_name = 'with_'
                    args_defs.append(param_name)

                orig_def = f'{func_name}({", ".join(args_orig_defs)})'
                func_def = f'{func_name}({", ".join(args_defs)})'

                if not func_merged:
                    prod.writeline('@dump_args')
                    prod.writeline(f'def {func_def}:')
                    prod.indent()
                    prod.writeline('"""')
                    prod.writeline(f'{orig_def}')
                    prod.writeline('"""')
                    prod.writeline(f'raise Exception("Not implemented function: {func_name}!")')
                    prod.writeline('return')
                    prod.indent(False)
                    prod.writeline()
                
                args_defs_noself_joned = ""
                for o in args_defs:
                    if o != 'self':
                        if args_defs_noself_joned: args_defs_noself_joned +=", "
                        args_defs_noself_joned += f'{o}={o}'

                for func_spell in rec["func_name_spellings"]:
                    if func_spell == func_name: continue
                    func_def = f'{func_spell}({", ".join(args_defs)})'
                    prod.writeline(f'def {func_def}: self.{func_name}({args_defs_noself_joned})')
                    prod.writeline()
            return

        funcs = sorted(self.index_file["statistics"]["funcs"].items())
        
        triggers = (rec for n, rec in funcs if rec["kind"] == 'trigger')
        produce_funcs(triggers, 'TRIGGERS')
        actions = (rec for n, rec in funcs if rec["kind"] == 'action')
        produce_funcs(actions, 'ACTIONS')
        identifiers = (rec for n, rec in funcs if rec["kind"] == 'identifier')
        produce_funcs(identifiers, 'IDENTIFIERS')
        prod.save()
        return


def condition_split(cond: str):
    result = cond.splitlines(False)
    if result and len(result) == 1 and result[0]:
        # fix possibility of incorrect joined lines
        # NumTimesTalkedTo(0)Subrace(Protagonist, Dwarf_Gray)Global("Dock_Goblin_Quest", "GLOBAL", 1)
        openedPar = 0
        index = 0
        line = result[0]
        result = list()
        while True:
            if line[index] == '(':
                openedPar += 1
            elif line[index] == ')':
                openedPar += -1
                if openedPar == 0:
                    index += 1
                    subline = line[:index]
                    result.append(subline)
                    if index >= len(line):
                        break
                    line = line[index:]
                    if not line:
                        break
                    index = -1
            index += 1
                
            if index >= len(line):
                result.append(line)
                break


    return result


class ScriptTran:
    def __init__(self, line: str, context: dict):
        self.line = line
        self.context = context
        return

    @staticmethod
    def translate_script_line(aline: str, context):
        result = None
        prefix = ""
        if aline and aline[0] == "!":
            prefix = "not "
            aline = aline.removeprefix("!").strip()

        result = ScriptTran.translate_script_line_ex(aline, context)
        if result is None:
            raise Exception("No line support!")
        return prefix + result

    @staticmethod
    def translate_script_line_ex(aline: str, context):
        aline = aline.replace('#', '"')
        result = None

        while True:
            lline = aline.lower()
            # first check simple things like True()
            whole_class = next((cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass) if issubclass(cls, ScriptTran) 
                and cls.is_whole_liner() and lline in cls.whole_lines()), None)
            if whole_class:
                result = whole_class(aline, context).do_translate_script_line(aline)
                break

            aline = aline.replace('#', '"')
            func_name, args = ScriptTran._parse_func(aline, context)
            if func_name is None:
                return None
            result = ScriptTran._process_func(aline, func_name, args, context)
            break
        if result is None:
            raise Exception("No line support!")
        return result

    @staticmethod
    def _process_func(aline, func_name, args, context):
        func_classes = [cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass) if issubclass(cls, ScriptTran) and cls.is_func_liner()]
        func_name_lo = func_name.lower()
        cls = next((cls for cls in func_classes for ffunc in cls.supports_func() if ffunc and func_name_lo == ffunc.lower()), None)
        if cls:
            o = cls(aline, context)
            result = o.translate_func(func_name, args)
            return result
        cls = next((cls for cls in func_classes if cls.supports_funcs_default()), None)
        if cls:
            o = cls(aline, context)
            result = o.translate_func(func_name, args)
            return result
        return None

    @staticmethod
    def _parse_func(line: str, context):
        line = line.replace("[", '"[').replace("]", ']"')
        if '//' in line:
            pos = line.index('//')
            if pos > 0:
                line = line[:pos]
                line = line.strip()
            elif(pos == 0):
                return None, None
            
        try:
            tree = ast.parse(line)
        except SyntaxError as e:
            if context:
                context["producer"].log_error(error_message=e.msg + ' ' + line)
            return None, None

        f = tree.body[0].value.func
        funct_name = None
        func_args = None
        if isinstance(f, ast.Name):
            funct_name = f.id
            func_args = list()
            for arg in tree.body[0].value.args:
                func_args.append(arg)
            return (funct_name, func_args)
        else:
            raise Exception("Not func!")
        return

    @classmethod
    def is_whole_liner(cls): return False

    @classmethod
    def is_func_liner(cls): return False

    @classmethod
    def whole_lines(cls): return (None, )

    @classmethod
    def supports_func(cls): return (None, )

    @classmethod
    def supports_funcs_default(cls): return False

    def do_translate_script_line(self, aline: str): return

    def translate_func(self, func_name: str, args: list): return

class ScriptTran_True(ScriptTran):
    @classmethod
    def is_whole_liner(cls): return True

    @classmethod
    def whole_lines(cls): return ("true()", )

    def do_translate_script_line(self, aline: str): return "True"

class ScriptTranFuncs(ScriptTran):
    def __init__(self, line: str, context: dict):
        super().__init__(line, context)
        self.args = None
        return

    @classmethod
    def is_func_liner(cls): return True

    def translate_func(self, func_name: str, args: list): 
        func_info = next((func_info for func_info in self.context["producer"].doc.commands.commands if func_info["func_name"].lower() == func_name.lower()), None)
        if not func_info:
            print(f"No info for func {func_name}, line: {self.line}")
            self.context["producer"].log_error(f"No info for func {func_name}, line: {self.line}")
            #raise Exception(f"No info for func {func_name}, line: {self.line}")
            return None
        return self.do_translate_func(func_name, args, func_info)
    
    def do_translate_func(self, func_name: str, args: list, func_info: dict): 
        strargs = list()
        strargs_src = list()
        self.args = args
        for index, arg in enumerate(args):
            arg_info = func_info["args"][index]
            s = self.do_translate_param(arg, index, arg_info)
            if s is None:
                s = ''
            src = self.do_get_param(arg, index, arg_info)
            strargs.append(s)
            strargs_src.append(src)
        result = "self.i" + func_name + "(" + ", ".join(strargs) + ")"
        self.context["producer"].log_func(self.line, func_name, strargs_src, strargs, func_info)

        if not self.context["producer"].check_func_implemented("i" + func_name):
            print(f"Func not implemented: {func_name} => {self.line}")

        return result

    def do_translate_param(self, arg, index: int, arg_info: dict):
        w = "'" if index in self.literal_params_to_wrap() else ""
        s = ""
        if isinstance(arg, ast.Name):
            s = self.d_translate_param_name(arg, index)
        elif isinstance(arg, ast.Call):
            #c = ast.Call(arg)
            c = arg
            s = ScriptTran._process_func(self.line, c.func.id, c.args, self.context)
        elif isinstance(arg, ast.UnaryOp):
            # ex: -2
            #c = ast.UnaryOp(arg)
            c = arg
            m = 1
            if isinstance(c.op, ast.USub):
                m = -1
            else:
                raise Exception("Unknown op!")
            v = c.operand.value
            v = v * m
            s = str(v)
        elif isinstance(arg, ast.BinOp):
            #c = ast.BinOp(arg)
            c = arg
            s = ""
            s += self.do_translate_param(c.left, index, arg_info)
            if isinstance(c.op, ast.BitOr):
                s += " | "
            else:
                raise Exception("Unknown op!")
            s += self.do_translate_param(c.right, index, arg_info)
        else:
            if 'value' in dir(arg):
                if isinstance(arg.value, int):
                    s = str(arg.value)
                elif isinstance(arg.value, str):
                    if arg.value and arg.value.startswith('['):
                        s = '"' + w + str(arg.value) + w + '"'
                    else:
                        s = self.do_translate_param_str(arg, index, arg_info, w)
                        #s = '"\'' + w + str(arg.value) + w + '\'"'
                else:
                    s = '"' + w + str(arg.value) + w + '"'
            else:
                print('Wrong value!')
        return s

    def do_translate_param_str(self, arg, index: int, arg_info: dict, wrap: str):
        return '"\'' + wrap + str(arg.value) + wrap + '\'"'

    def do_get_param(self, arg, index: int, arg_info: dict):
        s = ""
        if isinstance(arg, ast.Name):
            s = arg.id
        elif isinstance(arg, ast.Call):
            s = arg.func.id
        elif isinstance(arg, ast.UnaryOp):
            # ex: -2
            #c = ast.UnaryOp(arg)
            c = arg
            m = 1
            if isinstance(c.op, ast.USub):
                m = -1
            else:
                raise Exception("Unknown op!")
            v = c.operand.value
            v = v * m
            s = str(v)
        else:
            if 'value' in dir(arg):
                if isinstance(arg.value, int):
                    s = str(arg.value)
                elif isinstance(arg.value, str):
                    s = '"' + arg.value + '"'
                else:
                    s = str(arg.value)
            else:
                print('Wrong value!')
        return s

    def d_translate_param_name(self, arg: ast.Name, index: int):
        s = arg.id
        if s.lower() == 'false': s = "False"
        elif s.lower() == 'true': s = "True"
        elif self.context and (producer := self.context.get('producer')) and producer.doc:
            if z := producer.doc.translate_param_name(s):
                s = z
            else:
                s = '"' + s + '"'
        return s

    def do_translate_param_str_spell_from_ints(self, arg, index: int, arg_info: dict, wrap: str):
        if self.context and (producer := self.context.get('producer')) and producer.doc and (spells := producer.doc.ids['SPELL.IDS']):
            s = str(arg.id) if isinstance(arg, ast.Name) else str(arg.value)
            number_of_spell_refs = len(s) // 4
            if len(s) > 4:
                print('')
            result = []
            for i in range(0, number_of_spell_refs):
                spell_ref = s[i*4:i*4+4]
                if (spell_code := spells.get(spell_ref) or (spell_code := spell_ref)):
                    spell_name = producer.doc.spell_codes_producer.get_spell_name(spell_code)
                    if not spell_name: spell_name = spell_code
                    #result.append(spell_code)
                    #result.append(f'const_inf.{spell_code}')
                    result.append(f'"{spell_name}"')
            #return '"' + ';'.join(result) + '"'
            if len(result) > 0: 
                if len(result) == 1:
                    return result[0]
                else:
                    return '[' + ', '.join(result) + ']'

        return super().do_translate_param_str(arg, index, arg_info, wrap)

    def d_translate_param_name_spell(self, arg: ast.Name, index: int):
        if self.context and (producer := self.context.get('producer')) and producer.doc:
            s = str(arg.id) if isinstance(arg, ast.Name) else str(arg.value)
            spell_code = s
            spell_name = producer.doc.spell_codes_producer.get_spell_name(spell_code)
            if not spell_name: spell_name = spell_code
            return f'"{spell_name}"'

        return super().d_translate_param_name(arg, index)

    @classmethod
    def literal_params_to_wrap(cls): return(None, )

class ScriptTranFuncsAny(ScriptTranFuncs):
    @classmethod
    def is_func_liner(cls): return True

    @classmethod
    def supports_funcs_default(cls): return True

class ScriptTranFuncsItem(ScriptTranFuncs):
    @classmethod
    def params_to_itemize(): return (None, ) # not sure

    def do_translate_func(self, func_name: str, args: list, func_info): 
        line = self.do_process_item(func_name, args, func_info, index_with_item = 0, make_create = True, make_proto = True)
        if not line is None:
            return line

        return super().do_translate_func(func_name, args, func_info)

    def do_process_item(self, func_name: str, args: list, func_info, index_with_item: int, make_create: bool, make_proto: bool):
        item_file_name = self.do_translate_param(args[index_with_item], index_with_item, func_info["args"][index_with_item])
        item_file_name = item_file_name.replace('"', '').strip()
        item_file_name = item_file_name.replace("'", '').strip()
        item_cls = produce_items.ItemBase.find_item_class(item_file_name)
        if item_cls:
            if make_create:
                line = item_cls.give_item_create_line(item_file_name, self.do_translate_param(args[2], 2, func_info["args"][2]) if len(args) > 2 else 0)
                if not line is None:
                    return line

            if make_proto:
                proto_const = item_cls.get_proto_const()
                if proto_const:
                    args2 = list()
                    for i, a in enumerate(args):
                        if i == 0:
                            args2.append(f'{proto_const}')
                        else:
                            args2.append(self.do_translate_param(a, i, func_info["args"][i]))
                    line = f'self.i{func_name}({", ".join([str(v or "") for v in args2])})' 
                    return line
        print(f"Not supported func {func_name} param: {item_file_name} => {self.line}")
        return

class ScriptTranFuncsItem_GiveItemCreate(ScriptTranFuncsItem):
    @classmethod
    def params_to_itemize(cls): return (0, )

    @classmethod
    def supports_func(cls): return ("GiveItemCreate", "GiveItem")

class ScriptTranFuncsItem_GiveItemEval(ScriptTranFuncsItem):
    @classmethod
    def params_to_itemize(cls): return (0, )

    def do_translate_func(self, func_name: str, args: list, func_info): 
        line = self.do_process_item(func_name, args, func_info, index_with_item = 0, make_create = False, make_proto = True)
        if not line is None:
            return line

        return super().do_translate_func(func_name, args, func_info)

    @classmethod
    def supports_func(cls): return ("PartyHasItem", "TakePartyItemNum", "HasItem", "TakePartyItemNum", "DestroyItem")

class ScriptTranFuncsItem_Debug(ScriptTranFuncs):
    @classmethod
    def supports_func(cls): return ("SetCriticalPathObject", )

class ScriptTranFuncCallScript(ScriptTranFuncs):
    @classmethod
    def supports_func(cls): return ("StartCutScene", )

    def do_translate_func(self, func_name: str, args: list, func_info): 
        script_name = self.do_get_param(args[0], 0, func_info['args'][0])
        script_name = common.strip_quotes(script_name)

        class_name, file_name, pkg_name = self.context["producer"].doc.bcsManager.ensure_bcs(
            bcs_name=script_name
            , hint_are_name = self.context["are_name"]
            , hint_cre_name=self.context["cre_name"]
            , hint_actor_name=self.context["actor_name"]
            , hint_script_code=self.context["script_code"]
            )
        #pkg_name_ = (pkg_name + '.') if pkg_name else ''
        self.context["file_producer"].add_import(file_name, pkg_name)

        is_complex = self.context.get("is_complex")
        if not is_complex:
            line = f'self.iStartCutScenePost({file_name}.{class_name}, self.locus_make())'
        else:
            line = f'self.iStartCutScene({file_name}.{class_name}, locus)'
            instructions = list()
            instructions.append({"line": line})
            line = {"instructions": instructions, "context": self.context, "breaks_after": 1, "is_post_code": 1}

        return line

class ScriptTranFuncWait(ScriptTranFuncs):
    @classmethod
    def supports_func(cls): return ("Wait", "SmallWait")

    def do_translate_func(self, func_name: str, args: list, func_info): 
        amount = self.do_get_param(args[0], 0, func_info['args'][0])

        is_complex = self.context.get("is_complex")
        if not is_complex:
            line = f'self.i{func_name}({amount})'
        else:
            line = f'self.i{func_name}(time={amount}, locus=locus)'
            instructions = list()
            instructions.append({"line": line})
            line = {"instructions": instructions, "context": self.context, "breaks_after": 1, "is_post_code": 1}

        return line


class ScriptTranFuncSmallWaitRandom(ScriptTranFuncs):
    @classmethod
    def supports_func(cls): return ("SmallWaitRandom", )

    def do_translate_func(self, func_name: str, args: list, func_info): 
        time_from = self.do_get_param(args[0], 0, func_info['args'][0])
        time_to = self.do_get_param(args[1], 1, func_info['args'][1])

        is_complex = self.context.get("is_complex")
        if not is_complex:
            line = f'self.i{func_name}({time_from}, {time_to})'
        else:
            line = f'self.i{func_name}({time_from}, {time_to}, locus=locus)'
            instructions = list()
            instructions.append({"line": line})
            line = {"instructions": instructions, "context": self.context, "breaks_after": 1, "is_post_code": 1}

        return line


class ScriptTranFuncParamCoords(ScriptTranFuncs):
    @classmethod
    def supports_func(cls): return ("MoveViewPoint", "JumpToPoint")

    @classmethod
    def params_to_coordinate(cls): return (0, ) # not sure

    def do_translate_param(self, arg, index: int, arg_info: dict):
        orig_value = self.do_get_param(arg, index, arg_info)
        orig_value = str(orig_value)
        if orig_value.startswith('[') or orig_value.startswith('"['):
            pair = orig_value.replace('[', '').replace(']', '').replace('"', '').replace('.', ',')
            if index in self.params_to_coordinate():
                if self.context["producer"].doc.current_are_producer:
                    result = self.context["producer"].doc.current_are_producer.producerOfCoords.translate_coords(pair)
                    return result

        return super().do_translate_param(arg, index, arg_info)

class ScriptTranFuncParamCoordsMoveToPoint(ScriptTranFuncParamCoords):
    @classmethod
    def supports_func(cls): return ("MoveToPoint", )

    @classmethod
    def params_to_coordinate(cls): return (0, ) # not sure

    def do_translate_func(self, func_name: str, args: list, func_info): 
        coords = self.do_translate_param(args[0], 0, func_info['args'][0])

        is_complex = self.context.get("is_complex")
        is_player = 'player' in str(self.context.get("CutSceneId") or '').lower()
        if not is_complex or is_player:
            line = f'self.i{func_name}({coords})'
        else:
            line = f'self.i{func_name}Post({coords}, locus=locus)'
            instructions = list()
            instructions.append({"line": line})
            line = {"instructions": instructions, "context": self.context, "breaks_after": 1, "is_post_code": 1}

        return line

class ScriptTranFuncsFloatMessage(ScriptTranFuncs):
    @classmethod
    def supports_func(cls): return ("FloatMessage", )

    def do_translate_func(self, func_name: str, args: list, func_info: dict):
        cutSceneId = self.context.get("CutSceneId")
        if cutSceneId:
            # maybe redo to bcs.used_strrefs
            strref = self.do_translate_param(args[1], 1, func_info['args'][1])
            if self.context["producer"].doc.current_are_producer.add_actor_strref_line(cutSceneId, strref):
                func_name = 'FloatMessageDialog'
                return super().do_translate_func(func_name, args, func_info)
        return super().do_translate_func(func_name, args, func_info)

class ScriptTranFuncsCutSceneId(ScriptTranFuncs):
    @classmethod
    def supports_func(cls): return ("CutSceneId", )

    def do_translate_func(self, func_name: str, args: list, func_info: dict):
        name = self.do_translate_param(args[0], 0, func_info['args'][0])
        if name:
            name = common.strip_quotes(common.strip_quotes(name))
        self.context["CutSceneId"] = name

        result = super().do_translate_func(func_name, args, func_info)
        # is_complex = self.context.get("is_complex")
        # if is_complex:
        #     line = result
        #     instructions = list()
        #     instructions.append({"line": line})
        #     result = {"instructions": instructions, "context": self.context, "is_conditional": 1}

        return result

class ScriptTranFuncsStartCutSceneMode(ScriptTranFuncs):
    @classmethod
    def supports_func(cls): return ("StartCutSceneMode", )

    def do_translate_func(self, func_name: str, args: list, func_info: dict):
        if not self.context.get("is_complex"):
            return 'self.iStartCutSceneMode(is_from_dialog=True)'

        return super().do_translate_func(func_name, args, func_info)

class ScriptTranFuncsMarkSpellAndObject(ScriptTranFuncs):
    @classmethod
    def supports_func(cls): return ("MarkSpellAndObject", )

    def do_translate_param_str(self, arg, index: int, arg_info: dict, wrap: str):
        if index == 0:
            return self.do_translate_param_str_spell_from_ints(arg, index, arg_info, wrap)

        return super().do_translate_param_str(arg, index, arg_info, wrap)

class ScriptTranFuncsHaveSpell(ScriptTranFuncs):
    @classmethod
    def supports_func(cls): return ("HaveSpell", "ForceMarkedSpell")

    def d_translate_param_name(self, arg, index: int):
        if index == 0:
            return self.d_translate_param_name_spell(arg, index)

        return super().d_translate_param_name(arg, index)
