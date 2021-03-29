def solution(N, number):
    if N == number:
        return 1

    formulas = [set() for _ in range(8)]
    for i in range(1, 9):
        formulas[i-1].add( int( str(N) * i))

    for i in range(8):
        for j in range(i):
            for op1 in formulas[j]:
                for op2 in formulas[i-j-1]:
                    formulas[i].add(op1 + op2)
                    formulas[i].add(op1 - op2)
                    formulas[i].add(op1 * op2)
                    if op2 != 0:
                        formulas[i].add(op1 // op2)
        if number in formulas[i]:
            return i + 1

    return -1

N, number = 5, 14
print(solution(N, number))