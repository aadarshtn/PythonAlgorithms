# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:46:47 2019

@author: ADARSH
"""

with open("Hitler.txt","r+") as ruler:
    print(ruler.read())
    ruler.write("He tried to conquer the world under Germany")
ruler.close()
    