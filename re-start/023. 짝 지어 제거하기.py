import collections
def solution(s):
    stack = collections.deque()
    for char in s:
        if not stack:
            stack.append(char)
        elif char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return 0 if len(stack) else 1

s = 'baabaa'
print(solution(s))