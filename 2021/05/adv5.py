input_data = "C:\\Users\\paul\\advent2021\\5\\input.txt"


class map:
    def __init__(self, data):
        self.map = []

    def check_if_won(self):
        # 5 x 5 grid
        
        won = False
        for i in range(5):
            if self.board_data[i][1] and self.board_data[i+5][1] and self.board_data[i+10][1] and self.board_data[i+15][1] and self.board_data[i+20][1]:
                won = True
            if self.board_data[5*i][1] and self.board_data[5*i+1][1] and self.board_data[5*i+2][1] and self.board_data[5*i+3][1] and self.board_data[5*i+4][1]:
                won = True
        self.won = won       
        return self.won

    def got_number(self, number):
        self.board_data = [(number, True) if x[0]==number else x for x in self.board_data]

    def get_score(self):
        score = 0
        for i in self.board_data:
            if not i[1]: score = score + int(i[0])
        return score
            

def get_input_data():
    with open(input_data) as f:
        data = f.readlines()
    return data

def parse_data(data):
    parsed_data = []
    for i in data:
        first, second = i.split(' -> ')
        x, y = first.split(',')
        x2, y2 = second.split(',')
        parsed_data.append(((int(x),int(y)),(int(x2),int(y2))))
    return parsed_data


def straight_line(line):
    return (line[0][0] == line[1][0]) or (line[0][1] == line[1][1])

def line_points(line):
    if line[0][0] == line[1][0] and line[0][1] <= line[1][1]:
        points = [(line[0][0],x) for x in range(line[0][1],line[1][1]+1)]
    elif line[0][0] == line[1][0] and line[0][1] > line[1][1]:
        points = [(line[0][0],x) for x in range(line[0][1],line[1][1]-1,-1)]
    elif line[0][1] == line[1][1] and line[0][0] <= line[1][0]:
        points = [(x, line[0][1]) for x in range(line[0][0],line[1][0]+1)]
    elif line[0][1] == line[1][1] and line[0][0] > line[1][0]:
        points = [(x, line[0][1]) for x in range(line[0][0],line[1][0]-1,-1)]
    return points

def line_points_with_diag(line):
    if line[0][0] == line[1][0] and line[0][1] <= line[1][1]:
        points = [(line[0][0],x) for x in range(line[0][1],line[1][1]+1)]
    elif line[0][0] == line[1][0] and line[0][1] > line[1][1]:
        points = [(line[0][0],x) for x in range(line[0][1],line[1][1]-1,-1)]
    elif line[0][1] == line[1][1] and line[0][0] <= line[1][0]:
        points = [(x, line[0][1]) for x in range(line[0][0],line[1][0]+1)]
    elif line[0][1] == line[1][1] and line[0][0] > line[1][0]:
        points = [(x, line[0][1]) for x in range(line[0][0],line[1][0]-1,-1)]
    else:
        points = []
        if line[0][0] < line[1][0]:
            x = [i for i in range(line[0][0], line[1][0]+1)]
        else:
            x = [i for i in range(line[0][0], line[1][0]-1, -1)]
        if line[0][1] < line[1][1]:
            y = [i for i in range(line[0][1], line[1][1]+1)]
        else:
            y = [i for i in range(line[0][1], line[1][1]-1, -1)]
        print(line, x, y)
        for count, i in enumerate(x):
            points.append((x[count], y[count]))
    return points

def points_to_dim(dimension, points):
    return points[0]+(points[1]*dimension)

test_data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

if __name__ == "__main__":
    dimension = 10
    # initialise list
    seabed = []
    for i in range(dimension * dimension): seabed.append(0)

    test_coords = parse_data(test_data.split('\n'))

    for line in test_coords:
        if straight_line(line):
            points = line_points(line)
            for point in points:
                dim = points_to_dim(dimension, point)
                seabed[dim] += 1
    
    for count, i in enumerate(seabed):
        if (count % dimension == 0): print()
        print("{} ".format(i), end='')

    overlapping = 0
    for i in seabed:
        if i > 1: overlapping += 1
    print("Overlapping: {}".format(overlapping))

    dimension = 1000
    # initialise list
    seabed = []
    for i in range(dimension * dimension): seabed.append(0)

    test_coords = parse_data(get_input_data())

    for line in test_coords:
        if straight_line(line):
            points = line_points(line)
            for point in points:
                dim = points_to_dim(dimension, point)
                seabed[dim] += 1
    
    overlapping = 0
    for i in seabed:
        if i > 1: overlapping += 1
    print("Overlapping: {}".format(overlapping))

    dimension = 10
    # initialise list
    seabed = []
    for i in range(dimension * dimension): seabed.append(0)

    test_coords = parse_data(test_data.split('\n'))

    for line in test_coords:
        points = line_points_with_diag(line)
        for point in points:
            dim = points_to_dim(dimension, point)
            seabed[dim] += 1
    
    for count, i in enumerate(seabed):
        if (count % dimension == 0): print()
        print("{} ".format(i), end='')

    overlapping = 0
    for i in seabed:
        if i > 1: overlapping += 1
    print("Overlapping: {}".format(overlapping))

    dimension = 1000
    # initialise list
    seabed = []
    for i in range(dimension * dimension): seabed.append(0)

    test_coords = parse_data(get_input_data())

    for line in test_coords:
        points = line_points_with_diag(line)
        for point in points:
            dim = points_to_dim(dimension, point)
            seabed[dim] += 1
    
    overlapping = 0
    for i in seabed:
        if i > 1: overlapping += 1
    print("Overlapping: {}".format(overlapping))
