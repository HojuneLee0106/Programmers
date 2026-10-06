def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    island=[]
    i=0
    while len(island)!=n:
        if len(island)==0:
            island.append(costs[i][0])
            island.append(costs[i][1])
            answer+=costs[i][2]
            costs.pop(0)
        else:
            if costs[i][0] in island and costs[i][1] not in island:
                answer+=costs[i][2]
                island.append(costs[i][1])
                costs.pop(i)
                i=0
            elif costs[i][0] not in island and costs[i][1] in island:
                answer+=costs[i][2]
                island.append(costs[i][0])
                costs.pop(i)
                i=0
            else:
                i+=1
    return answer