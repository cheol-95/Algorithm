# import collections
# import itertools
# def solution(orders, course):
#     answer = []
#     menu_map = {c: collections.defaultdict(int) for c in course}
#     for order in orders:
#         for c in course:
#             for row in list(map(lambda x: ''.join(x), itertools.combinations(order, c))):
#                 menu_map[c][''.join(sorted(row))] += 1
#
#     for length, menus_map in menu_map.items():
#         if not menus_map:
#             continue
#         menus = sorted(menus_map.items(), key=lambda x:x[1], reverse=True)
#         max_length = menus[0][1]
#         if max_length < 2:
#             continue
#         for menu, l in menus:
#             if max_length == l:
#                 answer.append(menu)
#
#     return sorted(answer)

from collections import Counter
from itertools import chain, combinations
def solution(orders, course):
    answer = []
    for c in course:
        comb = list(chain(*[map(lambda x: ''.join(sorted(x)), combinations(order, c)) for order in orders]))
        cnts = Counter(comb).most_common()
        [answer.append(menu) for menu, cnt in cnts if cnt == cnts[0][1] and cnt > 1]
    return sorted(answer)

orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]
# orders, course = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]
# orders, course = ["XYZ", "XWY", "WXA"], [2, 3, 4]

print(solution(orders, course))
