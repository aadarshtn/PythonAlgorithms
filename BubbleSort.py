# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:51:41 2019

@author: ADARSH
"""

def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
a=[2,4,3,8,1,9]

bubble(a)

for i in a:
    print(i)
            