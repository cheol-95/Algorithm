# def factorial(n):
#     if n <= 1:
#         DP[n] = 1
#         return DP[n]
#
#     if DP[n]:
#         return DP[n]
#
#     DP[n] = n * factorial(n-1)
#     return DP[n]
#
# if __name__ == '__main__':
#     N, K = map(int, input().split())
#     DP = [0] * (N+1)
#     print((factorial(N)//(factorial(K)*factorial(N-K)) % 1000000007))

def multi(start, end, next):
    result = 1
    for i in range(start, end, next):
        result *= i
    return result

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(multi(N, N-K, -1) // multi(K, 0, -1) % 1000000007)