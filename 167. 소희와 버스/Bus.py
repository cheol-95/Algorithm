N, T = map(int, input().split())
bus = [list(map(int, (input().split()))) for _ in range(N)]
result = [1000, 999999]

for idx, (s, d) in enumerate(bus):
    while s < T:
        s += d
    if s < result[1]:
        result = [idx + 1, s]

print(result[0])