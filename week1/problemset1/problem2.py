# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:26:13 2018
@author: guenther.wasser

Problem Set 1 / Problem 2:

Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2 
"""
#Predefined Variable just for testing
s = 'oqbbobbcgjobobbobbaobobobobbobbaoobob'

#Setup variables
occurance = 0
position = 0
#Checking String
for c in s:
    if c == 'b' and position < (len(s)-2):
        if s[position+1] == 'o' and s[position+2] == 'b':
            occurance += 1
    position += 1
print("Number of times bob occurs is: " + str(occurance))


#Correct Result: 10 Points
#on second try with error correction (string length)
