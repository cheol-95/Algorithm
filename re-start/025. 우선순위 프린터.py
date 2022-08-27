import collections
def solution(priorities, location):
    cnt = 0
    target = (location, priorities[location])
    ids = collections.deque((i, v) for i, v in enumerate(priorities))

    while ids:
        M = max(ids, key=lambda x: x[1])[1]
        now = ids.popleft()
        if now[1] == M:
            cnt += 1
            if now == target:
                return cnt
        else:
            ids.append(now)



# priorities, location = [2, 1, 3, 2], 2
priorities, location = [1, 1, 9, 1, 1, 1], 0
print(solution(priorities, location))