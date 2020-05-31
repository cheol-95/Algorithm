def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for k in range(len(arr2[0])):
            sum = 0
            for j in range(len(arr1[0])):
                sum += arr1[i][j]*arr2[j][k]
            tmp.append(sum)
        answer.append(tmp)
    return answer

arr1, arr2 =[[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]
print(solution(arr1,arr2))