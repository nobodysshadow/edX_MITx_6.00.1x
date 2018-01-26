# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:42:58 2018

@author: guent
"""

x = 0
while x <= 8:
  x += 2
  print(x)
print("Goodbye!")

x = 10
print("Hello!")
while x >= 2:
  print(x)
  x -= 2

x = 1
end = 6
summary = 0
while x <= end:
  summary = summary + x
  x += 1
print(summary)

for x in range(2,11,2):
  print(x)
print("Goodbye!")

print("Hello!")
for x in range(10,1,-2):
  print(x)
  
end = 6
summary = 0
for x in range(1,end+1):
  summary = summary + x
print(summary)