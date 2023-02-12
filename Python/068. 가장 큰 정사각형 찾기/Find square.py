# def solution(board):
#     answer = [1]
#     ylength = len(board)
#     xlength = len(board[0])
#     cnt = 2
#     for i in range(ylength-1):
#         if i + cnt > ylength:
#             break
#         for j in range(xlength-1):
#             if board[i][j] == 1:
#                 flag = True
#                 while flag == True:
#                     if j + cnt > xlength:
#                         break
#                     for y in range(cnt):
#                         for x in range(cnt):
#                             if not board[i+y][j+x]:
#                                 flag = False
#                                 break
#                     if flag == True:
#                         answer.append(cnt**2)
#                         cnt += 1
#     return max(answer)

def square(board, y, x, cnt):
    li = [1]
    while True:
        try:
            for i in range(0,cnt):
                for j in range(0,cnt):
                    if not board[y+i][x+j]:
                        return [max(li),cnt]
            li.append(cnt**2)
            cnt += 1
        except:
            return [max(li), cnt]

def solution(board):
    answer = [1]
    ylength = len(board)
    xlength = len(board[0])
    cnt = 2
    for i in range(ylength-1):
        if ylength < i + cnt -1:
            break
        for j in range(xlength-1):
            if xlength < j + cnt - 1:
                break
            if board[i][j]:
                tmp = square(board, i, j, cnt)
                answer.append(tmp[0])
                cnt = tmp[1]
    return max(answer)



board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))