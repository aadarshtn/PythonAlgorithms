# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:03:35 2019

@author: ADARSH
"""

def magicsqr(n):
    mgsqr = []
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        mgsqr.append(l)
        
    i = n//2
    j = n-1
    
    count=1
    num=n*n
    
    while(count<=num):
        if(i==-1 and j==n):
            j = n-2
            i = 0
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        
        if(mgsqr[i][j]!=0):
            j=j-2
            i=i+1
            continue
        
        else:
            mgsqr[i][j] = count
            count = count + 1
        
            i = i-1
            j = j+1
        
    for i in range(n):
        for j in range(n):
            print (mgsqr[i][j], end=" ")
        print()
        
    print("The sum of all the elements in a row/column/diagonal is : "+str(n*((n**2)+1)/2))
        
magicsqr(21)
            