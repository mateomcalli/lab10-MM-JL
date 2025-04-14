import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        try:
            assert add(1, 1) == 2
        except ValueError as e:
            print("Error:", str(e))
        try:
            assert add(2, 3) == 5
        except ValueError as e:
            print("Error:", str(e))
        try:
            assert add(4, 4) == 8
        except ValueError as e:
            print("Error:", str(e))

    def test_subtract(self):  # 3 assertions
        try:
            assert subtract(3, 1) == 2
        except ValueError as e:
            print("Error:", str(e))
        try:
            assert subtract(1, 1) == 0
        except ValueError as e:
            print("Error:", str(e))
        try:
            assert subtract(10, 2) == 8
        except ValueError as e:
            print("Error:", str(e))

    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        try:
            assert logarithm(2, 8) == 3
        except ValueError as e:
            print("Error:", str(e))
        try:
            assert logarithm(3, 27) == 3
        except ValueError as e:
            print("Error:", str(e))
        try:
            assert logarithm(5, 625) == 4
        except ValueError as e:
            print("Error:", str(e))

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 100)
    # ##########################

    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()