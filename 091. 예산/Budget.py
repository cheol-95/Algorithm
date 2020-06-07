def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    for i in d:
        sum += i
        answer += 1
        if sum > budget:
            return answer -1
    return answer

d, budget = [1, 3, 2, 5, 4], 9
# d, budget = [2,2,3,3], 10
print(solution(d, budget))


'''
def solution(d, budget):
    cnt = 1
    while True:
        tmp_d = [_ for _ in d]
        cnt += 1
        tmp = 0
        if budget < min(d):
            return 0
        if cnt > len(d):
            return cnt -1
        for i in range(cnt):
            tmp += min(tmp_d)
            tmp_d.remove(min(tmp_d))
        if tmp > budget:
            return cnt-1
        '''