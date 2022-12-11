import os
import sys
import pandas as pd
import numpy as np

def get_input():
  
    with open(os.path.join(sys.path[0], 'input.txt'), 'r') as f:
        data = [line.replace('\n', '') for line in f.readlines()]

    return data

def solve(data):

    def mapping(letter):
        if 'a' <= letter <= 'z':
            value = ord(letter) - 96
        else:
            value = ord(letter) - 38

        return value


    # Solution 1
    
    final_list = []

    for x in data:
        bagsize = len(x)
        bagsize_half = len(x)//2
        bag_left = slice(0, bagsize_half)
        bag_right = slice(bagsize_half, bagsize)
        shared_item = [y for y in x[bag_left] if y in x[bag_right]][0]
        shared_item_value = mapping(shared_item)
        final_list.append(shared_item_value)

    df = pd.DataFrame(final_list)

    solution1 = df.sum()


    # Solution 2

    final_list = []

    for x in range(0, len(data), 3):
        group = data[x:x+3]
        shared_item = [
            y for y in group[0] 
            if y in group[1] 
            and y in group[2]
            ][0]
        shared_item_value = mapping(shared_item)
        final_list.append(shared_item_value)

    df = pd.DataFrame(final_list)

    solution2 = df.sum()

    return solution1, solution2

if __name__ == '__main__':
    
    data = get_input()
    solution1, solution2 = solve(data)

    print(solution1)
    print(solution2)
