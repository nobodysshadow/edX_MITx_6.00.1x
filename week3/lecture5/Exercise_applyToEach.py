# -*- coding: utf-8 -*-

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def addOne(a):
    return a + 1

def multItself(a):
    return abs(a * a)


testList = [1, -4, 8, -9]
# applyToEach(testList, abs)
# applyToEach(testList, addOne)
applyToEach(testList, multItself)

print(testList)
