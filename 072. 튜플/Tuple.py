def solution(s):
    answer = []
    tmp = sorted(s[2:len(s) - 2].split('},{'), key=lambda x: len(x))
    for i in tmp:
        tmp1 = list(map(int, i.split(',')))
        for j in tmp1:
            if j not in answer:
                answer.append(j)
    return answer

s= "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))