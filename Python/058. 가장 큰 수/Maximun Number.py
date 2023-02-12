def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: (x*3)[:4], reverse=True)
    return str(int(''.join(numbers)))