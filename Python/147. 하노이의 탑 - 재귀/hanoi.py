def hanoi(num, start, end, mid, result):
    if num == 1:
        result.append([start, end])
        return
    hanoi(num - 1, start, mid, end, result)
    result.append([start, end])
    hanoi(num - 1, mid, end, start, result)

def solution(n):
    result = []
    hanoi(n, 1, 3, 2, result)
    return result

n = 4
print(solution(n))