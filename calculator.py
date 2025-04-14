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

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    try:
        if a != 0:
            return b/a
        else: raise ZeroDivisionError
    except ZeroDivisionError as e:
        print(e)

def logarithm(a,b):
    try:
        if a <= 0 or b <= 1:
            raise ValueError
        else: return math.log(b,a)
    except ValueError as e:
        print(e)

def exponent(a,b):
    return a**b

def add(a, b):
    return a + b

def sub(a,b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        if a == 0:
            raise ValueError("Dividing by 0")
        return b / a
    except ValueError as e:
        print("Error:", str(e))

def log(a, b):
    try:
        if b < 0 or a == 1 or a < 0:
            raise ValueError("Invalid Value.")
        return math.log(b, a)
    except ValueError as e:
        print("Error:", str(e))
def exp(a, b):
    return a ** b

