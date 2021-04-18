s1, s2 = [], []
n = 5

for i in range(1, n+1):
    s1.append(i)
    s2.append(s1.pop())

for i in s2:
    print(i)