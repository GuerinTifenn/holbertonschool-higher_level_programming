#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Add two integers, casting floats to integers.

    Args:
        a: First number, must be int or float.
        b: Second number, must be int or float, default is 98.

    Returns:
        The sum of a and b as integers.

    Raises:
        TypeError: If a or b are not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
