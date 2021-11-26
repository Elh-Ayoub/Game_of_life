import unittest
from herbivores import Herbivore

class TestHerbivore(unittest.TestCase):
    herbivore = Herbivore()
    def test(self):
        self.assertRaises(TypeError, Herbivore, True)
    def test_creatures(self):
        self.assertEqual(self.herbivore.isAlive(), True)
        self.herbivore.kill()
        self.assertEqual(self.herbivore.isAlive(), False)
    def test_coordinates(self):
        self.herbivore.x = 4
        self.herbivore.y = 7
        self.assertRaises(TypeError, self.herbivore.coordinates(), True)
        