def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    user_index = {id: idx for idx, id in enumerate(id_list)}
    report_map = {id: {
        'report_count': 0,
        'reporters': set()
    } for idx, id in enumerate(id_list)}

    for row in report:
        reporter, recipient = row.split()
        report_map[recipient]['reporters'].add(reporter)

    for id, values in report_map.items():
        if len(values['reporters']) >= k:
            for reporter in values["reporters"]:
                answer[user_index[reporter]] += 1

    return answer

# id_list, report, k = ["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2
id_list, report, k = ["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3

print(solution(id_list, report, k))