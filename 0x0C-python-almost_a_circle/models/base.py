#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """manage id attr in all future classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    def update(self, *args, **kwargs):
        if args:
            for key, value in enumerate(args):
                setattr(self, self.__class__.name__ + str(key), value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        else:
            istance = cls()
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                list_dictionaries = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, "w") as f:
            f.write(json_string)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                list_dictionaries = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dictionaries]
        except FileNotFoundError:
            return []
