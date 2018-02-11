# -*- coding: utf-8 -*-
########################################
# Created on Sun Feb 11 10:57:57 2018
#
# @author: guenther.wasser
######################################## 
#
# Problem 4:
# ----------
# Implement a function that meets the specifications below.
# 
# def deep_reverse(L):
#     """ assumes L is a list of lists whose elements are ints
#     Mutates L such that it reverses its elements and also 
#     reverses the order of the int elements in every element of L. 
#     It does not return anything.
#     """
# 
# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) 
# mutates L to be [[7, 6, 5], [4, 3], [2, 1]]
# 
# Please read carefully. The question states that you need to mutate L. 
# Your code must work when you do this:
# L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
# deep_reverse(L) 
# print(L)

def deep_reverse(L):
  """Reverse a nested list of elements
  
  assumes L is a list of lists whose elements are ints
  Mutates L such that it reverses its elements and also 
  reverses the order of the int elements in every element of L. 
  
  Args:
    L ([list]): List of ints
  Return:
    None: It does not return anything.
  """
  for element in L:
    element.reverse()
  L.reverse()

L = [[1, 2], [3, 4], [5, 6, 7]]
print("Before:   ", L)
deep_reverse(L) 
print("After:    ", L)
L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
print("Before:   ", L)
deep_reverse(L) 
print("After:    ", L)
