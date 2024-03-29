#!/usr/bin/python3

""" A Base class model for the almost a circle project. """

import json
import turtle
import csv


class Base:
    """Manage id attr in all future classes in this project.
    Private Class Attribute:
        __nb_object (int): Number of intialized bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initilizing of the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converting string to json """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Function to save file in json"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Loading from json file"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    def update(self, *args, **kwargs):
        """ updating parameters """
        if args:
            for key, value in enumerate(args):
                setattr(self, self.__class__.name__ + str(key), value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def create(cls, **dictionary):
        """Using kwargs in a different way"""
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
        """loaing file from a json"""
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
        """save file to a csv."""
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, "w") as f:
            f.write(json_string)

    @classmethod
    def load_from_file_csv(cls):
        """Load from a csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                list_dictionaries = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dictionaries]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangle, list_squares):
        """Turtle draw from instructions"""
        for rect in list_rectangle:
            turtle.color("black")
            turtle.begin_fill()
            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)
            turtle.right(90)
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.right(90)
            turtle.end_fill()
            turtle.forward(50)
        for square in list_squares:
            turtle.color("brown")
            turtle.begin_fill()
            turtle.forward(square.size)
            turtle.left(90)
            turtle.forward(square.size)
            turtle.left(90)
            turtle.forward(square.size)
            turtle.left(90)
            turtle.forward(square.size)
            turtle.left(90)
            turtle.end_fill()
            turtle.forward(50)
        turtle.exitonclick()
