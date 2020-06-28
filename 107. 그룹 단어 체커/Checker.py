count = int(input())
score = 0
for i in range(count):
    word = input()
    length = len(word)
    old = []
    tmp = ''
    while word:
        if word[0] == tmp or word[0] not in old:
            old.append(word[0])
        elif word[0] != tmp and word[0] in old:
            break
        tmp = word[0]
        word = word[1:]
    if length == len(old):
        score += 1
print(score)