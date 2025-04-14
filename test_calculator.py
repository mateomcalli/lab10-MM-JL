# https://github.com/mateomcalli/lab10-MM-JL
# Partner 1: Mateo McAllister | Partner 2: Jamie Laird

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
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
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()