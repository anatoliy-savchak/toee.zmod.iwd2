import json

from json import JSONEncoder
class EncodeAsDict(JSONEncoder):
    def default(self, o):
        return o.__dict__ 

def tDict(**kwargs):
    return dict(kwargs)

def lines_find(lines: list, after: str, after_line_id: int = None):
    return next((index for index, line in enumerate(lines) if (after_line_id is None or index > after_line_id) and after in line), None)

def lines_find_lower(lines: list, after: str, after_line_id: int = None):
    return next((index for index, line in enumerate(lines) if (after_line_id is None or index > after_line_id) and after in line.lower()), None)

def lines_after_cutoff(lines: list, after: str, add_more_line_count: int = 0):
    index = lines_find(lines, after)
    if not index is None:
        del lines[index + 1 + add_more_line_count:]
    return index

def lines_after_before_cutoff(lines: list, after: str, before: str):
    index_after = lines_find(lines, after)
    if index_after is None:
        return None
    index_before = lines_find(lines, before, after_line_id = index_after)
    if not index_after is None and not index_before is None:
        if index_after + 1 < index_before:
            del lines[index_after+1:index_before]
    return index_after+1

def marked_line(code: str):
    return f"#### {code} ####"

def lines_method(lines: list, method_line: str):
    subline = method_line
    found_def = len(lines)
    found_def_return = found_def + 1

    found_defs = [index for index, line in enumerate(lines) if subline in line ]
    if not found_defs:
        lines.append("")
        lines.append(method_line)
        lines.append("\t\t"+"return")
        found_def_return = len(lines) - 1
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

def write_json(file_path: str, obj):
    with open(file_path, 'w') as f:
        json.dump(obj, f, indent=4)
    return

def text_of_strrefs(d: dict, name1: str, name2: str = None):
    text = None
    if el := d.get(name1):
        if text := el.get("Text"):
            return text
    if name2:
        if el := d.get(name2):
            if text := el.get("Text"):
                return text
    return text
    
def strip_quotes(s, notify = False):
	if s and (s[0] == "'" or s[0] == '"'):
		r = s.strip()
		r = r[1:-1]
		if notify:
			return r, s[0]
		else:
			return r
	else:
		if notify:
			return s, None
		else:
			return s
	return

def parse_mes_lines(lines: list, make_key_int: bool = False) -> dict:
    result = dict()
    for line in lines:
        line = str(line)
        if not line.startswith('{'): continue
        line = line.replace('\n', '')
        _, code_, value_ = line.split('{', 2)
        code, _ = code_.split('}', 2)
        value, _ = value_.split('}', 2)
        if make_key_int:
            code = int(code)
        result[code] = value
    return result

def str_to_name(s: str):
    return s.replace(' ', '_').replace('(', '').replace(')', '')