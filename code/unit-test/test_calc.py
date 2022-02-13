import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self): #the method name needs to begin with 'test_'
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self): #the method name needs to begin with 'test_'
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self): #the method name needs to begin with 'test_'
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self): #the method name needs to begin with 'test_'
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        self.assertRaises(ValueError, calc.divide, 10, 0)

# with only the above script, this command syntax is needed to run from the command line: python -m unittest test_calc.py
# we can make simpler with the below:

if __name__ == '__main__':
    unittest.main()