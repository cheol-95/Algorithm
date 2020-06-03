def solution(str1, str2):
    str11, str22 = [], []
    for i in range(1,len(str1)):
        if str1[i-1].isalpha() and str1[i].isalpha():
            str11.append((str1[i-1]+str1[i]).lower())
    for i in range(1,len(str2)):
        if str2[i-1].isalpha() and str2[i].isalpha():
            str22.append((str2[i-1]+str2[i]).lower())
    length = len(str11)+len(str22)
    mini = 0
    cnt = 0
    while 1:
        if cnt >= len(str11):
            break
        elif str11[cnt] in str22:
            mini += 1
            str22.remove(str11[cnt])
            str11.remove(str11[cnt])
        else:
            cnt += 1
    maxi = length-mini
    if mini == maxi:
        return 65536
    return int((mini/maxi)*65536)


str1, str2 = 'FRANCE', 'french'
# str1, str2 = 'handshake', 'shake hands'
print(solution(str1, str2))