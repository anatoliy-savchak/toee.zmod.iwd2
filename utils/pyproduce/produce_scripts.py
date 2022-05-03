import sys
import inspect
import ast
import produce_items
#import pyproduce

_inf_scripting_lines = None

def init_inf_scripting_lines():
    global _inf_scripting_lines
    if _inf_scripting_lines:
        return

    fn = "D:/Dev.Home/GitHub/anatoliy-savchak/toee.zmod.iwd2/src/zmod_iwd2_core/scr/inf_scripting.py"
    with open(fn , 'r') as f:
        _inf_scripting_lines = f.readlines()

    return

def transate_trigger_lines(trigger_lines: list, producer_app):
    lines = list()
    for i, trigger_line in enumerate(trigger_lines):
        #line = transate_trigger_line(trigger_line)
        line = ScriptTran.translate_script_line(trigger_line, producer_app)
        if i == 0:
            line = "if " + line
        else:
            line = "\t and " + line

        if i == len(trigger_lines) - 1: # last
            line = line + ":"
        else:
            line = line + " \\"
        lines.append(line)

    return lines

def transate_action_lines(action_lines: list, producer_app):
    lines = list()
    for i, action_line in enumerate(action_lines):
        #line = transate_trigger_line(action_line)
        line = ScriptTran.translate_script_line(action_line, producer_app)
        lines.append(line)

    return lines

def transate_trigger_line(trigger_line: str):
    line = ""
    if not trigger_line: return line
    if trigger_line[0] == "!":
        line += "not "
        trigger_line = trigger_line.removeprefix("!")
        
    line_tup = reassamble_call(trigger_line)
    line_tup = process_func(line_tup)
    trigger_line = line_tup[0]
    #trigger_line = ScriptTran.translate_script_line(trigger_line)

    line += trigger_line

    return line

def reassamble_call(line: str):
    line = line.replace("[", '"[').replace("]", ']"')
    tree = ast.parse(line)
    f = tree.body[0].value.func
    funct_name = None
    func_args = None
    if isinstance(f, ast.Name):
        funct_name = f.id
        result = "i" + funct_name + "("
        comma = ""
        func_args = list()
        for arg in tree.body[0].value.args:
            s = ""
            sarg = None
            if isinstance(arg, ast.Name):
                s = '"' + arg.id + '"'
                sarg = arg.id
            else:
                if isinstance(arg.value, int):
                    s = str(arg.value)
                    sarg = arg.value
                else:
                    if funct_name == "ClassEx":
                        funct_name = "ClassEx"
                    s = '"' + str(arg.value) + '"'
                    sarg = arg.value
            func_args.append(sarg)
            result += comma + s
            comma = ", "
        result += ")"

        if not check_func_implemented("i" + funct_name):
            print(f"Func not implemented: {funct_name} => {line}")
    else:
        if line == "True()":
            return ("True", None, None)
        print(f"Unparsed: {line}")
        return (line, funct_name, func_args)
    result = "self." + result 
    return (result, funct_name, func_args)

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

def check_func_implemented(func_name: str):
    global _inf_scripting_lines
    if not _inf_scripting_lines:
        init_inf_scripting_lines()
    if not _inf_scripting_lines:
        return False
    func_name = "def "+ func_name
    result = not next((line for line in _inf_scripting_lines if func_name in line), None) is None
    return result

def process_func(line_tup: tuple):
    result = line_tup
    if line_tup and line_tup[1]:
        # is function
        func_namel = line_tup[1].lower()
        func_namel = str(func_namel).replace('"', '')
        if func_namel == "giveitemcreate":
            item_file_name = line_tup[2][0].replace('"', '')
            item_cls = produce_items.ItemBase.find_item_class(item_file_name)
            if item_cls:
                line = item_cls.give_item_create_line(item_file_name, line_tup[2][2] if len(line_tup[2]) > 2 else 0)
                if line:
                    return (line, line_tup[1], line_tup[2])

                proto_const = item_cls.get_proto_const()
                if proto_const:
                    args = list()
                    for a in line_tup[2]:
                        if len(args) == 0:
                            args.append(f'"{proto_const}"')
                        else:
                            args.append(a)
                    line = f'{line_tup[1]}({", ".join([str(v or "") for v in args])})' 
                    result = (line, line_tup[1], line_tup[2])

    return result

