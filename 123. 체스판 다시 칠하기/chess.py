n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
score = []

for a in range(n - 7):
    for i in range(m - 7):
        cnt = [0,0]
        for b in range(a, a + 8):
            for j in range(i, i + 8):
                if (j + b)%2 == 0:
                    if board[b][j] != 'W': cnt[0] += 1
                    if board[b][j] != 'B': cnt[1] += 1
                else :
                    if board[b][j] != 'B': cnt[0] += 1
                    if board[b][j] != 'W': cnt[1] += 1
        score.append(min(cnt))

print(min(score))