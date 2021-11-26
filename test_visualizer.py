import unittest
from visualizer import Visualizer

class TestVisualizer(unittest.TestCase):
    v = Visualizer()
    def test(self):
        self.assertRaises(TypeError, Visualizer, True)
    def test_str(self):
        self.assertRaises(TypeError, print(self.v), True)
    def test_setting_entities(self):
        l = [[1,2,3],[1,2,3],[1,2,3]]
        self.assertRaises(TypeError or ValueError, self.v.set_entities(l), True)
        