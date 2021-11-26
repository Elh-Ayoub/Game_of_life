import unittest
import main

class TestMain(unittest.TestCase):
    def test_prob(self):
        self.assertAlmostEqual(main.g_0 + main.g_3, 1.0)
        self.assertGreater(main.iterations, -1)
        