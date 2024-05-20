# Python - Test-driven Development

## Project Overview
This project focuses on Test-Driven Development (TDD) in Python. The tasks require writing documentation and tests before implementing the actual code. The goal is to ensure code reliability and handle all possible edge cases.

## Background Context
- Always write documentation and tests first, before writing the implementation.
- Intranet checks will be available after the first deadline.
- Collaboration on test cases is encouraged to cover all edge cases.

## Resources
- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [doctest – Testing through documentation](https://docs.python.org/3/library/doctest.html)
- [Unit Tests in Python](https://realpython.com/python-testing/)

## Learning Objectives
- Understand the importance of tests.
- Write Docstrings to create tests.
- Document modules and functions.
- Use basic option flags for tests.
- Identify edge cases.

## Requirements

### Python Scripts
- Editors: `vi`, `vim`, `emacs`
- Python 3.8.5 on Ubuntu 20.04 LTS
- Files end with a new line
- First line: `#!/usr/bin/python3`
- Code style: `pycodestyle` (version 2.7.*)
- Files must be executable
- Length of files tested using `wc`

### Python Test Cases
- Editors: `vi`, `vim`, `emacs`
- Files end with a new line
- Test files inside `tests` folder
- Test files are text files (`.txt`)
- Run tests using: `python3 -m doctest ./tests/*`
- Document modules and functions
- Tests should cover all possible cases

## Tasks

  - [0-add_integer.py](./0-add_integer.py)
  - [tests/0-add_integer.txt](./tests/0-add_integer.txt)
  - [2-matrix_divided.py](./2-matrix_divided.py)
  - [tests/2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  - [3-say_my_name.py](./3-say_my_name.py)
  - [tests/3-say_my_name.txt](./tests/3-say_my_name.txt)
  - [4-print_square.py](./4-print_square.py)
  - [tests/4-print_square.txt](./tests/4-print_square.txt)
  - [5-text_indentation.py](./5-text_indentation.py)
  - [tests/5-text_indentation.txt](./tests/5-text_indentation.txt)
  - [tests/6-max_integer_test.py](./tests/6-max_integer_test.py)

### 0. Integers addition
Write a function that adds 2 integers.
- **Prototype**: `def add_integer(a, b=98):`
- **TypeError** if `a` or `b` are not integers or floats.
- Cast floats to integers.
- Returns an integer.

### 1. Divide a matrix
Write a function that divides all elements of a matrix.
- **Prototype**: `def matrix_divided(matrix, div):`
- **TypeError** if `matrix` elements are not lists of integers/floats.
- **TypeError** if rows are not the same size.
- **TypeError** if `div` is not a number.
- **ZeroDivisionError** if `div` is 0.
- Elements divided by `div`, rounded to 2 decimal places.
- Returns a new matrix.

### 2. Say my name
Write a function that prints `My name is <first name> <last name>`.
- **Prototype**: `def say_my_name(first_name, last_name=""):`
- **TypeError** if `first_name` or `last_name` are not strings.

### 3. Print square
Write a function that prints a square with the character `#`.
- **Prototype**: `def print_square(size):`
- **TypeError** if `size` is not an integer.
- **ValueError** if `size` is less than 0.
- **TypeError** if `size` is a float and less than 0.

### 4. Text indentation
Write a function that prints a text with 2 new lines after `.` `?` and `:`.
- **Prototype**: `def text_indentation(text):`
- **TypeError** if `text` is not a string.
- No space at the beginning or end of each printed line.

### 5. Max integer - Unittest
Write unittests for the function `def max_integer(list=[]):`.
- Test files inside `tests` folder
- Use `unittest` module
- Test files are Python files (`.py`)
- Run tests using: `python3 -m unittest tests.6-max_integer_test`
