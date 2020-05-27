# def solution(n):
#     answer = 0
#     for i in range(1,n//2+1):
#         sum = 0
#         for j in range(i,n):
#             sum += j
#             if sum == n:
#                 answer += 1
#                 break
#             if sum > n:
#                 break
#     return answer+1

def solution(n):
    answer = 0
    for i in range(1,n+1,2):
        if n%i == 0:
            answer+=1
    return answer

n = 15
print(solution(n))