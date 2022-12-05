import os
import sys
import pandas as pd
import numpy as np

def get_input():
  
    df = pd.read_csv(os.path.join(sys.path[0], 'input.txt'), sep=" ", header=None)

    return df

def solve(df):

    df.columns = ['p1', 'p2']

    conditions = [
        df['p1'].eq('A') & df['p2'].eq('X'),
        df['p1'].eq('B') & df['p2'].eq('X'), 
        df['p1'].eq('C') & df['p2'].eq('X'), 
        df['p1'].eq('A') & df['p2'].eq('Y'), 
        df['p1'].eq('B') & df['p2'].eq('Y'), 
        df['p1'].eq('C') & df['p2'].eq('Y'), 
        df['p1'].eq('A') & df['p2'].eq('Z'), 
        df['p1'].eq('B') & df['p2'].eq('Z'), 
        df['p1'].eq('C') & df['p2'].eq('Z')
    ]

    points = [
        1 + 3, 1 + 0, 1 + 6, 2 + 6, 2 + 3, 2 + 0, 3 + 0, 3 + 6, 3 + 3
    ]

    df['points'] = np.select(conditions, points)

    solution1 = df['points'].sum()

    points2 = [
        3 + 0, 1 + 0, 2 + 0, 1 + 3, 2 + 3, 3 + 3, 2 + 6, 3 + 6, 1 + 6
    ]

    df['points2'] = np.select(conditions, points2)

    solution2 = df['points2'].sum()

    return solution1, solution2


if __name__ == '__main__':
    
    data = get_input()
    solution1, solution2 = solve(data)

    print(solution1)
    print(solution2)
