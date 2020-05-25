def solution(s):
    status = 0
    for i in s:
        if i == '(':
            status -= 1
        else:
            status += 1
        if status > 0:
            return False
    if status != 0:
        return False
    return True

s = '(())()'
print(solution(s))