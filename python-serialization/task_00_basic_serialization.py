#!/usr/bin/python3
"""Basic serialization module that adds the functionality"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON file.

    :param data: The Python dictionary to serialize.
    :param filename: The name of the output JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Deserializes it into a Python dictionary.

    :param filename: The name of the JSON file to load.
    :return: A Python dictionary with the deserialized data.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
