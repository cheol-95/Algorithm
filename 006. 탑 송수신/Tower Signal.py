def solution(heights):
    answer = [0]
    for i in range(len(heights)):
        for j in range(i):
            # 실제 인덱스 : i , i-j-1
            if(max(heights[:i]) <= heights[i-j]):
                answer.append(0)
                break
            if(heights[i] < heights[i-j-1]):
                answer.append(i-j) # 입력 인덱스 : 실제 인덱스 +1
                break
    return answer

heights = [1,5,3,6,7,6,5]
print(solution(heights))

'''
def solution(heights):
    answer = [0] * len(heights)
    for i in range(len(heights)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j+1
                break
    return answer
'''