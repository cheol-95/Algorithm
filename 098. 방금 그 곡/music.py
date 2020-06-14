def solution(m, musicinfos):
    candidate = []
    m = m.replace('C#','H').replace('D#','I').replace('F#','J').replace('G#','K').replace('A#','L')
    for i in musicinfos:
        tmp = i.split(',')
        length = (int(tmp[1][:2])*60+int(tmp[1][3:]) - (int(tmp[0][:2])*60+int(tmp[0][3:])))
        tmp[3] = tmp[3].replace('C#','H').replace('D#','I').replace('F#','J').replace('G#','K').replace('A#','L')
        music = (tmp[3]*(length))[:length]
        if m in music:
            candidate.append([tmp[2],length])
    if len(candidate) == 0:
        return '(None)'
    return sorted(candidate,key=lambda x:x[1],reverse=True)[0][0]

m, musicinfos = "ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))