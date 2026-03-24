#!/usr/bin/python3
"""Module that defines a Square with a private size attribute."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size):
        """Initializes the square instance.

        Args:
            size: The size of the square.
        """
        self.__size = size
