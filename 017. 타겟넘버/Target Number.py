def solution(numbers, target):
    sup = [0]
    for i in numbers:
        sub = []
        for j in sup:
            sub.append(j + i)
            sub.append(j - i)
        sup=sub
    print(sup.count(target))

numbers, target = [1,1,1,1,1], 3
solution(numbers, target)