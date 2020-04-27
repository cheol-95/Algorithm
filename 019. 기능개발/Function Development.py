def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            if not progresses:
                break
        if cnt:
            answer.append(cnt)
    return answer

progresses, speeds = [93,30,55], [1,30,5]
print(solution(progresses, speeds))