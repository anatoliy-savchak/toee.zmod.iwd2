from cmath import e
from email import message
import os
import sys
import inspect
import ast
import produce_items
import producer_base
import json
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

        self.current_are_name = None
        self.current_cre_name = None
        self.current_actor_name = None
        self.error_messages = list()
        self.log_usage = False
        self.log_strrefs = False
        self.log_statistics = False
        return

    def transate_trigger_lines(self, trigger_lines: list, are_name: str, cre_name: str, actor_name: str = None):
        self.current_are_name = are_name
        self.current_cre_name = cre_name
        self.current_actor_name = actor_name
        if actor_name == 'Jorun':
            print('J')
            if next((line for line in trigger_lines if 'Dwarf_Gray' in line), None):
                print('Dwarf_Gray')

        trigger_lines2 = list()
        for i, action_line in enumerate(trigger_lines):
            action_linea = self.remove_comment(action_line)
            if not action_linea: continue
            trigger_lines2.extend(condition_split(action_linea))

        lines = list()
        or_left = 0
        or_count_max = 0
        for i, trigger_line in enumerate(trigger_lines2):
            #line = transate_trigger_line(trigger_line)
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
                line = ScriptTran.translate_script_line(trigger_linea, self)
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

            if i == len(trigger_lines) - 1: # last
                line = line + ":"
            else:
                line = line + " \\"
            lines.append(line)

        return lines

    def transate_action_lines(self, action_lines: list, are_name: str = None, cre_name: str = None):
        self.current_are_name = are_name
        self.current_cre_name = cre_name

        if cre_name == '10JORUN':
            print('J')
            if next((line for line in action_lines if 'Dwarf_Gray' in line), None):
                print('Dwarf_Gray')

        lines = list()
        action_lines2 = list()
        for i, action_line in enumerate(action_lines):
            action_linea = self.remove_comment(action_line)
            if not action_linea: continue
            action_lines2.extend(condition_split(action_linea))
        
        for i, action_line in enumerate(action_lines2):
            #line = transate_trigger_line(action_line)
            action_linea = action_line.strip()
            if not action_linea: continue
            action_linea = action_linea.replace('#', '"')
            line = ScriptTran.translate_script_line(action_linea, self)
            if line is None:
                line = 'pass'
            lines.append(line)

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

    def produce_func_defs(self, out_file_path: str = None):
        if not out_file_path:
            out_file_path = os.path.join(self.doc.core_dir, "scr/inf_scripting_auto.py")
        template_path = 'data/inf_scripting_auto.py'
        prod = producer_base.ProducerOfFile(self.doc, out_file_path, template_path, True)
        prod.indent()

        def produce_funcs(commands, label: str):
            nonlocal prod
            prod.writeline(f'########## {label} ##########')
            for rec in commands:
                func_name = rec["func_name"]
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
    def __init__(self, line: str, producer):
        self.line = line
        self.producer = producer
        return

    @staticmethod
    def translate_script_line(aline: str, producer):
        if aline == 'SubRace(LastSeenBy(Myself),PURERACE)':
            print()
        result = None
        prefix = ""
        if aline and aline[0] == "!":
            prefix = "not "
            aline = aline.removeprefix("!").strip()

        while True:
            lline = aline.lower()
            # first check simple things like True()
            whole_class = next((cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass) if issubclass(cls, ScriptTran) 
                and cls.is_whole_liner() and lline in cls.whole_lines()), None)
            if whole_class:
                result = whole_class(aline, producer).do_translate_script_line(aline)
                break

            aline = aline.replace('#', '"')
            func_name, args = ScriptTran._parse_func(aline, producer)
            if func_name is None:
                return None
            result = ScriptTran._process_func(aline, func_name, args, producer)
            break
        if result is None:
            raise Exception("No line support!")
        return prefix + result

    @staticmethod
    def _process_func(aline, func_name, args, producer):
        func_classes = [cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass) if issubclass(cls, ScriptTran) and cls.is_func_liner()]
        func_name_lo = func_name.lower()
        if func_name_lo == "giveitemcreate":
            func_name_lo = func_name_lo
        cls = next((cls for cls in func_classes if func_name_lo in cls.supports_func()), None)
        if cls:
            o = cls(aline, producer)
            result = o.translate_func(func_name, args)
            return result
        cls = next((cls for cls in func_classes if cls.supports_funcs_default()), None)
        if cls:
            o = cls(aline, producer)
            result = o.translate_func(func_name, args)
            return result
        return None

    @staticmethod
    def _parse_func(line: str, producer):
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
            if producer:
                producer.log_error(error_message=e.msg + ' ' + line)
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
    def __init__(self, line: str, producer):
        super().__init__(line, producer)
        self.args = None
        return

    @classmethod
    def is_func_liner(cls): return True

    def translate_func(self, func_name: str, args: list): 
        func_info = next((func_info for func_info in self.producer.doc.commands.commands if func_info["func_name"].lower() == func_name.lower()), None)
        if not func_info:
            print(f"No info for func {func_name}, line: {self.line}")
            self.producer.log_error(f"No info for func {func_name}, line: {self.line}")
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
        self.producer.log_func(self.line, func_name, strargs_src, strargs, func_info)

        if not self.producer.check_func_implemented("i" + func_name):
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
            s = ScriptTran._process_func(self.line, c.func.id, c.args, self.producer)
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
                        s = '"\'' + w + str(arg.value) + w + '\'"'
                else:
                    s = '"' + w + str(arg.value) + w + '"'
            else:
                print('Wrong value!')
        return s

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
        if s.lower() == 'false': return "False"
        elif s.lower() == 'true': return "True"
        return '"' + arg.id + '"'

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
        if item_file_name == "00Leat01":
            print("")
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
    def supports_func(cls): return ("GiveItemCreate".lower(), "GiveItem".lower())

class ScriptTranFuncsItem_GiveItemEval(ScriptTranFuncsItem):
    @classmethod
    def params_to_itemize(cls): return (0, )

    def do_translate_func(self, func_name: str, args: list, func_info): 
        line = self.do_process_item(func_name, args, func_info, index_with_item = 0, make_create = False, make_proto = True)
        if not line is None:
            return line

        return super().do_translate_func(func_name, args, func_info)

    @classmethod
    def supports_func(cls): return ("PartyHasItem".lower(), "TakePartyItemNum".lower())

class ScriptTranFuncsItem_Debug(ScriptTranFuncs):
    @classmethod
    def supports_func(cls): return ("SetCriticalPathObject".lower(), )

    #def do_translate_func(self, func_name: str, args: list, func_info): return super().do_translate_func(func_name, args, func_info)

    #def do_translate_param(self, arg, index: int, arg_info): return super().do_translate_param(arg, index, arg_info)
