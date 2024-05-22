#!/usr/bin/python3
"""function check if obj is class or an instance of"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, if the object is an instance
    of a class that inherited from, the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        True if obj is an instance or inherited instance class, False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
