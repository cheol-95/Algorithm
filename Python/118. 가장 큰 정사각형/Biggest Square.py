def solution(board):
    answer = 0
    row = len(board)
    colum=len(board[0])
    max_length = 0
    
    if len(board) < 3 or len(board[0]) < 3:
        for i in board:
            for j in i:
                if j == 1:
                    max_length = 1
        
    for i in range(row):
        for j in range(colum):
            if i==0 or j==0:
                continue
            if board[i][j]:
                board[i][j]=min(board[i-1][j-1], board[i-1][j], board[i][j-1])+1
                if board[i][j] > max_length:
                    max_length = board[i][j]
                    
    return max_length**2