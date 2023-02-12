#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    import collections
    result = 0
    tmp = collections.Counter(ar).most_common()
    for t, count in tmp:
        if count < 2:
            break
        result += count // 2
    return result

if __name__ == '__main__':
    # n, ar = 9, [10, 20, 20, 10, 10, 30, 50, 10, 20]
    n, ar = 9, [42] * 100

    # n, ar = 9, [10]

    result = sockMerchant(n, ar)
    print(result)

