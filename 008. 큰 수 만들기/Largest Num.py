def solution(number, k):
    answer = ''
    li = []
    mIndex = 0
    for i in range(len(number)):
        li.append(int(number[i]))

    for i in range(len(number)-k,0,-1):
        max1 = max(li[mIndex:len(number) - i+1])
        answer += str(max1)
        mIndex = li.index(max1)+1
    return answer

# number, k = "1924", 2
# number, k = "1231234", 3
number, k = "4177252841", 4
print(solution(number, k))