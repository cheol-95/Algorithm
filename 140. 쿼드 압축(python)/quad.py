def solution(arr):
    def check(y, x, size):
        if size == 1:
            return [0, 1] if arr[y][x] == 1 else [1, 0]

        next_size = size // 2
        one = check(y, x, next_size)
        two = check(y, x + next_size, next_size)
        three = check(y + next_size, x, next_size)
        four = check(y + next_size, x + next_size, next_size)

        if one == two == three == four:
            return one
        else:
            return list(map(sum, zip(one, two, three, four)))

    return check(0, 0, len(arr))

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
# arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr =  [[0,0],[0,0]]
print(solution(arr))