# -*- coding: utf-8 -*-


def get_gamma_rate(data):
    list_length = len(data)
    counts = dict()
    word_length = len(data[0])
    for i in data:
        for pos in range(word_length):
            if i[pos] == '1': counts[pos] = counts.get(pos, 0) + 1
    result = ''
    gamma_func = lambda x, y: 1 if x >= y / 2 else 0
    for pos in range(word_length): result = result + str(gamma_func(counts[pos], list_length))
    return int(result, 2)

def read_data(source = "input.txt"):
    with open(source) as f:
        data = f.readlines()
    # clean whitespace out
    clean_data = []
    for i in data:
        clean_data.append(i.strip())
    return clean_data    

def get_epsilon_from_gamma(word_length, gamma):
    return (2 ** word_length -1) - gamma

def get_power_consumption(gamma, epsilon):
    return gamma * epsilon

def oxygen_generator_rating(position, data):
    if len(data) > 1:
        sum0 = 0
        sum1 = 0
        for i in data:
            if i[position] == '0': sum0 += 1
            else: sum1 += 1
        if sum1 >= sum0:
            reduced_data = [ x for x in data if x[position] == '1' ]
        else:
            reduced_data = [ x for x in data if x[position] == '0' ]
        data = oxygen_generator_rating(position + 1, reduced_data)
    return data

def co2_scrubber_rating(position, data):
    print(position, data)
    if len(data) > 1:
        sum0 = 0
        sum1 = 0
        for i in data:
            print(i)
            if i[position] == '0': sum0 += 1
            else: sum1 += 1
        print(sum0, sum1)
        if sum0 <= sum1:
            reduced_data = [ x for x in data if x[position] == '0' ]
        else:
            reduced_data = [ x for x in data if x[position] == '1' ]
        data = co2_scrubber_rating(position + 1, reduced_data)
    return data    



if __name__ == "__main__":
    test_data = ['00100','11110','10110','10111','10101','01111','00111','11100',
                 '10000','11001','00010','01010']

    word_length = len(test_data[0])
    gamma_rate = get_gamma_rate(test_data)
    epsilon_rate = get_epsilon_from_gamma(word_length, gamma_rate)
    print(gamma_rate, epsilon_rate, get_power_consumption(gamma_rate, epsilon_rate))

    d = read_data()
    word_length = len(d[0])
    gamma_rate = get_gamma_rate(d)
    epsilon_rate = get_epsilon_from_gamma(word_length, gamma_rate)
    print(gamma_rate, epsilon_rate, get_power_consumption(gamma_rate, epsilon_rate))
    
    oxy = oxygen_generator_rating(0, test_data)[0]
    co2 = co2_scrubber_rating(0, test_data)[0]
    life_support = int(oxy, 2) * int(co2, 2)
    print(life_support)
    
    oxy = oxygen_generator_rating(0, d)[0]
    co2 = co2_scrubber_rating(0, d)[0]
    life_support = int(oxy, 2) * int(co2, 2)
    print(life_support)
    