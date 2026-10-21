def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    dan=-30001
    for i in range(len(routes)):
        if dan<routes[i][0]:
            answer+=1
            dan=routes[i][1]
    return answer