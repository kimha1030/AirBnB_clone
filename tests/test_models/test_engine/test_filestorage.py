import unittest
import pep8
import json
from os import remove
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test for File Storage"""
    def test_init_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_init_docstring(self):
        """Check the docstring in the class"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_all(self):
        """Check method all"""
        FileStorage._FileStorage__objects = {}
        base1 = BaseModel()
        my_dict = FileStorage._FileStorage__objects
        self.assertEqual(type(my_dict), dict)

    def test_new(self):
        """Check method new"""
        st_file = FileStorage()
        FileStorage._FileStorage__objects = {}
        base2 = BaseModel()
        size1 = len(FileStorage._FileStorage__objects)
        base3 = BaseModel()
        size2 = len(FileStorage._FileStorage__objects)
        self.assertTrue(size2 > size1)
        self.assertTrue(len(FileStorage._FileStorage__objects), 2)

    def test_save(self):
        """ Check the method save"""
        st_file1 = FileStorage
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}
        base4 = BaseModel()
        base4.save()
        id_key = type(base4).__name__ + "." + base4.id
        with open("file.json", 'r', encoding="UTF-8") as data_file:
            read_file = data_file.read()
            self.assertEqual(type(read_file), str)
        with open("file.json", 'r', encoding="UTF-8") as data_file1:
            data = json.load(data_file1)
            for k, v in data.items():
                FileStorage._FileStorage__objects[k] =\
                 eval(v['__class__'])(**v)
                new_obj = FileStorage._FileStorage__objects[id_key]
                self.assertIsInstance(new_obj, BaseModel)
