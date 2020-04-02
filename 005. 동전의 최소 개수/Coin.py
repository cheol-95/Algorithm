def solution(n, k):
    answer = 0
    list = []
    for i in range(n):
        list.append(int(input()))

    while k != 0:
        if(k >= list[len(list)-1]):
            k -= list[len(list)-1]
            answer += 1
        else:
            list.pop()
    return answer

N = 10
K = 4200
# list = [1,5,10,50,100,500,1000,5000,10000,50000]
print(solution(N, K))