import sys
input = sys.stdin.readline

h, w = map(int, input().split())
board = [[0] * w for _ in range(h)]

for _ in range(int(input())):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(l):
            board[x - 1][y - 1 + i] = 1
    else:
        for i in range(l):
            board[x - 1 + i][y - 1] = 1

for row in board:
    print(*row)