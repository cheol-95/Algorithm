def solution(genres, plays):
    answer = []
    sgenres = list(set(genres))
    count, music = {x:0 for x in sgenres}, {x:[] for x in sgenres}

    for i in range(len(genres)):
        count[genres[i]] += plays[i]
        tmp = music[genres[i]]
        tmp.append([i, plays[i]])
        music[genres[i]] = tmp
    rank = sorted(count.items(), key=lambda x:x[1], reverse=True)

    for key in rank:
        play_list = music[key[0]]
        play_list = sorted(play_list, key=lambda x: (-x[1], x[0]))
        for i in range(len(play_list)):
            if i == 2:
                break
            answer.append(play_list[i][0])
    return answer

genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
print(solution(genres, plays))