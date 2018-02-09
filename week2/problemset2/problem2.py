# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:04:25 2018
@author: guenther.wasser

Problem Set 2 / Problem 2:
Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but instead 
is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.
The following variables contain values as described below:
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will 
pay off all debt in under 1 year, for example:
Lowest Payment: 180 
Assume that the interest is compounded monthly according to the balance at 
the end of the month (after the payment for that month is made). The monthly 
payment must be a multiple of $10 and is the same for all months. Notice that 
it is possible for the balance to become negative using this payment scheme, 
which is okay. A summary of the required math is found below:
    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
Test Cases to Test Your Code With. Be sure to test these on your own machine - 
and that you get the same output! - before running your code on this webpage!

Test Cases:
	      Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310
      
	      Test Case 2:
	      balance = 4773
	      annualInterestRate = 0.2
	      
	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 440
      
	      Test Case 3:
	      balance = 3926
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 360
"""

balance = 3926
annualInterestRate = 0.2

def getRemainingBalance(balance, annualInterestRate, monthlyPaymentRate):
    """
    Input   balance - the outstanding balance on the credit card
            annualInterestRate - annual interest rate as a decimal
            monthlyPaymentRate - minimum monthly payment rate as a decimal
    Return  the remaining balance at the end of the year, rounded to 2 decimals
    """
    monthlyInterestRate = annualInterestRate / 12.0
    remainingBalance = balance
    for month in range(12):
        minimumMonthlyPayment = monthlyPaymentRate * remainingBalance
        monthlyUnpaidBalance = remainingBalance - minimumMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        remainingBalance = updatedBalanceEachMonth
        # print('Month ', month, ' Remaining balance: ', round(remainingBalance, 2))
    return round(remainingBalance, 2)

def getLowestPayment(balance, annualInterestRate):
    """
    Input   balance - the outstanding balance on the credit card
            annualInterestRate - annual interest rate as a decimal
    Return  the remaining balance at the end of the year, rounded to 2 decimals
    """
    monthlyPayment = int((balance + (balance * annualInterestRate))/14)
    remainingBalance = balance
    while remainingBalance >= 0:
        for month in range(1,13):
            monthlyInterestRate = annualInterestRate/12
            monthlyUnpaidBalance = remainingBalance - monthlyPayment
            updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
            remainingBalance = updatedBalanceEachMonth
            # print('Month ', month, ': my monthly payment= ', monthlyPayment, ' and the Remaining balance: ', round(remainingBalance, 2))
        if remainingBalance <= 0:
            lastdigit = monthlyPayment % 10
            print(monthlyPayment, lastdigit)
            if lastdigit == 0:
                return round(monthlyPayment, -1)
            elif lastdigit <= 5:
                return round(monthlyPayment+5, -1)
            else:
                return round(monthlyPayment, -1)
        else:
            monthlyPayment += 1
            remainingBalance = balance

print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 4773; annualInterestRate = 0.2    # OK - 440
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 3926; annualInterestRate = 0.2    # OK - 360
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 716; annualInterestRate = 0.18    # OK - 70
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 130; annualInterestRate = 0.18    # OK - 20
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 242; annualInterestRate = 0.2     # OK - 30
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 625; annualInterestRate = 0.18    # OK - 60
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 3593; annualInterestRate = 0.2    # OK - 330
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 4115; annualInterestRate = 0.04    # OK - 350
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 3115; annualInterestRate = 0.18    # OK - 290
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 3647; annualInterestRate = 0.04    # OK - 310
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 4642; annualInterestRate = 0.2     # OK - 430
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 4427; annualInterestRate = 0.18    # OK - 400
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 4772; annualInterestRate = 0.04    # OK - 410
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
balance = 4679; annualInterestRate = 0.2     # OK - 430
print('Lowest Payment: ', getLowestPayment(balance, annualInterestRate))
