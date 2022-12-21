#!/usr/bin/python3
"""A class that defines a square."""


class Square:
    """A class representing a square.

    Attributes:
        size (int): defination of a square.

    """
    def __init__(self, size=0):
        """Initializing a square.

        Args:
            size (int, optional):

        Raises:
            TypeError:
            ValueError:

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Initializes self"""
        return self.__size ** 2
