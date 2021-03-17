def check(query, info):
    for idx in range(4):
        if query[idx] != '-' and query[idx] != info[idx]:
            return False
    if int(query[4]) > int(info[4]):
        return False
    return True

def solution(info, query):
    answer = []
    info = list(map(lambda x: x.split(' '), info))
    query = list(map(lambda x: x.replace(' and ', ' ').split(' '), query))

    for q in query:
        count = 0
        for i in info:
            if check(q, i):
                count += 1
        answer.append(count)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
tmp = solution(info, query)
print(tmp)