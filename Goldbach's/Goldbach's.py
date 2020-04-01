def sosu(y):
    li = []
    for i in range(2, y+1):
        for j in range(2, i):
            if i % j == 0:
                break
            elif j+1 == i:
                li.append(i)
    return li

def gold(anum, sList):
    res = []
    for i in sList:
        if int(anum-i) in sList:
            res.append(i)
    lth = len(res)
    if(lth % 2 == 1):
        index = int(lth / 2)
        gnum = res[index]
        print('{} = {} + {}'.format(anum, gnum, gnum))
    else:
        index2 = int(lth / 2)
        index1 = index2-1
        gnum1, gnum2 = res[index1],res[index2]
        print('{} = {} + {}'.format(anum, gnum1, gnum2))

if __name__ == '__main__':
    n, cmds=3,[8,10,16]
    for _ in range(n):
        gold(cmds[_], sosu(cmds[_]))