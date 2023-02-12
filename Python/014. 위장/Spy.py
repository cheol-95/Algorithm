# from collections import Counter
# def solution(clothes):
#     answer = 1
#     count = Counter(list(v for i,v in clothes))
#     for i in count:
#         answer *= count[i]+1
#     return answer-1

def solution(clothes):
    clothes_type = {}
    for c, t in clothes:
        if t not in clothes_type: # 없으면 2추가
            clothes_type[t] = 2
        else: # 있으면 1 추가
            clothes_type[t] += 1
    cnt = 1
    for num in clothes_type.values():
        cnt *= num
    return cnt - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))


# collections.Counter 사용
'''
from collections import Counter
def solution(clothes):
    answer = 1
    count = Counter(list(v for i,v in clothes))
    for i in count:
        answer *= count[i]+1
    return answer-1
'''