import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        low = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, low + 2*second)
        answer += 1
    return -1 if len(scoville) == 1 and scoville[0] < K else answer


scoville, k = [1, 2], 7
print(solution(scoville, k))