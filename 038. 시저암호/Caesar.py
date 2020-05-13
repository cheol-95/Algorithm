def solution(s, n):
    answer = ''
    for i in s:
        tmp = ord(i) + n
        if i == ' ':
            answer += ' '
            continue
        if i.isupper() == True and tmp > 90 or i.islower() == True and tmp > 122:
            tmp -= 26
        answer += chr(tmp)
    return answer