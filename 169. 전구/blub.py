def start_switch(n, blubs, target, status):
    count = 0
    if status:
        count += 1
        blubs[0] = (blubs[0] + 1) % 2
        blubs[1] = (blubs[1] + 1) % 2

    for i in range(1, n-1):
        if blubs[i-1] != target[i-1]:
            count += 1
            blubs[i - 1] = (blubs[i - 1] + 1) % 2
            blubs[i] = (blubs[i] + 1) % 2
            blubs[i + 1] = (blubs[i + 1] + 1) % 2

    if target == blubs:
        return count
    count += 1
    blubs[i] = (blubs[i] + 1) % 2
    blubs[i + 1] = (blubs[i + 1] + 1) % 2

    if target == blubs:
        return count
    else:
        return False


n = int(input())
b = list(map(int, list(input())))
t = list(map(int, list(input())))

tmp = start_switch(n, b, t, 1)
if tmp:
    print(tmp)

tmp = start_switch(n, b, t, 0)
if tmp:
    print(tmp)

