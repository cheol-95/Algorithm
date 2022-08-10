def solution(a, b):
    return sum(map(lambda x: x[0] * x[1], zip(a, b)))

a, b = [1, 2, 3, 4], [-3, -1, 0, 2]
print(solution(a, b))