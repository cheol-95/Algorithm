def solution(n,a,b):
    answer = 0
    if a>b:
        a,b = b,a
    while True:
        answer += 1
        if b%2 == 0 and a == b-1:
            return answer
        a,b = (a+1)//2, (b+1)//2

n, a, b = 8, 4, 7
print(solution(n,a,b))