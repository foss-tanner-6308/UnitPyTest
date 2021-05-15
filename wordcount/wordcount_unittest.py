import unittest
from wordcount import *


class TestCase(unittest.TestCase):
    # make sure it correctly counts words
    def test_works(self):
        self.assertEqual(wordcount("I hope this words"), 4)

    # make sure it identifies input with incorrect expected output
    def test_bad(self):
        self.assertEqual(wordcount("Please work"), 3)

    # make sure numbers work
    def test_nums(self):
        self.assertEqual(wordcount("1 2 3 4 5"), 5)


if __name__ == "__main__":
    unittest.main()