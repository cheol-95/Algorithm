from collections import deque
def solution(board, moves):
    answer = 0
    basket = deque([])
    board_q = [deque([]) for _ in range(len(board))]
    for row in board:
        for idx, doll in enumerate(row):
            if doll != 0: board_q[idx].append(doll)

    for idx in moves:
        if len(board_q[idx - 1]):
            doll = board_q[idx - 1].popleft()
            basket.append(doll)

            while len(basket) >= 2 and basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2

    return answer


board, moves = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))