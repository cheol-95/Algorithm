def makestr(num, length):
    cnt = 1
    s = '0'
    numstr = { 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F' }
    while len(s) < length:
        tmp = ''
        tcnt = cnt
        while tcnt >= 1:
            if tcnt % num >= 10:
                tmp += numstr[tcnt % num]
            else:
                tmp += str(tcnt % num)
            tcnt //= num
        tmp += str(tcnt // 8)
        tmp = tmp[::-1]
        if tcnt // num == 0:
            tmp = tmp[1:]
        cnt += 1
        s += tmp
    return s

def solution(n, t, m, p):
    answer = ''
    nums = makestr(n, t*m)[:t*m]
    for i in range(len(nums)):
        if i%m == p-1:
            answer += nums[i]
    return answer

# n, t, m, p = 2,4,2,1
# n, t, m, p = 16, 16, 2, 1
n, t, m, p = 16,16,2,2
print(solution(n,t,m,p))
