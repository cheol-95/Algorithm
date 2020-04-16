from collections import Counter
def solution(clothes):
    answer = 1
    count = Counter(list(v for i,v in clothes))
    for i in count:
        answer *= count[i]+1
    return answer-1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))