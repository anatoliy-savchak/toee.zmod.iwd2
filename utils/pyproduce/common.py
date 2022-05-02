import json

from json import JSONEncoder
class EncodeAsDict(JSONEncoder):
    def default(self, o):
        return o.__dict__ 

def tDict(**kwargs):
    return dict(kwargs)

def lines_find(lines: list, after: str):
    return next((index for index, line in enumerate(lines) if after in line), None)

def lines_after_cutoff(lines: list, after: str, add_more_line_count: int = 0):
    index = lines_find(lines, after)
    if not index is None:
        del lines[index + 1 + add_more_line_count:]
    return index

def lines_after_before_cutoff(lines: list, after: str, before: str):
    index_after = lines_find(lines, after)
    index_before = lines_find(lines, before)
    if not index_after is None and not index_before is None:
        if index_after + 1 < index_before:
            del lines[index_after+1:index_before-1]
    return index_after + 1

def marked_line(code: str):
    return f"#### {code} ####"

def lines_method(lines: list, method_line: str):
    subline = method_line
    found_def = len(lines)
    found_def_return = found_def + 1

    found_defs = [index for index, line in enumerate(lines) if subline in line ]
    if not found_defs:
        lines.append(method_line)
        lines.append("\t"+"return")
        lines.append("")
    else:
        found_def = found_defs[0]
        subline = "\t\treturn"
        found_def_returns = [index for index, line in enumerate(lines) if index > found_def and str(line).startswith(subline)]
        if found_def_returns:
            found_def_return = found_def_returns[0]

        while found_def_return > found_def +1 and found_def_return < len(lines):
            found_def_return += -1
            lines.pop(found_def_return)
    return found_def_return

def read_file_json(file_path: str) -> dict:
    with open(file_path, encoding='utf-8', mode='r') as f:
        file_ = json.load(f)
    return file_
