# Python - Hello, World

## Concepts
For this project, we expect you to look at this concept:

- Python programming

## Author’s disclaimer
Welcome to the Python world!

You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.

Python has a linter / style guide, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

- Guillaume

## Resources
Read or watch:

- Use this playlist as long as you are learning Python:
  - Learn to Program
  - Whetting Your Appetite
  - Using the Python Interpreter
  - An Informal Introduction to Python (Read up until “3.1.2. Strings” included)
  - How To Use String Formatters in Python 3
  - Pycodestyle – Style Guide for Python Code

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- **General:**
  - How to use the Python interpreter
  - How to print text and variables using print
  - How to use strings
  - What are indexing and slicing in Python
  - What is the official Python coding style and how to check your code with pycodestyle

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### More Info
- Pycodestyle
  - Pycodestyle is now the new standard of Python style code

## Tasks

- [2-print.py](./2-print.py)
- [3-print_number.py](./3-print_number.py)
- [4-print_float.py](./4-print_float.py)
- [5-print_string.py](./5-print_string.py)
- [6-concat.py](./6-concat.py)
- [7-edges.py](./7-edges.py)
- [8-concat_edges.py](./8-concat_edges.py)
- [9-easter_egg.py](./9-easter_egg.py)

### 0. Hello, print
- Write a Python script that prints exactly "Programming is like building a multilingual puzzle", followed by a new line.
- Use the function print
- Example:


### 1. Print integer
- Complete this source code in order to print the integer stored in the variable `number`, followed by "Battery street", followed by a new line.
- The output of the script should be:
the number, followed by Battery street,
- You are not allowed to cast the variable `number` into a string
- Your code must be 3 lines long
- You have to use f-strings
- Example: 98 Battery street
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py).

### 2. Print float
- Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.
- The output of the program should be:
Float:, followed by the float with only 2 digits
- You are not allowed to cast `number` to string
- You have to use f-strings
- Example:
Float: 3.14
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py).

### 3. Print string
- Complete this source code in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.
- The output of the program should be:
3 times the value of str
followed by the 9 first characters of str
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long
- Example:
Holberton SchoolHolberton SchoolHolberton School
Holberton
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py).

### 4. Play with strings
- Complete this source code to print "Welcome to Holberton School!"
- You are not allowed to use any loops or conditional statements.
- You have to use the variables `str1` and `str2` in your new line of code
- Your program should be exactly 5 lines long
- Example:
Welcome to Holberton School!
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py).

### 5. Copy - Cut - Paste
- Complete this source code
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- `word_first_3` should contain the first 3 letters of the variable `word`
- `word_last_2` should contain the last 2 letters of the variable `word`
- `middle_word` should contain the value of the variable `word` without the first and last letters
- Example:
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py).

### 6. Create a new sentence
- Complete this source code to print "object-oriented programming with Python", followed by a new line.
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals
- Example:
object-oriented programming with Python
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py).

### 7. Easter Egg
- Write a Python script that prints “The Zen of Python”, by Tim Peters, followed by a new line.
- Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)
- Example:
The Zen of Python, by Tim Peters
