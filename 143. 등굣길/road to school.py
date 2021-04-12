def solution(m, n, puddles):
    puddles = list(map(lambda x: x[::-1], puddles))
    result = [[0] * (m+1) for _ in range(n+1)]
    result[1][1] = 1

    for y in range(1, n+1):
        for x in range(1, m+1):
            if y == 1 and x == 1:
                continue
            if [y, x] in puddles:
                result[y][x] = 0
            else:
                result[y][x] = result[y-1][x] + result[y][x-1]

    return result[n][m] % 1000000007


m, n, puddles = 4, 3, [[2, 2]]
print(solution(m, n, puddles))