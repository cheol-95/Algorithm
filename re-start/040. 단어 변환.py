from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    q = deque()
    q.append([begin, 0, []])
    while q:
        prev_word, d, v = q.pop()
        for idx, word in enumerate(words):
            diff_count = sum(map(lambda x: x[0] != x[1], zip(prev_word, word)))
            if diff_count == 1 and idx not in v:
                if word == target:
                    return d+1
                v.append(idx)
                q.append([word, d+1, v])
    return answer


begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))

# word_1, word_2= 'abc', 'abd'
# tmp = sum([x != y for x, y in zip(word_1, word_2)]) == 1
# print(tmp)

