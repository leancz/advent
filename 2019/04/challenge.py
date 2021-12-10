# -*- coding: utf-8 -*-


def is_six_digits(n):
    return 99999 < n < 1000000

def two_adjacent_digits_match(n):
    return ((int(n / 100000) % 10 == int (n / 10000) % 10) and (int(n / 10000) % 10 != int (n / 1000) % 10)) or \
    ((int(n / 100000) % 10 != int (n / 10000) % 10) and (int(n / 10000) % 10 == int (n / 1000) % 10) and (int(n / 1000) % 10 != int (n / 100) % 10)) or \
    ((int(n / 10000) % 10 != int (n / 1000) % 10) and (int(n / 1000) % 10 == int (n / 100) % 10) and (int(n / 100) % 10 != int (n / 10) % 10)) or \
    ((int(n / 1000) % 10 != int (n / 100) % 10) and (int(n / 100) % 10 == int (n / 10) % 10) and (int(n / 10) % 10 != int (n / 1) % 10)) or \
    ((int(n / 100) % 10 != int (n / 10) % 10) and (int(n / 10) % 10 == int (n / 1) % 10))

def never_decreasing_digits(n):
    return (int(n / 100000) % 10 <= int (n / 10000) % 10) and \
    (int(n / 10000) % 10 <= int (n / 1000) % 10) and \
    (int(n / 1000) % 10 <= int (n / 100) % 10) and \
    (int(n / 100) % 10 <= int (n / 10) % 10) and \
    (int(n / 10) % 10 <= int (n / 1) % 10)  
    
if __name__ == "__main__":
    candidates = [122345, 111123, 135679, 111111, 223450, 123789]

    for candidate in candidates:
        print(is_six_digits(candidate))
        print("{} Has two adjacent digits matching {}".format(candidate, two_adjacent_digits_match(candidate)))
        print("{} Never decreasing digits {}".format(candidate, never_decreasing_digits(candidate)))
        
        sum = 0
        for i in range(125730, 579381+1):
            if is_six_digits(i) and two_adjacent_digits_match(i) and never_decreasing_digits(i):
                print(i)
                sum += 1
        print("sum: {}".format(sum))