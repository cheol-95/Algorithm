#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    result = 0

    length = len(s)
    for i in range(length - m + 1):
        if sum(s[i:i+m]) == d:
            result += 1

    return result

if __name__ == '__main__':
    s, d, m = [1, 2, 1, 3 , 2], 3, 2
    result = birthday(s, d, m)
    print(result)
