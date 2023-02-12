def solution(n, computers):
    answer = 0
    for i in range(len(computers)):
        if answer < computers[i].count(0):
            answer = computers[i].count(0)
    return answer


n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))