# Python - Object-relational Mapping (ORM)

## Background Context
In this project, you will link two amazing worlds: Databases and Python! Initially, you will use the module MySQLdb to connect to a MySQL database and execute SQL queries. Later, you will transition to using SQLAlchemy, an Object Relational Mapper (ORM), which abstracts database interactions into Python objects, eliminating the need to write SQL queries directly.

## Resources
- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/14/tutorial/index.html)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)

## Learning Objectives
- Connect to a MySQL database from a Python script
- SELECT rows in a MySQL table from a Python script
- INSERT rows in a MySQL table from a Python script
- Understand what ORM means
- Map a Python class to a MySQL table

## Requirements
- All code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- Files executed with MySQLdb version 2.0.x and SQLAlchemy version 1.4.x
- Code style: `pycodestyle` (version 2.7.*)
- All modules, classes, and functions must have documentation

## Setup Instructions
1. **Install MySQL 8.0 on Ubuntu 20.04 LTS**
    ```bash
    sudo apt update
    sudo apt install mysql-server
    mysql --version
    ```
2. **Connect to MySQL server**
    ```bash
    sudo mysql
    quit
    ```
3. **Install MySQLdb module version 2.0.x**
    ```bash
    sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
    sudo pip3 install mysqlclient
    python3 -c 'import MySQLdb; print(MySQLdb.version_info)'
    ```
4. **Install SQLAlchemy module version 1.4.x**
    ```bash
    sudo pip3 install SQLAlchemy
    python3 -c 'import sqlalchemy; print(sqlalchemy.__version__)'
    ```

## Tasks

### 0. Get all states
Write a script that lists all states from the database `hbtn_0e_0_usa`.
- Arguments: `mysql username`, `mysql password`, `database name`
- Use the module `MySQLdb`
- Results sorted in ascending order by `states.id`
- [0-select_states.py](./0-select_states.py)

### 1. Filter states
Write a script that lists all states with a name starting with `N` from the database `hbtn_0e_0_usa`.
- Arguments: `mysql username`, `mysql password`, `database name`
- Use the module `MySQLdb`
- Results sorted in ascending order by `states.id`
- [1-filter_states.py](./1-filter_states.py)

### 2. Filter states by user input
Write a script that takes in an argument and displays all values in the `states` table where `name` matches the argument.
- Arguments: `mysql username`, `mysql password`, `database name`, `state name searched`
- Use the module `MySQLdb`
- Use `format` to create the SQL query with user input
- [2-my_filter_states.py](./2-my_filter_states.py)

### 3. SQL Injection...
Write a script that is safe from MySQL injections.
- Arguments: `mysql username`, `mysql password`, `database name`, `state name searched`
- Use the module `MySQLdb`
- [3-my_safe_filter_states.py](./3-my_safe_filter_states.py)

### 4. Cities by states
Write a script that lists all cities from the database `hbtn_0e_4_usa`.
- Arguments: `mysql username`, `mysql password`, `database name`
- Use the module `MySQLdb`
- Results sorted in ascending order by `cities.id`
- [4-cities_by_state.py](./4-cities_by_state.py)

### 5. All cities by state
Write a script that takes in the name of a state as an argument and lists all cities of that state.
- Arguments: `mysql username`, `mysql password`, `database name`, `state name`
- Use the module `MySQLdb`
- [5-filter_cities.py](./5-filter_cities.py)

### 6. First state model
Write a Python file that contains the class definition of a `State` and an instance `Base = declarative_base()`.
- Class `State` links to the MySQL table `states`
- Use the module `SQLAlchemy`
- [6-model_state.py](./6-model_state.py)

### 7. All states via SQLAlchemy
Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`.
- Arguments: `mysql username`, `mysql password`, `database name`
- Use the module `SQLAlchemy`
- Results sorted in ascending order by `states.id`
- [7-model_state_fetch_all.py](./7-model_state_fetch_all.py)

### 8. First state
Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`.
- Arguments: `mysql username`, `mysql password`, `database name`
- Use the module `SQLAlchemy`
- [8-model_state_fetch_first.py](./8-model_state_fetch_first.py)

### 9. Contains `a`
Write a script that lists all `State` objects that contain the letter `a`.
- Arguments: `mysql username`, `mysql password`, `database name`
- Use the module `SQLAlchemy`
- [9-model_state_filter_a.py](./9-model_state_filter_a.py)

### 10. Get a state
Write a script that prints the `State` object with the name passed as an argument.
- Arguments: `mysql username`, `mysql password`, `database name`, `state name to search`
- Use the module `SQLAlchemy`
- [10-model_state_my_get.py](./10-model_state_my_get.py)

### 11. Add a new state
Write a script that adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`.
- Arguments: `mysql username`, `mysql password`, `database name`
- Use the module `SQLAlchemy`
- Print the new `states.id` after creation
- [11-model_state_insert.py](./11-model_state_insert.py)

### 12. Update a state
Write a script that changes the name of a `State` object where `id = 2` to `New Mexico`.
- Arguments: `mysql username`, `mysql password`, `database name`
- Use the module `SQLAlchemy`
- [12-model_state_update_id_2.py](./12-model_state_update_id_2.py)

### 13. Delete states
Write a script that deletes all `State` objects with a name containing the letter `a`.
- Arguments: `mysql username`, `mysql password`, `database name`
- Use the module `SQLAlchemy`
- [13-model_state_delete_a.py](./13-model_state_delete_a.py)

### 14. Cities in state
Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.
- `City` class links to the MySQL table `cities`
- Write a script that prints all `City` objects from the database `hbtn_0e_14_usa`.
- Arguments: `mysql username`, `mysql password`, `database name`
- Use the module `SQLAlchemy`
- Results sorted in ascending order by `cities.id`
- [model_city.py](./model_city.py)
- [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py)
