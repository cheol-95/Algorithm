import heapq
def solution(scoville, k):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + 2*heapq.heappop(heap))
        except IndexError:
            return -1
        answer += 1

    return answer


scoville, k = [1,2,3,9,10,12], 7
print(solution(scoville, k))
