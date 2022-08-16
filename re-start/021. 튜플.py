def solution(s):
    answer = []
    s = sorted(list(map(lambda x: x.split(','), s.rstrip('}').lstrip('{').split('},{'))), key=lambda x: len(x))
    [[answer.append(x) for x in row if x not in answer] for row in s]
    return list(map(int, answer))


s = "{{4,2,3},{3},{2,3,4,111},{2,3}}"
print(solution(s))