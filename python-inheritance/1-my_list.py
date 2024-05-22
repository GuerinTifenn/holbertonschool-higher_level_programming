#!/usr/bin/python3
"""A module that defines a class MyList"""


class MyList(list):
    """
    MyList class inherits from list.

    Public instance method:
        print_sorted(self): Prints the list in sorted order (ascending).
                            Assumes all elements of the list are of type int.
    """
    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).
        """

        sorted_list = sorted(self)

        print(sorted_list)
