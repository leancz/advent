# -*- coding: utf-8 -*-


eof = False
first = True
total = 0
prev = 9999999999 # horrible
with open("j:\\advent2021\\1\\input.txt") as f:
    while not eof:
        data = f.readline()
        if not data: eof = True
        else:
            if first:
                first = False
            else:
                if int(data) > prev:
                    total = total + 1
            prev = int(data)
print(total)
    