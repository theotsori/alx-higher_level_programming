#!/usr/bin/python3
"""A class that defines a square."""


class Square:
    """
    This class represents a square. It has a size and a position,\
    and provides methods to calculate its area and print to stdout.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square instance with the given size and position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Return the size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Set the size of the square to the given value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """
        Return the position of thee square.
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Set te position of the square to the given value.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        Return the area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Print the square to stdout.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Return a string representation of the square.
        """
        s = ""
        if self.size == 0:
            return "\n"

        for i in range(self.position[1]):
            s += "\n"
        for i in range(self.size):
            s += " " * self.position[0] + "#" * self.size + "\n"
        return s
