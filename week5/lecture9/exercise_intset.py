'''
Created on Wed Feb 18 10:27 2018
@author: guenther.wasser

Exercise: int set
-----------------

Consider the following code from the last lecture video:

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

Your task is to define the following two methods for the intSet class:

Define an intersect method that returns a new intSet containing elements that appear in both sets. In other words,

s1.intersect(s2)
would return a new intSet of integers that appear in both s1 and s2. Think carefully - what should happen if s1 and s2 have no elements in common?

Add the appropriate method(s) so that len(s) returns the number of elements in s.

Hint: look through the Python docs to figure out what you'll need to solve this problem.
'''

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def __len__(self):
      """Returns the length of the set"""
      return len(self.vals)

    def len(self):
      """Returns the length of the set"""
      return len(self.vals)

    def intersect(self, other):
      """All elements in both sets
      
      Returns a new intSet containing elements that appear in both sets.
      s1.intersect(s2) - would return a new intSet of integers that appear in both s1 and s2.
      
      Args:
        other ([intSet]): another object of the intSet class
      """
      newIntSet = intSet()
      if self.__len__() == 0 or other.__len__() == 0:
        return newIntSet
      for item in self.vals:
        if other.member(item):
          newIntSet.insert(item)
      return newIntSet

s1 = intSet()
s2 = intSet()
s3 = s1.intersect(s2)
print(s1, s2, s3)
print(s1.len(), s2.len(), s3.len())

s1.insert(2)
s1.insert(3)
s1.insert(4)
s2.insert(2)
s2.insert(3)
s2.insert(4)
s4 = s1.intersect(s2)
print(s1, s2, s4)
print(s1.len(), s2.len(), s4.len())

s5 = intSet()
s6 = intSet()
s5.insert(2)
s5.insert(3)
s5.insert(4)
s6.insert(1)
s6.insert(5)
s6.insert(6)
s7 = s5.intersect(s6)
print(s5, s6, s7)
print(intSet.len(s5), intSet.len(s6), intSet.len(s7))
