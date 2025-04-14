"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# https://github.com/mateomcalli/lab10-MM-JL
# Partner 1: Mateo McAllister | Partner 2: Jamie Laird

import math

def add(a, b): 
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a != 0:
        return b/a
    else: raise ZeroDivisionError

def log(a,b):
    if a <= 0 or b <= 1:
        raise ValueError
    return math.log(b,a)

def exp(a,b):
    return a**b



