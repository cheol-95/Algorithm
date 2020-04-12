money = int(input(''))
charge = 1000-money
coin = [500,100,50,10,5,1]

cnt = 0
for i in range(len(coin)):
    while charge >= coin[i]:
        charge -= coin[i]
        cnt +=1

print(cnt)