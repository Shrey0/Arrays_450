# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:50:31 2021

@author: jagad
"""
def lol(arr,n,k):
    arr.sort()
    return arr[k-1]

n = 6
k = 3
arr= [7,10,4,3,20,15]
print(lol(arr,n,k))        