import unittest
from areacircle import area_of_circle
from math import pi

class Test_Area_of_Circle(unittest.TestCase):
    def test_area(self): #Note - a test method added to the test class must start with 'test' to be added to the test suite by unittest.main() and run ons cript exeuction
        # Test radius only greater than 0 or > 0
        self.assertAlmostEqual(area_of_circle(0), 0)
        self.assertAlmostEqual(area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle(3.5), pi * 3.5**2)

    def test_values(self):
        self.assertRaises(ValueError, area_of_circle, -1)

if __name__ == "__main__":
    unittest.main()