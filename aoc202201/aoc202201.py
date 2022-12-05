import os
import sys
import pandas as pd

def get_input():

    with open(os.path.join(sys.path[0], 'input.txt'), 'r') as f:
        data = f.read()

    return data

def solve(data):

    data = data.split('\n\n')
    data = [i.splitlines() for i in data]
    
    df = pd.DataFrame(data).fillna(0).astype('int')

    series = df.sum(axis='columns')

    solution1 = series.max()

    solution2 = series.nlargest(3).sum()

    return solution1, solution2


if __name__ == '__main__':
    
    data = get_input()
    solution1, solution2 = solve(data)

    print(solution1)
    print(solution2)
