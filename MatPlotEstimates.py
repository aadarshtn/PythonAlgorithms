# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 23:38:44 2019

@author: ADARSH
"""

import matplotlib.pyplot as graphs
import statistics
estimates=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
y=[]
estimates.sort()
tv=int(0.1*len(estimates))
estimates=estimates[tv:len(estimates)-tv]
for i in range(len(estimates)):
    y.append(1)
m=int(statistics.mean(estimates))
print(m)
graphs.plot(estimates,y,'ro')
graphs.plot(statistics.mean(estimates),1,'g^')
graphs.plot(23,1,'bo')