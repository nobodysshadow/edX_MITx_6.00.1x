# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:57:45 2018
@author: guenther.wasser@gmail.com

Exercise gcdIter:
The greatest common divisor of two positive integers is the largest integer 
that divides each of them without remainder. For example,
gcd(2, 12) = 2
gcd(6, 12) = 6
gcd(9, 12) = 3
gcd(17, 12) = 1
Write an iterative function, gcdIter(a, b), that implements this idea. 
One easy way to do this is to begin with a test value equal to the smaller of 
the two input arguments, and iteratively reduce this test value by 1 until you 
either reach a case where the test divides both a and b without remainder, or 
you reach 1.
"""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    for i in range(b-1,0,-1):
       #print("a=",a," b=",b," i=",i)
       if (a % i) == False and (b % i) == False:
           return i
       
print("GCD von 2 und 12:  ",gcdIter(2, 12))
print("GCD von 6 und 12:  ",gcdIter(6, 12))
print("GCD von 9 und 12:  ",gcdIter(9, 12))
print("GCD von 17 und 12: ",gcdIter(17, 12))
