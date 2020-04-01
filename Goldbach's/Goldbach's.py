def sosu(y):
    li = []
    for i in range(2, y+1):
        for j in range(2, i):
            if i % j == 0:
                break
            elif j+1 == i:
                li.append(i)
    print(f'소수 : {li}')
    return li

def gold(anum, sList):
    res = []
    for i in sList:
        if int(anum-i) in sList:
            res.append(i)
    print(f'res : {res}')

    lth = len(res)
    if(lth % 2 == 1):
        index = int(lth / 2)
        gnum = res[index]
        print('{} = {} + {}\n'.format(anum, gnum, gnum))
    else:
        index2 = int(lth / 2)
        index1 = index2-1
        gnum1, gnum2 = res[index1],res[index2]
        print('{} = {} + {}\n'.format(anum, gnum1, gnum2))

if __name__ == '__main__':
    count = int(input("반복횟수:"))
    for _ in range(count):
        anum = int(input("숫자: "))
        gold(anum, sosu(anum))