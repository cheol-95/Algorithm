def solution(dirs):
    loads = []
    point = [0, 0]
    for move in dirs:
        start = (''.join(map(str, point)))
        if move == 'U':
            if point[0] == 5:
                continue
            point[0] += 1

        elif move == 'D':
            if point[0] == -5:
                continue
            point[0] -= 1

        elif move == 'L':
            if point[1] == -5:
                continue
            point[1] -= 1

        elif move == 'R':
            if point[1] == 5:
                continue
            point[1] += 1

        end = (''.join(map(str, point)))
        loads += [start+end, end+start]

    return len(set(loads)) // 2

dirs = "LULLLLLLU"
tmp = solution(dirs)
print(tmp)