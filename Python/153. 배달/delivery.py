# import collections
#
# def setRoad(road):
#     roads = collections.defaultdict(list)
#     for a, b, c in road:
#         roads[a].append([b, c])
#         roads[b].append([a, c])
#     return roads
#
# def setRoad(road):
#     roads = collections.defaultdict(list)
#     for a, b, c in road:
#         roads[a].append([b, c])
#         roads[b].append([a, c])
#     return roads

# def solution(N, road, K):
#     checked = []
#     roads = setRoad(road)
#     queue = collections.deque([[1, 0]])
#
#     while queue:
#         start, time = queue.popleft()
#         checked.append(start)
#
#         for end, c in roads[start]:
#             if end not in checked and time + c <= K:
#                 queue.append([end, time + c])
#
#     return len(list(set(checked)))

##################################################################

# import collections
#
# def setRoad(road):
#     roads = collections.defaultdict(list)
#     for a, b, c in road:
#         roads[a].append([b, c])
#         roads[b].append([a, c])
#     return roads
#
# def dfs(N, K, roads, start, length, checked, visited):
#     for end, count in roads[start]:
#         if end not in checked and length + count <= K:
#             checked.append(end)
#             visited.add(end)
#             dfs(N, K, roads, end, length + count, checked, visited)
#             checked.pop()
#
# def solution(N, road, K):
#     visited = set([1])
#     checked = [1]
#     roads = setRoad(road)
#     dfs(N, K, roads, 1, 0, checked, visited)
#     return len(visited)

##################################################################

def get_roads(N, road):
    roads = [[987654321] * N for _ in range(N)]
    for start, end, cost in road:
        roads[start - 1][start -1] = 0
        roads[end - 1][end - 1] = 0
        roads[start - 1][end - 1] = cost if cost < roads[start - 1][end - 1] else roads[start - 1][end - 1]
        roads[end - 1][start - 1] = cost if cost < roads[end - 1][start - 1] else roads[end - 1][start - 1]
    return roads

def get_small_cost(d, v, N):
    minimum = 987654321
    idx = 987654321
    for i in range(N):
        if d[i] < minimum and not v[i]:
            minimum = d[i]
            idx = i
    return idx


def solution(N, road, K):
    roads = get_roads(N, road)
    start = 0
    d = roads[start]
    v = [False] * N
    v[start] = True

    for i in range(N-1):
        small = get_small_cost(d, v, N)
        for j in range(N):
            if roads[small][j] + d[small] < d[j]:
                d[j] = roads[small][j] + d[small]
        v[small] = True

    result = 0
    for i in d:
        if i <= K:
            result += 1
    return result






N, road, K = 5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3
# N, road, K = 6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4
print(solution(N, road, K))
