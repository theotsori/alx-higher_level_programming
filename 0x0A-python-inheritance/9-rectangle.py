#!/usr/bin/python3
"""A class REctangle that inherits form BaseGeometry"""


class BaseGeometry:
    """A parent class to Rectangle"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater tahn 0".format(name))


class Rectangle(BaseGeometry):
    """A class Rectangle initialization"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
