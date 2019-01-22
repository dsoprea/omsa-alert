import json

def get_pretty_json(data):
    return json.dumps(
        data,
        sort_keys=True,
        indent=4,
        separators=(',', ': '))

def check_expected_values(info, healthy_values):
    for field_name, expected_values in healthy_values.items():
        actual_value = info[field_name]
        if actual_value not in expected_values:
            error_message = \
                "'{}' value '{}' not in {}".format(
                field_name, actual_value, expected_values)

            return error_message

    return None
