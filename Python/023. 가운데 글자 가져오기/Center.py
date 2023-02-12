def solution(s):
    n = len(s)
    if n%2 == 0:
        return s[int(n/2)-1:int(n/2)+1]
    else:
        return s[int(n/2)]

# s = 'abcde'
s = 'qwer'
print(solution(s))