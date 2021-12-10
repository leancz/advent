# -*- coding: utf-8 -*-

def read_data(source = "input.txt"):
    with open(source) as f:
        data = f.readlines()
    return data

def format_data(data):
    int_data = []
    for i in data:
        int_data.append([int(x) for x in i.strip('\n')])
    return int_data 


def low_point(data, x, y):
    x_dim = len(data[0]) - 1
    y_dim = len(data) - 1
#    print(x, y, x_dim, y_dim)
    neighbours = []
    
#    if x < x_dim:
#        if data[y][x+1] < data[y][x]:
#            lower_neighbour = True
#    if x > 0:
#        if data[y][x-1] < data[y][x]:
#            lower_neighbour = True
#    if y < y_dim:
#        if data[y+1][x] < data[y][x]:
#            lower_neighbour = True
#    if y > 0:
#        if data[y-1][x] < data[y][x]:
#            lower_neighbour = True
    if x < x_dim:
        neighbours.append(data[y][x+1])
    if x > 0:
        neighbours.append(data[y][x-1])
    if y < y_dim:
        neighbours.append(data[y+1][x])
    if y > 0:
        neighbours.append(data[y-1][x])
    
    return data[y][x] < min(neighbours)

def get_neighbours(data, x, y):
    x_dim = len(data[0]) - 1
    y_dim = len(data) - 1
#    print(x, y, x_dim, y_dim)
    neighbours = []
    if x < x_dim:
        neighbours.append((x+1, y))
    if x > 0:
        neighbours.append((x-1, y))
    if y < y_dim:
        neighbours.append((x, y+1))
    if y > 0:
        neighbours.append((x, y-1))
    
    return neighbours


def get_risk_level_sum(data):
    x_dim = len(data[0]) 
    y_dim = len(data) 
    sum = 0
    for x in range(x_dim):
        for y in range(y_dim):
            if low_point(data, x, y):
                print(x, y, data[y][x])
                sum = sum + data[y][x] + 1
    return sum    

def get_low_points(data):
    x_dim = len(data[0]) 
    y_dim = len(data) 
    low_points = []
    for x in range(x_dim):
        for y in range(y_dim):
            if low_point(data, x, y):
                low_points.append((x,y))
    return low_points    

def get_not_9_neighbours(data, start):
    result = []
    x, y = start
    neighbours = get_neighbours(data, x, y)
    for neighbour in neighbours:
        nx, ny = neighbour
        if data[ny][nx] < 9: result.append((nx, ny))
    return result

def get_basin_size(data, point):
    count = 1
    visited = [point,]
    new = get_not_9_neighbours(data, point)
    while len(new) > 0:
        i = new.pop()
        if i in visited: continue
        visited.append(i)
        count += 1
        new = new + get_not_9_neighbours(data, i)
    return count

def get_all_basin_sizes(data):
    sizes = []
    low_points = get_low_points(data)
    for point in low_points:
        sizes.append(get_basin_size(data, point))    
    return sizes

if __name__ == "__main__":
    test_data = ['2199943210','3987894921','9856789892','8767896789','9899965678']
    int_data = format_data(test_data)
    print(get_risk_level_sum(int_data))
    
    int_data = format_data(read_data())
    print(get_risk_level_sum(int_data))
    
    test_data = ['2199943210','3987894921','9856789892','8767896789','9899965678']
    int_data = format_data(test_data)
    sizes = get_all_basin_sizes(int_data)
    print(sizes)
    sizes.sort()
    print(sizes)
    product = 1
    for i in sizes[-3:]:
        product = product * i
    print(product)

    int_data = format_data(read_data())
    sizes = get_all_basin_sizes(int_data)
    print(sizes)
    sizes.sort()
    print(sizes)
    product = 1
    for i in sizes[-3:]:
        product = product * i
    print(product)
