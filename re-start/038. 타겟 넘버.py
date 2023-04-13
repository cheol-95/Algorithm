# from collections import deque
# def solution(numbers, target):
#     answer = 0
#     dq = deque([[0, 0]])
#     while dq:
#         tmp_sum, idx = dq.pop()
#         if idx == len(numbers):
#             if tmp_sum == target:
#                 answer += 1
#             continue
#         dq.append([tmp_sum + numbers[idx], idx+1])
#         dq.append([tmp_sum - numbers[idx], idx+1])
#     return answer

from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


# numbers, target = [1, 1, 1, 1, 1], 3
numbers, target = [4, 1, 2, 1], 4

print(solution(numbers, target))