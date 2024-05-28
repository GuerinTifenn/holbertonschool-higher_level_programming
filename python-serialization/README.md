# Python - Serialization

## Introduction:

Welcome to our exploration of marshaling and serialization, two fundamental concepts in computer science that enable the efficient storage and transmission of data. In this programming project, you will delve deep into how data can be transformed and communicated between different parts of a system, or even across different systems. This project is designed to enhance your understanding and practical skills in handling data in real-world applications.

## What is Marshaling?

Marshaling is the process of transforming memory objects into a format that can be stored or transmitted over a network. It involves packaging complex objects and their attributes into a simpler, often binary, format. This is crucial in scenarios such as remote procedure calls, where objects need to be represented in a standard format across different computing platforms.

## What is Serialization?

Serialization, closely related to marshaling, specifically involves converting data structures or object states into a format that can be easily saved to a file or sent over a network. The main goal of serialization is to preserve the state of an object, so it can be recreated in an identical state elsewhere. This becomes essential in developing applications that require data persistence, distributed computing, and data sharing between different software components.

## Learning Objectives:

- Articulate the differences and similarities between marshaling and serialization.
- Implement serialization in a practical programming task.
- Understand how serialized data can be used in web applications, databases, and network communications.
- Evaluate the performance implications of different serialization formats, like JSON, XML, and binary formats.

## Resources:

- [Real Python Serialization](https://realpython.com/python-serialization/)
- [Real Python: Working With JSON Data in Python](https://realpython.com/python-json/)
- [Python’s pickle documentation](https://docs.python.org/3/library/pickle.html)
- [Corey Schafer on Pickle](https://www.youtube.com/watch?v=2twZMLsATqg)
- [CSV to JSON in Python](https://realpython.com/python-csv/)
- [Python XML ElementTree Guide](https://docs.python.org/3/library/xml.etree.elementtree.html)
- [Socket Programming Guide](https://realpython.com/python-sockets/)

This project will equip you with the skills needed to manipulate and manage data effectively, preparing you for more advanced topics in computer science and software development. Get ready to build a solid foundation in data handling that will support your future projects and career in the technology sector.

## Tasks

- [task_00_basic_serialization.py](./task_00_basic_serialization.py)
- [task_01_pickle.py](./task_01_pickle.py)
- [task_02_csv.py](./task_02_csv.py)
- [task_03_xml.py](./task_03_xml.py)

### 0. Basic Serialization

Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

**Instructions:**

Write a Python module named `task_00_basic_serialization.py` with the following functions:

```python
def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    pass

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    pass
```

The function `serialize_and_save_to_file` takes 2 parameters:
- `data`: A Python Dictionary with data
- `filename`: The filename of the output JSON file. If the output file already exists it should be replaced.

The function `load_and_deserialize` takes 1 parameter:
- `filename`: The filename of the input JSON file. This function returns a Python Dictionary with the deserialized JSON data from the file.

### 1. Pickling Custom Classes

Learn how to serialize and deserialize custom Python objects using the `pickle` module.

**Instructions:**

Create a custom Python class named `CustomObject`. This class should have the following attributes:
- `name` (a string)
- `age` (an integer)
- `is_student` (a boolean)

Additionally, the class should have a method `display` to print out the object’s attributes with the following format:

```
Name: John
Age: 25
Is Student: True
```

Implement two methods within this class:
- `serialize(self, filename)`: This method will take a filename as its parameter. Using the `pickle` module, it will serialize the current instance of the object and save it to the provided filename.
- `@classmethod deserialize(cls, filename)`: This class method will take a filename as its parameter. Using the `pickle` module, it will load and return an instance of the `CustomObject` from the provided filename.

Save your code in a file named `task_01_pickle.py`.

### 2. Converting CSV Data to JSON Format

The objective of this exercise is to gain experience in reading data from one format (CSV) and converting it into another format (JSON) using serialization techniques.

**Instructions:**

Begin by importing the required modules:
```python
import csv
import json
```

Define a function named `convert_csv_to_json` that takes the CSV filename as its parameter and writes the JSON data to `data.json`.

Inside this function:
- Use Python’s `csv` module to open the CSV file and read the data. Use the `DictReader` class to convert each row into a dictionary.
- Serialize the list of dictionaries using the `json` module.
- Write the serialized JSON data to `data.json`.

The function should return `True` if the conversion was successful. Handle exceptions, such as file not found. The function should return `False` in this case.

Save your work in `task_02_csv.py`.

### 3. Serializing and Deserializing with XML

In this exercise, we’ll explore serialization and deserialization using XML as an alternative format to JSON.

**Instructions:**

Begin by importing the required modules. You can use the `xml.etree.ElementTree` module which is a part of Python’s standard library for XML processing:
```python
import xml.etree.ElementTree as ET
```

Define two main functions:
- `serialize_to_xml(dictionary, filename)`: This will take a Python dictionary and a filename as parameters. It should serialize the dictionary into XML and save it to the given filename.
- `deserialize_from_xml(filename)`: This will take a filename as its parameter, read the XML data from that file, and return a deserialized Python dictionary.

For `serialize_to_xml`:
- Create a root element, e.g., `<data>`.
- Iterate through the dictionary items and add them as child elements to the root.
- Write the XML tree to the provided filename using the `ET.ElementTree` class.

For `deserialize_from_xml`:
- Parse the XML file using `ET.parse`.
- Navigate through the XML elements to reconstruct the dictionary.
- Return the constructed dictionary.

Be cautious about data types. XML doesn’t differentiate between numbers and strings, etc., like Python does. You might need to manage type conversions.

Save your work in `03-xml.py`.
