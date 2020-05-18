def solution(skill, skill_trees):
    answer = len(skill_trees)
    for tree in skill_trees:
        tmp = skill
        for j in tree:
            if j in tmp[1:]:
                answer -= 1
                break
            if j == tmp[0]:
                tmp = tmp[1:]+'0'
    return answer


skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))