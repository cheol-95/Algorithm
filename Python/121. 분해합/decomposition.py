N = int(input())

for i in range(N):
  temp = i

  for j in str(i):
    temp += int(j)

  if temp == N:
    print(i)
    break
else:
  print(0)