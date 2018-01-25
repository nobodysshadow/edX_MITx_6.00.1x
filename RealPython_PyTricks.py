# [🐍PyTricks]: Mail from2018-01-25
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

# [🐍PyTricks]: Mail from2018-01-26
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

# [🐍PyTricks]: Mail from2018-01-27
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

# [🐍PyTricks]: Mail from2018-01-30
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

