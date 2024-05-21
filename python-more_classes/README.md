# Python - More Classes and Objects

## Resources
Read or watch:
- [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” (excluded))
- [Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/) (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
- [Class and Instance Attributes](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)
- [classmethods and staticmethods](https://realpython.com/instance-class-and-static-methods-demystified/)
- [Properties vs. Getters and Setters](https://www.python-course.eu/python3_properties.php) (Mainly the last part “Public instead of Private Attributes”)
- [str vs repr](https://realpython.com/python-str-vs-repr/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What is OOP
- “First-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected, and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- What are the special `__str__` and `__repr__` methods and how to use them
- What is the difference between `__str__` and `__repr__`
- What is a class attribute
- What is the difference between an object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to objects and classes
- What is and what does contain `__dict__` of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the `getattr` function

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks

# Python - More Classes and Objects

## Tasks

- [0-rectangle.py](./0-rectangle.py)
- [1-rectangle.py](./1-rectangle.py)
- [2-rectangle.py](./2-rectangle.py)
- [3-rectangle.py](./3-rectangle.py)
- [4-rectangle.py](./4-rectangle.py)
- [5-rectangle.py](./5-rectangle.py)
- [6-rectangle.py](./6-rectangle.py)
- [7-rectangle.py](./7-rectangle.py)
- [8-rectangle.py](./8-rectangle.py)
- [9-rectangle.py](./9-rectangle.py)

### 0. Simple Rectangle
Create an empty class `Rectangle` that defines a rectangle. This class does not contain any attributes or methods.

### 1. Real Definition of a Rectangle
Enhance the `Rectangle` class to include:
- Private instance attributes `width` and `height`
- Property getters and setters for `width` and `height` with appropriate type and value checks

### 2. Area and Perimeter
Add methods to the `Rectangle` class to calculate and return the area and perimeter of the rectangle.

### 3. String Representation
Override the `__str__` method to print the rectangle with the `#` character. If either width or height is zero, return an empty string.

### 4. Eval is Magic
Override the `__repr__` method to return a string that can recreate a new instance of the rectangle using `eval()`.

### 5. Detect Instance Deletion
Print the message `Bye rectangle...` when an instance of `Rectangle` is deleted.

### 6. How Many Instances
Add a public class attribute `number_of_instances` that tracks the number of `Rectangle` instances. Increment this attribute upon instantiation and decrement it upon deletion.

### 7. Change Representation
Add a public class attribute `print_symbol` that can be used for the string representation of the rectangle. This symbol can be changed and used instead of `#`.

### 8. Compare Rectangles
Add a static method `bigger_or_equal` that compares the area of two rectangles and returns the one with the larger area.

### 9. A Square is a Rectangle
Add a class method `square` that returns a new `Rectangle` instance where `width` and `height` are equal.
