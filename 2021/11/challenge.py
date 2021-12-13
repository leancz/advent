# -*- coding: utf-8 -*-

def format(data):
    new_data = []
    new_row = []
    for row in data:
        new_row = [int(x) for x in row]
        new_data.append(new_row)
    return new_data

def increment_all(data):
    dimension = len(data)
    for y in range(dimension):
        for x in range(dimension):
            data[x][y] += 1

def can_flash(data):
    can = False
    for y in data:
        for x in y:
            if x > 9: can = True
    return can

def count_flashed(data):
    sum = 0
    for y in data:
        for x in y:
            if x == 0: sum += 1
    return sum

def get_neighbours(dimension, x, y):
    neighbours = []
    if x > 0:
        if y > 0:
            neighbours.append((x-1, y-1))
        neighbours.append((x-1, y))
        if y < dimension -1:
            neighbours.append((x-1, y+1))

    if x < dimension - 1:
        if y > 0:
            neighbours.append((x+1, y-1))
        neighbours.append((x+1, y))
        if y < dimension - 1:
            neighbours.append((x+1, y+1))

    if y > 0: neighbours.append((x, y-1))
    if y < dimension - 1: neighbours.append((x, y+1))
    return neighbours

def perform_flashes(data):
    dimension = len(data)
    flashes = 0
    while can_flash(data):
        for y in range(dimension):
            for x in range(dimension):
                if data[x][y] > 9:
                    flashes += 1
                    neighbours = get_neighbours(dimension, x, y)
                    for neighbour in neighbours:
                        data[neighbour[0]][neighbour[1]] += 1
                    data[x][y] = -99999
        
    for y in range(dimension):
        for x in range(dimension):
            if data[x][y] < 0: data[x][y] = 0
    return flashes


if __name__ == "__main__":
    test1_data = ['11111', '19991', '19191', '19991', '11111']
    test2_data = ['5483143223', '2745854711', '5264556173', '6141336146',
                  '6357385478', '4167524645', '2176841721', '6882881134',
                  '4846848554', '5283751526',]

    prod_data = ['8271653836', '7567626775', '2315713316', '6542655315',
                 '2453637333', '1247264328', '2325146614', '2115843171',
                 '6182376282', '2384738675',]


    dimension = len(test1_data)
    test1_data = format(test1_data)
    increment_all(test1_data)
    print(test1_data)
    print(perform_flashes(test1_data))

    score = 0
    test2_data = format(test2_data)
    for i in range(100):
        increment_all(test2_data)
        score = score + perform_flashes(test2_data)
    print("Total score: {}".format(score))

    score = 0
    prod_data = format(prod_data)
    for i in range(100):
        increment_all(prod_data)
        score = score + perform_flashes(prod_data)
    print("Total score: {}".format(score))

    test2_data = ['5483143223', '2745854711', '5264556173', '6141336146',
                  '6357385478', '4167524645', '2176841721', '6882881134',
                  '4846848554', '5283751526',]
    test2_data = format(test2_data)
    i = 1
    while True:
        increment_all(test2_data)
        _ = perform_flashes(test2_data)
        cf = count_flashed(test2_data)
        print(i, cf, test2_data)
        if cf == len(test2_data) * len(test2_data):
            print("Step {} syncronised flashing".format(i))
            break
        i += 1



    prod_data = ['8271653836', '7567626775', '2315713316', '6542655315',
                 '2453637333', '1247264328', '2325146614', '2115843171',
                 '6182376282', '2384738675',]
    prod_data = format(prod_data)
    i = 1
    while True:
        increment_all(prod_data)
        _ = perform_flashes(prod_data)
        cf = count_flashed(prod_data)
        print(i, cf, prod_data)
        if cf == len(prod_data) * len(prod_data):
            print("Step {} syncronised flashing".format(i))
            break
        i += 1
