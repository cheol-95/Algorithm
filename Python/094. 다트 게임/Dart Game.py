def solution(dartResult):
    answer = []
    cnt = -1
    pas = -2
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric():
            if i == pas:
                continue
            cnt += 1
            if dartResult[i+1].isnumeric():
                answer.append(int(dartResult[i] + dartResult[i+1]))
                pas = i+1
            else:
                answer.append(int(dartResult[i]))
        elif dartResult[i] == 'D':
            answer[cnt] = pow(answer[cnt], 2)
        elif dartResult[i] == 'T':
            answer[cnt] = pow(answer[cnt], 3)
        elif dartResult[i] == '#':
            answer[cnt] = answer[cnt]*-1
        elif dartResult[i] == '*':
            if cnt != 0:
                answer[cnt - 1] = answer[cnt - 1] * 2
            answer[cnt] = answer[cnt] * 2
    return sum(answer)


dartResult = "1D2S#10S"
print(solution(dartResult))
