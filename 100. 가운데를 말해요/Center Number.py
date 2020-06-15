import heapq
N = int(input())
heap = []
for i in range(N):
    heapq.heappush(heap, int(input()))
    tmp = heapq.nlargest((i+1)//2+1, heap)
    print(tmp[len(tmp)-1])
