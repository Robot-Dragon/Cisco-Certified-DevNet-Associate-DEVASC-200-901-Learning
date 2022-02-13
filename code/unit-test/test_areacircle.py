import unittest
from areacircle import area_of_circle
from math import pi

class TestAreaOfCircle(unittest.TestCase):
    def test_area(self):
        # Test radius >= 0
        self.assertAlmostEqual(area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle(0), 0)
        self.assertAlmostEqual(area_of_circle(3.5), pi * 3.5**2)

    def test_values(self):
        self.assertRaises(ValueError, area_of_circle, -1)