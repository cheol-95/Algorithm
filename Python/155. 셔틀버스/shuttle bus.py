def solution(n, t, m, timetable):
    crews = sorted([int(time.split(':')[0]) * 60 + int(time.split(':')[1]) for time in timetable])
    bus = [[(540 + t * i), 0, None] for i in range(n)]

    length = len(crews)
    c_idx, b_idx = 0, 0
    while c_idx < length:
        crew = crews[c_idx]
        if b_idx == n:
            break

        if crew <= bus[b_idx][0] and bus[b_idx][1] < m:
            bus[b_idx][1] += 1
            bus[b_idx][2] = crew
            c_idx += 1
        else:
            b_idx += 1

    if bus[-1][1] < m:
        result = bus[-1][0]
    else:
        result = bus[-1][2]-1

    return f'{str(result // 60).rjust(2, "0")}:{str(result % 60).rjust(2, "0")}'



# n, t, m, timetable = 1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]
n, t, m, timetable = 2, 10, 2, ["09:10", "09:09", "08:00"]
# n, t, m, timetable = 	10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
print(solution(n, t, m, timetable))


