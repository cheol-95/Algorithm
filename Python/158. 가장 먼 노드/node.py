import collections

def get_vertex(edge):
    vertex = collections.defaultdict(list)
    for a, b in edge:
        vertex[a].append(b)
        vertex[b].append(a)
    return vertex

def solution(n, edge):
    dist = [0] * n
    dist[0] = 1
    vertex = get_vertex(edge)
    queue = collections.deque([[1, 0]])

    while queue:
        start, count = queue.popleft()

        for end in vertex[start]:
            if not dist[end-1]:
                queue.append([end, count+1])
                dist[end - 1] = count+1

    return dist.count(max(dist))



n, edge = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))