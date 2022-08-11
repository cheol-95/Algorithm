def solution(record):
    u_map = {row.split(" ")[1]: row.split(" ")[2] for row in record if row.split(" ")[0][0] != 'L'}
    return [f'{u_map[row.split(" ")[1]]}님이 {"들어왔습니다" if row.split(" ")[0] == "Enter" else "나갔습니다"}.' for row in record if row.split(" ")[0][0] != 'C']

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))