def solution(n):
    dp = [0] * n
    dp[0], dp[1] = 1, 2

    for i in range(2, n):
        dp[i] = dp[i-2] % 1000000007 + dp[i-1] % 1000000007

    return dp[n-1]

n = 4
print(solution(n))