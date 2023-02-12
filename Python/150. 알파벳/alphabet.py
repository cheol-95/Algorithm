# def dfs(y, x, alpha, count):
#     global board, R, C, max_count
#     max_count = max(max_count, count)
#
#     directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#     for dy, dx in directions:
#         ny, nx = y + dy, x + dx
#
#         if 0 <= ny < R and 0 <= nx < C:
#             alpha_count = ord(board[ny][nx]) - 65
#             if not alpha[alpha_count]:
#                 alpha[alpha_count] = True
#                 dfs(ny, nx, alpha, count + 1)
#                 alpha[alpha_count]= False
#
# R, C = map(int, input().split())
# board = [list(input()) for _ in range(R)]
#
# alpha = [False] * 26
# alpha[ord(board[0][0])-65] = True
#
# max_count = 0
# dfs(0, 0, alpha, 1)
# print(max_count)

import sys

def dfs(y, x, al, count):
    global board, R, C, max_count
    max_count = max(max_count, count)

    dy = [0, -1, 0, 1]
    dx = [-1, 0, 1, 0]

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < R and 0 <= nx < C:
            c = ord(board[ny][nx]) - 65
            if not al[c]:
                al[c] = True
                dfs(ny, nx, al, count + 1)
                al[c]= False

R, C = map(int, input().split())
board = [sys.stdin.readline() for _ in range(R)]

alpha = [False] * 26
alpha[ord(board[0][0])-65] = True

max_count = 0
dfs(0, 0, alpha, 1)
print(max_count)