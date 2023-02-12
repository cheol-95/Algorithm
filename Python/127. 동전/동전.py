N, money = list(map(int, input().split()))
coin_list = sorted([int(input()) for _ in range(N)], reverse=True)
result = 0

for coin in coin_list:
    if money >= coin:
        result += money//coin
        money %= coin

print(result)

