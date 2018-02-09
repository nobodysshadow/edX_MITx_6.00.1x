# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 18:32:18 2018
@author: guenther.wasser

Exercise biggest:
Consider the following sequence of expressions:
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
We want to write some simple procedures that work on dictionaries to return information.
This time, write a procedure, called biggest, which returns the key 
corresponding to the entry with the largest number of values associated with it. 
If there is more than one such entry, return any one of the matching keys.
Example usage:
biggest(animals)
'd'
If there are no values in the dictionary, biggest should return None.
"""
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    totalItems = 0
    maxItems = 0
    maxKey = ''
    for item in aDict:
        if maxItems < len(aDict[item]):
           maxKey = item
           maxItems = len(aDict[item])
        totalItems += len(aDict[item])
    if maxItems == 0:
        return None
    return maxKey

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(biggest(animals))
cars = {}
print(biggest(cars))