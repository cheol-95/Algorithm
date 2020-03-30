# strings = ["sun","bed","car"]
strings = ["abce", "abcd", "cdx"]
n = int(input('기준 index 입력: '))

for i in range(len(strings) - 1):
    for j in range(i + 1, len(strings)):
        if (strings[i][n] > strings[j][n]):
            strings[j], strings[i] = strings[i], strings[j]
        elif (strings[i][1] == strings[j][1]):
            if (strings[i] > strings[j]):
                strings[j], strings[i] = strings[i], strings[j]

print(strings)