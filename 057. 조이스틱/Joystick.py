def solution(name):
    name = list(name)
    last = ['A' for i in range(len(name))]
    answer = 0
    i = 0
    print(answer, i, name)
    while last != name:
        if name[i] != 'A':
            tmp = ord(name[i])-ord('A')
            if tmp > 13:
                tmp = 26 - tmp
            answer += tmp
            name[i] = 'A'
            print(answer, i, name)
            if last == name:
                break
        left, right = 0, 0
        for j in range(1, len(name) // 2 + 1):
            if i < 0:
                i = len(name) + i
            rTmp = i + j
            if rTmp >= len(name):
                rTmp = rTmp - len(name)

            if name[i - j] != 'A':
                left = j
            if name[rTmp] != 'A':
                right = j

            if left > right:
                i = i - j
                answer += j
                break
            elif left <= right and right:
                i = i + j
                answer += j
                break
    return answer