def solution(arrangement):
    answer = 0
    cnt = 0
    tmp = ''
    for i in arrangement:
        if i == '(':
            cnt += 1
            tmp = 1
        else:
            cnt -= 1
            if tmp == 1:
                answer += cnt
            else:
                answer += 1
            tmp = 0
    return answer