# import collections
#
# def get_route(fares):
#     route = collections.defaultdict(list)
#     for c1, c2, cost in fares:
#         route[c1].append([c2, cost])
#         route[c2].append([c1, cost])
#     return route
#
# def get_small_route(n, s, a, b, routes):
#     dist = [999999999] * n
#     checked = [s+1]
#
#     queue = collections.deque([[s+1, 0]])
#
#     while queue:
#         s, cost = queue.popleft()
#         print(s, cost, routes[s], checked)
#
#         for n_s, n_cost in routes[s]:
#             if n_s not in checked:
#                 checked.append(n_s)
#                 queue.append([n_s, cost + n_cost])
#
#     print(dist)
#     exit()
#
# def solution(n, s, a, b, fares):
#     dp = [[0, 0, 0, 0] for _ in range(n)]
#     routes = get_route(fares)
#
#     for idx in range(n):
#         tmp = get_small_route(n, idx, a, b, routes)
#         for i in tmp:
#             print(i)
#         print()
#
#     queue = collections.deque([[s-1, 0]])
#
#     while queue:
#         start, cost = queue.popleft()
#         print(start, cost)
#
#     return 1
#
# n, s, a, b, fares = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# print(solution(n, s, a, b, fares))


import collections

def floy(n, fares):
    d = [[999999] * n for _ in range(n)]

    for idx in range(n):
        d[idx][idx] = 0

    for c1, c2, cost in fares:
        d[c1-1][c2-1] = cost
        d[c2-1][c1-1] = cost

    for m in range(n):
        for s in range(n):
            for e in range(n):
                if d[s][m] + d[m][e] < d[s][e]:
                    d[s][e] = d[s][m] + d[m][e]
    return d

def solution(n, s, a, b, fares):
    dp = floy(n, fares)
    minimum = 9999999
    for idx in range(n):
        minimum = min(minimum, dp[s - 1][idx] + dp[idx][a - 1] + dp[idx][b - 1])
    return minimum


n, s, a, b, fares = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))