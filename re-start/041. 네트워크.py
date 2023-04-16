# def find(v, x):
#     if v[x] == x:
#         return x
#     else:
#         v[x] = find(v, v[x])
#         return v[x]
#
# def union(v, y, x):
#     y_root = find(v, y)
#     x_root = find(v, x)
#     v[x_root] = v[y_root]
#
# def solution(n, computers):
#     v = [_ for _ in range(n)]
#     for start, row in enumerate(computers):
#         for end, is_connect in enumerate(row):
#             if start < end and is_connect:
#                 union(v, start, end)
#
#     return len(set(find(v, i) for i in range(n)))
#
from collections import deque
def bfs(computers, visit, com, n):
    q = deque([com])
    while q:
        d_com = q.pop()
        visit[d_com] = 1
        for tmp in range(n):
            if computers[d_com][tmp] and not visit[tmp]:
                q.append(tmp)

def solution(n, computers):
    answer = 0
    visit = [0 for _ in range(n)]
    for com in range(n):
        if not visit[com]:
            bfs(computers, visit, com, n)
            answer += 1
    return answer

# def solution(n, computers):
#     v = [_ for _ in range(n)]
#     for start, row in enumerate(computers):
#         for end, is_connect in enumerate(row):
#             if is_connect:
#                 v[end] = v[start]
#     print(v)
#     return len(set(v))

n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# n, computers = 4, [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
# n, computers = 4, [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]]
# n, computers = 7, [[1, 0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1, 1]]


print(solution(n, computers))
