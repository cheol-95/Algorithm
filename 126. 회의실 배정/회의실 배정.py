start_time, end_time = 1, 0
tmp = [0, 0]

n = int(input())

times = [list(map(int, input().split())) for _ in range(n)]

times.sort(key = lambda x: x[0])

for time in times:
    if time[0] >= start_time:
        tmp = time

print(times)


