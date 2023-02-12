def solution(N, stages):
    answer = []
    res = []
    uCnt = len(stages)
    for i in range(N):
        answer.append(stages.count(i+1)/uCnt)
        uCnt -= stages.count(i+1)
    for i,v in enumerate(answer):
        res.append(answer.index(max(answer))+1)
        answer[answer.index(max(answer))] = -1
    return res