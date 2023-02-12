def solution(heights):
    answer = [0]
    for i in range(len(heights)):
        for j in range(i):
            # 실제 인덱스 : i , i-j-1
            if(max(heights[:i]) <= heights[i-j]):  #앞의 맥스보다 해당값이 클경우
                answer.append(0)
                break
            if(heights[i] < heights[i-j-1]): # 앞이 더 클경우
                answer.append(i-j) # 입력 인덱스 : 실제 인덱스 +1
                break
    return answer

heights = [1,5,3,9,7,6,5]
print(solution(heights))

# [1,5,3,9,7,6,5]
# [0,0,2,0,4,5,6]


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