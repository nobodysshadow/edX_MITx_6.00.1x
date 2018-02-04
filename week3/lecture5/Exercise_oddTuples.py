# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:44:17 2018
@author: guenther.wasser

Exercise Odd Tuples:
Write a procedure called oddTuples, which takes a tuple as input, and returns 
a new tuple as output, where every other element of the input tuple is copied, 
starting with the first one. 
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating 
oddTuples on this input would return the tuple ('I', 'a', 'tuple').
"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    for i in range(len(aTup)):
        if (i % 2) == 0:
            newTup += aTup[i:i+1]
    return newTup

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))