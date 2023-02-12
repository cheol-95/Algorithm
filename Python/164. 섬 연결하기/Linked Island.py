def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    con = set()
    con.add(0)

    while len(con) != n:
        for a, b, c in costs:
            if a in con or b in con:
                if a in con and b in con:
                    pass
                else:
                    con.add(a)
                    con.add(b)
                    answer += c
                    break
    return answer

n, costs = 4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
print(solution(n, costs))