def solution(prices):
    length = len(prices)
    answer = [0 for i in range(length)]
    for i in range(length-1):
        for j in range(i+1,length):
            if prices[i] <= prices[j]:
                answer[i] += 1
            elif prices[i] > prices[j]:
                answer[i] += 1
                break
    return answer

prices=[1,2,3,2,2,1,3]
print(solution(prices))