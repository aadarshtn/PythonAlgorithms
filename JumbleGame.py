# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 01:02:39 2019

@author: ADARSH
"""
import random

def choose():
    random_words=["rainbow","cricket","random","india","boat","Mountain","Vehicle","Football"]
    pick=random.choice(random_words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(pn1,pn2,pp1,pp2):
    print(pn1,"Your Score is : ",pp1)
    print(pn2,"Your Score is : ",pp2)
    print("Thank You For Playing , See You Again")
def play():
    pn1=input("Player 1 , Please Enter your name : ")
    pn2=input("Player 2 , Please Enter your name : ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computers task
        picked_word=choose()
        #question
        qn=jumble(picked_word)
        print(qn)
        #player1
        if turn%2==0:
            print(pn1,"Its Your Turn : ")
            answer = input("What is on my mind?... : ")
            if answer == picked_word:
                pp1=pp1+10
                print("Your Score is : ",pp1)
            else:
                print("Sorry Thats not what I thought... :( I thought : ",picked_word)

            c=input("Press 1 to continue or 0 to quit")
            if c==0:
                thank(pn1,pn2,pp1,pp2)
                break
        #player2
        else:
            print(pn2,"Its Your Turn : ")
            answer = input("What is on my mind?... : ")
            if answer == picked_word:
                pp2=pp2+10
                print("Your Score is : ",pp2)
            else:
                print("Sorry Thats not what I thought... :( I thought : ",picked_word)
                
            c=input("Press 1 to continue or 0 to quit")
            if c==0:
                thank(pn1,pn2,pp1,pp2)
                break
        turn=turn+1
        
play()