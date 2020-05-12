def solution(s):
    tmp = list(s)
    if len(s) == 4 or len(s) == 6:
        for i in tmp:
            try:
                int(i)
            except:
                return False
        return True
    return False

s = 'a234'
print(solution(s))