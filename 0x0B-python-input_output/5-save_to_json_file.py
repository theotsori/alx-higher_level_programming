#!/usr/bin/python3
"""function that save object to file"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to a text file
       json_obj = json.dumps(my_obj)
       with open(filename, "w") as file:
          file.write(json_obj)
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
