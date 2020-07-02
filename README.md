# Repository for project 0x00. AirBnB clone - The console
This project is our version of the console of the Airbnb clone, developed for educational purposes, following the guidelines of the Holberton School.

---
## Description
Airbnb clone - The console is a command line interpreter that allows us to manipulate data without a visual interface. In our case, being able to manage the objects of our project, as:
* Create a new object (ex: a new User or a new Place).
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…).
* Update attributes of an object.
* Destroy an object.

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

### 1. Be PEP8 compliant!
* Write beautiful code that passes the PEP8 checks.

### [2. Unittests](./tests/test_models)
* All the files, classes, functions was tested with unit tests.
* The tests was executed using the following commands:
**To check all tests:**
```
python3 -m unittest discover tests
```
**To check file by file. In this case: test_base_model.py:**
```
python3 -m unittest tests/test_models/test_base_model.py
```
**The expected output for any of these tests is:**
```
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

### [8. First User](./models/user.py)
* Write a class User that inherits from BaseModel. (File: user.py)

### [9. More classes!](./models)
* Write all those classes that inherit from BaseModel: state, city, amenity, place and review. (Filea: state.py, city.py, amenity.py, place.py and review.py)

### [10. Console 1.0](./console.py)
* Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review
* Update the command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously. (Files: filestorage.py and console.py)

### [11. All instances by class name](./console.py)
* Update the command interpreter (console.py) to retrieve all instances of a class by using: class name.all(). (File: console.py)

### [12. Count instances](./console.py)
* Update the command interpreter (console.py) to retrieve the number of instances of a class: class name.count(). (File: console.py)

### [13. Show](./console.py)
* Update the command interpreter (console.py) to retrieve an instance based on its ID: class name.show(id).
* Errors management must be the same as previously. (File: console.py)

### [14. Destroy](./console.py)
* Update the command interpreter (console.py) to destroy an instance based on his ID: class name.destroy(id).
* Errors management must be the same as previously. (File: console.py)

### [15. Update](./console.py)
* Update the command interpreter (console.py) to update an instance based on his ID: class name.update(id, attribute name, attribute value).
* Errors management must be the same as previously. (File: console.py)

---
## Examples
This is how our command interpreter works:
```
holberton@holberton-med:~/Documents/AirBnB_clone$ ./console.py 
(hbnb) create User
ddc8e538-997c-4d09-87ac-5b151a4584b4
(hbnb) create Place
3aa8d48e-d00c-4537-9c71-68d7a6f392aa
(hbnb) create City
6d663295-6ee2-4124-9e9a-af0771ae832a
(hbnb) create User
bef93cef-a7e2-4d02-a9ed-00af4ce9f9f2
(hbnb) all
["[User] (ddc8e538-997c-4d09-87ac-5b151a4584b4) {'id': 'ddc8e538-997c-4d09-87ac-5b151a4584b4', 'created_at': datetime.datetime(2020, 7, 2, 10, 32, 27, 463749), 'updated_at': datetime.datetime(2020, 7, 2, 10, 32, 27, 463801)}", "[Place] (3aa8d48e-d00c-4537-9c71-68d7a6f392aa) {'id': '3aa8d48e-d00c-4537-9c71-68d7a6f392aa', 'created_at': datetime.datetime(2020, 7, 2, 10, 32, 32, 874163), 'updated_at': datetime.datetime(2020, 7, 2, 10, 32, 32, 874199)}", "[City] (6d663295-6ee2-4124-9e9a-af0771ae832a) {'id': '6d663295-6ee2-4124-9e9a-af0771ae832a', 'created_at': datetime.datetime(2020, 7, 2, 10, 32, 39, 273573), 'updated_at': datetime.datetime(2020, 7, 2, 10, 32, 39, 273611)}", "[User] (bef93cef-a7e2-4d02-a9ed-00af4ce9f9f2) {'id': 'bef93cef-a7e2-4d02-a9ed-00af4ce9f9f2', 'created_at': datetime.datetime(2020, 7, 2, 10, 34, 1, 990836), 'updated_at': datetime.datetime(2020, 7, 2, 10, 34, 1, 990887)}"]
(hbnb) show User ddc8e538-997c-4d09-87ac-5b151a4584b4
[User] (ddc8e538-997c-4d09-87ac-5b151a4584b4) {'id': 'ddc8e538-997c-4d09-87ac-5b151a4584b4', 'created_at': datetime.datetime(2020, 7, 2, 10, 32, 27, 463749), 'updated_at': datetime.datetime(2020, 7, 2, 10, 32, 27, 463801)}
(hbnb) update User ddc8e538-997c-4d09-87ac-5b151a4584b4 email "user1@email.com"
[User] (ddc8e538-997c-4d09-87ac-5b151a4584b4) {'id': 'ddc8e538-997c-4d09-87ac-5b151a4584b4', 'created_at': datetime.datetime(2020, 7, 2, 10, 32, 27, 463749), 'updated_at': datetime.datetime(2020, 7, 2, 10, 32, 27, 463801), 'email': 'user1@email.com'}
(hbnb) User.update("bef93cef-a7e2-4d02-a9ed-00af4ce9f9f2", "first-name", "Frank")
[User] (bef93cef-a7e2-4d02-a9ed-00af4ce9f9f2) {'id': 'bef93cef-a7e2-4d02-a9ed-00af4ce9f9f2', 'created_at': datetime.datetime(2020, 7, 2, 10, 34, 1, 990836), 'updated_at': datetime.datetime(2020, 7, 2, 10, 34, 1, 990887), 'first-name': 'Frank'}
(hbnb) User.all()
["[User] (ddc8e538-997c-4d09-87ac-5b151a4584b4) {'id': 'ddc8e538-997c-4d09-87ac-5b151a4584b4', 'created_at': datetime.datetime(2020, 7, 2, 10, 32, 27, 463749), 'updated_at': datetime.datetime(2020, 7, 2, 10, 32, 27, 463801), 'email': 'user1@email.com'}", "[User] (bef93cef-a7e2-4d02-a9ed-00af4ce9f9f2) {'id': 'bef93cef-a7e2-4d02-a9ed-00af4ce9f9f2', 'created_at': datetime.datetime(2020, 7, 2, 10, 34, 1, 990836), 'updated_at': datetime.datetime(2020, 7, 2, 10, 34, 1, 990887), 'first-name': 'Frank'}"]
(hbnb) User.count()
2
(hbnb) destroy User ddc8e538-997c-4d09-87ac-5b151a4584b4
(hbnb) User.count()
1
(hbnb) Place.update("3aa8d48e-d00c-4537-9c71-68d7a6f392aa", "number_rooms", 12)
[Place] (3aa8d48e-d00c-4537-9c71-68d7a6f392aa) {'id': '3aa8d48e-d00c-4537-9c71-68d7a6f392aa', 'created_at': datetime.datetime(2020, 7, 2, 10, 32, 32, 874163), 'updated_at': datetime.datetime(2020, 7, 2, 10, 32, 32, 874199), 'number_rooms': '12'}
(hbnb) City.destroy("6d663295-6ee2-4124-9e9a-af0771ae832a")
(hbnb) all
["[Place] (3aa8d48e-d00c-4537-9c71-68d7a6f392aa) {'id': '3aa8d48e-d00c-4537-9c71-68d7a6f392aa', 'created_at': datetime.datetime(2020, 7, 2, 10, 32, 32, 874163), 'updated_at': datetime.datetime(2020, 7, 2, 10, 32, 32, 874199), 'number_rooms': '12'}", "[User] (bef93cef-a7e2-4d02-a9ed-00af4ce9f9f2) {'id': 'bef93cef-a7e2-4d02-a9ed-00af4ce9f9f2', 'created_at': datetime.datetime(2020, 7, 2, 10, 34, 1, 990836), 'updated_at': datetime.datetime(2020, 7, 2, 10, 34, 1, 990887), 'first-name': 'Frank'}"]
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help quit
Quit command to exit the program
(hbnb) help create
Create an instance of BaseModel

        Args:
            args (str): Class Name
        
(hbnb)
(hbnb)
(hbnb) quit
```
---
## Installation
To use this project, you must follow these steps:
* Clone this repository.
* Subsequently, run the executable file, writing in the command line: ./console.py
* After the above, you can see the command interpreter, in which you can use the actions: show, create, destroy, update and all with all classes.

---
## Authors
* **Nasser Abuchaibe** - [NasserAbuchaibe](https://github.com/NasserAbuchaibe)
* **Kimberly Hinostroza Acevedo** - [kimha1030](https://github.com/kimha1030)