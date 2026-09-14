from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = 0
    queue=deque([(0,0,1)])
    maps[0][0]=0
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while queue:
        y,x,dist=queue.popleft()
        if x==m-1 and y==n-1:
            return dist
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<=m-1 and nx>=0 and ny<=n-1 and ny>=0 and maps[ny][nx]==1:
                queue.append((ny,nx,dist+1))
                maps[ny][nx]=0
    return -1