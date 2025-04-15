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
    if a <= 0:
        raise ValueError
    if a == 1:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(b,a)

def mul(a, b):
    return a * b

def div(a, b):
        if a == 0:
            raise ZeroDivisionError
        return b / aa

def exp(a, b):
    return a ** b
