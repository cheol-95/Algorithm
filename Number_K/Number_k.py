def solution(nList, cmds):
    result = []
    for i in range(len(cmds)):
        result.append(sorted(nList[cmds[i][0]-1:cmds[i][1]])[cmds[i][2]-1])
    print(result)

nList = [1,5,2,6,3,7,4]
cmds = [[2,5,3],[4,4,1],[1,7,3]]
solution(nList, cmds)
