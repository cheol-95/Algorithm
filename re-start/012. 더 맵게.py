import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2 and scoville[0] < K:
        answer += 1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
    return answer if scoville[0] >= K else -1

# scoville, K = [1, 2, 3, 9, 10, 12], 7
scoville, K = [1, 2], 7
print(solution(scoville, K))