# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:22:57 2021

@author: bainesp
"""


with open("input.txt") as f:
    data = f.readlines()
# test data = ['forward 5\n', 'down 5\n', 'forward 8\n', 'up 3\n', 'down 8\n', 'forward 2\n']
horizontal = 0
depth = 0
aim = 0
for i in data:
    instruction, value = i.split()
    if instruction == "forward":
        horizontal = horizontal + int(value)
        depth = depth + aim * int(value)
    if instruction == "down": aim = aim + int(value)
    if instruction == "up": aim = aim - int(value)
    print(i, horizontal, depth, aim)
print(horizontal, depth, horizontal * depth)
