import collections
def solution(grid):
    rows, cols = len(grid), len(grid[0])
    loads = []
    dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    starts = []
    for r in range(rows):
        for c in range(cols):
            for d in range(0, 4):
                starts.append(f'{r},{c},{d}')

    load_map = collections.defaultdict(int)
    for start in starts:
        cnt = 0
        next = start
        while load_map[next] == 0:
            if load_map[next]:
                break
            cnt += 1
            load_map[next] = 1
            y, x, d_idx = map(int, next.split(','))
            y, x = y % rows, x % cols
            if grid[y][x] == 'L':
                d_idx = (d_idx - 1) % 4
            elif grid[y][x] == 'R':
                d_idx = (d_idx + 1) % 4
            dy, dx = dr[d_idx]
            next = f'{(y + dy) % rows},{(x + dx) % cols},{d_idx}'
        if cnt:
            loads.append(cnt)

    return sorted(loads)

# def solution(grid):
#     R, C = len(grid), len(grid[0])
#     dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌
#     grf = [[[0,0,0,0] for _ in range(C)] for _ in range(R)]  # 상우하좌
#
#     def solve(x, y, d):
#         res = 0
#         while not grf[x][y][d]:
#             grf[x][y][d] = 1
#             x, y = (x+dxy[d][0]) % R, (y+dxy[d][1]) % C
#             if grid[x][y] == 'L': d = (d+1) % 4
#             elif grid[x][y] == 'R': d = (d-1) % 4
#             res += 1
#         return res
#
#
#     ans = []
#     for i in range(R):
#         for j in range(C):
#             for k in range(4):
#                 if grf[i][j][k] == 0:
#                     ans.append(solve(i, j, k))
#     return sorted(ans)

# grid = ["SL", "LR"]
# grid = ["S"]
grid = ["R", "R"]
# grid = ["S", "S"]

print(solution(grid))