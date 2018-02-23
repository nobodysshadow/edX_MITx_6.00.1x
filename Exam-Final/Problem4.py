# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:39:33 2018
@author: guenther.wasser

Final Exam - Problem 4:
"""
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    def checkList(L):
        '''
        L : List of integers and strings
        Returns a dictionary with the elements sorted to how often they occure.
        '''
        tempDict = {}
        # Create the dictionary
        for e in L:
            try:
                tempDict[e] += 1
            except:
                tempDict[e] = 1

        return tempDict
    
    def findMax(D):
        '''
        D : Dictionary with mixed (int & str) keys and int only values
        Returns the key with the max integer value.
        '''
        maxValue = 0
        maxKey = ''
        for i in D.keys():
            if D[i] > maxValue:
                maxValue = D[i]
                maxKey = i
        return maxKey
    
    dictL1 = checkList(L1)
    dictL2 = checkList(L2)
    if dictL1 == {} or dictL2 == {}:
        return (None, None, None)
    k1 = findMax(dictL1)
    k2 = findMax(dictL2)
    if k1 == k2 and dictL1[k1] == dictL2[k2]:
        return (k1, dictL1[k1], type(k1))
    else:
        return False

L1 = ['a', 'a', 'b']
L2 = ['a', 'b']  # False
L3 = [1, 'b', 2, 'c', 'c', 1, 'd', 'c']
L4 = ['c', 1, 'b', 2, 1, 'c', 'd', 'c'] # (1, 3, <class 'int'>)
L5 = []
L6 = []
print(is_list_permutation(L1, L2))
print(is_list_permutation(L3, L4))
print(is_list_permutation(L5, L6))

  