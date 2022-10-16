def solution(sizes):
    M, N = 0, 0
    for size in sizes:
        m, n = max(size), min(size)
        M = max(M, m)
        N = max(N, n)
    return M*N


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(sizes))