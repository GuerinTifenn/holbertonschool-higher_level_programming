#!/usr/bin/python3
"""function writes a text file (UTF8) and returns the num of characters"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
