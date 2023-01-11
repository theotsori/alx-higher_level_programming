#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """ Function that returns the dictionary
        description with simple data
    """
    obj_dict = obj.__dict__
    json_compatible_obj_dict = {}
    for key, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_compatible_obj_dict[key] = value
    return json_compatible_obj_dict
