#!/usr/bin/python3
"""Module that defines a Square with property getters and setters."""


class Square:
    """Defines a square by its size with property accessors."""

    def __init__(self, size=0):
        """Initializes the square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            The area of the square (size squared).
        """
        return self.__size ** 2
