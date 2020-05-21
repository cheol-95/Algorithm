def solution(p):
    if not p:
        return ''
    cnt1, cnt2 = 0, 0
    proper = True
    for i,v in enumerate(p):
        if v == '(':
            cnt1 += 1
        else:
            cnt2 += 1
            if cnt1 < cnt2:
                proper = False
        if cnt1 == cnt2:
            if proper == False:
                tmp = '(' + solution(p[i+1:len(p)]) + ')'
                for j in p[1:i]:
                    if j == '(':
                        tmp += ')'
                    if j == ')':
                        tmp += '('
                return tmp
            else:
                tmp = p[:i+1] + solution(p[i+1:len(p)])
                return tmp