def solution(n):
    cnt = 2
    lookup= [0,1]
    while cnt-1 < n:
        lookup.append(lookup[cnt-1]+lookup[cnt-2])
        cnt += 1
    return lookup[n]%1234567


n = 5
print(solution(n))