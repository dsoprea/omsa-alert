import json

def get_pretty_json(data):
    return json.dumps(
        data,
        sort_keys=True,
        indent=4,
        separators=(',', ': '))
