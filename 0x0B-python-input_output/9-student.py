#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """ Implemetation of the student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        obj_dict = self.__dict__
        json_compatible_obj_dict = {}
        for key, value in obj_dict.items():
            if isinstance(value, (str, int)):
                json_compatible_obj_dict[key] = value
        return json_compatible_obj_dict
