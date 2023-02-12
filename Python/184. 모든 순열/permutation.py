def back_tracking(numbers, N, v):
    if len(v) == N:
        print(*v)
        return

    for idx, num in enumerate(numbers):
        if num not in v:
            v.append(num)
            back_tracking(numbers, N, v)
            v.pop()

res = []
N = int(input())
back_tracking(range(1, N+1), N, [])

