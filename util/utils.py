import json

from dict2xml import dict2xml
from flatdict import FlatterDict
from string_utils.validation import is_integer, is_decimal


def format_output(data, output_format: str):
    if output_format == 'dict-flat':
        return dict(FlatterDict(data, delimiter='.'))
    elif output_format == 'json':
        return json.dumps(data)
    elif output_format == 'json-pretty':
        return json.dumps(data, indent=4)
    elif output_format == 'xml':
        return dict2xml(data, wrap='author')
    elif output_format == 'xml-flat':
        flat = format_output(data, output_format='dict-flat')
        return format_output(flat, output_format='xml')
    else:
        return data


def cast(string: str):
    string = string.strip()

    if is_integer(string):
        return int(string)
    elif is_decimal(string):
        return float(string)
    elif string == '-':
        return None
    else:
        return string


def listify(val) -> list:
    return [val] if type(val) not in (list, tuple) else val


def compact_list(_list: list):
    return _list[0] if len(_list) == 1 else _list


def singlify(val):
    return val[0] if type(val) in (list, tuple) else val


def run_thread(worker, iterable, **kwargs):
    from concurrent.futures import ThreadPoolExecutor

    result = []

    with ThreadPoolExecutor() as executor:
        for i in iterable:
            executor.submit(worker, i, result, **kwargs)

    return result
