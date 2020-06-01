def solution(n, words):
    stack = []
    for i in range(len(words)):
        if stack and stack[-1][-1] != words[i][0] or words[i] in stack:
            return [i%n+1,i//n+1]
        stack.append(words[i])
    else:
        return [0,0]

n, words = 3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))