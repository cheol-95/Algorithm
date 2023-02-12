#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    min = 999999
    tmp = []
    for i in s:
        tmp += i

    square_list = [
        [8,3,4,1,5,9,6,7,2],
        [8,1,6,3,5,7,4,9,2],
        [4,3,8,9,5,1,2,7,6],
        [6,1,8,7,5,3,2,9,4],
        [2,7,6,9,5,1,4,3,8],
        [2,9,4,7,5,3,6,1,8],
        [6,7,2,1,5,9,8,3,4],
        [4,9,2,3,5,7,8,1,6]
    ]

    for row in square_list:
        res = 0
        for idx, col in enumerate(row):
            res += abs(col - tmp[idx])
        if res < min:
            min = res

    return min



if __name__ == '__main__':
    # s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

    result = formingMagicSquare(s)
    print(result)