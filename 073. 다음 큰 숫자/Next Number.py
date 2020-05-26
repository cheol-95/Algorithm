def solution(n):
    cnt = bin(n).count('1')
    while True:
        n+= 1
        if cnt == bin(n).count('1'):
            return n

n = 78
print(solution(n))

'''
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
'''