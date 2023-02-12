import heapq
def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < k:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + 2*heapq.heappop(scoville))
        except IndexError:
            return -1
        answer += 1

    return answer


scoville, k = [1,2,3,9,10,12], 7
print(solution(scoville, k))
