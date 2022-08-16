import itertools
def solution(expression):
    answer = 0
    operands = set([_ for _ in expression if not _.isdigit()])
    expressions = expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').split(' ')
    for ops in list(itertools.permutations(operands, len(operands))):
        tmp_expressions = expressions.copy()
        for op in ops:
            while op in tmp_expressions:
                idx = tmp_expressions.index(op)
                tmp_expressions[idx] = str(eval(''.join(tmp_expressions[idx-1: idx+2])))
                tmp_expressions.pop(idx + 1)
                tmp_expressions.pop(idx - 1)
        answer = max(answer, abs(int(tmp_expressions[0])))
    return answer

expression = "100-200*300-500+20"
print(solution(expression))