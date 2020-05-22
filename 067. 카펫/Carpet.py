def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for height in range(3,brown):
        if total < height**2:
            break
        width = total / height
        if not width%1:
            width = int(width)
            if yellow == (width - 2) * (height - 2):
                return [width, height]

# brown, yellow= 10, 2
# brown, yellow= 8, 1
brown, yellow= 24, 24
print(solution(brown, yellow))