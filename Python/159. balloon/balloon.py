def solution(a):
    result = 1
    length = len(a)
    left, right = a[0], a[-1]
    maps = [[0 for _ in range(length)] for q in range(2)]

    for idx in range(length):
        if left > a[idx]:
            left = a[idx]
            maps[0][idx] = True

    for idx in range(length-1, -1, -1):
        if right > a[idx]:
            right = a[idx]
            maps[1][idx] = True

    for map in maps:
        result += map.count(True)

    return result

a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
# a = [3, 2, 1]
print(solution(a))