N = int(input(''))
P = sorted(list(map(int, input().split())),reverse=True)
result = 0
for i,v in enumerate(P):
    result += (i+1)*v
print(result)