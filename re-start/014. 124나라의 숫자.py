def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer += str([1, 2, 4][n % 3])
        n //= 3
    return answer[::-1]

n = 12
print(solution(n))
