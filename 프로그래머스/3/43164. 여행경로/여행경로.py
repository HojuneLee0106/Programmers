from collections import deque
import copy
def solution(tickets):
    route={}
    for i in range(len(tickets)):
        if tickets[i][0] not in route:
            route[tickets[i][0]]=[tickets[i][1]]
        else:
            route[tickets[i][0]].append(tickets[i][1])
            route[tickets[i][0]].sort()
    queue=deque()
    queue.append(["ICN",copy.deepcopy(route), ["ICN"]])
    answer = ["ICN"]
    while queue:
        start, r,path=queue.pop()
        if len(path)==len(tickets)+1:
            answer=path
            break
        if start not in r or not r[start]:
            continue
        x=len(r[start])
        for i in range(x - 1, -1, -1):
            new_r = copy.deepcopy(r)
            new_path = copy.deepcopy(path)
            ne = new_r[start].pop(i)
            new_path.append(ne)
            queue.append([ne, new_r, new_path])
    
    return answer