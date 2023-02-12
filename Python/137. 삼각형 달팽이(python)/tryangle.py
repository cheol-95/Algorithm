def solution(n):
    left = [[] for _ in range(n)]
    right = [[] for _ in range(n)]
    flags = ['down', 'right', 'up']
    length = sum(range(n + 1))

    count = 0
    height = -1
    flag = 0
    for idx in range(1, length + 1):
        if count == n:
            count = 0
            n -= 1
            flag += 1
            flag %= 3

        if flags[flag] == 'down':
            height += 1
            left[height].append(idx)

        if flags[flag] == 'right':
            left[height].append(idx)

        if flags[flag] == 'up':
            height -= 1
            right[height].insert(0, idx)
        count += 1

    length = len(left)
    answer = []
    for idx in range(length):
        answer += left[idx] + right[idx]

    return answer