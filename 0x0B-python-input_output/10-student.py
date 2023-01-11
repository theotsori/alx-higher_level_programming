#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """ A class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        obj_dict = self.__dict__
        json_compatible_obj_dict = {}
        if attrs is None:
            for key, value in obj_dict.items():
                if isinstance(value, (str, int)):
                    json_compatible_obj_dict[key] = value
        else:
            for key, value in obj_dict.items():
                if key in attrs and isinstance(value, (str, int)):
                    json_compatible_obj_dict[key] = value
        return json_compatible_obj_dict
