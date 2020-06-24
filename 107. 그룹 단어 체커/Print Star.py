def star(n):
    for i in range(n//3):
        for j in range(n//3):
            if i == 1 and j == 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()


# n = int(input())
n = 27
print(star(n))