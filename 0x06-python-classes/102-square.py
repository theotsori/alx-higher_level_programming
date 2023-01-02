class Square:
    """Class that represents a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a square with a given size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """int: The size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not a number.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Returns the current square area.

        Returns:
            int: The current square area.
        """
        return self.size ** 2

    def __eq__(self, other):
        """Compares two squares based on their area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the two squares have the same area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares two squares based on their area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the two squares have different area, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Compares two squares based on their area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the current square has a greater area than the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Compares two squares based on their area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the current square has a greater or equal area than the other square, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compares two squares based on their area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the current square has a smaller area than the other square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Compares two squares based on their area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the current square has a smaller or equal area than the other square, False otherwise.
        """
        return self.area() <= other.area()
