#!/usr/bin/python
"""unittest User class
"""
import unittest
from models.city import City
import pep8


class TestCity(unittest.TestCase):
    """Test User class"""

    def test_init_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_init_docstring(self):
        """Check the docstring in the class"""
        self.assertTrue(len(City.__doc__) >= 1)

    def test_city(self):
        city1 = City()
        self.assertTrue(type(city1.name) == str)
        self.assertTrue(len(city1.name) == 0)
        city1.name = "Medellin"
        self.assertTrue(city1.name == "Medellin")
        self.assertTrue(type(city1.state_id) == str)
        self.assertTrue(len(city1.state_id) == 0)

if __name__ == '__main__':
    unittest.main()
