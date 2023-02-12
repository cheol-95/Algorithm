def solution(a, b):
    day = ['WED','THU','FRI','SAT','SUN','MON','TUE']
    aN = int(a/2)
    if a == 1:
        pass
    elif a%2 == 1:
        b += aN*31 + (aN-1)*30 + 29 +1
    elif a%2 == 0:
        b += (aN-1)*31 + aN*30 + 29 +1
    return day[b%7]

a, b = 5,24
print(solution(a,b))

#패키지 사용
# import datetime
# def solution(a, b):
#     day_of_the_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
#     return day_of_the_week[datetime.datetime(2016, a, b).weekday()]