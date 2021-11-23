import unittest
from plants import Plant

class TestInit(unittest.TestCase):
    plant = Plant()
    def test(self):
        self.assertRaises(TypeError, Plant, True)
    def test_creatures(self):
        self.assertEqual(self.plant.isAlive(), True)
        self.plant.kill()
        self.assertEqual(self.plant.isAlive(), False)
    def test_coordinates(self):
        self.plant.x = 0
        self.plant.y = 7
        self.assertRaises(TypeError, self.plant.coordinates(), True)
        