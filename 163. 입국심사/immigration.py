def solution(n, times):
    result = 0
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        count = sum(map(lambda x: mid // x, times))

        if count >= n:
            result = mid
            right = mid - 1
        elif count < n:
            left = mid + 1

    return result

n, times = 6, [7, 10]
print(solution(n, times))