#!/usr/bin/python3
"""
This module defines an empty class named Square.
"""


class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): Private instance attribute representing size of square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
