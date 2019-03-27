# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 06:57:48 2019

@author: ADARSH
"""

import string
dict={}
data=""
file=open("op_file.txt","r+")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-2]
with open("ip_file.txt") as t:
    while True:
        m=t.read(1)
        if not m:
            print("End Of File")
            break
        if m in dict:
            data=dict[m]
        else:
            data=m
        file.write(data)
        print(data)
file.close()
