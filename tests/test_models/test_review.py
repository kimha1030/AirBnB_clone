#!/usr/bin/python
"""unittest Review class
"""
import unittest
from models.review import Review
import pep8


class TestReview(unittest.TestCase):
    """Test Review class"""

    def test_review_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_review_docstring(self):
        """Check the docstring in the class"""
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_review(self):
        review1 = Review()
        self.assertTrue(type(review1.place_id) == str)
        self.assertTrue(len(review1.place_id) == 0)
        self.assertTrue(type(review1.user_id) == str)
        self.assertTrue(len(review1.user_id) == 0)
        self.assertTrue(type(review1.text) == str)
        self.assertTrue(len(review1.text) == 0)
        review1.user_id = "h33"
        self.assertTrue(review1.user_id == "h33")

if __name__ == '__main__':
    unittest.main()
