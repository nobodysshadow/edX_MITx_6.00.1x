# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:26:13 2018
@author: guenther.wasser

Problem Set 1 / Problem 1:

Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5    
"""

#Setup variables
s = 'azcbobobegghakl'
vowels_count = 0
valid_vowels = ['a', 'e', 'i', 'o', 'u']
#Checking String
for c in s:
    if c in valid_vowels:
        vowels_count += 1
print("Number of vowels: " + str(vowels_count))


#Correct Result: 10 Points