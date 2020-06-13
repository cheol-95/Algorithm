def splitnum(msg):
    num = False
    div = []
    for i in range(len(msg)):
        if msg[i].isnumeric():
            div.append(i)
            num = True
        elif num == True:
            return [msg[:div[0]], msg[div[0]:i], msg[i:]]
    return [msg[:div[0]], msg[div[0]:], '']

def solution(files):
    answer = []
    for i in files:
        answer.append(splitnum(i))
    answer.sort(key=lambda x:int(x[1]))
    answer.sort(key=lambda x:x[0].lower())
    for i in range(len(answer)):
        tmp = answer[i][0] + str(answer[i][1]) + answer[i][2]
        answer[i] = tmp
    return answer

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))