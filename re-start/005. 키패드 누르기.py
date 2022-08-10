def get_distance(num, left, right):
    num, left, right = map(lambda x: x if x != 0 else 11, [num, left, right])
    l_abs, r_abs = abs(left - num), abs(right - num)
    return l_abs // 3 + l_abs % 3, r_abs // 3 + r_abs % 3

def set_answer(answer, t, num):
    return answer + t, num

def solution(numbers, hand):
    answer, left, right = '', 10, 12

    for num in numbers:
        if num in [1, 4, 7]:
            answer, left = set_answer(answer, 'L', num)
        elif num in [3, 6, 9]:
            answer, right = set_answer(answer, 'R', num)
        else:
            l_dis, r_dis = get_distance(num, left, right)
            if l_dis < r_dis:
                answer, left = set_answer(answer, 'L', num)
            elif l_dis > r_dis:
                answer, right = set_answer(answer, 'R', num)
            else:
                if 'left' == hand:
                    answer, left = set_answer(answer, 'L', num)
                else:
                    answer, right = set_answer(answer, 'R', num)
    return answer

# numbers, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
numbers, hand = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"
print(solution(numbers, hand))
