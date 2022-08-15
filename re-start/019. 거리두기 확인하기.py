import collections
def bfs(place, y, x):
    direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    v = [[y, x]]
    q = collections.deque([[y, x, 0]]) # 좌표, length
    while q:
        [n_y, n_x, length] = q.popleft()
        for d_y, d_x in direct:
            t_y, t_x = n_y + d_y, n_x + d_x
            if 0 <= t_y <= 4 and 0 <= t_x <= 4 and [t_y, t_x] not in v and length <= 1:
                if place[t_y][t_x] == 'P':
                    return False
                if place[t_y][t_x] == 'O':
                    q.append([t_y, t_x, length+1])
                    v.append([t_y, t_x])
    return True

def check(place):
    for y in range(len(place)):
        for x in range(len(place[y])):
            if place[y][x] == 'P' and not bfs(place, y, x):
                return 0
    return 1

def solution(places):
    return [check(place) for place in places]

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))