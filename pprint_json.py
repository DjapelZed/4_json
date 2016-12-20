import json
import codecs


def load_data(filepath):
    json_to_parse = codecs.open(filepath, 'r', 'utf-8')
    parsed_json = json.loads(json_to_parse.read())
    json_to_parse.close()
    return parsed_json


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    pretty_print_json(load_data(input('File path: ')))
