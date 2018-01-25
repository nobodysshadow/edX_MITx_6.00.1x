# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:12:10 2018

@author: guent
"""
varA = 5
varB = 7

if type(varA) is int and type(varB) is int:
  if varA > varB:
    print("bigger")
  elif varA == varB:
    print("equal")
  else:
    print("smaller")
else:
  print("string involved")