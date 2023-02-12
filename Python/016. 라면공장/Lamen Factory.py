import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    pq = []
    while stock < k:
        for i in range(idx, len(dates)):
            if stock < dates[i]:
                break
            heapq.heappush(pq, -supplies[i])
            idx = i+1
        stock += (heapq.heappop(pq) * -1)
        answer += 1
    return answer

stock, dates, supplies, k = 4, [4,10,15], [20,5,10], 30
print(solution(stock, dates, supplies, k))

''' 내 풀이
def solution(stock, dates, supplies, k):
    answer = 0
    dates.append(k)

    for i in range(len(dates)-1):
        stock -= dates[i]
        if dates[i+1]-dates[i+1] >= stock:
            stock += supplies[i]
            answer+=1

    return answer
    '''