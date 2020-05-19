def solution(citations):
    answer = []
    for i in citations:
        tmp = list(map(lambda x:x>=i, citations))
        cnt = tmp.count(True)
        insert = i
        for index,value in enumerate(tmp):
            if not value and citations[index] > cnt:
                insert = 0
                break
        answer.append(insert)
    return max(answer)

citations = [3,0,6,1,5]
print(solution(citations))