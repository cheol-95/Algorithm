from itertools import chain

def solution(genres, plays):
    g_dict = {g: [0, []] for g in set(genres)}
    for i, [g, p] in enumerate(zip(genres, plays)):
        g_dict[g][0] += p
        g_dict[g][1] = sorted([*g_dict[g][1], [i, p]], key=lambda x: x[1], reverse=True)[:2]
    res = list(sorted(g_dict.values(), key=lambda x: x[0], reverse=True))
    return list(chain(*map(lambda x: list(map(lambda y: y[0], x[1])), res)))


genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
print(solution(genres, plays))