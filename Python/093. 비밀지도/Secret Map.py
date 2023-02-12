def solution(n, arr1, arr2):
    for i in range(len(arr1)):
        sum = bin(arr1[i] | arr2[i])[2:].replace('1','#').replace('0',' ')
        if len(sum) < n:
            sum = ' '*(n-len(sum))+sum
        arr1[i] = sum
    return arr1

n, arr1, arr2 = 5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]
n, arr1, arr2 = 6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))
tmp = bin(30)[2:]