#!/usr/bin/python
"""unittest User class
"""
import unittest
from models.state import State
import pep8


class TestState(unittest.TestCase):
    """Test User class"""

    def test_init_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_init_docstring(self):
        """Check the docstring in the class"""
        self.assertTrue(len(State.__doc__) >= 1)

    def test_state(self):
        state1 = State()
        self.assertTrue(type(state1.name) == str)
        self.assertTrue(len(state1.name) == 0)
        state1.name = "Antioquia"
        self.assertTrue(state1.name == "Antioquia")

if __name__ == '__main__':
    unittest.main()
