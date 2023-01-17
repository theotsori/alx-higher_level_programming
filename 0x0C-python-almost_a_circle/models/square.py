#!/usr/bin/python3
""" A class rectangle that inherits from Square """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Implemetation of the square def from class rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing from rectangle"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """(int) width to be used"""
        return self.width

    @size.setter
    def size(self, value):
        """checks if size value is int and greater than 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    @Rectangle.width.setter
    def width(self, value):
        """(int) size width"""
        self.size = value

    @Rectangle.height.setter
    def height(self, value):
        """(int) size height"""
        self.size = value

    def update(self, *args, **kwargs):
        """checks args and kwargs"""
        if args:
            if len(args) > 4:
                raise TypeError("update() takes from 1 to 4 positional"
                                "argument but {} were given".format(len(args)))
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
        """Stdout display"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """chekcs self on dictioary"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
