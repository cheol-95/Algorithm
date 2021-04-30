import heapq
N, M = map(int, input().split())
tmp = [[] for _ in range(N+1)]
precede = [0 for _ in range(N+1)]
queue, res = [], []

for _ in range(M):
    a, b = map(int, input().split())
    tmp[a].append(b)
    precede[b] += 1

for i in range(1, N+1):
    if precede[i] == 0:
        heapq.heappush(queue, i)

while queue:
    print(queue)
    num = heapq.heappop(queue)
    res.append(num)
    for i in tmp[num]:
        precede[i] -= 1
        if precede[i] == 0:
            heapq.heappush(queue, i)

for i in res:
    print(i, end=' ')