def solution(s):
    tmp = list(s)
    if len(s) in (4,6):
        for i in tmp:
            try:
                int(i)
            except:
                return False
        return True
    return False

s = 'a234'
print(solution(s))

'''
def solution(s):
    return s.isdigit() and len(s) in (4,6)
'''