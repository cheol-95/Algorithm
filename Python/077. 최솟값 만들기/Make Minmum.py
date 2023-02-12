def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    cnt = 0
    while cnt < len(A):
        answer += A[cnt]*B[cnt]
        cnt+=1
    return answer

    # return sum(x*y for x,y in zip(sorted(A), sorted(B,reverse=True)))

A, B = [1, 4, 2], [5, 4, 4]
print(solution(A,B))