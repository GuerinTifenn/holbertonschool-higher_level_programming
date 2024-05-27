# Python - Input/Output

## Description

This project focuses on handling files and JSON serialization/deserialization in Python. It covers how to read and write files, work with JSON data, and use command line arguments in Python scripts.

## Learning Objectives

By the end of this project, you should be able to explain:

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to ensure a file is closed after using it
- What the `with` statement is and how to use it
- What JSON is
- What serialization is
- What deserialization is
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure
- How to access command line parameters in a Python script

## Resources

- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files](http://www.diveintopython3.net/files.html) (until "11.4 Binary Files" included)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/2e/chapter8/) (ch. 8 p 180-183 and ch. 14 p 326-333)
- [sys package](https://docs.python.org/3/library/sys.html)

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `pycodestyle` (version 2.7.*)
- All files must be executable
- The length of files will be tested using `wc`

### Python Test Cases

- Allowed editors: `vi`, `vim`, `emacs`
- All files should end with a new line
- All test files should be inside a folder `tests`
- All test files should be text files (extension: `.txt`)
- All tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)
- Collaboration on test cases is strongly encouraged to cover all edge cases

## Tasks

- [0-read_file.py](./0-read_file.py)
- [1-write_file.py](./1-write_file.py)
- [2-append_write.py](./2-append_write.py)
- [3-to_json_string.py](./3-to_json_string.py)
- [4-from_json_string.py](./4-from_json_string.py)
- [5-save_to_json_file.py](./5-save_to_json_file.py)
- [6-load_from_json_file.py](./6-load_from_json_file.py)
- [7-add_item.py](./7-add_item.py)
- [8-class_to_json.py](./8-class_to_json.py)
- [9-student.py](./9-student.py)
- [10-student.py](./10-student.py)
- [11-student.py](./11-student.py)
- [12-pascal_triangle.py](./12-pascal_triangle.py)

## 0. Read file

**Objectif :** Écrire une fonction qui lit un fichier texte (UTF8) et l'affiche sur stdout.

**Prototype :** `def read_file(filename=""):`

**Instructions :**
- Utilisez l'instruction `with`.
- Ne gérez pas les permissions de fichier ou les exceptions liées à l'absence de fichier.
- Vous ne pouvez pas importer de module.

## 1. Write to a file

**Objectif :** Écrire une fonction qui écrit une chaîne de caractères dans un fichier texte (UTF8) et retourne le nombre de caractères écrits.

**Prototype :** `def write_file(filename="", text=""):`

**Instructions :**
- Utilisez l'instruction `with`.
- La fonction doit créer le fichier s'il n'existe pas.
- La fonction doit écraser le contenu du fichier s'il existe déjà.
- Vous ne pouvez pas importer de module.

## 2. Append to a file

**Objectif :** Écrire une fonction qui ajoute une chaîne de caractères à la fin d'un fichier texte (UTF8) et retourne le nombre de caractères ajoutés.

**Prototype :** `def append_write(filename="", text=""):`

**Instructions :**
- Utilisez l'instruction `with`.
- Si le fichier n'existe pas, il doit être créé.
- Vous ne pouvez pas importer de module.

## 3. To JSON string

**Objectif :** Écrire une fonction qui retourne la représentation JSON d'un objet (chaîne de caractères).

**Prototype :** `def to_json_string(my_obj):`

**Instructions :**
- Ne gérez pas les exceptions si l'objet ne peut pas être sérialisé.

## 4. From JSON string to Object

**Objectif :** Écrire une fonction qui retourne un objet (structure de données Python) représenté par une chaîne JSON.

**Prototype :** `def from_json_string(my_str):`

**Instructions :**
- Ne gérez pas les exceptions si la chaîne JSON ne représente pas un objet.

## 5. Save Object to a file

**Objectif :** Écrire une fonction qui écrit un objet dans un fichier texte, en utilisant une représentation JSON.

**Prototype :** `def save_to_json_file(my_obj, filename):`

**Instructions :**
- Utilisez l'instruction `with`.
- Ne gérez pas les exceptions si l'objet ne peut pas être sérialisé.
- Ne gérez pas les exceptions liées aux permissions de fichier.

## 6. Create object from a JSON file

**Objectif :** Écrire une fonction qui crée un objet à partir d'un fichier JSON.

**Prototype :** `def load_from_json_file(filename):`

**Instructions :**
- Utilisez l'instruction `with`.
- Ne gérez pas les exceptions si la chaîne JSON ne représente pas un objet.
- Ne gérez pas les exceptions liées aux permissions de fichier.

## 7. Load, add, save

**Objectif :** Écrire un script qui ajoute tous les arguments à une liste Python, puis les enregistre dans un fichier.

**Instructions :**
- Utilisez la fonction `save_to_json_file` de `5-save_to_json_file.py`.
- Utilisez la fonction `load_from_json_file` de `6-load_from_json_file.py`.
- La liste doit être enregistrée sous forme de représentation JSON dans un fichier nommé `add_item.json`.
- Si le fichier n'existe pas, il doit être créé.
- Ne gérez pas les exceptions liées aux permissions de fichier.

## 8. Class to JSON

**Objectif :** Écrire une fonction qui retourne la description d'un dictionnaire avec une structure de données simple (liste, dictionnaire, chaîne, entier et booléen) pour la sérialisation JSON d'un objet.

**Prototype :** `def class_to_json(obj):`

**Instructions :**
- `obj` est une instance d'une classe.
- Tous les attributs de la classe `obj` doivent être sérialisables : liste, dictionnaire, chaîne, entier et booléen.
- Vous ne pouvez pas importer de module.

## 9. Student to JSON

**Objectif :** Écrire une classe `Student` qui définit un étudiant avec :

- Attributs d'instance publics :
  - `first_name`
  - `last_name`
  - `age`
- Instantiation avec `first_name`, `last_name` et `age` : `def __init__(self, first_name, last_name, age):`
- Méthode publique `def to_json(self):` qui récupère une représentation du dictionnaire d'une instance de `Student`.

## 10. Student to JSON with filter

**Objectif :** Écrire une classe `Student` qui définit un étudiant avec :

- Attributs d'instance publics :
  - `first_name`
  - `last_name`
  - `age`
- Instantiation avec `first_name`, `last_name` et `age` : `def __init__(self, first_name, last_name, age):`
- Méthode publique `def to_json(self, attrs=None):` qui récupère une représentation du dictionnaire d'une instance de `Student`. Si `attrs` est une liste de chaînes, seules les propriétés nommées contenues dans cette liste doivent être récupérées. Sinon, toutes les propriétés doivent être récupérées.

## 11. Student to disk and reload

**Objectif :** Écrire une classe `Student` qui définit un étudiant avec :

- Attributs d'instance publics :
  - `first_name`
  - `last_name`
  - `age`
- Instantiation avec `first_name`, `last_name` et `age` : `def __init__(self, first_name, last_name, age):`
- Méthode publique `def to_json(self, attrs=None):` qui récupère une représentation du dictionnaire d'une instance de `Student`.
- Méthode publique `def reload_from_json(self, json):` qui remplace tous les attributs de l'instance `Student` à partir d'un dictionnaire `json` :


## 12. Pascal's Triangle

**Objectif :** Créer une fonction `def pascal_triangle(n):` qui retourne une liste de listes d'entiers représentant le triangle de Pascal de `n` :

**Instructions :**
- Retournez une liste vide si `n <= 0`.
- Vous pouvez supposer que `n` est toujours un entier.
