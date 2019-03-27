# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:00:26 2019

@author: ADARSH
"""
import random

doors=[0]*3
goat_doors=[0]*2

swap=0
no_swap=0
stop=False
x=random.randint(0,2)
doors[x]="BMW"

for i in range(0,3):
    if(i==x):
        continue
    else:
        doors[i]="Goat"
        goat_doors.append(i)
    while stop==False:
        choice=int(input("Enter Your Choice Of Doors(0,1,2)"))
        door_open=random.choice(goat_doors)
        while door_open==choice:
            door_open=random.choice(goat_doors)
        ch=input("Do You Want To Swap? (y/n) ")
        if ch=="y":
            if doors[choice]=="Goat":
                print("Player Wins")
                swap=swap+1
            else:
                print("Player Lost")
                no_swap=no_swap+1
        else:
            if doors[choice]=="Goat":
                print("Player Lost")
                no_swap=no_swap+1
            else:
                print("Player Lost")
                swap=swap+1
        
        a=int((swap/(swap+no_swap))*100)
        b=(no_swap/(swap+no_swap))*100
        
        print("Percentage Of Wins when Swapped = ",a)
        print("Percentage Of Wins when not Swapped = ",b) 
        end=input("Do You Want To Continue Playing? (y/n)")
        if end=="y":
            stop=False
        else:
            stop=True
        continue
    
        