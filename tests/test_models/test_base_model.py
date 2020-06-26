import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for Base Model"""
    def test_base_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

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
