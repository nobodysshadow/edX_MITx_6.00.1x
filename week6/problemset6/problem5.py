'''
 You have 2 attempts for this problem.

Here is code for linear search that uses the fact that a set of elements is sorted in increasing order:

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
 
    

Consider the following code, which is an alternative version of search.

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

    

Which of the following statements is correct? You may assume that each function is tested with a list L whose elements are sorted in increasing order; for simplicity, assume L is a list of positive integers.
'''

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
 
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

L1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
L2 = [0,2]
L3 = []

print(search(L1, 5)) # True
print(search(L2, 5)) # False
print(search(L3, 5)) # True
print(search(L1, 2)) # True
print(search(L2, 2)) # False
print(search(L3, 2)) # True
print(search(L1, 22)) # False
print(search(L2, 22)) # False
print(search(L3, 22)) # False
print('\n\n')
print(newsearch(L1, 5)) # True
print(newsearch(L2, 5)) # False
print(newsearch(L3, 5)) # True
print(newsearch(L1, 2)) # True
print(newsearch(L2, 2)) # False
print(newsearch(L3, 2)) # True
print(newsearch(L1, 22)) # False
print(newsearch(L2, 22)) # False
print(newsearch(L3, 22)) # False
