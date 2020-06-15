import itertools
N, M = map(int, input().split())
for i in itertools.permutations([i for i in range(1,N+1)], M):
    for j in i:
        print(j, end=' ')
    print()

'''
import itertools
N, M = map(int, input().split())
for i in itertools.permutations(range(1,N+1),M):
    print(*i)
'''
