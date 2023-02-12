def solution(n, lost, reserve):
    cnt = len(lost)
    for i in range(len(lost)):
        if lost[i] - 1 in reserve:
            reserve.remove(lost[i]-1)
            cnt -= 1
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            cnt -= 1
    return n-cnt

# n, lost, reserve = 5, [2,4], [1,3,5]
# n, lost, reserve = 5, [2,4], [3]
# n, lost, reserve = 3, [3], [1]
print(solution(n, lost, reserve))