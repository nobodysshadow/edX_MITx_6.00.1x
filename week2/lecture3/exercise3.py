# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:54:25 2018
@author: guenther.wasser

Exercise: guess my number (3)
In this problem, you'll create a program that guesses a secret number!
The program works as follows: you (the user) thinks of an integer between 
0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you 
give it input - is its guess too high or too low? Using bisection search, 
the computer will guess the user's secret number!
Note: your program should use input to obtain the user's input! Be sure to 
handle the case when the user's input is not one of h, l, or c.
When the user enters something invalid, you should print out a message to the 
user explaining you did not understand their input. Then, you should re-ask 
the question, and prompt again for input.
"""

def get_input(comment):
    """
    Check that the input is a correct number
    comment: give the text to ask for the number.
    """
    while True:
        try:
            feedback = str(input(comment))
        except Exception:
            print("This was no character!")
        if feedback == 'h' or feedback == 'l' or feedback == 'c':
            return feedback
        else:
            feedback = "Sorry, I did not understand your input."
            return feedback

x = 100
low = 0
high = x
found = False
print("Please think of a number between 0 and 100!")
while found is not True:
    num = int((high+low)/2)
    #print(str(low), " ", str(high), " ", str(num))
    print("Is your secret number ", str(num), "?")
    answer = get_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.  ")
    #print(answer)
    if answer == 'h':
        high = num
    elif answer == 'l':
        low = num
    elif answer == 'c':
        print("Game over. Your secret number was: ", str(num))
        found = True
    else:
        print(answer)

