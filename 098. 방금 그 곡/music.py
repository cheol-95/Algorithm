def solution(m, musicinfos):
    candidate = []
    for i in musicinfos:
        tmp = i.split(',')
        length = (int(tmp[1][:2])*60+int(tmp[1][3:]) - (int(tmp[0][:2])*60+int(tmp[0][3:])))
        music = (tmp[3]*(length+tmp[3].count('#')))[:length+tmp[3].count('#')]
        print(music)
        if m in music and music[music.index(m[0])+len(m)] != '#':
            candidate.append([tmp[2],length])
    if len(candidate) == 0:
        return '(None)'
    return sorted(candidate,key=lambda x:x[1],reverse=True)[0][0]

m, musicinfos = "ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# m, musicinfos = "CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
# m, musicinfos = "ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))