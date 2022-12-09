def read_data(source = "input_day9.txt"):
    with open(source) as f:
        data = f.read()
    return data 

def format_data(d):
    return d.split('\n')
    
        
def do_it():
    visited = set()
    knots = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),]
    visited.add(knots[9])
    for i in moves:
        direction, number = i.split(' ')
#        print(direction, number)
        for j in range(int(number)):
            old_xy = knots[0]
            if direction == 'R': knots[0] = (knots[0][0]+1, knots[0][1])
            if direction == 'L': knots[0] = (knots[0][0]-1, knots[0][1])
            if direction == 'U': knots[0] = (knots[0][0], knots[0][1]+1)
            if direction == 'D': knots[0] = (knots[0][0], knots[0][1]-1)
            for k in range(0, len(knots)-1):
                if abs(knots[k][0] - knots[k+1][0]) <= 1 and abs(knots[k][1] - knots[k+1][1]) <= 1:
                    print(k, knots[k], knots[k+1], len(visited), "passing")
                    pass
                else:
                    interim_xy = knots[k+1]
                    knots[k+1] = old_xy
                    print(k, knots[k], knots[k+1], len(visited))
                    old_xy = interim_xy
            visited.add(knots[9])
    return visited



moves = ['R 4','U 4','L 3','D 1','R 4','D 1','L 5','R 2',]
print(len(do_it()))

moves = ['R 5', 'U 8', 'L 8', 'D 3', 'R 17', 'D 10', 'L 25', 'U 20']
print(len(do_it()))

#moves=format_data(read_data())
#print(len(do_it()))
