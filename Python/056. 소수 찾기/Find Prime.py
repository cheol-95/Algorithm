import itertools
def solution(numbers):
    cnt = 0
    
    List = []
    for i in range(1,len(numbers)+1):
        List += map(''.join,itertools.permutations(numbers, i))
    List = list(set(list(map(int, List))))
    tmp = max(List)
    
    era = [False,False] + [True]*(tmp-1)
    primes=[]
    for i in range(2,tmp+1):
        if era[i]:
            primes.append(i)
            for j in range(2*i, tmp+1, i):
                era[j] = False
    for i in List:
        if i in primes:
            cnt += 1
            
    return cnt