def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        dict={}
        for j in range(len(skill)):
            dict[j]=skill[j]
        pos=True
        current=0
        for k in range(len(i)):
            if i[k] not in dict.values():
                continue
            else:
                if i[k]==dict[current]:
                    current+=1
                    continue
                else:
                    pos=False
                    break
        if pos:
            answer+=1
    return answer