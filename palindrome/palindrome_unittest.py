import unittest
from palindrome import *


class TestCase(unittest.TestCase):
    # make sure it correctly identifies palindrome
    def test_works(self):
        self.assertEqual(pali("yellowolley"), True)

    # make sure it identifies input with incorrect expected output
    def test_bad(self):
        self.assertEqual(pali("Ooogabooga"), True)

    # make sure numbers work
    def test_nums(self):
        self.assertEqual(pali("12321"), True)


if __name__ == "__main__":
    unittest.main()
