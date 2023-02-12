def fatorial(N):
    if N == 0:
        return 1
    elif N == 1:
        return N
    else:
        return N*fatorial(N-1)

N = int(input())
print(fatorial(N))


'''
import math
print(math.factorial(int(input())))
'''