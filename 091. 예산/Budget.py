def solution(d, budget):
    cnt = 1
    while True:
        tmp_d = [_ for _ in d]
        cnt += 1
        tmp = 0
        if cnt > len(d):
            return cnt -1
        for i in range(cnt):
            tmp += min(tmp_d)
            tmp_d.remove(min(tmp_d))
        if tmp > budget:
            return cnt-1

d, budget = [1, 3, 2, 5, 4], 9
d, budget = [2,2,3,3], 10
print(solution(d, budget))