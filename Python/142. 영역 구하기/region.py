def check_square(area, position):
    for y in range(position[1], position[3]):
        for x in range(position[0], position[2]):
            area[y][x] = True
    return area


def is_empty_area(area, y, x):
    for sub_y in range(y):
        for sub_x in range(x):
            if area[sub_y][sub_x] == 0:
                return [sub_y, sub_x]
    return False


def get_area(area, start, y, x):
    stack = [start]
    count = 1
    area[start[0]][start[1]] = 1
    while stack:
        tmp_y, tmp_x = stack.pop()

        if tmp_y < y - 1 and area[tmp_y + 1][tmp_x] == 0:
            stack.append([tmp_y + 1, tmp_x])
            area[tmp_y + 1][tmp_x] = area[tmp_y][tmp_x] + 1
            count += 1

        if 0 < tmp_y and area[tmp_y - 1][tmp_x] == 0:
            stack.append([tmp_y - 1, tmp_x])
            area[tmp_y - 1][tmp_x] = area[tmp_y][tmp_x] + 1
            count += 1

        if tmp_x < x - 1 and area[tmp_y][tmp_x + 1] == 0:
            stack.append([tmp_y, tmp_x + 1])
            area[tmp_y][tmp_x + 1] = area[tmp_y][tmp_x] + 1
            count += 1

        if 0 < tmp_x and area[tmp_y][tmp_x - 1] == 0:
            stack.append([tmp_y, tmp_x - 1])
            area[tmp_y][tmp_x - 1] = area[tmp_y][tmp_x] + 1
            count += 1

    return area, count

M, N, K = list(map(int, input().split(' ')))
area = [[False] * N for _ in range(M)]
for row in range(K):
    area = check_square(area, list(map(int, input().split())))

result = []

while is_empty_area(area, M, N):
    start = is_empty_area(area, M, N)
    area, count = get_area(area, start, M, N)
    result.append(count)

print(len(result))
print(' '.join(map(str, sorted(result))))
