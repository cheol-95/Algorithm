# def get_times(lines):
#     times = []
#     for time in lines:
#         ms = []
#         tmp = time.split(' ')
#         temp = list(map(float, tmp[1].split(':')))
#         ms.append(int(temp[0] * 60 * 60 + temp[1] * 60 + temp[2]) * 1000)
#         ms.append(ms[0] - int(float(tmp[2][:-1]) * 1000))
#         times.append(ms)
#
#     return times
#
# def solution(lines):
#     maximum = 0
#     times = get_times(lines)
#     times.sort(key=lambda x: x[-1])
#
#     for start, end in times:
#         count = 0
#         A, B = end, end + 999
#
#         for a, b in times:
#             if a <= A <= b or a <= B <= b or A <= a and b <= B:
#                 count += 1
#
#         maximum = maximum if maximum > count else count
#
#     return maximum
#
#
# lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
# print(solution(lines))

import copy

def rotation(key, N):
    tmp_key = copy.deepcopy(key)
    for y in range(N):
        for x in range(N):
            tmp_key[x][abs(N-1-y)] = key[y][x]
    return tmp_key

def get_input_maps(N, maps, t_key, y, x):
    for row in range(N):
        for col in range(N):
            maps[y + row][x + col] += t_key[row][col]
    return maps

def get_delete_maps(N, maps, t_key, y, x):
    for row in range(N):
        for col in range(N):
            maps[y + row][x + col] -= t_key[row][col]
    return maps

def check(maps, M):
    for y in range(M-1, M*2-1):
        for x in range(M-1, M*2-1):
            if maps[y][x] != 1:
                return False
    return True

def solution(key, lock):
    N, M = len(key), len(lock)

    t_length = M + 2 * (N-1)
    maps = [[0]*t_length for _ in range(t_length)]

    for y in range(M):
        for x in range(M):
            maps[y+N-1][x+N-1] = lock[y][x]

    for rotate in range(4):
        t_key = rotation(key, N)

        for y in range(t_length - N + 1):
            for x in range(t_length - N + 1):
                maps = get_input_maps(N, maps, t_key, y, x)

                if check(maps, M):
                    return True

                maps = get_delete_maps(N, maps, t_key, y, x)

    return False



key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))