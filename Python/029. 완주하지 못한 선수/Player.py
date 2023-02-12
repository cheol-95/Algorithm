import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

participant, completion = ['b','b','c'], ['b','c']
print(solution(participant, completion))