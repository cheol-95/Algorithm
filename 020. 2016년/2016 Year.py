def solution(a, b):
    answer = ''
    cnt = 1
    if a == 1:
        cnt += 0
    elif a == 2:
        cnt += 29
    elif a == 3:
        cnt += 60
    elif a == 4:
        cnt += 90
    elif a == 5:
        cnt += 121
    elif a == 6:
        cnt += 151
    elif a == 7:
        cnt += 182
    elif a == 8:
        cnt += 213
    elif a == 9:
        cnt += 243
    elif a == 10:
        cnt += 274
    elif a == 11:
        cnt += 304
    elif a == 12:
        cnt += 335
    cnt += b

    res = cnt % 7

    if res == 0:
        answer = 'SUN'
    if res == 1:
        answer = 'SAT'
    if res == 2:
        answer = 'FRI'
    if res == 3:
        answer = 'SAT'
    if res == 4:
        answer = 'SUN'
    if res == 5:
        answer = 'MON'
    if res == 6:
        answer = 'TUE'
    return answer

a, b = 5, 24
print(solution(a,b))

