import itertools
import collections

def solution(orders, course):
    answer = []
    for cnt in course:
        combinations = []
        for order in orders:
            combinations += list(map(lambda x: ''.join(x), (itertools.combinations(sorted(order), cnt))))

        sorted_orders = collections.Counter(combinations).most_common()
        most = sorted_orders[0][1] if len(sorted_orders) else 0
        for candidate, count in sorted_orders:
            if (count > 1 and count == most):
                answer.append(candidate)

    return sorted(answer)

orders, course = ["XYZ", "XWY", "WXA"], [2, 3, 4]
print(solution(orders, course))