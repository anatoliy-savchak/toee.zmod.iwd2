import ast
import produce_items

_inf_scripting_lines = None

def init_inf_scripting_lines():
    global _inf_scripting_lines
    if _inf_scripting_lines:
        return

    fn = "D:/Dev.Home/GitHub/anatoliy-savchak/toee.zmod.iwd2/src/zmod_iwd2_core/scr/inf_scripting.py"
    with open(fn , 'r') as f:
        _inf_scripting_lines = f.readlines()

    return

def transate_trigger_lines(trigger_lines: list):
    lines = list()
    for i, trigger_line in enumerate(trigger_lines):
        line = transate_trigger_line(trigger_line)
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

def transate_action_lines(action_lines: list):
    lines = list()
    for i, action_line in enumerate(action_lines):
        line = transate_trigger_line(action_line)
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
            if isinstance(arg, ast.Name):
                s = '"' + arg.id + '"'
            else:
                if isinstance(arg.value, int):
                    s = str(arg.value)
                else:
                    s = '"' + str(arg.value) + '"'
            func_args.append(s)
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
                    line = f'{line_tup[1]}({", ".join(args)})' 
                    result = (line, line_tup[1], line_tup[2])

    return result