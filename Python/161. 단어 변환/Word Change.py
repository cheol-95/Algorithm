import collections

def get_route(words, begin):
    length = len(words[0])
    route = collections.defaultdict(list)
    start_words = words + [begin]

    for word in start_words:
        for tmp in words:
            count = 0
            for idx in range(length):
                if word[idx] == tmp[idx]:
                    count += 1
            if count == length-1:
                route[word].append(tmp)
    return route

def solution(begin, target, words):
    result = 50
    if target not in words:
        return 0

    route = get_route(words, begin)
    d = {word: 0 for word in words}
    queue = collections.deque([[begin, 0]])

    while queue:
        begin, count = queue.popleft()
        if begin == target:
            result = result if result < count else count

        for word in route[begin]:
            if not d[word]:
                queue.append([word, count + 1])
                d[word] = 1

    return result if result != 50 else 0


# begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
# begin = "hit"
# target = "hhh"
# words = ["hhh","hht"]
# print(solution(begin, target, words))
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
# print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
print(solution("1234567000", "1234567899", [
      "1234567800", "1234567890", "1234567899"]), 3)
# print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)


# import collections
#
# def get_route(words, begin):
#     length = len(words[0])
#     route = collections.defaultdict(list)
#     start_words = words + [begin]
#
#     for word in start_words:
#         for tmp in words:
#             count = 0
#             for idx in range(length):
#                 if word[idx] == tmp[idx]:
#                     count += 1
#             if count == 2:
#                 route[word].append(tmp)
#     return route
#
# def solution(begin, target, words):
#     if target not in words:
#         return 0
#
#     route = get_route(words, begin)
#     print(route)
#     exit()
#     d = {word: 0 for word in words}
#     queue = collections.deque([[begin, 0]])
#
#     while queue:
#         begin, count = queue.popleft()
#         if begin == target:
#             return count
#
#         for word in route[begin]:
#             if not d[word]:
#                 queue.append([word, count + 1])
#                 d[word] = 1
#
#     return 0
#
#
# begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
# print(solution(begin, target, words))