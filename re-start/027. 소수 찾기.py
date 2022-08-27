import itertools
def solution(numbers):
    pers = []
    for i in range(len(numbers)):
        pers += list(map(lambda x: int(''.join(x)), itertools.permutations(numbers, i+1)))
    pers = set(pers)
    era = [True for _ in range(max(pers)+1)]
    era[0], era[1] = False, False
    for i in range(2, max(pers)+1):
        if era[i] == True:
            for j in range(i+i, max(pers)+1, i):
                era[j] = False
    return list(map(lambda p: era[p], pers)).count(True)

numbers = "011"
print(solution(numbers))