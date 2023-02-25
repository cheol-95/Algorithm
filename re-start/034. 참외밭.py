# K = 7
# loads = [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]]


# K = int(input())
# loads = [list(map(int, input().split())) for _ in range(6)]
# res = 0
# visit_d = [0, 0, 0, 0]
# for idx, [d, l] in enumerate(loads):
#     visit_d[d-1] = 1
#     p_d = d - 1 if d % 2 == 0 else d + 1
#     if visit_d[p_d - 1] and not res:
#         [pre_d, pre_l] = loads[idx-1]
#         area_1 = pre_l*l
#
#         tmp = loads[idx+2:idx+4]
#         area_2 = tmp[0][1] * tmp[1][1]
#
#         area = area_1 + area_2
#         res = area * K
#
# print(res)


# K = int(input())
# loads = [list(map(int, input().split())) for _ in range(6)]

K = 7
loads = [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]]

K = int(input())
loads = [list(map(int, input().split())) for _ in range(6)]
area = 0
lengths = [0, 0, 0, 0]
prev_d = loads[-1][0]
exclude_directs = [[1, 3], [2, 4], [3, 2], [4, 1]]
for idx, [d, l] in enumerate(loads):
    lengths[d-1] += l
    for [prev_d, now_d] in exclude_directs:
        if prev_d == loads[idx-1][0] and d == now_d:
            area -= loads[idx - 1][1] * l

area += lengths[1] * lengths[3]
print(area * K)
#
# 1 > 3
# 2 > 4
# 3 > 2
# 4 > 1