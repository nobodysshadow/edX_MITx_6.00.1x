# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:26:52 2018
@author: guenther.wasser

Exercise: iterPower
Write an iterative function iterPower(base, exp) that calculates the 
exponential baseexp by simply using successive multiplication. For example, 
iterPower(base, exp) should compute baseexp by multiplying base times itself 
exp times. Write such a function below.
This function should take in two values - base can be a float or an integer; 
exp will be an integer ≥ 0. It should return one numerical value. 
Your code must be iterative - use of the ** operator is not allowed.
"""
def iterPower(base, exp = 1):
    """
    that calculates the exponential baseexp by simply using successive multiplication
    base: can be a float or an integer
    exp: will be an integer ≥ 0
    """
    result = 1
    for i in range(exp):
        result = result * base
    return result

print(iterPower(2.5,5))
