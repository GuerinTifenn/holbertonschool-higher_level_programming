#!/usr/bin/python3
"""
This module defines an empty class named Square.
"""


class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): Private instance attribute representing size of square.
        __position (tuple): Private instance attribute representing the
        position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with optional size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or if position is not a tuple
            of two positive integers.
            ValueError: If size is less than 0 or if position contains negative
            integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
            value (int): The size value to be set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for retrieving the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position of the square.

        Args:
            value (tuple): The position value to be set.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
            ValueError: If value contains negative integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(x, int) for x in value) or
            value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' using the specified position.

        If the size of the square is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
