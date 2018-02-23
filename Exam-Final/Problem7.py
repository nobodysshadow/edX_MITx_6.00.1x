# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:22 2018
@author: guenther.wasser

Final Exam - Problem 7:
"""
# Implement the class myDict with the methods below, which will represent a dictionary without using a dictionary object. The methods you implement below should have the same behavior as a dict object, including raising appropriate exceptions. Your code does not have to be efficient. Any code that uses a Python dictionary object will receive 0.
# For example:
# With a dict:  |    With a myDict:
# -------------------------------------------------------------------------------
# d = {}             md = myDict()        # initialize a new object using your choice of implementation
# d[1] = 2           md.assign(1,2)       # use assign method to add a key,value pair
# print(d[1])        print(md.getval(1))  # use getval method to get value stored for key 1
# del(d[1])          md.delete(1)         # use delete method to remove key,value pair associated with key 1
#
# class myDict(object):
#     """ Implements a dictionary without using a dictionary """
#     def __init__(self):
#         """ initialization of your representation """
#         #FILL THIS IN
#         
#     def assign(self, k, v):
#         """ k (the key) and v (the value), immutable objects  """
#         #FILL THIS IN
#         
#     def getval(self, k):
#         """ k, immutable object  """
#         #FILL THIS IN
#         
#     def delete(self, k):
#         """ k, immutable object """   
#         #FILL THIS IN
#     
# Paste your entire class in the box below. Do not leave any print statements.

class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.keyList = []
        self.keyValues = []
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        if k in self.keyList:
            i = self.keyList.index(k)
            self.keyValues[i] = v
        else:
            self.keyList.append(k)
            self.keyValues.append(v)
        
    def getval(self, k):
        """ k, immutable object  """
        if k in self.keyList:
            i = self.keyList.index(k)
            return self.keyValues[i]
        else:
            raise KeyError('Key not found in myDict object')
        
    def delete(self, k):
        """ k, immutable object """   
        if k in self.keyList:
            i = self.keyList.index(k)
            self.keyList.remove(k)
            del self.keyValues[i]
        else:
            raise KeyError('Key not found in myDict object')


md = myDict()        # initialize a new object using your choice of implementation
md.assign(1,2)       # use assign method to add a key,value pair
md.assign(10,2)
md.assign(2,3)
md.assign(15,5)
md.assign(8,6)
md.assign(2,5)
print(md.getval(15))  # use getval method to get value stored for key 1
print(md.getval(10))
print(md.getval(8))
print(md.getval(1))
print(md.getval(2))
md.delete(1)         # use delete method to remove key,value pair associated with key 1
md.delete(15)
#md.delete(1)
print(md.getval(10))
#print(md.getval(15))
print(md.getval(8))
#print(md.getval(1))
print(md.getval(2))


class myDict2(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.keyList = []
        self.keyValues = []
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        if k in self.keyList:
            i = self.keyList.index(k)
            self.keyValues[i].append(v)
        else:
            self.keyList.append(k)
            self.keyValues.append([v])
        
    def getval(self, k):
        """ k, immutable object  """
        if k in self.keyList:
            i = self.keyList.index(k)
            return self.keyValues[i]
        else:
            raise KeyError('Key not found in myDict object')
        
    def delete(self, k):
        """ k, immutable object """   
        if k in self.keyList:
            i = self.keyList.index(k)
            self.keyList.remove(k)
            del self.keyValues[i]
        else:
            raise KeyError('Key not found in myDict object')