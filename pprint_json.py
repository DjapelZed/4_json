import json
import shutil
import codecs
import os


def load_data(filepath):
    shutil.copy2(filepath, r'json-txt.txt')
    json_to_parse = codecs.open('json-txt.txt', 'r', 'utf_8_sig')
    parsed_json = json.loads(json_to_parse.read())
    json_to_parse.close()
    os.remove('file_json.txt')
    return parsed_json


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    pretty_print_json(load_data(input()))
