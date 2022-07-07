import json

from dict2xml import dict2xml
from flatdict import FlatDict
from string_utils.validation import is_integer, is_decimal


def format_output(data, output_format):
    if output_format == 'dict-flat':
        return dict(FlatDict(data, delimiter='.'))
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


def listify(val):
    return [val] if type(val) not in [list, tuple] else val


def compact_list(_list):
    return _list[0] if len(_list) == 1 else _list


def run_thread(worker, iterable, *args, **kwargs):
    from concurrent.futures import ThreadPoolExecutor

    worker_result = []

    with ThreadPoolExecutor() as executor:
        for i in iterable:
            executor.submit(worker, i, worker_result, **kwargs)

    return worker_result
