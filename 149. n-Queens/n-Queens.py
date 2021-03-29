def possible(candidate, col):
    current_row = len(candidate)
    for row in range(current_row):
        if candidate[row] == col or abs(candidate[row] - col) == current_row - row:
            return False
    return True

def dfs(n, current_row, candidate, result):
    if current_row == n:
        result.append(candidate[:])
        return

    for col in range(n):
        if possible(candidate, col):
            candidate.append(col)
            dfs(n, current_row + 1, candidate, result)
            candidate.pop()

def solution(n):
    result = []
    dfs(n, 0, [], result)
    return len(result)

n = 4
print(solution(n))