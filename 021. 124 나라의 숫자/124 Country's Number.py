def solution(n):
    answer =''
    while n>0:
        r = n % 3
        n = n // 3
        if r ==0:
            n -= 1
        answer = '412'[r] + answer
    return answer

n = 7
print(solution(n))