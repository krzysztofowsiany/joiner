import random
import unittest
from Joiner import Joiner

class Test1(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_loadfile(self):
        j = Joiner
        self.assertTrue(j is Joiner)

if __name__ == '__main__':
    unittest.main()