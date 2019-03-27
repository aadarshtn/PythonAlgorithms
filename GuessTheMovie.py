# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:11:47 2019

@author: ADARSH
"""
import random

movies = ["CAPTAIN MARVEL","BOHEMIAN RAPHSODY","GREEN BOOK","A STAR IS BORN","AVENGERS ENDGAME","AQUAMAN","US","HELLBOY","OVERLORD","AFTER","CREED 2","BLACK PANTHER","ROBINHOOD","DEADPOOL 2"]

def create_qn(movie):
    lom=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(lom):
        if letters[i]==" ":
            temp.append(" ")
        else:
            temp.append("*")
    qn="".join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    lom=len(movie)
    for i in range(lom):
        if ref[i]==" " or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qn_list[i]=="*":
                temp.append("*")
            else:
                temp.append(ref[i])
    qn_new="".join(str(x) for x in temp)
    return qn_new   
    
    

def play():
    p1name=input("Player1!... Enter your name...")
    p2name=input("Player2!... Enter your name...")
    p1points=0
    p2points=0
    turn=0
    willing=True
    while willing:
        if (turn%2==0):
            print(p1name+" It is your turn")
            picked_movie=random.choice(movies)
            qn=create_qn(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Enter your choice of probable letter : ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to guess the movie or 2 to unlock another letter"))
                    if d==1:
                        ans=input("Enter the movie name: ")
                        if ans==picked_movie:
                            p1points=p1points+1
                            print("You are Spot On!!")
                            not_said=False
                            print(p1name," Your score is: ",p1points)
                        else:
                            print("Sorry thats the wrong answer , Please continue unlocking")
                            
                else:
                    print(letter+" Not found")
            c=int(input("Press 1 to continue or 0 to Quit"))
            if c==0:
                print(p1name," Your score: ",p1points)
                print(p2name," Your score: ",p2points)
                print("Thank You Playing ... Have a nice day!!!")
                willing=False
                
        else:
            print(p2name+" It is your turn")
            picked_movie=random.choice(movies)
            qn=create_qn(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Enter your choice of probable letter : ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to guess the movie or 2 to unlock another letter"))
                    if d==1:
                        ans=input("Enter the movie name: ")
                        if ans==picked_movie:
                            p2points=p2points+1
                            print("You are Spot On!!")
                            not_said=False
                            print(p2name," Your score is: ",p2points)
                        else:
                            print("Sorry thats the wrong answer , Please continue unlocking")
                            
                else:
                    print(letter+" Not found")
            c=int(input("Press 1 to continue or 0 to Quit"))
            if c==0:
                print(p1name," Your score: ",p1points)
                print(p2name," Your score: ",p2points)
                print("Thank You Playing ... Have a nice day!!!")
                willing=False
            
        turn=turn=1 
play()