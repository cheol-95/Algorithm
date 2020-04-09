def solution(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    return ''.join(st[:len(st) - k])

# number, k = "1924", 2
# number, k = "1231234", 3
number, k = "4177252841", 4
print(solution(number, k))