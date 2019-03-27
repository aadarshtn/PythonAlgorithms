# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:00:45 2019

@author: ADARSH
"""

player_1={0:"Rock",1:"Paper",2:"Scissor"}
player_2={1:"Rock",0:"Scissor",2:"Paper"}

def rock_paper_scissor(num1,num2,bit1,bit2):
    pp1=0
    pp2=0
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if player_1[p1]==player_2[p2]:
        print("Game Drawn")
    elif player_1[p1]=="Rock" and player_2[p2]=="Scissor":
        print("Player One , You Won")
        pp1=pp1+1
    elif player_1[p1]=="Rock" and player_2[p2]=="Paper":
        print("Player Two , You Won")
        pp2=pp2+1
    elif player_1[p1]=="Paper" and player_2[p2]=="Scissor":
        print("Player Two , You Won")
        pp2=pp2+1
    elif player_1[p1]=="Paper" and player_2[p2]=="Rock":
        print("Player One , You Won")
        pp1=pp1+1
    elif player_1[p1]=="Scissor" and player_2[p2]=="Paper":
        print("Player One , You Won")
        pp1=pp1+1
    elif player_1[p1]=="Scissor" and player_2[p2]=="Rock":
        print("Player Two , You Won")
        pp2=pp2+1
    print(pp1,pp2)
while(1):
    num1=input("Player one, Enter your choice")
    num2=input("Player two, Enter your choice")
    bit1=int(input("Player one, Enter your secret bit position: "))
    bit2=int(input("Player two, Enter your secret bit position: "))
    
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("Do you want to continue? y/n :")
    if(ch=="n"):
        break
    

    
    