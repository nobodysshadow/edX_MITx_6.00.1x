# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:39:58 2018
@author: guenther.wasser@gmx.net
"""
'''
Grader
Regular Polygons: polysum
A regular polygon has 'n' number of sides. Each side has length 's'.
* The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
* The perimeter of a polygon is: length of the boundary of the polygon
Write a function called 'polysum' that takes 2 arguments, 'n' and 's'. 
This function should sum the area and square of the perimeter of the regular 
polygon. The function returns the sum, rounded to 4 decimal places.
'''
import math

def polyarea(n, s):
    """
    Input  n:   Number of sides (as integer)
           s:   Length of each side (as integer or float)
    return: Area of the Regular Polygon rounded to 4 decimals
    """
    return round(((0.25 * n * s**2) / (tan(pi / n))),4)

def polyperimeter(n, s):
    """
    Input  n:   Number of sides (as integer)
           s:   Length of each side (as integer or float)
    return: Perimeter of the Regular Polygon rounded to 4 decimals
    """
    return round(n*s,4)    

def polysum(n, s):
    """
    Input  n:   Number of sides (as integer)
           s:   Length of each side (as integer or float)
    return: Sum of the area and square of the perimeter rounded to 4 decimals
    """
    area = polyarea(n,s)
    perimeter = polyperimeter(n,s)
    return round((area + perimeter**2),4)
