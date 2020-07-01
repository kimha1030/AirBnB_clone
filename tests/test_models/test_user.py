#!/usr/bin/python
"""unittest User class
"""
import unittest
from models.user import User
import pep8


class TestUser(unittest.TestCase):
    """Test User class"""

    def test_init_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_init_docstring(self):
        """Check the docstring in the class"""
        self.assertTrue(len(User.__doc__) >= 1)

    def test_user(self):
        user1 = User()
        self.assertTrue(type(user1.id) == str)
        self.assertTrue(type(user1.email) == str)
        user1.email = "nasser@dev.com"
        self.assertTrue(user1.email == "nasser@dev.com")
        self.assertTrue(len(user1.first_name) == 0)
        self.assertTrue(type(user1.first_name) == str)

if __name__ == '__main__':
    unittest.main()
