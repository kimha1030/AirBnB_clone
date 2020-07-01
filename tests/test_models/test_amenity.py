#!/usr/bin/python
"""unittest Amenity class
"""
import unittest
from models.amenity import Amenity
import pep8


class TestState(unittest.TestCase):
    """Test Amenity class"""

    def test_amenity_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_amenity_docstring(self):
        """Check the docstring in the class"""
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_state(self):
        amenity1 = Amenity()
        self.assertTrue(type(amenity1.name) == str)
        self.assertTrue(len(amenity1.name) == 0)
        amenity1.name = "ok"
        self.assertTrue(amenity1.name == "ok")

if __name__ == '__main__':
    unittest.main()
