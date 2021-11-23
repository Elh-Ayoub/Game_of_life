import unittest
import init
from __init__ import *

class TestInit(unittest.TestCase):
    def test_input(self):
        self.assertTrue(type(init.width) is int)
        self.assertTrue(type(init.height) is int)
        # self.assertGreater(init.width, init.height)
    # def test_proba(self):
    #     self.assertRaises(TypeError, updateField, True)