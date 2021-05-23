import collections
def bfs(computers, visit, com, n):
    queue = collections.deque([com])
    while queue:
        d_com = queue.popleft()
        visit[d_com] = 1
        for tmp in range(n):
            if computers[d_com][tmp] and not visit[tmp]:
                queue.append(tmp)


def solution(n, computers):
    answer = 0
    visit = [0 for _ in range(n)]    
    for com in range(n):
        if not visit[com]:
            bfs(computers, visit, com, n)
            answer += 1
    return answer


n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))