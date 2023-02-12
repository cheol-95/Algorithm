from string import ascii_uppercase
def solution(msg):
    answer = []
    TEXT = {}
    for i in range(len(ascii_uppercase)):
        TEXT[ascii_uppercase[i]] = i+1

    cnt = 0
    length = len(msg)
    while cnt < length:
        stmp = msg[cnt]
        if cnt == length-1:
            answer.append(TEXT[stmp])
            cnt += 1
        else:
            while stmp + msg[cnt+1] in TEXT:
                stmp += msg[cnt+1]
                cnt += 1
                if cnt == length-1:
                    answer.append(TEXT[stmp])
                    return answer
            answer.append(TEXT[stmp])
            TEXT[stmp+msg[cnt+1]] = len(TEXT)+1
            cnt += 1
    return answer

msg = 'KAKAO'
msg = 'TOBEORNOTTOBEORTOBEORNOT'
msg = 'ABABABABABABABAB'
print(solution(msg))