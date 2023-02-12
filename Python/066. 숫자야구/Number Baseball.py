import itertools
def solution(baseball):
    answer = 0
    length = len(baseball)
    number = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    for i in number:
        cnt = 0
        for v in baseball:
            string = str(v[0])
            tmp0, tmp1, tmp2 = int(string[0]), int(string[1]), int(string[2])
            strike = 0
            ball = 0
            if i[0] == tmp0:
                strike += 1
            if i[1] == tmp1:
                strike += 1
            if i[2] == tmp2:
                strike += 1
            if i[0] == tmp1 or i[0] == tmp2:
                ball += 1
            if i[1] == tmp0 or i[1] == tmp2:
                ball += 1
            if i[2] == tmp0 or i[2] == tmp1:
                ball += 1
            if strike == v[1] and ball == v[2]:
                cnt += 1
            else:
                break
        if cnt == length:
            answer += 1
    return answer

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))