class ScriptTran:
    def __init__(self, line: str, producer_app):
        self.line = line
        self.producer_app = producer_app
        return

    @staticmethod
    def translate_script_line(aline: str, producer_app):
        result = None
        prefix = ""
        if aline and aline[0] == "!":
            prefix = "not "
            aline = aline.removeprefix("!")

        while True:
            lline = aline.lower()
            # first check simple things like True()
            whole_class = next((cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass) if issubclass(cls, ScriptTran) 
                and cls.is_whole_liner() and lline in cls.whole_lines()), None)
            if whole_class:
                result = whole_class(aline, producer_app).do_translate_script_line(aline)
                break

            func_classes = [cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass) if issubclass(cls, ScriptTran) and cls.is_func_liner()]
            if func_classes:
                func_name, args = ScriptTran._parse_func(aline)
                func_name_lo = func_name.lower()
                if func_name_lo == "giveitemcreate":
                    func_name_lo = func_name_lo
                cls = next((cls for cls in func_classes if func_name_lo in cls.supports_func()), None)
                if cls:
                    o = cls(aline, producer_app)
                    result = o.translate_func(func_name, args)
                    break
                cls = next((cls for cls in func_classes if cls.supports_funcs_default()), None)
                if cls:
                    o = cls(aline, producer_app)
                    result = o.translate_func(func_name, args)
                    break
            break
        if result is None:
            raise Exception("No line support!")
        return prefix + result

    @staticmethod
    def _parse_func(line: str):
        line = line.replace("[", '"[').replace("]", ']"')
        tree = ast.parse(line)
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
    def __init__(self, line: str, producer_app):
        super().__init__(line, producer_app)
        self.args = None
        return

    @classmethod
    def is_func_liner(cls): return True

    def translate_func(self, func_name: str, args: list): 
        func_info = next((func_info for func_info in self.producer_app.commands.commands if func_info.func_name.lower() == func_name.lower()), None)
        if not func_info:
            raise Exception(f"No info for func {func_name}")
        return self.do_translate_func(func_name, args, func_info)
    
    def do_translate_func(self, func_name: str, args: list, func_info): 
        strargs = list()
        self.args = args
        for index, arg in enumerate(args):
            arg_info = func_info.args[index]
            s = self.do_translate_param(arg, index, arg_info)
            strargs.append(s)
        result = "self.i" + func_name + "(" + ", ".join(strargs) + ")"

        if not check_func_implemented("i" + func_name):
            print(f"Func not implemented: {func_name} => {self.line}")

        return result

    def do_translate_param(self, arg, index: int, arg_info):
        w = "'" if index in self.literal_params_to_wrap() else ""
        s = ""
        if isinstance(arg, ast.Name):
            s = self.d_translate_param_name(arg, index)
        else:
            if isinstance(arg.value, int):
                s = str(arg.value)
            else:
                s = '"' + w + str(arg.value) + w + '"'
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
        item_file_name = self.do_translate_param(args[index_with_item], index_with_item, func_info.args[index_with_item])
        item_file_name = item_file_name.replace('"', '').strip()
        if item_file_name == "00Leat01":
            print("")
        item_cls = produce_items.ItemBase.find_item_class(item_file_name)
        if item_cls:
            if make_create:
                line = item_cls.give_item_create_line(item_file_name, self.do_translate_param(args[2], 2, func_info.args[2]) if len(args) > 2 else 0)
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
                            args2.append(self.do_translate_param(a, i, func_info.args[i]))
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
