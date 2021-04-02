def solution(triangle):
    length = len(triangle)
    for i in range(length-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += triangle[i+1][j] if triangle[i+1][j] > triangle[i+1][j+1] else triangle[i+1][j+1]

    return triangle[0][0]


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))