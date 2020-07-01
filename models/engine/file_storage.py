#!/usr/bin/python3
"""File_Storage Class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.city import City


class FileStorage():
    """ [Class FileStorage]
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in objs with specific key"""
        id_key = type(obj).__name__ + "." + obj.id
        self.__objects[id_key] = obj

    def save(self):
        """Serailizes __objects to json file"""
        my_dict = {}
        for k in self.__objects:
            my_dict[k] = self.__objects[k].to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as data_file:
            json.dump(my_dict, data_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as data_file:
                data = json.load(data_file)
                for k, v in data.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
        except:
            pass
