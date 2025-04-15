# https://github.com/mateomcalli/lab10-MM-JL
# Partner 1: Mateo McAllister | Partner 2: Jamie Laird

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(5, 3), 8)
        self.assertNotEqual(add(2, 3), 6)
        self.assertEqual(add(2, 3), 5)


    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(3, 1), 2)
        self.assertNotEqual(subtract(1, 1), 1)
        self.assertEqual(subtract(5, 3), 2)

    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5,3), 15)
        self.assertNotEqual(mul(1,5), 1)
        self.assertAlmostEqual(mul(14.21, 2.12), 30.1252)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(1,21), 21)
        self.assertNotEqual(div(5,1.5), 7.5)
        self.assertIs(div(0,1), None)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,10)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertNotEqual(logarithm(3, 27), 8)
        self.assertNotEqual(logarithm(32, 2), 5)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            logarithm(0, 10)
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        self.assertIs(logarithm(-1,5),None)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4),5)
        self.assertNotEqual(hypotenuse(4,5),6)
        self.assertAlmostEqual(hypotenuse(9,16),18.35755975)

    def test_sqrt(self): # 3 assertions
        self.assertIs(square_root(-1), None)
        self.assertEqual(square_root(4),2)
        self.assertNotEqual(square_root(16),1)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()