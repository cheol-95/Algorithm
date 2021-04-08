def check(board, K, y, x):
    count = 0
    for ty in range(y, y+K):
        for tx in range(x, x+K):
            if board[ty][tx]:
                count += 1
    return count

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = N * N

    for y in range(N-K+1):
        for x in range(N-K+1):
            tmp = check(board, K, y, x)
            result = tmp if tmp < result else result
    print(result)
