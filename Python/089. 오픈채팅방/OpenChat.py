def solution(record):
    answer = []
    id_nic = {}
    for i in record:
        spt = i.split()
        if spt[0] == 'Enter' or spt[0] == 'Change':
            id_nic[spt[1]]= spt[2]

    for i in record:
        spt = i.split()
        tmp = '' + id_nic[spt[1]]
        if spt[0] == 'Enter':
            tmp += '님이 들어왔습니다.'
        elif spt[0] == 'Leave':
            tmp += '님이 나갔습니다.'
        else:
            continue
        answer.append(tmp)
    return answer

record=	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))