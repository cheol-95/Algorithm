def solution(nums):
    return min(len(nums)//2, len(set(nums)))

nums = [3,3,3,2,2,4]
print(solution(nums))