import string

def check_id(id, pass_char):
    id_length = len(id)
    if id_length < 3 or id_length > 15:
        return False


    if id[0] == '.' or id[-1] == '.':
        return False

    if ".." in id:
        return False

    for char in id:
        if char not in pass_char:
            return False

    return True


def solution(new_id):
    answer = ''
    pass_char = list(string.ascii_lowercase) + list(map(str, range(0, 10))) + ['-', '_', '.']

    if check_id(new_id, pass_char):
        return new_id

    for char in new_id:
        if char.lower() not in pass_char:
            continue
        if char.isupper():
            answer += char.lower()
        else:
            answer += char

    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer[0] == '.':
        answer = answer[1:]

    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:len(answer)-1]

    if answer == '':
        answer = 'a'

    if len(answer) > 15:
        answer = answer[:15]

    if answer[-1] == '.':
        answer = answer[:len(answer)-1]

    while len(answer) < 3:
        answer += answer[-1]

    return answer



# new_id = "...!@BaT#*..y.abcdefghijklm."
new_id = "=.="
tmp = solution(new_id)
print(tmp)