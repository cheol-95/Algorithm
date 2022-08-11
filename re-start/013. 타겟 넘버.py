import collections
def solution(numbers, target):
    answer = 0
    end_idx = len(numbers)
    stack = [[numbers[0], 1], [-numbers[0], 1]]
    stack = collections.deque(stack)

    while stack:
        num, now = stack.popleft()
        if now == end_idx:
            if num == target:
                answer += 1
            continue
        stack.append([num+numbers[now], now + 1])
        stack.append([num-numbers[now], now + 1])
    return answer

numbers, target = [4, 1, 2, 1], 4
print(solution(numbers, target))

