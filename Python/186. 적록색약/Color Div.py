import collections
import sys
input = sys.stdin.readline

def dfs(y, x, visit, target_1, target_2):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = collections.deque([[y, x]])

    while queue:
        ty, tx = queue.popleft()
        for dy, dx in direction:
            ny, nx = ty + dy, tx + dx

            if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx]:
                if board[ny][nx] == target_1 or board[ny][nx] == target_2:
                    visit[ny][nx] = 1
                    queue.append([ny, nx])

    return visit

result = [0, 0]
N = int(input())
board = [list(input()[:-1]) for _ in range(N)]
n_visit, o_visit = [[0] * N for _ in range(N)], [[0] * N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if not n_visit[y][x]:
            n_visit = dfs(y, x, n_visit, board[y][x], board[y][x])
            result[0] += 1

        if not o_visit[y][x]:
            if board[y][x] == 'B':
                o_visit = dfs(y, x, o_visit, 'B', 'B')
            else:
                o_visit = dfs(y, x, o_visit, 'G', 'R')
            result[1] += 1

print(*result)

