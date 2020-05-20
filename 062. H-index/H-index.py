def solution(citations):
    for i in range(len(citations),0,-1):
        up = list(map(lambda x:x>=i, citations)).count(True)
        down = list(map(lambda x:x<i, citations)).count(True)
        if up >= i and down <= i:
            return i
    return 0

citations = [3,0,6,1,5]
print(solution(citations))