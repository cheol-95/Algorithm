def solution(s):
    answer = ''
    cnt = 0
    for i,v in enumerate(s):
        if v == ' ':
            cnt = i+1
            answer += ' '
        elif (i-cnt)%2 == 0:
            answer += v.upper()
        else:
            answer += v.lower()
    return answer