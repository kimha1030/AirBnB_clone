#!/usr/bin/python
"""unittest init class
"""
import unittest
import pep8
from datetime import datetime
from models import __init__


class TestInit(unittest.TestCase):
    """Test for file init"""
    def test_init_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/__init__.py'])
        self.assertEqual(result.total_errors, 0)

    def test_init_docstring(self):
        """Check the docstring in the class"""
        self.assertTrue(len(__init__.__doc__) >= 1)

if __name__ == '__main__':
    unittest.main()
