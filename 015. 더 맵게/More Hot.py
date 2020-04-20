def solution(scoville, K):
    answer = 0
    for i in range(len(scoville)):
        if scoville[i] < 7:
            scoville[i+1] = scoville[i] + scoville[i+1]*2
            answer += 1
    return answer

scoville, k = [1,2,3,9,10,12], 7
print(solution(scoville, k))