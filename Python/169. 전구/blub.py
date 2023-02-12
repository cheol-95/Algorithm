def change(n):
    return (n+1) % 2


def set_pair(now, count):
    if count:
        now[:2] = [change(now[0]), change(now[1])]

    for i in range(1, N):
        if now[i-1] != target[i-1]:
            count += 1
            now[i-1] = change(now[i-1])
            now[i] = change(now[i])
            if i < N-1:
                now[i+1] = change(now[i+1])
    return count if now == target else -1


N = int(input())
now = list(map(int, input()))
target = list(map(int, input()))

res1 = set_pair(now[:], 0)
res2 = set_pair(now[:], 1)

if res1 >= 0 and  res2 >= 0:
    print(min(res1, res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print(-1)