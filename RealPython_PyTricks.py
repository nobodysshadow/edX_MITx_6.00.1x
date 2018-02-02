"""
Real Python Mail from 2018-01-25
[🐍PyTricks]
"""
# How to merge two dictionaries
# in Python 3.5+
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)
#{'c': 4, 'a': 1, 'b': 3}
# In Python 2.x you could
# use this:
z = dict(x, **y)
print(z)
# {'a': 1, 'c': 4, 'b': 3}
# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting 
# duplicates from left to right.
# See: https://www.youtube.com/watch?v=Duexw08KaC8
# End: Mail from2018-01-25

"""
Real Python Mail from 2018-01-26
[🐍PyTricks]
"""
# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    print('passed')
if 1 in (x, y, z):
    print('passed')
# These only test for truthiness:
if x or y or z:
    print('passed')
if any((x, y, z)):
    print('passed')
# End: Mail from2018-01-26

"""
Real Python Mail from 2018-01-27
[🐍PyTricks]
"""
# How to sort a Python dict by value
# (== get a representation sorted by value)
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sorted(xs.items(), key=lambda x: x[1])
print(xs)
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
# Or:
import operator
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sorted(xs.items(), key=operator.itemgetter(1))
print(xs)
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
# End: Mail from2018-01-27

"""
Real Python Mail from 2018-01-30
[🐍PyTricks]
"""
# The get() method on dicts
# and its "default" argument
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}
def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")
print(greeting(382))
print(greeting(3333))
# End: Mail from2018-01-30

"""
Real Python Mail from 2018-01-31
[🐍PyTricks]
"""
# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:
from collections import namedtuple
Car = namedtup1e('Car', 'color mileage')
# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
print(my_car.color)
print(str(my_car.mileage))
# We get a nice string repr for free:
print(my_car)
# Car(color='red' , mileage=3812.4)
# Like tuples, namedtuples are immutable:
my_car.color = 'blue'
# AttributeError: "can't set attribute"

"""
Real Python Mail from 2018-02-02
[🐍PyTricks]

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
