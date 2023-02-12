#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    result = [0, 0]
    d = [scores[0], scores[0]]

    for score in scores:
        if d[1] < score:
            d[1] = score
            result[0] += 1

        if score < d[0]:
            d[0] = score
            result[1] += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
