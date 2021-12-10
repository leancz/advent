# -*- coding: utf-8 -*-


def get_data():
    with open("input.txt") as f:
        string_data = f.readlines()
    return string_data

def parse_data(string_data):
        string_data1 = string_data[0].split(',')
        string_data2 = string_data[1].split(',')
        data1 = [x for x in string_data1]
        data2 = [x for x in string_data2]
        return data1, data2

def get_coords(pos, instruction):
    coords=[]
    direction = instruction[0]
    distance = int(instruction[1:])
    if direction == 'U':
        for i in range(1, distance+1):
            coords.append((pos[0],pos[1]+i))
    if direction == 'D':
        for i in range(1, distance+1):
            coords.append((pos[0],pos[1]-i))
    if direction == 'R':
        for i in range(1, distance+1):
            coords.append((pos[0]+i,pos[1]))
    if direction == 'L':
        for i in range(1, distance+1):
            coords.append((pos[0]-i,pos[1]))
    return coords

def get_line(wire_commands):
    line=[]
    pos = (0,0)
    for command in wire_commands:
        new_coordinates = get_coords(pos, command)
#        print(command, new_coordinates)
        line = line + new_coordinates
        pos = new_coordinates[-1]
    return line

def get_intersections(line1, line2):
    set1 = set(line1)
    set2 = set(line2)
    return set1.intersection(set2)

def get_manhatten_distances(values):
    return [abs(x[0])+abs(x[1]) for x in values]

def get_lowest_intersection_distance(w1, w2):
    line1 = get_line(w1)
    line2 = get_line(w2)
    intersections = get_intersections(line1, line2)
    distances = get_manhatten_distances(intersections)
    return (min(distances))

def get_steps_to_intersections(line1, line2, intersections):
    steps = []
    for intersection in intersections:
        steps1 = line1.index(intersection) + 1 # as we don't have (0,0) in the list
        steps2 = line2.index(intersection) + 1
        steps.append(steps1+steps2)
    return steps
        
    
def get_lowest_steps_to_intersection(w1, w2):
    line1 = get_line(w1)
    line2 = get_line(w2)
    intersections = get_intersections(line1, line2)
    steps = get_steps_to_intersections(line1, line2, intersections)
    return (min(steps))

if __name__ == "__main__":
    wire1_commands, wire2_commands = parse_data(['R8,U5,L5,D3','U7,R6,D4,L4'])
    lowest_distance = get_lowest_intersection_distance(wire1_commands, wire2_commands)
    print("Lowest distance = {}".format(lowest_distance))
    
    wire1_commands, wire2_commands = parse_data(['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83'])
    lowest_distance = get_lowest_intersection_distance(wire1_commands, wire2_commands)
    print("Lowest distance = {}".format(lowest_distance))
    
    wire1_commands, wire2_commands = parse_data(['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'])
    lowest_distance = get_lowest_intersection_distance(wire1_commands, wire2_commands)
    print("Lowest distance = {}".format(lowest_distance))
    
    wire1_commands, wire2_commands = parse_data(get_data())
    lowest_distance = get_lowest_intersection_distance(wire1_commands, wire2_commands)
    print("Lowest distance = {}".format(lowest_distance))
    
    wire1_commands, wire2_commands = parse_data(['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83'])
    lowest_steps = get_lowest_steps_to_intersection(wire1_commands, wire2_commands)
    print("Lowest steps = {}".format(lowest_steps))    

    wire1_commands, wire2_commands = parse_data(['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'])
    lowest_steps = get_lowest_steps_to_intersection(wire1_commands, wire2_commands)
    print("Lowest steps = {}".format(lowest_steps))    
    
    wire1_commands, wire2_commands = parse_data(get_data())
    lowest_steps = get_lowest_steps_to_intersection(wire1_commands, wire2_commands)
    print("Lowest steps = {}".format(lowest_steps))    
        