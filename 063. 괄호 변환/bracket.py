def solution(p):
    cnt1 = 0
    cnt2 = 0
    u = ''
    stack = []
    for i,char in enumerate(p):
        if stack and stack[-1] == '(' and char == ')':
            stack.pop()
        else:
            stack.append(char)
        if char == '(':
            u, cnt1 = u + '(', cnt1 + 1
        else:
            u, cnt2 = u + ')', cnt2 + 1
        if cnt1 and cnt1 == cnt2:
            if stack: # 올바르지 않은 문자열
                tmp1 = ''
                for v in u[1:len(u)-1]:
                    if v == '(':
                        tmp1 += ')'
                    else:
                        tmp1 += '('
                if len(u)==2:
                    return '(' + tmp1 + ')'
                return '(' + solution(p[i+1:]) + ')' + tmp1
            else: #올바른 괄호 문자열
                if not p[i+1:] or len(p)==2:
                     return u
                return u+solution(p[i+1:])


# p = "(()())()"
# p = ')('
# p = "()))((()"
p = '(((())))'
print(solution(p))