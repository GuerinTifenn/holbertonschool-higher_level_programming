# Python - Inheritance

### Resources
Read or watch:
- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://realpython.com/inheritance-composition-python/)
- [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=pTB0EiLXUC8)

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- What is a superclass, base class, or parent class
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit a class from another
- How to define a class with multiple base classes
- What is the default class every class inherits from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when, and how to use `isinstance`, `issubclass`, `type`, and `super` built-in functions

### Requirements
#### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
#### Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- We strongly encourage you to work together on test cases so that you don’t miss any edge case

### Documentation
- Do not use the words import or from inside your comments; the checker will think you are trying to import some modules

### Tasks
- [0-lookup.py](./0-lookup.py)
- [1-my_list.py](./1-my_list.py)
- [2-is_same_class.py](./2-is_same_class.py)
- [3-is_kind_of_class.py](./3-is_kind_of_class.py)
- [4-inherits_from.py](./4-inherits_from.py)
- [5-base_geometry.py](./5-base_geometry.py)
- [6-base_geometry.py](./6-base_geometry.py)
- [7-base_geometry.py](./7-base_geometry.py)
- [8-rectangle.py](./8-rectangle.py)
- [9-rectangle.py](./9-rectangle.py)
- [10-square.py](./10-square.py)
- [11-square.py](./11-square.py)

### 0. Lookup

- Écrire une fonction `lookup(obj)` qui retourne la liste des attributs et méthodes disponibles pour un objet donné.
- Prototype : `def lookup(obj)`
- Retourne : un objet de type liste
- Vous n'êtes pas autorisé à importer de module.

### 1. My list

- Écrire une classe `MyList` qui hérite de `list` et implémente une méthode `print_sorted()` qui affiche la liste dans l'ordre croissant.

### 2. Exact same object

- Écrire une fonction `is_same_class(obj, a_class)` qui retourne `True` si `obj` est exactement une instance de `a_class`, sinon `False`.

### 3. Same class or inherit from

- Écrire une fonction `is_kind_of_class(obj, a_class)` qui retourne `True` si `obj` est une instance de `a_class` ou si `obj` est une instance d'une classe qui hérite de `a_class`, sinon `False`.

### 4. Only sub class of

- Écrire une fonction `inherits_from(obj, a_class)` qui retourne `True` si `obj` est une instance d'une classe qui a hérité (directement ou indirectement) de `a_class`, sinon `False`.

### 5. Geometry module

- Écrire une classe vide `BaseGeometry`.

### 6. Improve Geometry

- Améliorer la classe `BaseGeometry` en ajoutant une méthode d'instance publique `area()` qui lève une Exception avec le message "area() is not implemented".

### 7. Integer validator

- Ajouter une méthode d'instance publique `integer_validator(self, name, value)` à la classe `BaseGeometry` qui valide la valeur comme suit :
  - Si `value` n'est pas un entier, lever une exception `TypeError` avec le message "<name> must be an integer".
  - Si `value` est inférieur ou égal à 0, lever une exception `ValueError` avec le message "<name> must be greater than 0".

### 8. Rectangle

- Écrire une classe `Rectangle` qui hérite de `BaseGeometry` et implémente l'instanciation avec la largeur et la hauteur.

### 9. Full rectangle

- Étendre la classe `Rectangle` en implémentant la méthode `area()` et en personnalisant les méthodes `print()` et `str()` pour afficher la description du rectangle.

### 10. Square #1

- Écrire une classe `Square` qui hérite de `Rectangle` et implémente l'instanciation avec la taille.

### 11. Square #2

- Étendre la classe `Square` en personnalisant les méthodes `print()` et `str()` pour afficher la description du carré.
