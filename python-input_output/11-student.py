#!/usr/bin/python3
"""Student to JSON and back module"""


class Student:
    """
    A class that defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student with first name, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved. Otherwise, all attributes must
        be retrieved.
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        You can assume json will always be a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
