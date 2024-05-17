#!/usr/bin/python3
"""
This module defines an empty class named Square.
"""


class Square:
    """
    This class represents a square with no attributes or methods.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): Private instance attribute representing the size of
            the square.
        """
        self.__size = size
