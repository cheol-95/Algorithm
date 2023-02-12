# from collections import deque
#
# for t in range(int(input())):
#     N, K = map(int, input().split())
#     indegree = [0] * (N+1)
#     graph = [[] for _ in range(N + 1)]
#     time = [0] + list(map(int, input().split()))
#
#     for _ in range(K):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         indegree[b] += 1
#
#     W = int(input())
#     queue = deque()
#     DP = time[:]
#
#     for i in range(1, N+1):
#         if not indegree[i]:
#             queue.append(i)
#
#     while queue:
#         for _ in range(len(queue)):
#             now = queue.popleft()
#             for n in graph[now]:
#                 indegree[n] -= 1
#                 DP[n] = max(DP[n], DP[now] + time[n])
#                 if not indegree[n]:
#                     queue.append(n)
#     print(DP[W])

from collections import deque
import sys
input = sys.stdin.readline


def topologicalSort():
    for _ in range(N):
        if not dq:
            return

        target = dq.popleft()

        for x in adjList[target]:
            sequence[x] = max(sequence[x], sequence[target] + D[x])
            indegree[x] -= 1

            if not indegree[x]:
                dq.append(x)

for _ in range(int(input())):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))

    sequence = [0] * (N + 1)
    indegree = [0] * (N + 1)
    adjList = [[] for _ in range(N + 1)]

    for _ in range(K):
        X, Y = map(int, input().split())
        indegree[Y] += 1
        adjList[X].append(Y)

    W = int(input())

    dq = deque()
    for i in range(1, N + 1):
        if not indegree[i]:
            sequence[i] = D[i]
            dq.append(i)

    topologicalSort()

    print(sequence[W])