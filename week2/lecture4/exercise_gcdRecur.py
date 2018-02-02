# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:54:48 2018
@author: guenther.wasser@gmail.com

Exercise gcdRecur:
The greatest common divisor of two positive integers is the largest integer 
that divides each of them without remainder. For example,
gcd(2, 12) = 2
gcd(6, 12) = 6
gcd(9, 12) = 3
gcd(17, 12) = 1
A clever mathematical trick (due to Euclid) makes it easy to find greatest 
common divisors. Suppose that a and b are two positive integers:
If b = 0, then the answer is a
Otherwise, gcd(a, b) is the same as gcd(b, a % b)
See this website for an example of Euclid's algorithm being used to find the gcd.
https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example
Write a function gcdRecur(a, b) that implements this idea recursively. This 
function takes in two positive integers and returns one integer
"""
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    #print("Intern: a=",a," b=",b)
    if a > b:
        x = b
        y = a
    else:
        x = a
        y = b
    r = y % x
    #print("Intern: x=",x," y=",y," r=",r)
    if r > 0:
        return gcdRecur(x, r)
    else:
        return x

print("GCD von 2 und 12:  ",gcdRecur(2, 12))
print("GCD von 6 und 12:  ",gcdRecur(6, 12))
print("GCD von 9 und 12:  ",gcdRecur(9, 12))
print("GCD von 17 und 12: ",gcdRecur(17, 12))
