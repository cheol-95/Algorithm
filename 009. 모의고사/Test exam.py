def solution(answers):
    result = []
    answer = [0] * 3
    a = '12345'
    b = '21232425'
    c = '3311224455'

    for i in range(len(answers)):
        if answers[i] == int(a[i]):
            answer[0] += 1
        if answers[i] == int(b[i]):
            answer[1] += 1
        if answers[i] == int(c[i]):
            answer[2] += 1
    result.append(answer.index(max(answer)))
    answer.remove(max(answer))
    print(result[len(result)-1], max(answer))
    while result[len(result)-1] == max(answer):
        print(answer, result)
        result.append(answer.index(max(answer)))
        answer.remove(max(answer))
    return result

# answers = [1,2,3,4,5]
answers = [1,3,2,4,2]
print(solution(answers))