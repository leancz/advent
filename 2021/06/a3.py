# -*- coding: utf-8 -*-


def get_state(data):
    state = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for i in data:
        state[i] = state.get(i, 0) + 1
    return state

def process(state):
    new_state = {}
    for i in range(1,9):
        new_state[i-1] = state[i]
    new_state[6] = new_state[6] + state[0]
    new_state[8] = state[0]
    return new_state

def get_total(state):
    total = 0
    for i in state.keys():
        total = total + state[i]
    return total
    
if __name__ == "__main__":
    test_state = [3,4,3,1,2]
    prod_state = [4,2,4,1,5,1,2,2,4,1,1,2,2,2,4,4,1,2,1,1,4,1,2,1,2,2,2,2,5,2,2,3,1,4,4,4,1,2,3,4,4,5,4,3,5,1,2,5,1,1,5,5,1,4,4,5,1,3,1,4,5,5,5,4,1,2,3,4,2,1,2,1,2,2,1,5,5,1,1,1,1,5,2,2,2,4,2,4,2,4,2,1,2,1,2,4,2,4,1,3,5,5,2,4,4,2,2,2,2,3,3,2,1,1,1,1,4,3,2,5,4,3,5,3,1,5,5,2,4,1,1,2,1,3,5,1,5,3,1,3,1,4,5,1,1,3,2,1,1,1,5,2,1,2,4,2,3,3,2,3,5,1,5,1,2,1,5,2,4,1,2,4,4,1,5,1,1,5,2,2,5,5,3,1,2,2,1,1,4,1,5,4,5,5,2,2,1,1,2,5,4,3,2,2,5,4,2,5,4,4,2,3,1,1,1,5,5,4,5,3,2,5,3,4,5,1,4,1,1,3,4,4,1,1,5,1,4,1,2,1,4,1,1,3,1,5,2,5,1,5,2,5,2,5,4,1,1,4,4,2,3,1,5,2,5,1,5,2,1,1,1,2,1,1,1,4,4,5,4,4,1,4,2,2,2,5,3,2,4,4,5,5,1,1,1,1,3,1,2,1]


    state = get_state(test_state)
    print("Initial state: {}".format(state))
    for days in range(1,81):
        state = process(state)
        # print("After {} days: {}".format(days, test_state))
        print("After {} days: {} fish".format(days, get_total(state)))
        
    state = get_state(prod_state)
    print("Initial state: {}".format(state))
    for days in range(1,81):
        state = process(state)
        # print("After {} days: {}".format(days, test_state))
        print("After {} days: {} fish".format(days, get_total(state)))

    state = get_state(test_state)
    print("Initial state: {}".format(state))
    for days in range(1,257):
        state = process(state)
        # print("After {} days: {}".format(days, test_state))
        print("After {} days: {} fish".format(days, get_total(state)))
        
    state = get_state(prod_state)
    print("Initial state: {}".format(state))
    for days in range(1,257):
        state = process(state)
        # print("After {} days: {}".format(days, test_state))
        print("After {} days: {} fish".format(days, get_total(state)))
