import heapq
def solution(jobs):
    last = -1
    now = 0
    answer = 0
    wait = []
    length = len(jobs)
    count = 0 
    while(count<length):
        for job in jobs:
            if last < job[0] <= now:
                answer += (now-job[0])
                heapq.heappush(wait, job[1])
        if len(wait)>0:
            answer += len(wait)*wait[0]
            last = now
            now += heapq.heappop(wait)
            count += 1
        else:
            now += 1
    return answer // length


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))


# import heapq
# def solution(jobs):
#     answer = 0
#     heapq.heapify(jobs)
#     start = heapq.nsmallest(1, jobs)[0]
#     tmp = sorted(jobs, key=lambda x: x[1])
#     tmp = [i for i in tmp if i[0] == start[0]] + [i for i in tmp if i[0] != start[0]]
#
#     for i in range(1,len(tmp)):
#         if tmp[i-1][1] > tmp[i][0]:
#             tmp[i][1] = tmp[i-1][1] + tmp[i][1]
#         else:
#             tmp[i][1] += tmp[i][0]
#
#     for i in tmp:
#         answer += i[1]-i[0]
#     return answer // len(jobs)