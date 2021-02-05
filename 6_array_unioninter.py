# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:09:39 2021

@author: jagad
"""
a1 =[]
a2 =[]
a3=[]
a4=[]
def Union(a1,a2):
    final=a1+a2
    return final

def Intersection(a1,a2):
    return list(set(a1) & set(a2)) 
    
n1 = int(input())

n2 = int(input())

for x in range(n1):
    g = int(input())
    a1.append(g)
    
for y in range(n2):
    h = int(input())
    a2.append(h)

a3=Union(a1,a2)
print(a3)

a4=Intersection(a1,a2)
print(a4)