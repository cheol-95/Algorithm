import collections
def solution(s):
    tmp = collections.Counter(s)
    p = tmp['p'] + tmp['P']
    y = tmp['y'] + tmp['Y']
    return p == y

s = 'pPoooyY'
# s = 'Pyy'
print(solution(s))