#!/usr/bin/python3
"""function that check if obj is class"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
