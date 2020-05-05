def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    tmp = []
    for i in words:
        if begin == target:
            return answer
        cnt = 0
        temp = []
        for j in range(len(i)):
            if i[j] == begin[j]:
                cnt += 1
                temp.append(j)
            if cnt == 2:
                if tmp == temp:
                    break
                tmp = temp
                begin = i
                answer += 1
                break
    return answer