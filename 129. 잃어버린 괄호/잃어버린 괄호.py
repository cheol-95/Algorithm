k = input().split('-')
s = 0

for i in k[0].split('+'):
    s += int(i)

for i in k[1:]:
    for j in i.split('+'):
        s -= int(j)

print(s)