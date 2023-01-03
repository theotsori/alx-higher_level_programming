#!/usr/bin/python3
"""A class Rectangle that deifnes a rectangle"""


class Rectangle:
    """A class rectangle that tests Eval magic"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for i in range(self.height))

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
