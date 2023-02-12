from collections import Counter
tmp = input()
large = Counter(tmp.upper()).most_common(2)
if len(large) > 1 and large[0][1] == large[1][1]:
    print('?')
else:
    print(large[0][0])