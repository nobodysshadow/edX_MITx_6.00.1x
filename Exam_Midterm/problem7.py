# -*- coding: utf-8 -*-
########################################
# Created on Sun Feb 11 13:35:07 2018
#
# @author: guenther.wasser
######################################## 
#
# Problem 7:
# ----------
# 
# Implement a function that meets the specifications below.
# 
# def applyF_filterG(L, f, g):
#     """
#     Assumes L is a list of integers
#     Assume functions f and g are defined for you. 
#     f takes in an integer, applies a function, returns another integer 
#     g takes in an integer, applies a Boolean function, 
#         returns either True or False
#     Mutates L such that, for each element i originally in L, L contains  
#         i if g(f(i)) returns True, and no other elements
#     Returns the largest element in the mutated L or -1 if the list is empty
#     """
# For example, the following functions, f, g, and test code:
# 
# def f(i):
#     return i + 2
# def g(i):
#     return i > 5
# 
# L = [0, -10, 5, 6, -4]
# print(applyF_filterG(L, f, g))
# print(L)
# Should print:
# 
# 6
# [5, 6]
# For this question, you will not be able to see the test cases we run. 
# This problem will test your ability to come up with your own test cases.
# 
# ----------
def f(i):
  """Add 2 to a value
  
  Args:
      i ([int]): integer value
  
  Returns:
      [int]: integer value
  """
  return i + 2

def g(i):
  """Evaluates value to be greater than 5
  
  Args:
      i ([int]): integer value
  
  Returns:
      [bool]: True if value is greater than 5
  """
  return i > 5

def applyF_filterG(L, f, g):
  """Mutates a list of integers
  
  Mutates L such that, for each element i originally in L, L contains  
  i if g(f(i)) returns True, and no other elements
  
  Decorators:
      guenther.wasser
  
  Args:
      L ([list]): List of integer values
      f ([function]): [description]
      g ([type]): [description]
  """
  newList = []
  L2 = L[:]
  maxValue = 0
  
  # Empty list return -1
  if len(L) == 0:     
    return -1
  
  # Create new List
  for i in L:
    if g(f(i)):
      newList.append(i)
  
  # Alter original List
  for i in L2:
    if i not in newList:
        L.remove(i)
  
  # Find max value
  for i in newList:
    if i > maxValue:
      maxValue = i
  return maxValue  

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)

L = [7, -1, 3, 4, -4, 8, -9]
print(applyF_filterG(L, f, g))
print(L)

L = []
print(applyF_filterG(L, f, g))
print(L)

L = [1, 2, 3, 4, 5, 6, 7]
print(applyF_filterG(L, f, g))
print(L)

# Only 16 from 20 points earned!
