#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    x1, v1, x2, v2 = map(int, [x1, v1, x2, v2])

    if x1 > x2 and v1 > v2 or x1 < x2 and v1 < v2 or v1 == v2:
        return 'NO'

    if abs(x1 - x2) % abs(v1 - v2) != 0:
        return 'NO'

    return 'YES'


if __name__ == '__main__':
    # x1, v1, x2, v2 = map(int, input().split(' '))
    x1, v1, x2, v2 = 43, 2, 70, 2
    result = kangaroo(x1, v1, x2, v2)

    print(result)
