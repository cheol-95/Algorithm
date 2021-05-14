import sys
input = sys.stdin.readline

N = int(input())
D = [0] * (N + 1)
t = 2

while t <= N:
    candidate = 1000
    if t % 3 == 0:
        candidate = D[t // 3] + 1 if D[t // 3] + 1 < candidate else candidate
    if t % 2 == 0:
        candidate = D[t // 2] + 1 if D[t // 2] + 1 < candidate else candidate
    if D[t-1]:
        candidate = D[t - 1] + 1 if D[t - 1] + 1 < candidate else candidate
    D[t] = candidate
    t += 1

print(D[N])


