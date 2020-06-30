# Repository for project 0x00. AirBnB clone - The console
This project is our version of the console of the Airbnb clone, developed for educational purposes, following the guidelines of the Holberton School.

---
## Description
Airbnb clone - The console is a command line interpreter that allows us to manipulate data without a visual interface. In our case, being able to manage the objects of our project, as:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

---
## Learning Objectives
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---
## Tasks

### [1. Be PEP8 compliant!]
* Write beautiful code that passes the PEP8 checks.

### [2. Unittests](./tests/test_models)
* All the files, classes, functions was tested with unit tests.
* The tests was executed using the following commands:
```
python3 -m unittest discover tests
python3 -m unittest tests/test_models/test_base_model.py

Output:
OK
```
(Directory: test_models)

### [3. BaseModel](./models/base_model.py)
* Write a class BaseModel that defines all common attributes/methods for other classes. (File: base_model.py)

### [4. Create BaseModel from dictionary](./models/base_model.py)
* Re-create an instance with the dictionary representation. (File: base_model.py)

### [5. Store first object](./models/engine/file_storage.py)
* Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances. (File: filestorage.py)

### [6. Console 0.01](./console.py)
* Write a program called console.py that contains the entry point of the command interpreter. (File: console.py)

### [7. Console 0.1](./console.py)
* Update the command interpreter (console.py) to have the commands: create, show, all, update and destroy. (File: console.py)

```
holberton@holberton-med:~/AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) help quit
Quit command to exit the program
(hbnb) quit
```

### [8. First User](./models/user.py)
* Write a class User that inherits from BaseModel. (File: user.py)

### [9. More classes!](./models)
* Write all those classes that inherit from BaseModel: state, city, amenity, place and review. (Filea: state.py, city.py, amenity.py, place.py and review.py)

### [10. Console 1.0](./console.py)
* Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review
* Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously. (Files: filestorage.py and console.py)

---
## Installation
To use this project, you must follow these steps:
* Clone this repository.
* Subsequently, run the executable file, writing in the command line: ./console.py
* After the above, you can see the command interpreter, in which you can enter commands and observe the obtained output.

---
## Authors
* **Nasser Abuchaibe** - [NasserAbuchaibe](https://github.com/NasserAbuchaibe)
* **Kimberly Hinostroza Acevedo** - [kimha1030](https://github.com/kimha1030)