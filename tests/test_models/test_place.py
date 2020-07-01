#!/usr/bin/python
"""unittest Place class
"""
import unittest
from models.place import Place
import pep8


class TestPlace(unittest.TestCase):
    """Test Place class"""

    def test_place_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_place_docstring(self):
        """Check the docstring in the class"""
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_place(self):
        place1 = Place()
        self.assertTrue(type(place1.name) == str)
        self.assertTrue(len(place1.name) == 0)
        place1.name = "Hotel"
        self.assertTrue(place1.name == "Hotel")
        self.assertTrue(type(place1.city_id) == str)
        self.assertTrue(len(place1.city_id) == 0)
        self.assertTrue(type(place1.latitude) == float)
        self.assertTrue(type(place1.longitude) == float)
        self.assertTrue(type(place1.number_rooms) == int)
        self.assertTrue(type(place1.number_bathrooms) == int)
        self.assertTrue(type(place1.amenity_ids) == list)
        self.assertTrue(place1.latitude == 0.0)
        place1.latitude = 3.5677
        self.assertTrue(place1.latitude == 3.5677)

if __name__ == '__main__':
    unittest.main()
