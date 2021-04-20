#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    import collections
    birds = collections.Counter(arr).most_common()
    maximum = birds[0][1]
    candidate = [birds[0][0]]

    for bird in birds:
        if maximum != bird[1]:
            return min(candidate)
        candidate.append(bird[0])

    return maximum

if __name__ == '__main__':
    # arr_count = int(input().strip())
    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
    result = migratoryBirds(arr)
    print(result)