def is_good(st):
    if st[0] == ')':
        return False
    stack = [st[0]]
    for ch in st[1:]:
        stack.append(ch)
        while len(stack) >= 2 and stack[-1] == ')' and stack[-2] == '(':
            stack.pop()
            stack.pop()
    return True if len(stack) == 0 else False

def div_u_v(p):
    open_cnt, end_cnt = 0, 0
    for ch in p:
        if ch == '(':
            open_cnt += 1
        elif ch == ')':
            end_cnt += 1
        if open_cnt == end_cnt:
            return p[:open_cnt+end_cnt], p[open_cnt+end_cnt:]

def solution(p):
    if p == '':
        return ''

    u, v = div_u_v(p)
    if is_good(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        tmp_u = u[1:-1]
        if tmp_u:
            return answer + ''.join(list(map(lambda x: ')' if x == '(' else '(', tmp_u)))
        else:
            return answer

p = '(()())()'
p = ')('
p = "()))((()"
print(solution(p))