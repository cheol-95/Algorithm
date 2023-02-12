import collections
import sys
input = sys.stdin.readline

def bfs(board, N, v, y, x):
    count = 0
    queue = collections.deque([[y, x]])
    v.append([y, x])
    directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    while queue:
        count += 1
        ty, tx = queue.popleft()

        for dy, dx in directions:
            ny, nx = [ty + dy, tx + dx]

            if 0 <= ny < N and 0 <= nx < N and [ny, nx] not in v and board[ny][nx]:
                queue.append([ny, nx])
                v.append([ny, nx])

    return count

res, v = [], []
N = int(input())
board = [list(map(int, list(input())[:-1])) for _ in range(N)]

for y in range(N):
    for x in range(N):
        if board[y][x] and [y, x] not in v:
            res.append(bfs(board, N, v, y, x))

res.sort()
print(len(res))
for i in res:
    print(i)