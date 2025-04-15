# https://github.com/mateomcalli/lab10-MM-JL
# Partner 1: Mateo McAllister | Partner 2: Jamie Laird

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        else: return math.sqrt(a)
    except ValueError as e:
        print(e)

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def logarithm(a,b):
    try:
        if a <= 0 or b <= 1:
            raise ZeroDivisionError
        else: return math.log(b,a)
    except ZeroDivisionError as e:
        print(e)

def mul(a, b):
    return a * b

def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError
        return b / a
    except ZeroDivisionError as e:
        print("Error:", str(e))

def exp(a, b):
    return a ** b
