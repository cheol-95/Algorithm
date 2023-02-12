N, K = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for row in range(1, N + 1):
    for col in range(1, K + 1):
        if col < item[row-1][0]:
            dp[row][col] = dp[row-1][col]
        else:
            dp[row][col] = max(dp[row-1][col], item[row-1][1] + dp[row-1][col-item[row-1][0]])

print(dp[N][K])