pList = [0,1]
count = int(input())

for i in range(2,count+1):
    pList.append(pList[i-1]+pList[i-2])

print(pList[count])