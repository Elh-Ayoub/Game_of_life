import unittest
from simulator import Simulator
from visualizer import Visualizer
import math

class TestSimulator(unittest.TestCase):
    visualizer = Visualizer()
    g = (0.5, 0.5)
    simulator = Simulator(visualizer, g)
    def test(self):
        if all(isinstance(element, float) for element in self.g) and math.isclose(sum(self.g[:]), 1.0):
            self.assertRaises(TypeError, Simulator, True)
        else: raise ValueError("Distribution must be exact for these probabilities")
    def test_draw(self):
        self.assertRaises(TypeError, self.simulator.draw(), True)

    def test_fill(self):
        self.assertRaises(TypeError, self.simulator.fill(), True)

    def test_step(self):
        self.assertRaises(TypeError, self.simulator.step(), True)

    # def test_clear(self):
    #     self.assertRaises(TypeError, self.simulator.clear(), True)
    
        