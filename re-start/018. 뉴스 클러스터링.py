def solution(str1, str2):
    str1 = [(ch_1 + ch_2).upper() for ch_1, ch_2 in zip(str1[:-1], str1[1:]) if ch_1.isalpha() and ch_2.isalpha()]
    str2 = [(ch_1 + ch_2).upper() for ch_1, ch_2 in zip(str2[:-1], str2[1:]) if ch_1.isalpha() and ch_2.isalpha()]
    if not str1 and not str2:
        return 65536
    union = 0
    for ch_1 in str1:
        if ch_1 in str2:
            union += 1
            str2.remove(ch_1)
    empty_set = len(str1) + len(str2)
    return int((union / empty_set) * 65536)

str1, str2 = "FRANCE", "french"
# str1, str2 = "aa1+aa2", "AAAA12"
# str1, str2 = "handshake", "shake hands"
# str1, str2 = "E=M*C^2", "e=m*c^2"

print(solution(str1, str2))