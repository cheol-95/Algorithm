#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    candidates = [_ for _ in range(a[-1], b[0]+1, a[-1])]
    result = [True] * len(candidates)

    for idx, candidate in enumerate(candidates):
        for A in a:
            if candidate % A != 0:
                result[idx] = False

        for B in b:
            if B % candidate != 0:
                result[idx] = False

    return result.count(True)

if __name__ == '__main__':
    a, b = [2, 4], [16, 32, 96]

    total = getTotalX(a, b)

    print(total)
