# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:22:57 2021

@author: bainesp
"""


with open("j:\\advent2021\\1\\input.txt") as f:
    data = f.readlines()
total = 0    
windows = [ (int(data[i]),int(data[i+1]),int(data[i+2])) for i in range(len(data[2:]))]
for i in range(len(windows)-1):
    if sum(windows[i+1]) > sum(windows[i]): total = total + 1
print(total)
