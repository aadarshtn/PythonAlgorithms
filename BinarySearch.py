# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 00:43:31 2019

@author: ADARSH
"""

def binary_search(n,x):
    
    first_pos = 0
    last_pos = len(a)-1
    flag=False
    count=0
    
    while(first_pos<=last_pos and flag==False):
        count+=1
        mid=(first_pos+last_pos)//2
        if x==a[mid]:
            flag=True
            print("The element is present at : "+str(mid))
            print("The number of iterations took : "+str(count))
            return
            
        else:
            if x<a[mid]:
                last_pos = mid-1
            else:
                first_pos = mid+1
    
    print("The number not found")
    
a=[]
for i in range(1,100001):
    a.append(i)
    
binary_search(a,100000)
            
        
