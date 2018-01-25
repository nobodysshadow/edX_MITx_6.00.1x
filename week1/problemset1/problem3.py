# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:26:13 2018
@author: guenther.wasser

Problem Set 1 / Problem 3:

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', 
then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, 
if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest that you 
move on to a different part of the course. If you have time, come back to 
this problem after you've had a break and cleared your head.
"""
#Predefined Variable just for testing
s = 'azcbobobegghakl'

#Setup variables
actual_position = 0
start_position = 0
next_position = 0
actual_length = 0
max_length = 0
alphabeth='abcdefghijklmnopqrstuvwxyz'
#Checking String
for i in s:
    position_check1 = 0
    if actual_position == 0:
        actual_position = 1
    else:
        actual_position += 1
    for c in alphabeth:
        position_check1 += 1
        if i == c:
            break
    print("Aktual Position: ", str(actual_position), " = Letter '", i, "' is letter number ", str(position_check1), " in alphabeth.")
    position_check2 = 0
    if actual_position == 1 or next_position == 1:
        next_position = 1
        for c in alphabeth:
            position_check2 += 1
            if s[1] == c:
                break
    elif actual_position <= len(s):
        next_position = actual_position
        for c in alphabeth:
            position_check2 += 1
            if s[next_position-1] == c:
                break
    else:
        break
    print("Compare Position: ", str(next_position), " = Letter '", s[next_position-1], "' is letter number ", str(position_check2), " in alphabeth.")
    print("Vergleiche: ", str(position_check1), " mit ", str(position_check2))
    if position_check1 <= position_check2:
        start_position = actual_position - 1
        actual_length += 1
        max_length += 1
    else:
        actual_length = max_length
    print("Start Position: ", str(start_position))
    print("Actual Length : ", str(actual_length))
    print("Maximal Lenght: ", str(max_length))


# print("Longest substring in alphabetical order is: " + substring)


#Correct Result: 10 Points
#on second try with error correction (string length)
