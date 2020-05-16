def solution(priorities, location):
    answer = 0
    tmp = [i for i in range(len(priorities))]
    while True:
        num = priorities.pop(0)
        if num < max(priorities):
            priorities.append(num)
            tmp.append(tmp.pop(0))
        else:
            answer += 1
            if tmp.pop(0) == location:
                break
    return answer