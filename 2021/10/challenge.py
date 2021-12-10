# -*- coding: utf-8 -*-

def read_data(source = "input.txt"):
    with open(source) as f:
        data = f.readlines()
    return data

def get_score(line):
    scores = {')': 3,
              ']': 57,
              '}': 1197,
              '>': 25137,
              }
    expect_stack = []
    score = 0
    openers = '([{<'
    closers = ')]}>'
    for i in line:
        if i in openers: expect_stack.append(closers[openers.index(i)])
        if i in closers:
            opener = expect_stack.pop()
            if i != opener:
                score = score + scores[i]
                break
    return score

def is_corrupted(line):
    expect_stack = []
    openers = '([{<'
    closers = ')]}>'
    for i in line:
        if i in openers: expect_stack.append(closers[openers.index(i)])
        if i in closers:
            opener = expect_stack.pop()
            if i != opener:
                return True
    return False

def remove_corrupted(data):
    output = []
    for i in data:
        if not is_corrupted(i):
           output.append(i)
    return output

def get_complete_score(line):
    scores = {')': 1,
              ']': 2,
              '}': 3,
              '>': 4,
              }
    expect_stack = []
    score = 0
    openers = '([{<'
    closers = ')]}>'
    for i in line:
        if i in openers: expect_stack.append(closers[openers.index(i)])
        if i in closers:
            opener = expect_stack.pop()
            if i != opener:
                print("Something went wrong {} at {} index:{}".format(line, i, line.index(i)))
    print("remainder: {}".format(expect_stack))
    while len(expect_stack) > 0:
        score = score * 5 + scores[expect_stack.pop()]
    return score  

if __name__ == "__main__":
    test_data = ['[({(<(())[]>[[{[]{<()<>>','[(()[<>])]({[<{<<[]>>(','{([(<{}[<>[]}>{[]{[(<()>',
                 '(((({<>}<{<{<>}{[]{[]{}','[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]',
                 '{<[[]]>}<{[{[{[]{()[[[]','[<(<(<(<{}))><([]([]()','<{([([[(<>()){}]>(<<{{',
                 '<{([{{}}[<[[[<>{}]]]>[]]',
                 ]
    score = 0
    for i in test_data:
        score = score + get_score(i)
    print(score)
    
    score = 0
    for i in read_data():
        score = score + get_score(i)
    print(score)

    scores = []
    clean_data = remove_corrupted(test_data)
    for i in clean_data:
        scores.append(get_complete_score(i))
    scores.sort()
    print(scores[int(len(scores)/2)])

    scores = []
    clean_data = remove_corrupted(read_data())
    for i in clean_data:
        scores.append(get_complete_score(i))
    scores.sort()
    print(scores[int(len(scores)/2)])