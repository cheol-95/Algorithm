from collections import deque

q = deque()
N, L = list(map(int, input().split()))
D = list(map(int, input().split()))

for i, d in enumerate(D):
    while q and q[-1] > d:
        q.pop()
    q.append(d)

    if i >= L and q[0] == D[i - L]:
        q.popleft()
    print(q[0], end=' ')