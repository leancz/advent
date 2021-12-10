# -*- coding: utf-8 -*-



with open("input.txt") as f:
    data = f.readlines()
horizontal = 0
depth = 0
for i in data:
    instruction, value = i.split()
    if instruction == "forward": horizontal = horizontal + int(value)
    if instruction == "down": depth = depth + int(value)
    if instruction == "up": depth = depth - int(value)
print(horizontal, depth, horizontal * depth)
