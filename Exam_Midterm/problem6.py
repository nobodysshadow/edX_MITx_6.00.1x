# -*- coding: utf-8 -*-
########################################
# Created on Sun Feb 11 13:11:07 2018
#
# @author: guenther.wasser
######################################## 
#
# Problem 6:
# ----------
# 
# Implement a function that meets the specifications below.
# def max_val(t): 
#     """ t, tuple or list
#         Each element of t is either an int, a tuple, or a list
#         No tuple or list is empty
#         Returns the maximum int in t or (recursively) in an element of t """ 
#     # Your code here
# For example,
# 
# max_val((5, (1,2), [[1],[2]])) returns 5.
# max_val((5, (1,2), [[1],[9]])) returns 9.
# Paste your entire function, including the definition, in the box below. 
# Do not leave any debugging print statements.
# 
# ----------
def max_val(t):
  """Get max int element of tuple or list
  
  Each element of t is either an int, a tuple, or a list
  No tuple or list is empty
  
  Decorators:
    guenther.wasser
  
  Args:
    t ([tuple, list]): tuple or list
  Return:
    Returns the maximum int in t or (recursively) in an element of t
  """
  maxValue = 0
  mv = 0
  for item in t:
    if type(item) == list or type(item) == tuple:
        mv = max_val(item)
    else:
      if item > maxValue:
        maxValue = item
    if mv > maxValue:
      maxValue = mv
  return maxValue

print(max_val((5, (1,2), [[1],[2]])))     # correct = 5
print(max_val((5, (1,2), [[1],[9]])))     # correct = 9
print(max_val(((5,10), 11, (12,32), [[15],[19]])))