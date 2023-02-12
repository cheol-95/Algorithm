def solution(s):
    answer = ''
    s += ' '
    cnt = 0
    while cnt < len(s):
        if s[cnt] == ' ':
            answer += ' '
            cnt += 1
        else:
            answer += s[cnt].upper()
            cnt += 1
            while s[cnt] != ' ':
                answer += s[cnt].lower()
                cnt += 1
    return answer[:-1]

s = '3people unFollowed me'
# s = 'for the last  week	'
print(solution(s))

'''
return s.title()
'''