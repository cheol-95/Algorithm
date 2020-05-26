def count(num):
    cnt = 0
    while num > 0:
        if num%2 == 1:
            cnt += 1
        num//=2
    return cnt

def solution(n):
    cnt = count(n)
    while True:
        n+=1
        if count(n) == cnt:
            return n

n = 78
print(solution(n))
# while n > 0:
#     tmp = n%2
#     n=n//2
#     print(tmp)