#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    pay = (sum(bill) - bill[k]) // 2
    if pay != b:
        print(b - pay)
    else:
        print('Bon Appetit')


if __name__ == '__main__':
    bill, k, b = [3, 10, 2, 9], 1, 6
    bonAppetit(bill, k, b)
