#!/usr/bin/python3
"""Unittest for BaseModel
"""
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for Base Model"""
    def test_base_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_unit_base_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        path = './tests/test_models/test_base_model.py'
        result = pep8style.check_files([path])
        self.assertEqual(result.total_errors, 0)

    def test_file_storage_docstring(self):
        """ Check the docstring in class """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_type(self):
        """Test type"""
        base1 = BaseModel()
        self.assertTrue(type(base1.id) == str)
        self.assertTrue(type(base1.updated_at) == datetime)
        self.assertTrue(type(base1.created_at) == datetime)

    def test_type_kwargs(self):
        """Test type"""
        my_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                   'created_at': '2017-09-28T21:03:54.052298',
                   '__class__': 'BaseModel', 'my_number': 89,
                   'updated_at': '2017-09-28T21:03:54.052302',
                   'name': 'Holberton'}
        base2 = BaseModel(my_dict)
        self.assertTrue(type(base2.id) == str)
        self.assertTrue(type(base2.updated_at) == datetime)
        self.assertTrue(type(base2.created_at) == datetime)

    def test_instaces(self):
        """Check if is a instance"""
        base2 = BaseModel()
        base3 = BaseModel()
        self.assertTrue(isinstance(base2, BaseModel))
        self.assertTrue(isinstance(base3, BaseModel))

    def test_type_instaces(self):
        """Check if is a instance"""
        base2 = BaseModel()
        base3 = BaseModel()
        self.assertTrue((type(base2), BaseModel))
        self.assertTrue((type(base3), BaseModel))

    def test_name(self):
        """Check name in BaseModel"""
        base4 = BaseModel()
        base4.name = "Holberton"
        self.assertEqual(type(base4.name), str)
        self.assertEqual(base4.name, "Holberton")

    def test_id(self):
        """Check id in BaseModel"""
        base4 = BaseModel()
        self.assertEqual(type(base4.id), str)

    def test_update(self):
        """Check if update is equal"""
        base5 = BaseModel()
        date_now = base5.updated_at
        base5.updated_at
        self.assertTrue(date_now, base5.updated_at)

    def test_to_dict(self):
        """Check into dictionary"""
        base6 = BaseModel()
        my_dict = base6.to_dict()
        self.assertEqual(type(my_dict), dict)
        self.assertEqual(my_dict['__class__'], 'BaseModel')
        self.assertEqual(type(my_dict['created_at']), str)
        self.assertEqual(type(my_dict['updated_at']), str)
        self.assertEqual(type(my_dict['id']), str)

    def test_check_instance_exist(self):
        """ Check if methods exist """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

if __name__ == '__main__':
    unittest.main()
