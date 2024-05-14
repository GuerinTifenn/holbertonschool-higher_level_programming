# Python - More Data Structures: Set, Dictionary

## Resources

### Read or Watch:
- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Lambda, filter, reduce and map](https://www.python-course.eu/python3_lambda.php)
- [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)

### Man or Help:
- `python3`

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without assistance:

### General
- Why Python programming is awesome
- What are sets and how to use them
- What are the most common methods of set and how to use them
- When to use sets versus lists
- How to iterate into a set
- What are dictionaries and how to use them
- When to use dictionaries versus lists or sets
- What is a key in a dictionary
- How to iterate over a dictionary
- What is a lambda function
- What are the `map`, `reduce`, and `filter` functions

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder of the project is mandatory
- Your code should use the `pycodestyle` (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks

- [0-square_matrix_simple.py](./0-square_matrix_simple.py)
- [1-search_replace.py](./1-search_replace.py)
- [2-uniq_add.py](./2-uniq_add.py)
- [3-common_elements.py](./3-common_elements.py)
- [4-only_diff_elements.py](./4-only_diff_elements.py)
- [5-number_keys.py](./5-number_keys.py)
- [6-print_sorted_dictionary.py](./6-print_sorted_dictionary.py)
- [7-update_dictionary.py](./7-update_dictionary.py)
- [8-simple_delete.py](./8-simple_delete.py)
- [9-multiply_by_2.py](./9-multiply_by_2.py)
- [10-best_score.py](./10-best_score.py)
- [11-multiply_list_map.py](./11-multiply_list_map.py)
- [12-roman_to_int.py](./12-roman_to_int.py)

### 0. Squared simple
**Mandatory**

Write a function that computes the square value of all integers of a matrix.

- Prototype: `def square_matrix_simple(matrix=[]):`
- matrix is a 2-dimensional array
- Returns a new matrix:
  - Same size as matrix
  - Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You are allowed to use regular loops, map, etc.


### 1. Search and Replace
**Mandatory**

Write a function that replaces all occurrences of an element by another in a new list.

- **Prototype:** `def search_replace(my_list, search, replace):`
- **Parameters:**
  - `my_list`: The initial list
  - `search`: The element to replace in the list
  - `replace`: The new element
- You are not allowed to import any module

### 2. Unique addition

**mandatory**

Write a function that adds all unique integers in a list (only once for each integer).

- **Prototype:** `def uniq_add(my_list=[]):`
- **Requirements:**
  - You are not allowed to import any module

### 3. Present in both

**mandatory**

Write a function that returns a set of common elements in two sets.

- **Prototype:** `def common_elements(set_1, set_2):`
- **Requirements:**
  - You are not allowed to import any module

### 4. Only differents

**mandatory**

Write a function that returns a set of all elements present in only one set.

- **Prototype:** `def only_diff_elements(set_1, set_2):`
- **Requirements:**
  - You are not allowed to import any module

### 5. Number of keys

**mandatory**

Write a function that returns the number of keys in a dictionary.

- **Prototype:** `def number_keys(a_dictionary):`
- **Requirements:**
  - You are not allowed to import any module

### 6. Print sorted dictionary

**mandatory**

Write a function that prints a dictionary by ordered keys.

- **Prototype:** `def print_sorted_dictionary(a_dictionary):`
- **Requirements:**
  - You can assume that all keys are strings
  - Keys should be sorted by alphabetic order
  - Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
  - Dictionary values can have any type
  - You are not allowed to import any module

### 7. Update dictionary

**mandatory**

Write a function that replaces or adds key/value pairs in a dictionary.

- **Prototype:** `def update_dictionary(a_dictionary, key, value):`
- **Requirements:**
  - The `key` argument will always be a string
  - The `value` argument can be of any type
  - If a key exists in the dictionary, its corresponding value will be replaced with the new value
  - If a key doesn’t exist in the dictionary, it will be created with the provided value
  - You are not allowed to import any module

### 8. Simple delete by key

**mandatory**

Write a function that deletes a key in a dictionary.

- **Prototype:** `def simple_delete(a_dictionary, key=""):`
- **Requirements:**
  - The `key` argument will always be a string
  - If the key doesn’t exist in the dictionary, the dictionary won’t change
  - You are not allowed to import any module

### 9. Multiply by 2

**mandatory**

Write a function that returns a new dictionary with all values multiplied by 2.

- **Prototype:** `def multiply_by_2(a_dictionary):`
- **Requirements:**
  - You can assume that all values are only integers
  - Returns a new dictionary
  - You are not allowed to import any module

### 10. Best score

**mandatory**

Write a function that returns a key with the biggest integer value.

- **Prototype:** `def best_score(a_dictionary):`
- **Requirements:**
  - You can assume that all values are only integers
  - If no score found, return None
  - You can assume all students have a different score
  - You are not allowed to import any module

### 11. Multiply by using map

**mandatory**

Write a function that returns a list with all values multiplied by a number without using any loops.

- **Prototype:** `def multiply_list_map(my_list=[], number=0):`
- **Returns:**
  - A new list with the same length as `my_list`
  - Each value should be multiplied by `number`
  - Initial list should not be modified
- **Requirements:**
  - You are not allowed to import any module
  - You have to use map
  - Your file should be max 3 lines

### 12. Roman to Integer

**mandatory**

Technical interview preparation:

Create a function `def roman_to_int(roman_string):` that converts a Roman numeral to an integer.

- You are not allowed to google anything
- Whiteboard first
- You can assume the number will be between 1 to 3999.
- `def roman_to_int(roman_string)` must return an integer
- If the `roman_string` is not a string or None, return 0

