import collections

def solution(maps):
    max_y, max_x = len(maps), len(maps[0])
    queue = collections.deque([[0, 0, 1]])
    position = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    while queue:
        y, x, cnt = queue.popleft()
        maps[y][x] = 0

        for ny, nx in position:
            dy, dx = ny + y, nx + x

            if y == max_y - 1 and x == max_x - 1:
                return cnt

            if 0 <= dy < max_y and 0 <= dx < max_x and maps[dy][dx] == 1:
                maps[dy][dx] = 0
                queue.append([dy, dx, cnt + 1])

    return -1


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))