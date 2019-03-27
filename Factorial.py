# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:30:19 2019

@author: ADARSH
"""

k = int(input())

fac = 1
for i in range(1,k+1):
    fac=fac*i
    if(k==0):
        break

print(fac)