def check_same(arr, sub_y, sub_x, size):
    num = arr[sub_y][sub_x]
    for y in range(sub_y, sub_y+size):
        for x in range(sub_x, sub_x+size):
            if arr[y][x] not in [num, 5] :
                return False
    return True

def change_arr(arr, sub_y, sub_x, size):
    num = arr[sub_y][sub_x]
    for y in range(sub_y, sub_y+size):
        for x in range(sub_x, sub_x+size):
            arr[y][x] = 5
    arr[sub_y][sub_x] = num
    return arr

def solution(arr):
    answer = [0, 0]
    size = 2
    length = len(arr)

    while size <= length:
        for y in range(0, length, size):
            for x in range(0, length, size):
                if check_same(arr, y, x, size):
                    arr = change_arr(arr, y, x, size)
        size *= 2

    for row in arr:
        answer[0] += row.count(0)
        answer[1] += row.count(1)

    return answer

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
# arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr =  [[0,0],[0,0]]
print(solution(arr))