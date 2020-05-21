import collections
def solution(people, limit):
    cnt = 0
    people = collections.deque(sorted(people))
    while people:
        cnt += 1
        tmp = 0 + people.pop()
        if not people:
            break
        while tmp + people[0] <= limit:
            tmp += people.popleft()
            if not people:
                break
    return cnt

'''
#정렬을 해서 가장 큰 것과 가장 작은 것을 태워 보낸다.
def solution(people, limit):
    people.sort()
    boatCnt = 0
    inboat = 0
    peopleCnt = len(people) - 1
    while inboat <= peopleCnt:
        boatCnt += 1
        if people[peopleCnt] + people[inboat] <= limit:
            inboat += 1
        peopleCnt -= 1

    return boatCnt
'''