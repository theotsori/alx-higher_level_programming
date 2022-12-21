#!/usr/bin/python3
"""A class Square that defines a sqaure"""


class Square:
    """A class representing a square.

    Attribute:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
    """Initailize a new square.

    Args:
        size (int, optional): The size of the square. Defaults to 0.
    """
        self.size = size

    @property
    def size(self):
    """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
    """Set the size of the square.

    Args:
        value (int): The new size of the square.

    Raises:
        TypeError: If 'value' is not an integer
        ValuError: If 'value' is less tan 0.
    """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
    """Return the current square area."""
        return self.size ** 2

    def my_print(self):
    """Print the sqaure with the character #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
