def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2+1):
        string = ''
        piece = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            if piece == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    string += piece
                else:
                    string += str(cnt) + piece
                piece = s[j:j+i]
                cnt = 1
        if cnt == 1:
            string += piece
        else:
            string += str(cnt) + piece
        answer.append(len(string))
        
    return min(answer)