# -*- coding: utf-8 -*-

def read_data(source = "input.txt"):
    with open(source) as f:
        data = f.readlines()
    return data 

def parse_pattern(pattern):
    pattern_list = pattern.split('|')
    input = pattern_list[0].split()
    output = pattern_list[1].split()
    return input,output
    
def get_1478_in_output_count(patterns):
    count = 0
    for pattern in patterns:
        input_signals, output_digits = parse_pattern(pattern)
        for i in output_digits:
            if len(i) in [2,4,3,7]: # segment count in 1,4,7,8
                count += 1
    return count

def get_map(input):
    map = {}
    one = [x for x in input if len(x) == 2][0]
    seven = [x for x in input if len(x) == 3][0]
    print(one,seven)
    map['a'] = ''.join(set(seven)-set(one))
    four = [x for x in input if len(x) == 4][0]
    bd_candidates = list(set(four)-set(one))
    # b occurs in 6 numbers, d occurs in 7 numbers
    if len([x for x in input if bd_candidates[0] in x]) == 6:
        # [0] is b as it occurs 6 times
        map['b'] = bd_candidates[0]
        map['d'] = bd_candidates[1]
    else:
        map['b'] = bd_candidates[1]
        map['d'] = bd_candidates[0]
    # get list of known values
    known = list(map.values())
    # the length five pattern with all three known (a, b and d) is 5
    length_five = [x for x in input if len(x) == 5]
    five = [x for x in length_five if known[0] in x and known[1] in x and known[2] in x]
    # remove a, b and d from five : left with f and g
    five_list = list(five[0])
    five_list.remove(known[0])
    five_list.remove(known[1])
    five_list.remove(known[2])
    # if one of these is in one, then it is f
    if five_list[0] in one:
        map['f'] = five_list[0]
        map['g'] = five_list[1]
    else:
        map['f'] = five_list[1]
        map['g'] = five_list[0]
    # from one we know c
    if one[0] == map['f']:
        map['c'] = one[1]
    else:
        map['c'] = one[0]
    # e is the only unassigned
    for i in 'abcdefg':
        if i not in map.values():
            map['e'] = i
    return map

def translate(map, text):
    output = ''
    for i in text:
        output = output + map[i]
    return output

def pattern_to_digit(pattern):
    table = [set('abcefg'),
             set('cf'),
             set('acdeg'),
             set('acdfg'),
             set('bcdf'),
             set('abdfg'),
             set('abdefg'),
             set('acf'),
             set('abcdefg'),
             set('abcdfg')]
    return str(table.index(set(pattern)))

def process(input):
    sum = 0
    for pattern in patterns:
        input, output = parse_pattern(pattern)
        map = get_map(input)
        reverse_map = dict((v,k) for k,v in map.items())
        print(map)
        print(reverse_map)
        result = ''
        for i in output:
            translated = translate(reverse_map, i)
            result = result + pattern_to_digit(translated)
        sum = sum + int(result)
    return sum
    
if __name__ == "__main__":
    patterns = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
#    print("Number of 1,4,7, or 8 == {}".format(get_1478_in_output_count(patterns)))
    
#    patterns = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
#     'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
#     'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
#     'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
#     'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
#     'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
#     'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
#     'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
#     'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
#     'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce']
#    print("Number of 1,4,7, or 8 == {}".format(get_1478_in_output_count(patterns)))
#    
#    patterns = read_data()
#    print("Number of 1,4,7, or 8 == {}".format(get_1478_in_output_count(patterns)))

    patterns = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
    print(process(patterns))

    patterns = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
     'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
     'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
     'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
     'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
     'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
     'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
     'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
     'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
     'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce']
    print(process(patterns))
    
    patterns = read_data()
    print(process(patterns))
    