import itertools

def solution(expression):
    ops = []
    ots = []
    result = 0
    temps = ''

    for char in expression:
        if char.isdigit():
            temps += char
        else:
            ops.append(int(temps))
            ots.append(char)
            temps = ''
    ops.append(int(temps))

    ots_ranks = list(itertools.permutations(set(ots), len(set(ots))))

    for ots_rank in ots_ranks:
        ops_copy = ops.copy()
        ots_copy = ots.copy()

        for rank in ots_rank:
            catches = []

            for ots_idx in range(len(ots_copy)):
                if ots_copy[ots_idx] == rank:
                    catches.append(ots_idx)

            for idx in catches:
                ops_copy[idx+1] = eval(str(ops_copy[idx]) + rank + str(ops_copy[idx+1]))

            count = 0
            for idx in catches:
                del ops_copy[idx - count]
                del ots_copy[idx - count]
                count += 1

        result = result if result > abs(ops_copy[0]) else abs(ops_copy[0])

    return result


# expression = "100-200*300-500+20"
expression = "50*6-3*2"
print(solution(expression))