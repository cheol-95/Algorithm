# sequence, k = [1, 2, 3, 4, 5, 6, 7], 5
sequence, k = [1, 2, 3, 4, 5], 7
# sequence, k = [2, 2, 2, 2, 2], 6
# sequence, k = [1,1,1,1,1,1,1], 7
# sequence, k = [7,5,5,1,1,50,50], 100

def solution(sequence, k):
    answer = []
    s, e, sum = 0, 0, sequence[0]
    len_min = len(sequence)

    while e < len(sequence):
        if sum == k:
            if e-s < len_min:
                len_min = e-s
                answer =[]
            answer.append([s, e])
            sum -= sequence[s]
            s += 1

        elif sum > k:
            sum -= sequence[s]
            s += 1

        else:
            e += 1
            if e == len(sequence):
                break
            sum += sequence[e]

    return sorted(answer, key=lambda x: x[0])[0]

print(solution(sequence, k))