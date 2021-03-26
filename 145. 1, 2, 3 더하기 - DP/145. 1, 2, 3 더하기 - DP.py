T = int(input())
answer = [int(input()) for _ in range(T)]
count = [1, 2, 4]

for idx in range(3, max(answer)):
    count.append(count[idx-1] + count[idx-2] + count[idx-3])

for idx in answer:
    print(count[idx-1])

