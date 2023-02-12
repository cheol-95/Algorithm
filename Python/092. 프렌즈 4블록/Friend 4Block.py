def solution(m, n, board):
    answer = 0
    sum = 1
    board_list = [[i for i in j] for j in board]
    tmp = [[0 for q in range(n)] for _ in range(m)]
    while sum != 0:
        sum = 0
        for x in range(m - 1):
            for y in range(n - 1):
                if board_list[x][y] == 0:
                    continue
                if  board_list[x][y] == board_list[x+1][y] == board_list[x][y+1] == board_list[x+1][y+1]:
                    tmp[x][y] = tmp[x+1][y] = tmp[x][y+1] = tmp[x+1][y+1] = 1
        for i in tmp:
            sum += i.count(1)
        for x in range(m):
            for y in range(n):
                if tmp[x][y] == 1:
                    tmp[x][y] = 0
                    for k in range(x,0,-1):
                        board_list[k][y] = board_list[k-1][y]
                        if k == 1:
                            board_list[k-1][y] = 0
        answer += sum
    return answer


m, n, board = 4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))