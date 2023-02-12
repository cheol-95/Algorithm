import itertools
import collections

def check(db, count, answer):
    cdt = []
    original = db
    if count == 1:
        for i in range(len(db)):
            tmp = collections.Counter(db[i])
            if max(tmp.values()) == 1:
                cdt.append(i)
                answer += 1
    else:

        length = list(itertools.combinations(range(len(db)), count))
        for i in length:
            if len(original)-len(cdt) < count:
                break
            sum = []
            for j in range(len(db[0])):
                lst = []
                for k in i:
                    lst.append(db[k][j])
                sum.append(tuple(lst))
            sum = tuple(sum)
            tmp = collections.Counter(sum)
            if max(tmp.values()) == 1:
                for _ in i:
                    cdt.append(_)
                answer += 1
    for i in cdt:
        del original[i]
    return original, answer


def solution(relation):
    answer = 0
    tmp = list(zip(*relation))
    cnt = 1
    while cnt <= len(tmp):
        tmp, answer = check(tmp, cnt, answer)
        cnt += 1
    return answer

relation = 	[["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
print(solution(relation))