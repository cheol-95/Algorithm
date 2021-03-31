def get_score(n, results):
    score = [[0] * n for _ in range(n)]

    for a, b in results:
        score[a-1][b-1] = 1
        score[b-1][a-1] = -1

    return score

def solution(n, results):
    result = 0
    score = get_score(n, results)

    for middle in range(n):
        for start in range(n):
            for end in range(n):
                if score[start][middle] == 1 and score[middle][end] == 1:
                    score[start][end] = 1
                if score[start][middle] == -1 and score[middle][end] == -1:
                    score[start][end] = -1

    for row in score:
        if row.count(1) + row.count(-1) == n -1:
            result += 1

    return result


n, results = 5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n ,results))