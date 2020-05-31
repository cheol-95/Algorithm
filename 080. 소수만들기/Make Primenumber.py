from math import sqrt
import itertools

def solution(nums):
    answer = 0
    for i in list(map(sum, itertools.combinations(nums, 3))):
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            answer += 1
    return answer

nums = [1,2,3,4]
nums = [1,2,7,6,4]
print(solution(nums))

'''
from math import sqrt
import itertools

def prime(x):
    for i in range(2,int(sqrt(x))+1):
        if x%i == 0:
            return False
    else:
        return True

def solution(nums):
    answer = 0
    candidate = list(map(sum, itertools.combinations(nums, 3)))
    for i in candidate:
        if prime(i) == True:
            answer += 1
    return answer
'''