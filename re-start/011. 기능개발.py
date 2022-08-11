from collections import deque
def solution(progresses, speeds):
    answer = []
    speeds = deque(speeds)

    while progresses:
        cnt = 0
        progresses = deque(map(lambda x: sum(x), zip(progresses, speeds)))

        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.popleft()
            speeds.popleft()
        if cnt:
            answer.append(cnt)
    return answer

progresses, speeds = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))