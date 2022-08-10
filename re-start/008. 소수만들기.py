import itertools
def solution(nums):
    answer = 0
    sums = list(map(sum, itertools.combinations(nums, 3)))
    M = max(sums)
    era = [True for _ in range(M)]
    for i in range(2, M//2+1):
        if era[i-1]:
            for j in range(i + i, M+1, i):
                era[j-1] = False
    for n in sums:
        if era[n-1]:
            answer +=1
    return answer

nums = [1,2,7,6,4]
print(solution(nums))