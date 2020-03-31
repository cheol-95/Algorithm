def sorting1(strings, n): #index 순회 (앞->뒤) + reverse
    for i in range(len(strings) - 1): #0 ~ strings길이-1
        for j in range(i + 1, len(strings)): #i+1 ~ strings길이
            if (strings[i][n] < strings[j][n]): #뒤가 앞보다 크면
                strings[j], strings[i] = strings[i], strings[j] #Swap
            if (strings[i][1] == strings[j][1] and strings[i] < strings[j]):
                #index 1의 문자가 같고 && 앞의 문자열이 뒤의 문자열보다 사전순으로 앞이라면
                strings[j], strings[i] = strings[i], strings[j] #Swap
    strings.reverse()
    print(strings)

def sorting2(strings, n): #index 순회 (뒤->앞)
    for i in range(len(strings)): #0 ~ strings길이-1
        for j in range(1, len(strings)-i): #i+1 ~ strings길이
            if (strings[j-1][n] > strings[j][n]): #앞이 뒤보다 크면
                strings[j], strings[j-1] = strings[j-1], strings[j] #Swap
            if (strings[j-1][1] == strings[j][1] and strings[j-1] > strings[j]):
                #index 1의 문자가 같고 && 앞의 문자열이 뒤의 문자열보다 사전순으로 앞이라면
                strings[j], strings[j-1] = strings[j-1], strings[j] #Swap
    print(strings)

def sorting3(strings, n): #lambda
    strings.sort()
    strings.sort(key=lambda x: x[n])
    print(strings)

if __name__ == '__main__':
    # strings = ["sun","bed","car"]
    strings = ["abce", "abcd", "cdx"]
    n = int(input('기준 index 입력: '))

    result = sorting1(strings, n)
    result = sorting2(strings, n)
    result = sorting3(strings, n)