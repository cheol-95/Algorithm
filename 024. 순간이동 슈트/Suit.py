def solution(n):
    ans = 0
    while n:
        if n%2 == 1:
            n -= 1
            ans += 1
        n//=2
    return ans

s= 5000
print(solution(s))