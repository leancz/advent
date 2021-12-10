# -*- coding: utf-8 -*-


def get_data():
    with open("input.txt") as f:
        string_data = f.readline().split(',')
        data = [int(x) for x in string_data]
        return data
    
#def alloc(size):
#    mem = []
#    for i in range(size):
#        mem.append(0)
#    return mem
instruction_pointer = 0
program = []

def add():
    global instruction_pointer, program
    first = program[instruction_pointer + 1]
    second = program[instruction_pointer + 2]
    third = program[instruction_pointer + 3]
#    print("{} Executing add {} {} {}".format(program, first, second, third), end="")
    program[third] = program[first] + program[second]
#    print(" {}".format(program))
    instruction_pointer += 4

def multiply():
    global instruction_pointer, program
    first = program[instruction_pointer + 1]
    second = program[instruction_pointer + 2]
    third = program[instruction_pointer + 3]
#    print("{} Executing mul {} {} {}".format(program, first, second, third), end="")
    program[third] = program[first] * program[second]
#    print(" {}".format(program))
    instruction_pointer += 4
    

opcodes = {1: add,
           2: multiply,}

def run():
    global instruction_pointer, program
    instruction_pointer = 0
    current_instruction = program[instruction_pointer]
    while(current_instruction != 99):
        opcodes[current_instruction]()
        current_instruction = program[instruction_pointer]
        
    print("END")
    return program
    

if __name__ == "__main__":
    program = [1,9,10,3,2,3,11,0,99,30,40,50]; assert run() == [3500,9,10,70,2,3,11,0,99,30,40,50]
    program = [1,0,0,0,99]; assert run() == [2,0,0,0,99]    
    program = [2,3,0,3,99]; assert run() == [2,3,0,6,99]
    program = [2,4,4,5,99,0]; assert run() == [2,4,4,5,99,9801]
    program = [1,1,1,4,99,5,6,0,99]; assert run() == [30,1,1,4,2,5,6,0,99]
    
    program = get_data()
    
    # fix
    program[1] = 12
    program[2] = 2
    program = run()
    print(program[0])
    
    # part two
    
    output = 0
    noun = 0
    verb = 0
    while True:
        program = get_data()
        program[1] = noun
        program[2] = verb
        run()
        output = program[0]
        if output == 19690720:
            print("Output {} from noun {} verb {}".format(output, noun, verb))
            break
        noun +=1
        if noun == 100:
            noun = 0
            verb += 1
            print("Verb", verb)
            if verb == 100:
                print("ERROR - verb is 100")
                break
            
    
#    for i in test_masses:
#        print(i, get_fuel_req(i))
#    
#    fuel_sum = 0
#    prod_masses = get_data()
#    for i in prod_masses:
#        fuel_sum += get_fuel_req(int(i))
#    print(fuel_sum)
#    
#    for i in test_masses:
#        initial_fuel = get_fuel_req(i)
#        extra_fuel = get_fuel_mass_req(initial_fuel)
#        print("Required fuel for {} mass: {} + {} == {}".format(i, initial_fuel, extra_fuel, initial_fuel + extra_fuel))
#        
#    fuel_sum = 0
#    prod_masses = get_data()
#    for i in prod_masses:
#        initial_fuel = get_fuel_req(int(i))
#        extra_fuel = get_fuel_mass_req(initial_fuel)
#        fuel_sum += initial_fuel + extra_fuel
#    print(fuel_sum)
    