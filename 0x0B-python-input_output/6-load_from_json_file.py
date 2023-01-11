#!/usr/bin/python3
"""function that creats an obj fro json file"""
import json


def load_from_json_file(filename):
    """Implementation of the function"""
    with open(filename, 'r') as json_file:
        json_string = json_file.read()
        return json.loads(json_string)
