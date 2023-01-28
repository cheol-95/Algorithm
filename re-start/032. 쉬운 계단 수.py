# def solution(N):
#     length_map = {n: {} for n in range(1, N+1)}
#     length_map[1] = {n: 1 for n in range(0, 10)}
#
#     for i in range(2, N+1):
#         for n in range(0, 10):
#             length_map[i][n] = 0
#             if n > 0:
#                 if i == 2:
#                     length_map[i][n] += 1
#                 else:
#                     length_map[i][n] += length_map[i-1][n-1]
#             if n < 9:
#                 if i == 2:
#                     length_map[i][n] += 1
#                 else:
#                     length_map[i][n] += length_map[i-1][n+1]
#
#
#     # for k, v in length_map.items():
#     #     print(k, v)
#     return sum(list(length_map[N].values())[1:]) % 1000000000
#
# N = 3
# print(solution(N))


N = int(input())
length_map = {n: {} for n in range(1, N+1)}
length_map[1] = {n: 1 for n in range(0, 10)}

for i in range(2, N+1):
    for n in range(0, 10):
        length_map[i][n] = 0
        if n > 0:
            if i == 2:
                length_map[i][n] += 1
            else:
                length_map[i][n] += length_map[i-1][n-1]
        if n < 9:
            if i == 2:
                length_map[i][n] += 1
            else:
                length_map[i][n] += length_map[i-1][n+1]

print(sum(list(length_map[N].values())[1:]) % 1000000000)