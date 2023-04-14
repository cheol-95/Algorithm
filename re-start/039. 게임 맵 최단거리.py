from collections import deque

def solution(maps):
    my, mx = len(maps), len(maps[0])
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque([[0, 0]])
    while queue:
        y, x = queue.popleft()
        dirs_points = list(map(lambda d: [y + d[0], x + d[1]], dirs))
        for ny, nx in dirs_points:
            if ny == my - 1 and nx == mx-1:
                return maps[y][x] + 1
            if -1 < ny < my and -1 < nx < mx and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append([ny, nx])
    return -1

maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
# maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(maps))