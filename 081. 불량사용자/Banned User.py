def equal(x,y):
    for i in range(len(x)):
        if x[i] == '*':
            y = y[:i] + '*' + y[i + 1:]
    if x == y:
        return True
    return False

def solution(user_id, banned_id):
    answer = 1
    li = []
    for i in range(len(banned_id)):
        tmp = []
        for j in range(len(user_id)):
            if len(banned_id[i]) == len(user_id[j]) and equal(banned_id[i], user_id[j]):
                tmp.append(j)
        li.append(tmp)
    print(li)
    i = 0
    while i < len(li):
        if li[i] in li[:i]+li[i+1:]:
            dlt = li[i]
            ntmp = 0
            while li[i] in li[:i]+li[i+1:]:
                ntmp += 1
                del li[li.index(dlt)]
            del li[li.index(dlt)]
            i -= ntmp
        i += 1

    for i in range(len(li)):
        if li[i] == [-1]:
            break
        syn = [i]
        for j in range(len(li)):
            if i == j:
                continue
            for k in li[i]:
                if k in li[j]:
                    syn.append(j)
        ans = []
        for v in syn:
            for a in li[v]:
                ans.append(a)
            if v != syn[0]:
                li[v] = [-1]
        li[syn[0]] = list(set(ans))

    for i in li:
        answer *= len(i)
    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id,banned_id))