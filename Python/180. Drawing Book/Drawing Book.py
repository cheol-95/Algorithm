#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n % 2 == 1:
        return min(p // 2, (n - p) // 2)
    else:
        return min(p // 2, (n + 1 - p) // 2)


if __name__ == '__main__':
    # n, p = 5, 4
    # n, p = 100, 6
    n, p = 7, 4


    result = pageCount(n, p)
    print(result)