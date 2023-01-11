#!/usr/bin/python3
"""
   Py script that adds all args to py
   list and save in a file
"""
import json
import sys


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as json_file:
        json_string = json.dumps(my_obj)
        json_file.write(json_string)


def load_from_json_file(filename):
    with open(filename, 'r') as json_file:
        json_string = json_file.read()
        return json.loads(json_string)


try:
    data = load_from_json_file('add_item.json')
except FileNotFoundError:
    data = []

for item in sys.argv[1:]:
    data.append(item)

save_to_json_file(data, 'add_item.json')
