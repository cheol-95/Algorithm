N, M = map(int, input().split())
history = list(map(int, input().split()))
total = [history[0]]

for i in range(1, N):
    total.append(total[i-1] + history[i])

for _ in range(M):
    res =''
    s, e = map(int, input().split())

    if s == 1:
        res = total[e-1]
    else:
        res = total[e-1] - total[s-2]

    if res > 0:
        res = '+' + str(res)
    print(res)
