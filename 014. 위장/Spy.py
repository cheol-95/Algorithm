def solution(clothes):
    li = []
    cnt = []
    for i, v in clothes:
        li.append(v)

    for i in range(len(li)):
        tmp = li[i]
        if type(tmp) == int:
            continue
        cnt.append(li.count(tmp))
        for v in range(cnt[i]):
            li[li.index(tmp)] = i
    li[1] = 1
    for i in cnt:
        li[1] *= i

    return sum(cnt) + li[1]


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))