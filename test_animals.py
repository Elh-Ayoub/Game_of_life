import unittest
from animals import Animal

class TestAnimal(unittest.TestCase):
    animal = Animal()
    def test(self):
        self.assertRaises(TypeError, Animal, True)
    def test_creatures(self):
        self.assertEqual(self.animal.isAlive(), True)
        self.animal.kill()
        self.assertEqual(self.animal.isAlive(), False)
    def test_coordinates(self):
        self.animal.x = 4
        self.animal.y = 7
        self.assertRaises(TypeError, self.animal.coordinates(), True)
    def test_eating(self):
        self.assertRaises(TypeError, self.animal.eat() , True)
        ##
        an = Animal()
        self.assertRaises(TypeError, an.eat(), True)