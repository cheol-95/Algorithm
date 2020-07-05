def solution(N):
    size = [1,1]
    for i in range(2, N):
        size.append(size[i-2]+size[i-1])
    return (size[N-1]*4 + size[N-2]*2)