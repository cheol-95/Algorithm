from functools import reduce
def solution(lottos, win_nums):
    hit_count = reduce(lambda acc, cur: acc + (cur in win_nums), lottos, 0)
    best = 6 if hit_count + lottos.count(0) <= 1 else 7 - (hit_count + lottos.count(0))
    worst = 6 if hit_count <= 1 else 7 - hit_count
    return [best, worst]

# lottos, win_nums = [0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]
lottos, win_nums = [7,8,9,10,11,0], [1,2,3,4,5,6]

# lottos, win_nums = [44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
