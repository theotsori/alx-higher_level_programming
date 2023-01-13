#!/usr/binpython3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_generation(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        
    def test_custom_id(self):
        b4 = Base(10)
        self.assertEqual(b4.id, 10)

if __name__ == '__main__':
    unittest.main()
