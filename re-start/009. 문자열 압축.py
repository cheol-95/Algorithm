def solution(s):
    answer = len(s)
    for length in range(len(s)//2, 0, -1):
        cnt = 1
        stack = []
        for i in range(len(s)//length):
            tmp = s[i * length: (i + 1) * length]
            if stack and stack[-1] == tmp:
                cnt += 1
            elif stack and stack[-1] != tmp:
                stack[-1] = str(cnt) + stack[-1] if cnt >= 2 else stack[-1]
                stack.append(tmp)
                cnt = 1
            else:
                stack.append(tmp)

        stack[-1] = str(cnt) + stack[-1] if cnt >= 2 else stack[-1]
        stack.append(s[(i + 1) * length:])
        answer = min(answer, len(''.join(stack)))
    return answer


# s = 'abcabcabcabcdededededede'
s = 'aabbaccc'
print(solution(s))