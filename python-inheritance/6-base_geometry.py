#!/usr/bin/python3
"""class BaseGeometrie"""


class BaseGeometry:
    """
    BaseGeometry class with a method area that raises an Exception.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
