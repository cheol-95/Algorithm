def solution(n):
    answer = [0]
    for i in range(1,n):
        tmp = []
        cnt = 0
        for j in answer:
            if cnt == 0:
                tmp.append(0)
                cnt = 1
            else:
                tmp.append(1)
                cnt = 0
            tmp.append(j)
        tmp.append(1)
        answer = tmp
    return answer

# n = 2
n = 4
print(solution(n))