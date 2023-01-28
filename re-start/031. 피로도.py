def solution(k, dungeons):
    dungeons.sort(key= lambda x:  ((x[1]+x[0])/x[0] ,x[1]))
    cnt = 0
    for r, p in dungeons:
        if k < r:
            break
        k -= p
        cnt += 1
    return cnt


k, dungeons = 80, [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))

# # import itertools
# # def solution(k, dungeons):
# #     res = 0
# #     for row in list(itertools.permutations(dungeons)):
# #         cnt = 0
# #         t_k = k
# #         for r, p in row:
# #             if t_k < r:
# #                 break
# #             t_k -= p
# #             cnt += 1
# #         res = max(res, cnt)
# #     return res
#
# answer = 0
# N = 0
# visited = []
#
#
# def dfs(k, cnt, dungeons):
#     print(visited)
#     global answer
#     if cnt > answer:
#         answer = cnt
#
#     for j in range(N):
#         if k >= dungeons[j][0] and not visited[j]:
#             visited[j] = 1
#             dfs(k - dungeons[j][1], cnt + 1, dungeons)
#             visited[j] = 0
#
#
# def solution(k, dungeons):
#     global N, visited
#     N = len(dungeons)
#     visited = [0] * N
#     dfs(k, 0, dungeons)
#
#     return answer
#
# k, dungeons = 80, [[80, 20], [50, 40], [30, 10]]
# print(solution(k, dungeons))