import json

from dict2xml import dict2xml
from string_utils.validation import is_integer, is_decimal


def format_output(obj, output_format):
    if output_format == 'json':
        return json.dumps(obj)
    elif output_format == 'json-pretty':
        return json.dumps(obj, indent=4)
    elif output_format == 'xml':
        return dict2xml(obj, wrap='author')
    elif output_format == 'xml-pretty':
        return dict2xml(obj, wrap='author', indent='    ')
    else:
        return obj


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


def listify(param):
    return [param] if type(param) not in [list, tuple] else param


def singlify(_list):
    return _list[0] if len(_list) == 1 else _list


def run_thread(worker, iterable, *args, **kwargs):
    from concurrent.futures import ThreadPoolExecutor

    worker_result = []

    with ThreadPoolExecutor() as executor:
        for i in iterable:
            executor.submit(worker, i, worker_result, **kwargs)

    return worker_result
