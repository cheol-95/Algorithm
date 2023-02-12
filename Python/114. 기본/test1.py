# def solution1(height):
#     for i in range(1, len(height)):
#         if height[i-1] > height[i]:
#             for idx, val in enumerate(height):
#                 if height[i] < val:
#                     return idx + 1
#
# height = [1,1,3,3,4,1]
# print(solution1(height))

#--------------------------------

# def solution2(arr):
#     for i, v in enumerate(arr):
#         bin_num = bin(v)
#         if bin_num[2] == '1' and bin_num[3:] == '0'*len(bin_num[3:]):
#             arr[i] = 1
#         else:
#             arr[i] = 0
#     return arr
#
# arr = [1,3,8,12,16]
# print(solution2(arr))

#--------------------------------
# 
# def _check(t, u):
#     for i in range(0, len(t), len(u)):  # 반복확인
#         if u != t[i:i + len(u)]:
#             return False
#     return True
# 
# def solution3(s ,t):
#     if not _check(s, t):
#         return -1
#     s = t
#     while True:
#         flag = False
#         for i in range(1, len(s)//2+1):
#             t = s[0:i] # 비교할 문자열 -> 조그만 문자열
#             if _check(s, t): # 체크가 True면!
#                 s = t
#                 flag = True
#                 break
#         if not flag:
#             return len(s)
# 
# s, t = 'bcdbcdbcdbcd', 'bcdbcd'
# print(solution3(s, t))
