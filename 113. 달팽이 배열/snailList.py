n = int(input())
snail = [['  '] * n for i in range(n)]  # 초기화
y, x = 0, -1  # 행과 열의 시작
status = 1  # 행과 열의 증감을 다루기 위한 변수

# 첫번째 줄 완성
for p in range(n):
    x = x + status
    snail[y][x] = '# '
n -= 1
while True:
    if n <= 0:
        break
    for p in range(n):
        y += status
        snail[y][x] = '# '
    status = status * -1

    for p in range(n):
        x += status
        snail[y][x] = '# '
    n -= 2

for i in snail:
    print(''.join(i))