# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:06:03 2021

@author: jagad
"""

array = []
n = int(input())
for x in range(n):
    t = int(input())
    array.append(t)
array.sort()
print(array)