def solution(m, n, puddles):
    load = [[0] * m for _ in range(n)]
    load[0][0] = 1

    for y in range(0, n):
        for x in range(0, m):
            if y == x == 0:
                continue
            if [x+1, y+1] in puddles:
                load[y][x] = 0
            else:
                load[y][x] = load[y][x-1] + load[y-1][x]

    return load[n-1][m-1] % 1000000007

# def solution(m, n, puddles):
#     load = [[1] * m for _ in range(n)]
#     for puddle_x, puddle_y in puddles:
#         load[puddle_y - 1][puddle_x - 1] = 0
#
#     for y in range(n - 2, -1, -1):
#         for x in range(m - 2, -1, -1):
#             if load[y][x]:
#                 load[y][x] = load[y + 1][x] + load[y][x + 1]
#
#     for i in load:
#         print(i)
#     return load[0][0]



m, n, puddles = 4, 3, [[2, 2]]
print(solution(m, n, puddles))
