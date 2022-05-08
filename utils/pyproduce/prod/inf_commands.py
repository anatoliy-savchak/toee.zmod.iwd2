import common

class InfCommands:
    def __init__(self):
        self.actions = list()
        self.triggers = list()
        self.commands = list()
        self.identifiers = list()
        return

    def _parse_file(self, file_path: str, kind: str):
        result = list()
        with open(file_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            # first skip incorrect lines, should be: 
            # 7 CreateCreature(S:NewObject*,S:ScriptName*,P:Location*,I:Face*)
            tup = line.split(" ", 1)
            if len(tup) <= 1: continue
            sline = tup[1]
            sline = sline.removesuffix("\n")
            ## CreateCreature(S:NewObject*,S:ScriptName*,P:Location*,I:Face*)
            tup = sline.split("(", 1)
            func_name = tup[0]
            sline = tup[1]
            ## S:NewObject*,S:ScriptName*,P:Location*,I:Face*)
            sline = sline.removesuffix(")")
            ## S:NewObject*,S:ScriptName*,P:Location*,I:Face*
            args = list()
            if sline:
                for arg_line in sline.split(","):
                    arg_type, rest = arg_line.split(":", 1)
                    arg_name, arg_ids = rest.split("*", 1) if "*" in rest else (rest, None)
                    arg_info = common.tDict(arg_type = arg_type, arg_name = arg_name, arg_ids = arg_ids, arg_line = arg_line)
                    args.append(arg_info)

            info = common.tDict(func_name = func_name, args = args, line = line, kind = kind)
            result.append(info)
        return result

    def parse_file_actions(self, file_path: str):
        self.actions = self._parse_file(file_path, 'action')
        self.commands.extend(self.actions)
        return

    def parse_file_triggers(self, file_path: str):
        self.triggers = self._parse_file(file_path, 'trigger')
        self.commands.extend(self.triggers)
        return

    def parse_file_identifiers(self, file_path: str):
        self.identifiers = self._parse_file(file_path, 'identifier')
        self.commands.extend(self.identifiers)
        return
