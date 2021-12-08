input_data = "C:\\Users\\paul\\advent2021\\4\\input.txt"


class board:
    def __init__(self, data):
        self.board_data = []
        for i in data:
            self.board_data.append((i, False))
        print('length',len(self.board_data))
        self.won = False

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

def get_bingo_numbers(data):
    return data[0].split(',')

def parse_and_create_boards(data):
    current_board = []
    board_data = data[2:]
    boards = []
    for i in board_data:
        if len(i.strip()) == 0:
            if board_data:
                boards.append(current_board)
                current_board = []
        current_board = current_board + i.split()
    return boards

def play_bingo(bingo_numbers, board_data):
    boards = []
    print(board_data)
    for i in board_data:
        boards.append(board(i))
    winner = False
    while not winner:
        i = next(bingo_numbers)
        print('draw', i)
        for aboard in boards:
            aboard.got_number(i)
        for aboard in boards:
            if aboard.check_if_won():
                winner = True
                print(aboard.board_data, 'won')
                print('score', aboard.get_score() * int(i))

def get_last_board(bingo_numbers, board_data):
    boards = []
    print(board_data)
    for i in board_data:
        boards.append(board(i))
    winner = False
    while len(boards) > 0:
        i = next(bingo_numbers)
        print('draw', i)
        for aboard in boards:
            aboard.got_number(i)
        for aboard in boards:
            if aboard.check_if_won():
                print(aboard.board_data, 'won')
                print(aboard.get_score() * int(i))
                boards.remove(aboard)
                

test_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 """

if __name__ == "__main__":
    bingo_numbers = iter(get_bingo_numbers(test_data.split('\n')))
    board_data = parse_and_create_boards(test_data.split('\n'))
    play_bingo(bingo_numbers, board_data)

    real_data = get_input_data()
    bingo_numbers = iter(get_bingo_numbers(real_data))
    board_data = parse_and_create_boards(real_data)
    play_bingo(bingo_numbers, board_data)

    bingo_numbers = iter(get_bingo_numbers(test_data.split('\n')))
    board_data = parse_and_create_boards(test_data.split('\n'))
    get_last_board(bingo_numbers, board_data)

    real_data = get_input_data()
    bingo_numbers = iter(get_bingo_numbers(real_data))
    board_data = parse_and_create_boards(real_data)
    get_last_board(bingo_numbers, board_data)



