#!/usr/bin/python3
"""
A class REctangle that inherits from Base

Attributes:
width (int): width of the rectangle
height (int): height of the rectangle
x (int): x-coordinate of the rectangle
y (int): y-coordinate of the rectangle
id (int): id of the rectangle

Methods:
area(self)
returns the area of the rectangle
display(self)
prints the rectangle using # characters
str(self)
returns a string representation of the rectangle
update(self, *args, **kwargs)
updates the attributes of the rectangle
to_dictionary(self)
returns a dictionary representation of the rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    A class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the rectangle object with given width, height,
        x and y coordinates, and id.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """int: width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width of the rectangle

        Args:
            value (int): width of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height of the rectangle

        Args:
            value (int): height of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: x-coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        set the x-coordinate of the rectangle

        Args:
            value (int): x-coordinate of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: y-coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        set the y-coordinate of the rectangle

        Args:
            value (int): y-coordinate of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints the rectangle using # characters
        """
        for i in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        returns a string representation of the rectangle

        Returns:
            str: string representation of the rectangle
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        updates the attributes of the rectangle

        Args:
            *args: variable length argument list
            **kwargs: keyworded variable length argument list
        """
        if len(args) > 0:
            self.__id = args[0]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if len(args) > 1:
            self.__width = args[1]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if len(args) > 2:
            self.__height = args[2]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if len(args) > 3:
            self.__x = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if len(args) > 4:
            self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns a dictionary representation of the rectangle

        Returns:
            dict: dictionary representation of the rectangle,
            containing the keys 'id', 'width', 'height', 'x' and
            'y' with corresponding values.
        """
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
