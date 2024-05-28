#!/usr/bin/python3
"""Serialization and deserialization using XML as alternative format to JSON"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize the dictionary into XML and save it to the given filename."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """Deserialize XML data from the file and return a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    deserialized_data = {}
    for child in root:
        deserialized_data[child.tag] = child.text
    return deserialized_data
