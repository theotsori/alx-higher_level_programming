#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Creating width and height options."""
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        Initialziing height as a private instance attribute.
        """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """
        setting the property setter for height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    @property
    def width(self):
        """
        Initializing the width attribute.
        """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
        setting the property for width attribute.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value
