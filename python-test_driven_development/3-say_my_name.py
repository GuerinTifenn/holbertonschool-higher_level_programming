#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size length of the square's side.
        Must be a non-negative integer.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
