def solution(s):
    answer = ''
    number_map = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    keys = number_map.keys()
    tmp = ''
    for char in s:
        if char.isdigit():
            answer += str(char)
        else:
            tmp += char
        if tmp in keys:
            answer += number_map[tmp]
            tmp = ''
    return int(answer)

s= 'one4seveneight'
print(solution(s))