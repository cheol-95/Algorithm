def solution(picks, minerals):
    fatigue = 0
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    minerals = minerals[:sum(picks)]
    mins = list(map(lambda x: [x.count('diamond'), x.count('iron'), x.count('stone')], minerals))
    mins.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    for d, i, s in mins:
        for p in range(3):
            if picks[0]:
                picks[0] -= 1
                fatigue += d + i + s
                break
            elif picks[1]:
                picks[1] -= 1
                fatigue += d*5 + i + s
                break
            elif picks[2]:
                picks[2] -= 1
                fatigue += d*5*5 + i*5 + s
                break
    return fatigue

picks, minerals = [1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
# picks, minerals = [0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(solution(picks, minerals))