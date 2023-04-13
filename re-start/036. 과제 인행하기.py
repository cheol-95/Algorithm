# plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
# plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
plans = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
# plans = [["aaa", "12:00", "10"], ["bbb", "12:01", "10"], ["ccc", "12:02", "10"], ["ddd", "14:00", "10"]]
# plans = [["1", "00:00", "30"], ["2", "00:10", "30"], ["3", "00:20", "30"], ["4", "01:50", "10"]]

def solution(plans):
    answer, stack = [], []
    plans = list(map(lambda x: [x[0], convertMinute(x[1]), int(x[2])], plans))
    plans.sort(key=lambda x: x[1])

    for study, start, playtime in plans:
        if stack:
            p_study, p_start, p_playtime = stack.pop()
            term = start - p_start

            if term < p_playtime:
                stack.append([p_study, p_start, p_playtime-term])
            else:
                answer.append(p_study)
                term -= p_playtime

                while stack and term:
                    p_study, p_start, p_playtime = stack.pop()

                    if term < p_playtime:
                        stack.append([p_study, p_start, p_playtime - term])
                        break
                    else:
                        answer.append(p_study)
                        term -= p_playtime

        stack.append([study, start, playtime])

    while stack:
        answer.append(stack.pop()[0])

    return answer

def convertMinute(time):
    h, m = list(map(int, time.split(':')))
    return h*60 + m

print(solution(plans))