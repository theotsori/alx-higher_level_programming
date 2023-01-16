#!/usr/bin/python3
""" A class rectangle that inherits from Square """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Implemetation of the square def from class rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    @Rectangle.width.setter
    def width(self, value):
        self.size = value

    @Rectangle.height.setter
    def height(self, value):
        self.size = value

    def update(self, *args, **kwargs):
        if args:
            if len(args) > 4:
                raise TypeError("update() takes from 1 to 4 positional arguments but {} were given".format(len(args)))
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
