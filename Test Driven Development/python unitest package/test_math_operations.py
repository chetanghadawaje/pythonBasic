"""
Unit tests for math operations file
"""

import unittest
from math_operations import add, subtract


class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(2,1), 1)
        self.assertEqual(subtract(-1, 1), 2)
        self.assertNotEqual(subtract(5,4), -1)


if __name__ == 'main':
    unittest.main()
