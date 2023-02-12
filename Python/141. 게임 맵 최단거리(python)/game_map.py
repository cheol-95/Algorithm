import collections

def solution(maps):
    my, mx = len(maps), len(maps[0])
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    queue = collections.deque([[0, 0]])
    while queue:
        y, x = queue.popleft()

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if ny == my - 1 and nx == mx-1:
                return maps[y][x] + 1

            if 0 <= ny < my and 0 <= nx < mx and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append([ny, nx])

    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))