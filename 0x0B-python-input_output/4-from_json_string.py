#!/usr/bin/python3
"""Function that returns an object rep by json string"""


def from_json_string(my_str):
    """From JSON string to object"""
    import json
    return json.loads(my_str)
