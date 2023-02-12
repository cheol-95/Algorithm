def solution(a, b):
    if a > b:
        a,b = b,a
    return sum(range(a,b+1))

a,b = 5,3
print(solution(a,b))