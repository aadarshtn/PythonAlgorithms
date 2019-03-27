# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:15:38 2019

@author: ADARSH
"""
import string
import random

letters = []

letters = list(string.ascii_letters)

card1=[0]*5
card2=[0]*5

pos1 = random.randint(0,4)
pos2 = random.randint(0,4)

samesymbol=random.choice(letters)
letters.remove(samesymbol)
if(pos1==pos2):
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    
    card1[pos2]=random.choice(letters)
    letters.remove(card1[pos2])
    card2[pos1]=random.choice(letters)
    letters.remove(card2[pos1])
 
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        alphabet1=random.choice(letters)
        letters.remove(alphabet1)
        card1[i]=alphabet1
        alphabet2=random.choice(letters)
        letters.remove(alphabet2)
        card2[i]=alphabet2
    i+=1
print (card1)
print (card2)

entry=input("The common element is :")
if (entry==samesymbol):
    print("You are correct")
else:
    print("You are wrong")

        

    
    
    
    
