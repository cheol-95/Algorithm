def solution(n, t, m, timetable):
    answer = ''
    timetable = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    timetable.sort()
    last = (60*9) + (n-1)*t

    for i in range(n):
        if len(timetable) < m:
            return '%02d:%02d'%(last//60,last%60)
        if i == n-1:
            if timetable[0] <= last:
                last = timetable[m-1]-1
                return '%02d:%02d'%(last//60,last%60)
        for j in range(m-1, -1, -1):
            bus = (60*9) + i * t
            if timetable[j] <= bus:
                del timetable[j]

    return answer