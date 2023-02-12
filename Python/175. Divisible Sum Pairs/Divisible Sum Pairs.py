#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for i, a in enumerate(ar[:n-1]):
        for b in ar[i+1:n]:
            if (a + b) % k == 0:
                count += 1

    return count

if __name__ == '__main__':
    # nk = input().split()
    # n = int(nk[0])
    # k = int(nk[1])
    # ar = list(map(int, input().rstrip().split()))
    n, k ,ar = 6, 3, [1,3,2,6,1,2]
    result = divisibleSumPairs(n, k, ar)
    print(result)