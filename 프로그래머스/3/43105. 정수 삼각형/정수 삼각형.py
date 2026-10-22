def solution(triangle):
    answer = 0
    x=0
    y=0
    tri=[[] for _ in range(len(triangle))]
    tri[0].append(triangle[0][0])
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:
                tri[i].append(tri[i-1][j]+triangle[i][j])
            elif j==len(triangle[i])-1:
                tri[i].append(tri[i-1][j-1]+triangle[i][j])
            else:
                tri[i].append(max(tri[i-1][j]+triangle[i][j], tri[i-1][j-1]+triangle[i][j]))
    answer=max(tri[len(triangle)-1])
    return answer