def solution(survey, choices):
    answer = ''
    kind = { 'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0 }

    for s, c in zip(survey, choices):
        if c < 4:
            kind[s[0]] += 4 - c
        else:
            kind[s[1]] += c - 4

    kind = list(kind.items())
    for idx in range(8):
        if idx % 2 == 1:
            answer += kind[idx-1][0] if kind[idx-1][1] >= kind[idx][1] else kind[idx][0]
    return answer

survey, choices = ["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]
print(solution(survey, choices))