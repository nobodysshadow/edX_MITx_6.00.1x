# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:56:41 2018
@author: guenther.wasser@gmail.com

Exercise isIn:
We can use the idea of bisection search to determine if a character is in a 
string, so long as the string is sorted in alphabetical order.
First, test the middle character of a string against the character you're 
looking for (the "test character"). If they are the same, we are done - 
we've found the character we're looking for!
If they're not the same, check if the test character is "smaller" than the 
middle character. If so, we need only consider the lower half of the string; 
otherwise, we only consider the upper half of the string. (Note that you can 
compare characters using Python's < function.)
Implement the function isIn(char, aStr) which implements the above idea 
recursively to test if char is in aStr. char will be a single character and 
aStr will be a string that is in alphabetical order. 
The function should return a boolean value.
As you design the function, think very carefully about what the base cases 
should be.

Hints
Basic function structuring
Be very careful about how you slice the string in the recursive cases! 
Before you execute the recursive cases, you test the middle character - 
so if you reach the recursive cases, you know the middle character cannot be 
a match, right? So be careful to not include this character when you make your 
recursive call!
What should your base case be?
You should be thinking about 3 situations:
What happens when the string is empty?
What happens when the string is of length 1?
What happens when the test character equals the middle character?
What should your recursive case be?
You should be thinking about 2 situations:
What happens when the test character is smaller than the middle character?
What happens when it is larger?
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    bStr = sorted(aStr.lower(),key=str.lower)
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return char == aStr
    else:
        middle = len(aStr) // 2
        if char == bStr[middle]:
            return True
        elif char < bStr[middle]:
            return isIn(char, ''.join(bStr[:middle]))
        else:
            return isIn(char, ''.join(bStr[middle:]))

print(isIn("a","DCeBAh"))

# Solution as correct answer proposed
def isIn2(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])

print(isIn2("a","DCeBAh"))