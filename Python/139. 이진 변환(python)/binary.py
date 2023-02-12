def solution(s):
    answer = [0, 0]
    while s != "1":
        answer[0] += 1
        answer[1] += s.count("0")
        s = bin(len(s.replace("0","")))[2:]
    return answer

s = "110010101001"
s = "01110"
tmp = solution(s)
print(tmp)