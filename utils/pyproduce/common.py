from json import JSONEncoder
class EncodeAsDict(JSONEncoder):
    def default(self, o):
        return o.__dict__ 

def tDict(**kwargs):
    return dict(kwargs)

def lines_find(lines: list, after: str):
    return next((index for index, line in enumerate(lines) if after in line), None)

def lines_after_cutoff(lines: list, after: str):
    index = lines_find(lines, after)
    if not index is None:
        del lines[index+1:]
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