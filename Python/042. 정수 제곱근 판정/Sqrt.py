import math
def solution(n):
    tmp = math.sqrt(n)
    if tmp - int(tmp) == 0:
        return (tmp+1)**2
    return -1