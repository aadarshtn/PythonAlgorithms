# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 23:54:44 2019

@author: ADARSH
"""
def linear_search(n,x):
    element=[]
    for i in range(1,n):
        element.append(i)
    
    count=0
    flag=False
    for i in element:
        if i==x:
            print("Yes!!! Found the number at position : "+str(i))
            flag=True
            break
        count=count+1
    if flag==False:
        print("Number not found")
    print("no of iterations took to find : "+str(count))
        
            

