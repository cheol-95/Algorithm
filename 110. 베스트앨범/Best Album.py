def solution(genres, plays):
    answer = []
    sgenres = list(set(genres))
    count, music = {x:0 for x in sgenres}, {x:[] for x in sgenres}

    for i in range(len(genres)):
        count[genres[i]] += plays[i]
        tmp = music[genres[i]]
        tmp.append([i, plays[i]])
        music[genres[i]] = tmp

    cnt = []
    for i in count:
        cnt.append([i, count[i]])
    cnt.sort(key=lambda x:x[1], reverse=True)

    for i in [cnt[0][0], cnt[1][0]]:
        tmp = music[i]
        tmp = sorted(tmp, key=lambda x: x[0])
        tmp = sorted(tmp, key=lambda x: x[1], reverse=True)
        answer += list(map(lambda x: x[0], tmp[:2]))
    return answer



genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
print(solution(genres, plays))