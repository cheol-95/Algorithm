def rotate(board, query):
    y_1, x_1, y_2, x_2 = query
    start = board[y_1][x_1]
    cand = [start]

    for y in range(y_1, y_2):
        cand.append(board[y+1][x_1])
        board[y][x_1] = board[y+1][x_1]

    for x in range(x_1, x_2):
        cand.append(board[y_2][x+1])
        board[y_2][x] = board[y_2][x+1]

    for y in range(y_2, y_1, -1):
        cand.append(board[y-1][x_2])
        board[y][x_2] = board[y-1][x_2]

    for x in range(x_2, x_1, -1):
        cand.append(board[y_1][x-1])
        board[y_1][x] = board[y_1][x-1]

    board[query[0]][query[1] + 1] = start
    return board, min(cand)

def solution(rows, columns, queries):
    answer = []
    board = [[c+(r*columns) for c in range(1, columns + 1)] for r in range(rows)]
    for query in queries:
        query = list(map(lambda x: x-1, query))
        board, minimum = rotate(board, query)
        answer.append(minimum)
    return answer

rows, columns, queries = 6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
print(solution(rows, columns, queries))
