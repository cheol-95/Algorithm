times = [list(map(int, input().split())) for _ in range(int(input()))]
times.sort(key = lambda time: time[0])
times.sort(key = lambda time: time[1])

cnt, start = 0, 0

for time in times:
    if time[0] >= start:
        start = time[1]
        cnt += 1

print(cnt)
