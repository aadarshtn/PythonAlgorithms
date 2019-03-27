# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:34:07 2019

@author: ADARSH
"""

def matrix():
    r=int(input("Enter the required number of rows: "))
    c=int(input("Enter the required number of coloumns: "))
    count=1
    m=[]
    for i in range(1,r+1):
        l=[]
        for j in range(1,c+1):
            l.append(count)
            count+=1
        m.append(l)
    
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()
    
matrix()