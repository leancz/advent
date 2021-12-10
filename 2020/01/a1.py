# -*- coding: utf-8 -*-



   
def pairs_sum_to_2020(data):
    result = []
    pairs = [(i, j) for i in data for j in data]
    for pair in pairs:
        if sum(pair) == 2020:
            result.append(pair)
    return result

def triplets_sum_to_2020(data):
    result = []
    triplets = [(i, j, k) for i in data for j in data for k in data]
    for triplet in triplets:
        if sum(triplet) == 2020:
            result.append(triplet)
    return result

def test_it():
    test_list = [1721, 979, 366, 299, 675, 1456]
    pairs = pairs_sum_to_2020(test_list)
    triplets = triplets_sum_to_2020(test_list)
    for pair in pairs:
        print(pair, pair[0] * pair[1])
    for triplet in triplets:
        print(triplet, triplet[0] * triplet[1] * triplet[2])

def run_it():
    integer_data = []
    with open("input.txt") as f:
        data = f.readlines()
        for i in data: integer_data.append(int(i))
    pairs = pairs_sum_to_2020(integer_data)
    triplets = triplets_sum_to_2020(integer_data)
    for pair in pairs:
        print(pair, pair[0] * pair[1])
    for triplet in triplets:
        print(triplet, triplet[0] * triplet[1] * triplet[2])


test_it()
run_it()