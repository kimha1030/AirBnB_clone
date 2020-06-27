#!/usr/bin/python3
"""File_Storage Class
"""
import json
import os


class FileStorage():
    """ [Class FileStorage]
    """
    path_name = os.getcwd()
    __file_path = path_name+"/file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in objs with specific key"""
        my_dict = obj.to_dict()
        id_key = my_dict["__class__"]+"."+str(my_dict['id'])
        self.__objects[id_key] = obj

    def save(self):
        """Serailizes __objects to json file"""
        with open(self.__file_path, "w", encoding="UTF-8") as data_file:
            data_file.write(json.dumps(self.__objects))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as data_file:
                __objects = json.loads(data_file.read())
        except:
            pass
