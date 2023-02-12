import collections
def solution(genres, plays):
    result = []
    g_plays = collections.defaultdict(dict)
    for i, [g, p] in enumerate(zip(genres, plays)):
        if not g_plays[g]:
            g_plays[g] = {'plays': 0, 'music': []}

        g_plays[g]['plays'] += p
        g_plays[g]['music'].append([i, p])

    music = sorted(g_plays.items(), key=lambda x: x[1]['plays'], reverse=True)
    for i in music:
        musics = i[1]['music']
        musics.sort(key=lambda x: x[0])
        musics.sort(key=lambda x: x[1], reverse=True)
        result += list(map(lambda x: x[0], musics))[:2]

    return result

genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
print(solution(genres, plays))