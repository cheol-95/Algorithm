def solution(n):
    count = [1,2]
    for i in range(2, n):
        count.append(count[i-2] + count[i-1])
    return count[n-1] % 1234567

n = 6
print(solution(n))