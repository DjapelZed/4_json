import json
import codecs


def load_data(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as json_to_parse:
        json_to_parse = json.loads(json_to_parse.read())
    return json_to_parse


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    pretty_print_json(load_data(input('File path: ')))
