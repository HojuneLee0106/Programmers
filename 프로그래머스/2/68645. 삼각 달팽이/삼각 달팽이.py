def solution(n):
    arr=[[0 for _ in range(n)] for _ in range(n)]
    dx=[0,1,-1]
    dy=[1,0,-1]
    start_x=0
    start_y=0
    direction=0
    for i in range(1,(n*n-n)//2+n+1):
        arr[start_y][start_x]=i
        if (start_y+dy[direction])>=n or (start_x+dx[direction])>=n or (start_y+dy[direction])<0 or (start_x+dx[direction])<0:
            direction+=1
            direction%=3
            start_x+=dx[direction]
            start_y+=dy[direction]
        elif arr[start_y+dy[direction]][start_x+dx[direction]]!=0:
            direction+=1
            direction%=3
            start_x+=dx[direction]
            start_y+=dy[direction]
        else:
            start_x+=dx[direction]
            start_y+=dy[direction]
    answer=[]
    for i in range(n):
        for j in range(0,i+1):
            answer.append(arr[i][j])
    return answer