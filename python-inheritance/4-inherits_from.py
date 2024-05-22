#!/usr/bin/python3
"""checks if obj is of a class that inherits"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        True if obj is an inherited instance of a_class,
        but not an instance of a_class itself.
    """
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    return False
