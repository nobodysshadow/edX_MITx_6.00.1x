# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:17:33 2018
@author: guenther.wasser

Final Exam - Problem 3:
"""
def isPalindrome(s):
    """ Return True, if a given text is a Palindrom. """
    def onlyChars(text):
        """ Check only letters in lower case """
        text = text.lower()
        feedback = ''
        for letter in text:
            if letter in "abcdefghijklmnopqrstuvwxyz":  #string.ascii_lowercase
                feedback += letter
        return feedback

    def checkPal(text):
        """ Walk trough the text and verify each letter """
        if len(text) <= 1:
            return True
        else:
            return text[0] == text[-1] and checkPal(text[1:-1])

    return checkPal(onlyChars(s))

print("")
print('Is eve a palindrome?')
print(isPalindrome('eve'))

print('')
print('Is able was I ere I saw Elba a palindrome?')
print(isPalindrome('Able was I, ere I saw Elba'))
