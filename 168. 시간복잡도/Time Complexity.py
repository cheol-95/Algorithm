N = int(input())
mod = 5
res = 0

while N >= mod:
    res += N // mod
    mod *= 5

print(res)
