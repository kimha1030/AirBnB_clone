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
