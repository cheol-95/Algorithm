N = int(input())
P = sorted(list(map(int, input().split())), reverse=False)

result = 0
for i in range(len(P), 0, -1):
    result += i*P[-i]

print(result)