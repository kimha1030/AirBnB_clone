#!/usr/bin/python3
"""Unittest for File Storage
"""
import unittest
import pep8
import json
from os import remove
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.__init__ import storage


class TestFileStorage(unittest.TestCase):
    """Test for File Storage"""
    def test_file_storage_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        path = './models/engine/file_storage.py'
        result = pep8style.check_files([path])
        self.assertEqual(result.total_errors, 0)

    def test_unit_file_storage_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        path1 = './tests/test_models/test_engine/test_file_storage.py'
        result = pep8style.check_files([path1])
        self.assertEqual(result.total_errors, 0)

    def test_file_storage_docstring(self):
        """ Check the docstring """
        self.assertIsNotNone(storage.__doc__)
        self.assertIsNotNone(storage.__init__.__doc__)
        self.assertIsNotNone(storage.all.__doc__)
        self.assertIsNotNone(storage.new.__doc__)
        self.assertIsNotNone(storage.save.__doc__)
        self.assertIsNotNone(storage.reload.__doc__)

    def test_all(self):
        """Check method all"""
        FileStorage._FileStorage__objects = {}
        base1 = BaseModel()
        id_key = type(base1).__name__ + "." + base1.id
        store = FileStorage()
        new_dict = store.all()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue(new_dict[id_key] is base1)

    def test_new(self):
        """Check method new"""
        st_file = FileStorage()
        FileStorage._FileStorage__objects = {}
        base2 = BaseModel()
        size1 = len(FileStorage._FileStorage__objects)
        base3 = BaseModel()
        size2 = len(FileStorage._FileStorage__objects)
        self.assertTrue(size2 > size1)
        self.assertEqual(len(FileStorage._FileStorage__objects), 2)

    def test_save(self):
        """ Check the method save"""
        st_file1 = FileStorage()
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
            self.assertIsInstance(data, dict)

    def test_reload(self):
        """ Check the method save"""
        st_file1 = FileStorage()
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}
        base4 = BaseModel()
        id_key = type(base4).__name__ + "." + base4.id
        base4.save()
        st_file1.reload()
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)
        self.assertEqual(type(FileStorage._FileStorage__objects[id_key]),
                         BaseModel)

    def test_check_instance_exist(self):
        """ Check if methods exist """
        self.assertTrue(hasattr(storage, "__init__"))
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(hasattr(storage, "reload"))
