# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:39:33 2018
@author: guenther.wasser

Final Exam - Problem 5:
"""
def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    key_code = {}
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    text_encrypted = code[:]
    newText = []
    for letter in text_encrypted:
      try:
        newText.append(key_code[letter])
      except:
        newText.append(letter)
    code = ''.join(newText)
    return (key_code, code)

feedback = cipher('ghijklmnopqrstuvwxyzabcdef', 'abcdefghijklmnopqrstuvwxyz', 'ck gxk zgqotm 6.00.1d')
print(feedback[1])
print(feedback[0])
