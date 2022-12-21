#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """A class defining a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """property defining size"""
        return self._size

    @size.setter
    def size(self, value):
        """setter defining square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """property defining square position"""
        return self._position

    @position.setter
    def position(self, value):
        """setter defining square position"""
        if not isinstance(value, tuple) or len(value) != 2 \
           or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position mest be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """used to obtain area of square"""
        return self.size ** 2

    def my_print(self):
        """used to print value and sie of square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
