# -*- coding: utf-8 -*-
########################################
# Created on Sun Feb 11 11:10:07 2018
#
# @author: guenther.wasser
######################################## 
#
# Problem 5:
# ----------
# 
# Write a function called dict_invert that takes in a dictionary with immutable 
# values and returns the inverse of the dictionary. The inverse of a dictionary 
# d is another dictionary whose keys are the unique dictionary values in d. 
# The value for a key in the inverse dictionary is a sorted list of all keys 
# in d that have the same value in d.
# 
# Here are some examples:
# If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
# If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
# If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
# 
def dict_invert(d):
  """inverts a dictionary with immutable values
  
  Takes in a dictionary with immutable values and returns the inverse of the 
  dictionary. The inverse of a dictionary d is another dictionary whose keys 
  are the unique dictionary values in d. The value for a key in the inverse 
  dictionary is a sorted list of all keys in d that have the same value in d.
  
  Decorators:
    guenther.wasser
  
  Args:
    d ([dict]): dictionary with immutable values
  """
  newDict = {}
  for x in d.values():
    newDict[x] = []
  for v in d.keys():
    newDict[d[v]] += [v,]
  for x in newDict.keys():
    if len(newDict[x]) > 1:
      newItem = newDict[x]
      newDict[x] = sorted(newItem)
  return newDict

d = {1:10, 2:20, 3:30}
print('Before:   ', d)
n = dict_invert(d)
print('After:    ', n)
d = {1:10, 2:20, 3:30, 4:30}
print('Before:   ', d)
n = dict_invert(d)
print('After:    ', n)
d = {4:True, 2:True, 0:True}
print('Before:   ', d)
n = dict_invert(d)
print('After:    ', n)
print()
print()
print()
d = {}
print('Before:   ', d)
n = dict_invert(d)
print('After:    ', n)
print()
d = {1: 1}
print('Before:   ', d)
n = dict_invert(d)
print('After:    ', n)
print()
d = {1: 3, 2: 4}
print('Before:   ', d)
n = dict_invert(d)
print('After:    ', n)
print()
d = {1: 1, 2: 1}
print('Before:   ', d)
n = dict_invert(d)
print('After:    ', n)
print()
d = {2: 3, 3: 20, 4: 10}
print('Before:   ', d)
n = dict_invert(d)
print('After:    ', n)
print()
d = {8: 6, 2: 6, 4: 6, 6: 6}
print('Before:   ', d)
n = dict_invert(d)
print('After:    ', n)
print()
d = {30000: 30, 600: 30, 2: 10}
print('Before:   ', d)
n = dict_invert(d)
print('After:    ', n)
print()
d = {1: 0, 2: True, 3: True, 4: True}
print('Before:   ', d)
n = dict_invert(d)
print('After:    ', n)
print()
d = {0: 9, 9: 9, 5: 9}
print('Before:   ', d)
n = dict_invert(d)
print('After:    ', n)
