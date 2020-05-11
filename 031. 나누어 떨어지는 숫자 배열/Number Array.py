def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if answer == []:
        return [-1]
    return sorted(answer)

    # 다른풀이
    # return sorted([i for i in arr if i%divisor == 0]) or [-1]

arr, divisor = [5,9,7,10], 5
print(solution(arr,divisor))